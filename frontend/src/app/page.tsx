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
    <main className="mx-auto flex min-h-screen w-full max-w-2xl flex-col px-4 py-6 sm:py-10">
      <header className="mb-6 border-b border-[var(--line)] pb-5 text-center">
        <h1 className="text-3xl font-bold tracking-wide sm:text-4xl">Nhóm ABC · Lớp L3B · Track A2</h1>
        <p className="mx-auto mt-3 max-w-xl text-sm leading-relaxed text-[var(--muted)]">
          Trợ lý Discord hỗ trợ sinh viên tra cứu hạn nộp lab nhanh chóng và chính xác từ thông báo chính thức.
        </p>
      </header>

      <section className="flex min-h-0 flex-1 flex-col gap-3 overflow-y-auto pb-4">
        {msgs.map((m, i) => (
          <div
            key={i}
            className={`max-w-[92%] whitespace-pre-wrap rounded-2xl px-4 py-3 text-sm leading-relaxed ${
              m.role === "user"
                ? "ml-auto bg-[var(--accent-dim)] text-white"
                : "mr-auto border border-[var(--line)] bg-[var(--bg1)]"
            }`}
          >
            {m.text}
          </div>
        ))}
        {busy ? (
          <div className="mr-auto text-sm text-[var(--muted)]">Đang hỏi…</div>
        ) : null}
        <div ref={bottom} />
      </section>

      <form
        onSubmit={onSubmit}
        className="flex gap-2 rounded-2xl border border-[var(--line)] bg-[var(--bg1)] p-2"
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Nhập câu hỏi…"
          disabled={busy}
          className="min-w-0 flex-1 bg-transparent px-3 py-2 text-sm outline-none placeholder:text-[var(--muted)]"
        />
        <button
          type="submit"
          disabled={busy || !input.trim()}
          className="rounded-xl bg-[var(--accent)] px-4 py-2 text-sm font-medium text-[#04140f] disabled:opacity-40"
        >
          Gửi
        </button>
      </form>
    </main>
  );
}
