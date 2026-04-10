import type { GuideExplainRequest, GuideExplainResponse, GuideExplainSuccess } from "@/types/guide";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://127.0.0.1:8000";

export async function explainGuide(payload: GuideExplainRequest): Promise<GuideExplainResponse> {
  const response = await fetch(`${API_BASE_URL}/api/v1/guide/explain`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload),
    cache: "no-store"
  });

  const data = (await response.json()) as GuideExplainResponse;

  if (response.ok) {
    return data as GuideExplainSuccess;
  }

  if (response.status === 404) {
    return data;
  }

  throw new Error("Lumina could not process the request right now. Please try again.");
}
