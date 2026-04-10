import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Lumina - AI Star Guide",
  description: "Explore stars and celestial objects with guided, dataset-backed explanations."
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="bg-stars" />
        <div className="lumina-noise" />
        {children}
      </body>
    </html>
  );
}
