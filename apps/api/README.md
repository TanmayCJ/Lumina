# Lumina API - Milestone 1

FastAPI backend milestone for Lumina's guided astronomy feature.

## Scope

- Curated local datasets for stars and celestial objects
- Search and detail endpoints for stars and objects
- Guided explanation endpoint with user-level adaptation
- Fully testable OpenAPI/Swagger documentation

## Directory Map

```text
apps/api
|-- README.md
|-- requirements.txt
`-- src
    |-- main.py
    |-- api/routers
    |   |-- health.py
    |   |-- stars.py
    |   |-- objects.py
    |   `-- guide.py
    |-- core
    |   |-- config.py
    |   `-- exceptions.py
    |-- models
    |   |-- common.py
    |   |-- health.py
    |   |-- stars.py
    |   |-- objects.py
    |   `-- guide.py
    |-- services
    |   |-- data_loader.py
    |   |-- stars_service.py
    |   |-- objects_service.py
    |   |-- guide_service.py
    |   `-- utils.py
    `-- data
        |-- stars.json
        `-- objects.json
```

## Datasets

- stars.json contains 12 curated stars
- objects.json contains 12 curated deep-sky objects

Included examples:
- Sirius, Betelgeuse, Polaris, Vega, Proxima Centauri
- Andromeda Galaxy, Orion Nebula, Pleiades, Sombrero Galaxy, Ring Nebula

## Endpoints

- GET /health
- GET /api/v1/stars
- GET /api/v1/stars/{star_id}
- POST /api/v1/stars/search
- GET /api/v1/objects
- GET /api/v1/objects/{object_id}
- POST /api/v1/objects/search
- POST /api/v1/guide/explain

## Guide Request Example

```json
{
  "name": "Betelgeuse",
  "category": "star",
  "user_level": "beginner",
  "include_scientific_facts": true
}
```

Notes:
- category can be omitted for auto-detection
- supported user levels: beginner, intermediate, advanced

## Run Locally

1. Install dependencies:

```bash
pip install -r apps/api/requirements.txt
```

2. Start the server:

```bash
uvicorn apps.api.src.main:app --reload
```

3. Open Swagger UI:

- http://127.0.0.1:8000/docs

4. Open OpenAPI JSON:

- http://127.0.0.1:8000/openapi.json
