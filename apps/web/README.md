# Lumina Web UI - Milestone 1

Premium frontend interface for Lumina's guided astronomy backend.

## Implemented Scope

- Sleek astronomy-inspired landing and hero experience
- Core interactive explorer form connected to backend guide endpoint
- Structured result panel with facts, explanation, and key facts
- Quick example prompts for instant testing
- Loading, empty, not-found, and error states
- Responsive, dark-first design with subtle motion

## Tech Stack

- Next.js (App Router) + React + TypeScript
- Tailwind CSS
- Framer Motion
- Lucide React icons

## Backend Dependency

This frontend expects your FastAPI backend to be running locally.

Default backend URL:
- `http://127.0.0.1:8000`

Configured via:
- `NEXT_PUBLIC_API_BASE_URL` in `.env.local`

## Local Setup

1. Create env file:

```bash
cp .env.example .env.local
```

2. Install dependencies:

```bash
npm install
```

3. Start frontend:

```bash
npm run dev
```

4. Open in browser:

- `http://localhost:3000`

## Run With Backend

1. Start backend from repository root:

```bash
uvicorn apps.api.src.main:app --reload
```

2. Confirm backend docs:

- `http://127.0.0.1:8000/docs`

3. Start frontend (`apps/web`):

```bash
npm run dev
```

4. Test the main UI flow:

- Use quick examples like `Betelgeuse` or `Andromeda Galaxy`
- Or submit custom query in the explorer form

## Current Endpoint Used by UI

- `POST /api/v1/guide/explain`

The UI is intentionally focused on the first product milestone and can be extended later for stars/objects listing workflows.
