"use client";

import { FormEvent, useEffect, useRef, useState } from "react";

type Msg = { role: "user" | "bot"; text: string };

export default function Home() {
  const [msgs, setMsgs] = useState<Msg[]>([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const bottom = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottom.current?.scrollIntoView({ behavior: "smooth" });
  }, [msgs, busy]);

  async function send(text: string) {
    const q = text.trim();
    if (!q || busy) return;
    setBusy(true);
    setInput("");
    setMsgs((m) => [...m, { role: "user", text: q }]);
    try {
      const res = await fetch("/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: q }),
      });
      const data = await res.json();
      const textOut = !res.ok
        ? data.error || `Lỗi HTTP ${res.status}`
        : data.output || "(trống)";
      setMsgs((m) => [...m, { role: "bot", text: textOut }]);
    } catch {
      setMsgs((m) => [
        ...m,
        { role: "bot", text: "Không kết nối được. Chạy lại python run.py rồi thử lại." },
      ]);
    } finally {
      setBusy(false);
    }
  }

  function onSubmit(e: FormEvent) {
    e.preventDefault();
    void send(input);
  }

  return (
    <main className="mx-auto flex h-screen w-full max-w-4xl flex-col px-5 py-8 sm:py-10">
      <header className="mb-6 text-center">
        <h1 className="bg-gradient-to-r from-[#7ee0bd] via-[#e8f0ec] to-[#7ee0bd] bg-clip-text text-4xl font-extrabold tracking-wide text-transparent sm:text-5xl">
          Nhóm ABC · Lớp L3B · Track A2
        </h1>
        <p className="mx-auto mt-4 max-w-2xl text-base leading-relaxed text-[var(--muted)] sm:text-lg">
          Trợ lý Discord hỗ trợ sinh viên tra cứu hạn nộp lab nhanh chóng và chính xác từ thông báo chính thức.
        </p>
      </header>

      <section className="flex min-h-0 flex-1 flex-col gap-4 overflow-y-auto rounded-3xl border border-[var(--line)] bg-[#101a16]/70 p-5 shadow-2xl shadow-black/30 backdrop-blur sm:p-7">
        {msgs.length === 0 && !busy ? (
          <div className="m-auto text-center text-base text-[var(--muted)]">
            Nhập câu hỏi về hạn nộp lab ở ô bên dưới để bắt đầu.
          </div>
        ) : null}
        {msgs.map((m, i) => (
          <div key={i} className={`flex items-end gap-3 ${m.role === "user" ? "justify-end" : "justify-start"}`}>
            {m.role === "bot" ? (
              <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-[var(--accent)] text-xs font-bold text-[#04140f]">
                AI
              </div>
            ) : null}
            <div
              className={`max-w-[80%] whitespace-pre-wrap break-words rounded-2xl px-5 py-3.5 text-base leading-relaxed ${
                m.role === "user"
                  ? "rounded-br-sm bg-[var(--accent-dim)] text-white"
                  : "rounded-bl-sm border border-[var(--line)] bg-[var(--bg1)]"
              }`}
            >
              {m.text}
            </div>
          </div>
        ))}
        {busy ? (
          <div className="flex items-end gap-3">
            <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-[var(--accent)] text-xs font-bold text-[#04140f]">
              AI
            </div>
            <div className="rounded-2xl rounded-bl-sm border border-[var(--line)] bg-[var(--bg1)] px-5 py-3.5 text-base text-[var(--muted)]">
              Đang trả lời…
            </div>
          </div>
        ) : null}
        <div ref={bottom} />
      </section>

      <form
        onSubmit={onSubmit}
        className="mt-5 flex gap-3 rounded-2xl border border-[var(--line)] bg-[var(--bg1)] p-3 shadow-lg shadow-black/20 focus-within:border-[var(--accent)]"
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Nhập câu hỏi…"
          disabled={busy}
          autoFocus
          className="min-w-0 flex-1 bg-transparent px-3 py-2 text-base outline-none placeholder:text-[var(--muted)]"
        />
        <button
          type="submit"
          disabled={busy || !input.trim()}
          className="rounded-xl bg-[var(--accent)] px-6 py-2.5 text-base font-semibold text-[#04140f] transition hover:brightness-110 disabled:opacity-40"
        >
          Gửi
        </button>
      </form>
    </main>
  );
}
