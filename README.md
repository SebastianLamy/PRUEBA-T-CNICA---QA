# PRUEBA-T-ECNICA---QA


## Requisitos
- Docker & Docker Compose


## Ejecutar todo
docker compose up --build


## Ejecutar solo API tests
docker compose run --rm api-tests


## Ejecutar E2E
docker compose run --rm e2e-tests


## Ejecutar k6 (local)
docker compose run --rm k6-jsonplaceholder