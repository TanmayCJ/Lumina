import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        lumina: {
          bg: "#f7f8fe",
          bgSoft: "#eef2ff",
          panel: "#ffffff",
          panelSoft: "#f7f9ff",
          border: "#dbe4ff",
          cyan: "#63d3e7",
          violet: "#9ea7ff",
          periwinkle: "#7f8ed4",
          navy: "#1b2b55",
          ink: "#2c3657"
        }
      },
      boxShadow: {
        glow: "0 0 0 1px rgba(99, 211, 231, 0.28), 0 18px 55px rgba(118, 144, 219, 0.22)",
        card: "0 14px 45px rgba(72, 92, 148, 0.15)",
        soft: "0 6px 22px rgba(97, 116, 172, 0.12)"
      },
      backgroundImage: {
        cosmos:
          "radial-gradient(1100px 500px at 8% -5%, rgba(137, 154, 240, 0.22), transparent 62%), radial-gradient(900px 440px at 88% 0%, rgba(140, 210, 230, 0.20), transparent 58%), radial-gradient(900px 420px at 48% 110%, rgba(205, 212, 255, 0.35), transparent 62%)"
      }
    }
  },
  plugins: []
};

export default config;
