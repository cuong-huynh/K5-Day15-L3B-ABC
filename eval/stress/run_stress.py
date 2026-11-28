"""Chạy hệ thống trên bộ câu kiểm tải do LLM khác sinh và đối chiếu tự động. Không thuộc benchmark chính thức.
Chạy: python eval/stress/run_stress.py [cases_50.json]   →  eval/stress/results_N.json
Đối chiếu: answer = output có đúng hạn; ask = output là câu hỏi lại; escalate = output là bản nháp chuyển TA, không chứa hạn."""
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "codebase"))
sys.stdout.reconfigure(encoding="utf-8")
import tracing  # noqa: E402
from agent import answer  # noqa: E402

DATE_RE = re.compile(r"\d{1,2}/\d{1,2}")


def kind(out):
    if out.startswith("Hạn nộp Lab"):
        return "answer"
    if out.startswith("Bạn hỏi hạn nộp") or out.startswith("Mình chỉ trả lời một lab"):
        return "ask"
    if out.startswith("Mình chưa chắc"):
        return "escalate"
    return "other"


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "cases_50.json")
    cases = json.load(open(path, encoding="utf-8"))
    res, ti, to = [], 0, 0
    for c in cases:
        tracing.begin(c["id"])
        try:
            out = answer(c["input"])["output"]
            err = None
        except Exception as e:
            out, err = "", "%s: %s" % (type(e).__name__, str(e)[:150])
        s, _ = tracing.end()
        ti += s["tokens_in"]
        to += s["tokens_out"]
        got = kind(out)
        ok = got == c["behavior"]
        if out.startswith("Mình chỉ trả lời một lab") and c["behavior"] == "escalate" and not c["lab"]:
            ok = True   # nhiều lab trong một câu: hỏi lại cũng chấp nhận được (không trả hạn nào)
        if ok and c["behavior"] == "answer":
            ok = c["deadline"] in out
        if got == "escalate":
            # phần câu hỏi gốc được trích lại trong bản nháp nên chỉ kiểm phần trước "Học viên hỏi:"
            ok = ok and not DATE_RE.search(out.split("Học viên hỏi:")[0])
        res.append({"id": c["id"], "input": c["input"], "expected": c["behavior"], "got": got, "auto_pass": bool(ok and not err),
                    "output": out, "error": err, "why": c["why"]})
        if err and "429" in err:
            time.sleep(20)
        time.sleep(2)
    n = 1
    while os.path.exists(os.path.join(HERE, "results_%d.json" % n)):
        n += 1
    json.dump(res, open(os.path.join(HERE, "results_%d.json" % n), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    bad = [r for r in res if not r["auto_pass"]]
    print("Tự động đạt: %d/%d · lỗi gọi: %d · token vào %d ra %d → results_%d.json" % (
        len(res) - len(bad), len(res), sum(1 for r in res if r["error"]), ti, to, n))
    for r in bad:
        print("\n%s [mong đợi %s, thực tế %s] %s\n   → %s" % (r["id"], r["expected"], r["got"], r["input"], (r["error"] or r["output"]).replace("\n", " ")[:170]))


if __name__ == "__main__":
    main()
