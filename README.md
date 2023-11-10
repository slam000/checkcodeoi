# README.md para el Proyecto "CheckCodeOI"

## Descripción
CheckCodeOI es una prueba de concepto que utiliza ChatGPT para analizar código Python. El proyecto interactúa con la API de OpenAI para evaluar scripts de Python proporcionados por el usuario. En la carpeta test puedes encontrar scripts que he utilizado durante las pruebas.

## Funcionalidad
- **Comprobación de Ruta de Archivo**: Verifica si el archivo especificado existe y es accesible.
- **Lectura de Contenido de Archivo**: Lee el contenido del archivo de Python proporcionado.
- **Análisis de Código con OpenAI**: Envía el contenido del archivo a la API de OpenAI para su análisis.

## Instalación

### Requisitos Previos
- Python 3.x
- Acceso a la API de OpenAI (requiere una clave API)

### Configuración del Entorno
1. **Crear un Entorno Virtual**:
   ```bash
   python -m venv venv
   ```
2. **Activar el Entorno Virtual**:
   - Windows: `venv\Scripts\activate`
   - Unix o MacOS: `source venv/bin/activate`
3. **Instalar Dependencias**:
   ```bash
   pip install openai
   ```

## Uso

1. **Configurar la Clave API de OpenAI**:
   Establezca su clave API de OpenAI como una variable de entorno `OPENAI_API_KEY`.

2. **Ejecutar el Script**:
   ```bash
   python main.py
   ```

3. **Ingresar la Ruta del Archivo de Python**:
   Cuando se le solicite, ingrese la ruta completa del archivo de Python que desea analizar.

4. **Revisar el Análisis**:
   El script proporcionará un análisis del código Python utilizando la API de OpenAI.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, envíe una solicitud de extracción para las mejoras propuestas.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - vea el archivo LICENSE para más detalles.
