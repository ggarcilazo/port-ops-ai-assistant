# ⚓ PROPUESTA TÉCNICO-ECONÓMICA: ASISTENTE DE IA GENERATIVA PORTUARIA

## 1. Resumen del Caso de Negocio
*   **Cliente:** Terminal Portuaria Operativa (Muelle de Contenedores).
*   **Problema:** Altos costos en tiempos de inducción de personal nuevo y riesgos de paralización del muelle por errores en el uso del software Navis N4.
*   **Solución:** Despliegue de un asistente inteligente con arquitectura RAG Serverless para consultas técnicas y protocolos de emergencia en tiempo real en el muelle.

## 2. Análisis Financiero FinOps (Costo Mensual Cloud)
Para eliminar los costos fijos de servidores encendidos las 24 horas, la solución se estructuró bajo una arquitectura Serverless en la nube, donde solo se factura por los milisegundos exactos de uso:

| Proveedor Cloud | Servicio Solicitado | Especificación Técnica | Costo Mensual Estimado |
| :--- | :--- | :--- | :--- |
| **Google Cloud** | Cloud Run / Functions | 50,000 invocaciones al mes | \$12.00 USD |
| **Google Cloud** | Cloud Storage | 10 GB de manuales indexados | \$0.30 USD |
| **Cohere / OpenAI** | API de Embeddings y LLM | Procesamiento de tokens consultas | \$15.00 USD |
| **TOTAL INVERSIÓN**| **Infraestructura Mensual**| **Solución Serverless de IA** | **\$27.30 USD** |

## 3. Matriz de Riesgos y Mitigación (Framework ITIL)
*   **Riesgo:** Alucinación de la IA en respuestas de seguridad críticas en el muelle.
*   **Mitigación:** Implementación del patrón RAG (Generación Aumentada por Recuperación), forzando a la IA a responder *únicamente* basándose en el manual técnico proveído (`manual_navis_n4.txt`), bloqueando respuestas externas de internet.
