"use client";

import { FormEvent, useEffect, useRef, useState } from "react";

type Msg = { role: "user" | "bot"; text: string };

const EXAMPLES = [
  "hạn nộp lab 3 là khi nào?",
  "lab 4 hạn bao giờ",
  "cho em điểm lab 3 của em",
];

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
      <header className="mb-6 border-b border-[var(--line)] pb-4">
        <p className="text-xs uppercase tracking-[0.2em] text-[var(--muted)]">ABC</p>
        <h1 className="mt-1 text-3xl font-semibold tracking-tight sm:text-4xl">
          Hỏi hạn lab
        </h1>
        <p className="mt-2 text-sm text-[var(--muted)]">
          Chỉ trả lời từ thông báo chính thức. Không chắc thì chuyển TA.
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

      <div className="mb-3 flex flex-wrap gap-2">
        {EXAMPLES.map((ex) => (
          <button
            key={ex}
            type="button"
            disabled={busy}
            onClick={() => void send(ex)}
            className="rounded-full border border-[var(--line)] bg-transparent px-3 py-1 text-xs text-[var(--muted)] transition hover:border-[var(--accent)] hover:text-[var(--text)] disabled:opacity-50"
          >
            {ex}
          </button>
        ))}
      </div>

      <form
        onSubmit={onSubmit}
        className="flex gap-2 rounded-2xl border border-[var(--line)] bg-[var(--bg1)] p-2"
      >
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="vd: hạn nộp lab 3 là khi nào?"
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
