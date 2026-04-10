"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import { ArrowDownRight, Database, Rocket, Telescope } from "lucide-react";

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
        <header className="mb-6 flex flex-wrap items-center justify-between gap-3 rounded-2xl border border-lumina-border/80 bg-white/70 px-4 py-3 shadow-soft backdrop-blur">
          <div className="flex items-center gap-3">
            <div className="h-10 w-10 overflow-hidden rounded-xl border border-lumina-border/70 bg-white">
              <Image src="/images/lumina-logo.png" alt="Lumina mark" width={80} height={80} className="h-full w-full object-cover" />
            </div>
            <div>
              <p className="text-sm font-semibold tracking-wide text-lumina-ink">Lumina</p>
              <p className="text-xs text-slate-500">Intelligent Star Guide</p>
            </div>
          </div>
          <a
            href="#explorer"
            className="inline-flex items-center gap-1 rounded-full border border-lumina-border/90 bg-white/90 px-3 py-1.5 text-xs font-semibold text-lumina-ink transition hover:border-cyan-300/80"
          >
            Start Exploring
            <ArrowDownRight className="h-3.5 w-3.5" />
          </a>
        </header>

        <LuminaHero />
        <LuminaExplorer />

        <section className="mt-8 rounded-[1.75rem] border border-lumina-border/80 glass p-6 section-glow">
          <h3 className="text-lg font-semibold text-lumina-ink">What Lumina Does Right Now</h3>
          <p className="mt-2 max-w-2xl text-sm text-slate-600">
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
                className="rounded-2xl border border-lumina-border/80 bg-white/82 p-4 shadow-soft"
              >
                <Icon className="h-5 w-5 text-cyan-500" />
                <p className="mt-2 text-sm font-semibold text-lumina-ink">{title}</p>
                <p className="mt-1 text-sm text-slate-600">{description}</p>
              </motion.div>
            ))}
          </div>
        </section>

        <footer className="mt-8 border-t border-lumina-border/70 pt-5 text-center text-xs text-slate-500">
          Lumina UI Milestone 1 - A light, celestial interface powered by astronomy datasets and guided AI-style explanations
        </footer>
      </div>
    </main>
  );
}
