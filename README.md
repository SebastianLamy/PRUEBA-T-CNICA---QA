````markdown
# Automatización de Pruebas QA — APIs, E2E y Performance  

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)  
![Pytest](https://img.shields.io/badge/Pytest-Framework-green?logo=pytest)  
![Playwright](https://img.shields.io/badge/Playwright-E2E%20Testing-purple?logo=microsoft-edge)  
![k6](https://img.shields.io/badge/k6-Performance-orange?logo=k6)  
![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)  
![Build](https://img.shields.io/badge/Build-Passing-success)  

---

Este proyecto implementa una **suite completa de automatización de pruebas** para validar APIs públicas, flujos end-to-end en una aplicación web y pruebas de rendimiento.  
El entorno está completamente **dockerizado**, permitiendo ejecutar todas las pruebas con un solo comando:  

```bash
docker compose up
````

---

## Estructura del Repositorio

```
PRUEBA-TÉCNICA-QA/
│
├── src/
│   ├── api_tests/        # Pruebas automatizadas de API (JSONPlaceholder, ReqRes)
│   ├── e2e_tests/        # Pruebas E2E (The Internet - Herokuapp)
│   ├── performance/      # Pruebas de carga y stress (k6)
│   └── utils/            # Utilidades, validadores, configuración
│
├── Dockerfile            # Imagen para ejecutar los tests
├── docker-compose.yml    # Orquestación del entorno completo
├── requirements.txt      # Dependencias de Python
├── pytest.ini            # Configuración global de pytest
├── report.html           # Reporte generado tras la ejecución
└── README.md             # Documentación técnica
```

---

## Ejecución con Docker

>  Requisitos previos:
>
> * Docker y Docker Compose instalados
> * Puerto 8080 disponible

### 1️ Construir e iniciar el entorno

```bash
docker compose up --build
```

### 2️ Ver resultados

* Los resultados de **pytest** se generarán automáticamente en `report.html`
* Los logs de consola mostrarán el resumen de las pruebas ejecutadas
* Los scripts de rendimiento (`k6`) pueden verse en la carpeta `src/performance`

### 3️ Detener los contenedores

```bash
docker compose down
```

---

## Ejecución manual (sin Docker)

Si prefieres ejecutar localmente:

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar pruebas API

```bash
pytest src/api_tests/ --html=report.html --self-contained-html
```

### Ejecutar pruebas E2E

```bash
pytest src/e2e_tests/
```

### Ejecutar pruebas de rendimiento

```bash
k6 run src/performance/test_load.js
```

---

## Herramientas Utilizadas

| Tipo de prueba | Herramienta                 | Descripción                                           |
| -------------- | --------------------------- | ----------------------------------------------------- |
| API Testing    | **pytest + requests**       | Validación de endpoints, esquemas y códigos de estado |
| E2E Testing    | **Playwright / Selenium**   | Automatización del flujo de usuario en UI             |
| Performance    | **k6**                      | Pruebas de carga, stress y métricas de latencia       |
| Orquestación   | **Docker + Docker Compose** | Entorno reproducible y aislado                        |
| Reportes       | **pytest-html**             | Generación de reportes visuales                       |

---

## Organización de Pruebas

### 🔹 API Tests

* CRUD completo en `/posts` (GET, POST, PUT, DELETE)
* Validación de esquemas JSON y tipos de datos
* Casos negativos y performance básico

### 🔹 E2E Tests

* Login, subida/descarga de archivos
* Elementos dinámicos y drag & drop
* Validaciones visuales y de interacción

### 🔹 Performance Tests

* Carga concurrente en JSONPlaceholder, ReqRes y Swagger Petstore
* Métricas: tiempo promedio, percentil 95, throughput y errores

---

### Basado en:

* [JSONPlaceholder](https://jsonplaceholder.typicode.com/)
* [ReqRes](https://reqres.in/)
* [The Internet - Herokuapp](https://the-internet.herokuapp.com/)
* [Swagger Petstore](https://petstore.swagger.io/)

```

