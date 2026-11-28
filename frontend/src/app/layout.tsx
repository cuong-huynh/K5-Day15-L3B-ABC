import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ABC · Hỏi hạn lab",
  description: "Trợ lý Discord — chỉ trả lời hạn lab từ thông báo chính thức",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi">
      <body>{children}</body>
    </html>
  );
}
