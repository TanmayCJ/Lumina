"use client";

import { motion } from "framer-motion";
import { Database, Rocket, Telescope } from "lucide-react";

import { LuminaExplorer } from "@/components/lumina-explorer";
import { LuminaHero } from "@/components/lumina-hero";

const CAPABILITIES = [
  {
    title: "Curated Astronomy Facts",
    description: "Local structured datasets for stars and deep-sky objects.",
    icon: Database
  },
  {
    title: "Guided Explanations",
    description: "Readable explanations adapted to beginner, intermediate, and advanced users.",
    icon: Telescope
  },
  {
    title: "Backend-Connected",
    description: "Live calls to Lumina FastAPI endpoints for demo-ready exploration.",
    icon: Rocket
  }
];

export default function HomePage() {
  return (
    <main className="min-h-screen bg-cosmos px-4 pb-16 pt-8 md:px-8">
      <div className="mx-auto max-w-7xl">
        <LuminaHero />
        <LuminaExplorer />

        <section className="mt-8 rounded-3xl border border-lumina-border/60 glass p-6 section-glow">
          <h3 className="text-lg font-semibold text-slate-100">What Lumina Does Right Now</h3>
          <p className="mt-2 max-w-2xl text-sm text-slate-300">
            This milestone focuses on one polished user flow: ask about a star or celestial object and get a clean,
            structured, educational response.
          </p>
          <div className="mt-5 grid grid-cols-1 gap-3 md:grid-cols-3">
            {CAPABILITIES.map(({ title, description, icon: Icon }) => (
              <motion.div
                key={title}
                initial={{ opacity: 0, y: 8 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.25 }}
                className="rounded-2xl border border-lumina-border/60 bg-lumina-panel/45 p-4"
              >
                <Icon className="h-5 w-5 text-cyan-300" />
                <p className="mt-2 text-sm font-semibold text-slate-100">{title}</p>
                <p className="mt-1 text-sm text-slate-300">{description}</p>
              </motion.div>
            ))}
          </div>
        </section>

        <footer className="mt-8 text-center text-xs text-slate-500">
          Lumina UI Milestone 1 - Powered by astronomy datasets + guided AI-style explanations
        </footer>
      </div>
    </main>
  );
}
