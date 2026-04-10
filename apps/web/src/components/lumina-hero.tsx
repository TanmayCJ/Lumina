"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import { Sparkles, Telescope } from "lucide-react";

export function LuminaHero() {
  return (
    <section className="relative overflow-hidden rounded-[2rem] border border-lumina-border/70 glass p-8 md:p-12 section-glow">
      <motion.div
        initial={{ opacity: 0, y: 16 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: "easeOut" }}
        className="relative z-10 grid gap-8 lg:grid-cols-[1.2fr_0.8fr] lg:items-center"
      >
        <div>
          <div className="mb-5 inline-flex items-center gap-2 rounded-full border border-cyan-300/40 bg-cyan-100/60 px-3 py-1 text-xs font-semibold tracking-wide text-lumina-navy">
            <Sparkles className="h-3.5 w-3.5" />
            Intelligent Star Guide
          </div>
          <h1 className="max-w-3xl text-3xl font-semibold leading-tight text-lumina-ink md:text-5xl md:leading-tight">
            A Luminous Way to <span className="text-gradient">Understand the Cosmos</span>
          </h1>
          <p className="mt-5 max-w-2xl text-sm leading-relaxed text-slate-600 md:text-base">
            Explore stars and celestial objects through structured datasets and guided explanations designed for every
            learning level. Lumina blends scientific clarity with calm, premium product design.
          </p>
          <div className="mt-8 inline-flex items-center gap-2 rounded-xl border border-lumina-border/80 bg-white/75 px-4 py-2 text-sm text-lumina-ink shadow-soft">
            <Telescope className="h-4 w-4 text-cyan-500" />
            Powered by astronomy datasets + guided AI-style reasoning
          </div>
        </div>

        <div className="relative mx-auto max-w-sm rounded-3xl border border-lumina-border/80 bg-white/80 p-5 shadow-card">
          <div className="pointer-events-none absolute -right-8 -top-8 h-28 w-28 rounded-full bg-cyan-300/30 blur-2xl" />
          <div className="pointer-events-none absolute -bottom-8 -left-8 h-24 w-24 rounded-full bg-violet-300/35 blur-2xl" />
          <Image
            src="/images/lumina-logo.png"
            alt="Lumina logo"
            width={640}
            height={360}
            className="relative z-10 h-auto w-full rounded-2xl"
            priority
          />
        </div>
      </motion.div>
      <div className="pointer-events-none absolute -right-20 -top-20 h-72 w-72 rounded-full bg-cyan-200/55 blur-3xl" />
      <div className="pointer-events-none absolute -bottom-24 left-1/3 h-72 w-72 rounded-full bg-indigo-200/60 blur-3xl" />
    </section>
  );
}
