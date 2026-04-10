import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: ["./src/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        lumina: {
          bg: "#070a14",
          panel: "#111933",
          panelSoft: "#1a2240",
          border: "#2b3864",
          cyan: "#67e8f9",
          violet: "#8b8fff",
          blue: "#3b82f6",
          gold: "#f4d27a"
        }
      },
      boxShadow: {
        glow: "0 0 0 1px rgba(103, 232, 249, 0.15), 0 16px 48px rgba(59, 130, 246, 0.22)",
        card: "0 8px 30px rgba(5, 8, 18, 0.7)"
      },
      backgroundImage: {
        cosmos:
          "radial-gradient(1200px 500px at 10% -10%, rgba(59,130,246,0.25), transparent 60%), radial-gradient(900px 400px at 80% 0%, rgba(139,143,255,0.28), transparent 55%), radial-gradient(700px 320px at 50% 100%, rgba(103,232,249,0.12), transparent 60%)"
      }
    }
  },
  plugins: []
};

export default config;
