# 📁 Módulo de Interfaz Visual del Operario (Streamlit App)

Este subdirectorio contiene la lógica de frontend interactiva diseñada para el personal operativo del muelle.

## 🚀 Componentes Técnicos

1. **`app.py`**: Código fuente en **Python** que inicializa la interfaz gráfica. Utiliza la librería `requests` para consumir de forma asíncrona la base de datos de conocimiento distribuida en GitHub, evitando acoplamientos y optimizando la velocidad de respuesta.
2. **`requirements.txt` (Raíz)**: Archivo de dependencias que le indica al clúster de servidores de Streamlit en la nube qué paquetes debe aprovisionar de forma automática para mantener la app en línea.

## 💻 Ejecución de Pruebas Locales

Si desea levantar este módulo en su entorno de desarrollo local, ejecute los siguientes comandos en su terminal:
```bash
pip install streamlit requests
streamlit run app-operario/app.py
```
