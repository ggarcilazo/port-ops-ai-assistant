# ⚓ Port Ops AI Assistant - Asistente de IA para Operaciones Portuarias (Navis N4)

Este repositorio contiene un ecosistema inteligente de nivel consultor senior diseñado para optimizar la inducción técnico-operativa del personal en terminales portuarias. Utiliza una arquitectura de Generación Aumentada por Recuperación (RAG) completamente Serverless y agnóstica a la nube, procesando manuales técnicos complejos y exponiendo las respuestas mediante una interfaz web interactiva de acceso público.

🌐 **Demo en Vivo en la Nube:** [https://streamlit.app](https://port-ops-navis-n4-ai-assistant.streamlit.app/#asistente-de-ia-operaciones-portuarias-navis-n4)

---

## 🏗️ Arquitectura de la Solución y Flujo RAG (Serverless)

<img width="1141" height="1378" alt="arq" src="https://github.com/user-attachments/assets/5b741862-d72c-441d-a72e-db18b6852b76" />

---

## 🛠️ Estructura del Proyecto y Módulos

*   **📁 `app-operario/` (Tus Entregables):** Contiene la lógica del prototipo de la aplicación móvil/web construida en **Streamlit (Python)**. Consume dinámicamente las respuestas estructuradas en la nube.
*   **📁 `docs-tecnicos/` (Entregable Conjunto):** Almacena el manual operativo simulado del software **Navis N4** y la matriz indexada en formato JSON producida por los algoritmos de Inteligencia Artificial.
*   **📁 `documentos-preventa/` (Tus Entregables):** Propuesta técnico-comercial (RFP) enfocada en el análisis FinOps para justificar el Retorno de Inversión (ROI) ante comités directivos.
*   **📄 `motor_ia_puerto.ipynb` (Módulo de tu Compañero):** Cuaderno de **Google Colab** que implementa el pipeline de NLP con **LangChain** para segmentar, limpiar y clasificar los fragmentos semánticos.

---

## 📊 Análisis FinOps: Estimación de Costos Mensuales

Para garantizar un entorno de alta disponibilidad y costo-eficiencia, el sistema se diseñó bajo una arquitectura 100% Serverless, reduciendo costos fijos de servidores encendidos:

| Proveedor Cloud | Servicio Solicitado | Especificación Técnica | Costo Mensual Estimado |
| :--- | :--- | :--- | :--- |
| **Google Cloud** | Cloud Run / Functions | 50,000 invocaciones al mes | \$12.00 USD |
| **Google Cloud** | Cloud Storage | 10 GB de manuales indexados | \$0.30 USD |
| **Cohere / OpenAI** | API de Embeddings y LLM | Procesamiento de tokens consultas | \$15.00 USD |
| **TOTAL INVERSIÓN**| **Infraestructura Mensual**| **Solución Serverless de IA** | **\$27.30 USD** |

---
## 👥 Colaboradores
*   **Joaquín Garcilazo** (`ggarcilazo`) - Consultor de Soluciones, Preventa Cloud & Frontend de IA (Streamlit), Ingeniero de Inteligencia Artificial & Científico de Datos
  
