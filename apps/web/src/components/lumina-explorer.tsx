"use client";

import { useMemo, useState } from "react";
import { motion } from "framer-motion";
import { Orbit, Search, Sparkle } from "lucide-react";

import { GuideResultCard } from "@/components/guide-result-card";
import { explainGuide } from "@/lib/api";
import type { GuideCategory, GuideExplainRequest, GuideExplainResponse, UserLevel } from "@/types/guide";

const EXAMPLES = [
  "Betelgeuse",
  "Sirius",
  "Polaris",
  "Andromeda Galaxy",
  "Orion Nebula",
  "Pleiades"
];

type FormState = {
  name: string;
  categoryChoice: "auto" | GuideCategory;
  userLevel: UserLevel;
  includeScientificFacts: boolean;
};

export function LuminaExplorer() {
  const [form, setForm] = useState<FormState>({
    name: "",
    categoryChoice: "auto",
    userLevel: "beginner",
    includeScientificFacts: true
  });
  const [result, setResult] = useState<GuideExplainResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const canSubmit = useMemo(() => form.name.trim().length > 0 && !loading, [form.name, loading]);

  async function onSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!canSubmit) return;

    setLoading(true);
    setError(null);

    const payload: GuideExplainRequest = {
      name: form.name.trim(),
      user_level: form.userLevel,
      include_scientific_facts: form.includeScientificFacts
    };

    if (form.categoryChoice !== "auto") {
      payload.category = form.categoryChoice;
    }

    try {
      const response = await explainGuide(payload);
      setResult(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Unexpected error");
      setResult(null);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section id="explorer" className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-[1.02fr_1fr]">
      <motion.form
        initial={{ opacity: 0, y: 14 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.35 }}
        onSubmit={onSubmit}
        className="glass section-glow rounded-[1.75rem] border border-lumina-border/80 p-6 md:p-7"
      >
        <div className="mb-5 flex items-center gap-2 text-lumina-ink">
          <Orbit className="h-5 w-5 text-cyan-500" />
          <h2 className="text-xl font-semibold">Lumina Explorer</h2>
        </div>

        <label className="mb-2 block text-xs font-semibold uppercase tracking-wide text-slate-500">Star or Object Name</label>
        <div className="relative">
          <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-500" />
          <input
            value={form.name}
            onChange={(e) => setForm((prev) => ({ ...prev, name: e.target.value }))}
            placeholder="Try Betelgeuse or Andromeda Galaxy"
            className="w-full rounded-xl border border-lumina-border/90 bg-white/85 py-3 pl-10 pr-3 text-sm text-lumina-ink outline-none transition placeholder:text-slate-400 focus:border-cyan-400/70 focus:shadow-soft"
          />
        </div>

        <div className="mt-5 grid grid-cols-1 gap-4 sm:grid-cols-2">
          <div>
            <label className="mb-2 block text-xs font-semibold uppercase tracking-wide text-slate-500">Category</label>
            <select
              value={form.categoryChoice}
              onChange={(e) =>
                setForm((prev) => ({
                  ...prev,
                  categoryChoice: e.target.value as FormState["categoryChoice"]
                }))
              }
              className="w-full rounded-xl border border-lumina-border/90 bg-white/85 p-3 text-sm text-lumina-ink outline-none transition focus:border-cyan-400/70 focus:shadow-soft"
            >
              <option value="auto">Auto Detect</option>
              <option value="star">Star</option>
              <option value="object">Object</option>
            </select>
          </div>

          <div>
            <label className="mb-2 block text-xs font-semibold uppercase tracking-wide text-slate-500">User Level</label>
            <select
              value={form.userLevel}
              onChange={(e) => setForm((prev) => ({ ...prev, userLevel: e.target.value as UserLevel }))}
              className="w-full rounded-xl border border-lumina-border/90 bg-white/85 p-3 text-sm text-lumina-ink outline-none transition focus:border-cyan-400/70 focus:shadow-soft"
            >
              <option value="beginner">Beginner</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
          </div>
        </div>

        <label className="mt-4 flex items-center gap-2 rounded-xl border border-lumina-border/90 bg-white/85 p-3 text-sm text-lumina-ink">
          <input
            type="checkbox"
            checked={form.includeScientificFacts}
            onChange={(e) => setForm((prev) => ({ ...prev, includeScientificFacts: e.target.checked }))}
            className="h-4 w-4 accent-cyan-500"
          />
          Include scientific fact enrichment
        </label>

        <button
          disabled={!canSubmit}
          className="mt-5 inline-flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-cyan-300 via-sky-300 to-indigo-300 px-4 py-3 text-sm font-semibold text-lumina-navy shadow-soft transition hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-55"
        >
          <Sparkle className="h-4 w-4" />
          {loading ? "Exploring..." : "Generate Guided Explanation"}
        </button>

        <div className="mt-6">
          <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-slate-500">Quick Examples</p>
          <div className="flex flex-wrap gap-2">
            {EXAMPLES.map((name) => (
              <button
                key={name}
                type="button"
                onClick={() => setForm((prev) => ({ ...prev, name }))}
                className="rounded-full border border-lumina-border/85 bg-white/80 px-3 py-1.5 text-xs font-medium text-lumina-ink transition hover:border-cyan-400/70 hover:text-sky-700"
              >
                {name}
              </button>
            ))}
          </div>
        </div>
      </motion.form>

      <div>
        <GuideResultCard result={result} loading={loading} error={error} />
      </div>
    </section>
  );
}
