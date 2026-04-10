export type GuideCategory = "star" | "object";
export type UserLevel = "beginner" | "intermediate" | "advanced";

export interface GuideExplainRequest {
  name: string;
  category?: GuideCategory;
  user_level: UserLevel;
  include_scientific_facts: boolean;
}

export interface StarData {
  id: number;
  name: string;
  category: "star";
  constellation?: string;
  distance_light_years?: number;
  magnitude?: number;
  spectral_type?: string;
  description?: string;
}

export interface ObjectData {
  id: number;
  name: string;
  category: "object";
  object_type?: string;
  constellation?: string;
  distance_light_years?: number;
  description?: string;
}

export type GuideData = StarData | ObjectData;

export interface GuideExplainSuccess {
  status: "success";
  object_found: true;
  data: GuideData;
  explanation: string;
  key_facts: string[];
}

export interface GuideExplainNotFound {
  status: "not_found";
  object_found: false;
  data: null;
  explanation: string;
  key_facts: string[];
}

export type GuideExplainResponse = GuideExplainSuccess | GuideExplainNotFound;
