"use client";

import { motion } from "framer-motion";
import { Sparkles, Telescope } from "lucide-react";

export function LuminaHero() {
  return (
    <section className="relative overflow-hidden rounded-3xl border border-lumina-border/50 glass p-8 md:p-12 section-glow">
      <motion.div
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="relative z-10"
      >
        <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-cyan-300/20 bg-cyan-300/10 px-3 py-1 text-xs font-medium tracking-wide text-cyan-200">
          <Sparkles className="h-3.5 w-3.5" />
          Lumina Milestone UI
        </div>
        <h1 className="max-w-3xl text-3xl font-semibold leading-tight md:text-5xl md:leading-tight">
          Your Guided Window Into the <span className="text-gradient">Living Night Sky</span>
        </h1>
        <p className="mt-5 max-w-2xl text-sm text-slate-300 md:text-base">
          Search stars and celestial objects through Lumina&apos;s curated astronomy datasets and receive guided,
          level-aware explanations crafted for learning and exploration.
        </p>
        <div className="mt-8 inline-flex items-center gap-2 rounded-xl border border-lumina-border/70 bg-lumina-panel/50 px-4 py-2 text-sm text-slate-200">
          <Telescope className="h-4 w-4 text-cyan-300" />
          Powered by local datasets + AI-style guidance logic
        </div>
      </motion.div>
      <div className="pointer-events-none absolute -right-20 -top-20 h-72 w-72 rounded-full bg-blue-500/20 blur-3xl" />
      <div className="pointer-events-none absolute -bottom-24 left-1/3 h-72 w-72 rounded-full bg-violet-400/20 blur-3xl" />
    </section>
  );
}
