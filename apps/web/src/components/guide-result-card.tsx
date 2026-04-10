"use client";

import { motion } from "framer-motion";
import { AlertCircle, CheckCircle2, Info, Sparkles } from "lucide-react";

import type { GuideExplainResponse } from "@/types/guide";

type GuideResultCardProps = {
  result: GuideExplainResponse | null;
  loading: boolean;
  error: string | null;
};

function FactPill({ label, value }: { label: string; value: string }) {
  return (
    <div className="rounded-xl border border-lumina-border/90 bg-white/85 px-3 py-2 shadow-soft">
      <p className="text-[11px] font-semibold uppercase tracking-wide text-slate-500">{label}</p>
      <p className="mt-1 text-sm font-medium text-lumina-ink">{value}</p>
    </div>
  );
}

export function GuideResultCard({ result, loading, error }: GuideResultCardProps) {
  if (loading) {
    return (
      <div className="glass section-glow rounded-[1.75rem] border border-lumina-border/80 p-6">
        <div className="mb-4 h-6 w-2/5 animate-pulse rounded bg-slate-200" />
        <div className="grid grid-cols-1 gap-3 md:grid-cols-2">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="h-16 animate-pulse rounded-xl bg-slate-200" />
          ))}
        </div>
        <div className="mt-4 h-20 animate-pulse rounded-xl bg-slate-200" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="rounded-[1.75rem] border border-rose-300/50 bg-rose-50 p-6 text-rose-700 shadow-card">
        <div className="mb-2 flex items-center gap-2 text-sm font-semibold">
          <AlertCircle className="h-4 w-4" />
          Request Error
        </div>
        <p className="text-sm text-rose-700/90">{error}</p>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="glass section-glow rounded-[1.75rem] border border-lumina-border/80 p-8 text-center">
        <Sparkles className="mx-auto mb-3 h-6 w-6 text-cyan-500" />
        <p className="text-base font-semibold text-lumina-ink">Ready to explore the cosmos?</p>
        <p className="mx-auto mt-2 max-w-md text-sm text-slate-600">
          Ask Lumina about a star or celestial object to see structured facts and a guided educational explanation.
        </p>
      </div>
    );
  }

  if (result.status === "not_found") {
    return (
      <div className="rounded-[1.75rem] border border-amber-300/45 bg-amber-50 p-6 text-amber-700 shadow-card">
        <div className="mb-2 flex items-center gap-2 text-sm font-semibold">
          <Info className="h-4 w-4" />
          No Match Found
        </div>
        <p className="text-sm text-amber-700/90">{result.explanation}</p>
      </div>
    );
  }

  const data = result.data;

  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.35 }}
      className="glass section-glow rounded-[1.75rem] border border-lumina-border/80 p-6"
    >
      <div className="mb-4 flex flex-wrap items-center gap-2">
        <span className="inline-flex items-center gap-2 rounded-full border border-emerald-300/60 bg-emerald-50 px-3 py-1 text-xs font-semibold text-emerald-700">
          <CheckCircle2 className="h-3.5 w-3.5" />
          Match Found
        </span>
        <span className="rounded-full border border-cyan-300/70 bg-cyan-50 px-3 py-1 text-xs font-medium text-cyan-700">
          {data.category}
        </span>
      </div>

      <h3 className="text-2xl font-semibold text-lumina-ink">{data.name}</h3>

      <div className="mt-4 grid grid-cols-1 gap-3 md:grid-cols-2">
        {data.constellation ? <FactPill label="Constellation" value={data.constellation} /> : null}
        {typeof data.distance_light_years === "number" ? (
          <FactPill label="Distance" value={`${data.distance_light_years} light-years`} />
        ) : null}
        {"magnitude" in data && typeof data.magnitude === "number" ? (
          <FactPill label="Magnitude" value={`${data.magnitude}`} />
        ) : null}
        {"spectral_type" in data && data.spectral_type ? <FactPill label="Spectral Type" value={data.spectral_type} /> : null}
        {"object_type" in data && data.object_type ? <FactPill label="Object Type" value={data.object_type} /> : null}
      </div>

      {data.description ? (
        <p className="mt-5 rounded-xl border border-lumina-border/90 bg-white/80 px-4 py-3 text-sm text-slate-700">
          {data.description}
        </p>
      ) : null}

      <div className="mt-5 rounded-xl border border-lumina-border/90 bg-white/80 px-4 py-4">
        <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">Guided Explanation</p>
        <p className="mt-2 text-sm leading-relaxed text-slate-700">{result.explanation}</p>
      </div>

      <div className="mt-5">
        <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">Key Facts</p>
        <ul className="mt-2 space-y-2">
          {result.key_facts.map((fact) => (
            <li key={fact} className="rounded-lg border border-lumina-border/90 bg-white/80 px-3 py-2 text-sm text-slate-700">
              {fact}
            </li>
          ))}
        </ul>
      </div>
    </motion.div>
  );
}
