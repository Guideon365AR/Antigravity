# Recorrido del Proyecto: Asistente de Redacción Administrativa (Guideon Admin)

He concluido con éxito el desarrollo y la adaptación de la aplicación web solicitada. La herramienta ha sido construida para operar localmente en el navegador y proporcionar un entorno **premium** y dinámico para la redacción de notas, orientada a la **Universidad Nacional de Rosario (UNR)**, tomando inspiración directa de `liquid-systems.html`.

## Cambios Realizados

1. **Estructura base y diseño (`app/index.html` y `app/styles.css`)**
   - Implementado un diseño *Glassmorphism* con efectos visuales avanzados utilizando Tailwind CSS.
   - La aplicación fue renombrada a **Guideon Admin**, adaptando textos y locaciones de Córdoba a Rosario.
   - Agregada una malla de fondo asimétrica con gradientes animados sutiles.
   - Creación de botones y tarjetas con sombra, blurs y difuminados para dar una sensación de cristal.

2. **Flujo de Asistente (Onboarding) (`app/app.js`)**
   - Un proceso de configuración al abrir la aplicación por primera vez.
   - Solicita el nombre visible para la firma automágica.
   - La opción de adjuntar una nota anterior, ahora **opcional**, que simula un proceso avanzado de extracción de estilos (hologramas giratorios implementados).

3. **Generador con "Inteligencia Artificial" (Prompting en Lenguaje Natural)**
   - El panel izquierdo de redacción fue rediseñado totalmente: se eliminaron los múltiples campos de formulario (Destinatario, Motivo, Fundamentación).
   - Ahora cuenta con **un único campo de instrucciones**. El usuario ingresa en formato libre lo que quiere redactar (Ej: "Escribe una nota a la decana para pedir vacaciones").
   - El sistema en JS procesa semánticamente este texto y estructura la nota con destreza, localizando el destinatario y distribuyendo el contenido en los párrafos reglamentarios.

4. **Exportación (NUEVO)**
   - **PDF:** Configurado empleando `html2pdf.js`, capturando la hoja en alta calidad conservando el estilo "imprescindible".
   - **DOCX / WORD:** Implementado forzando el tipo MIME `application/msword` con encapsulamiento XML, lo que permite guardar el archivo `.doc` listo para un retoque rápido en Office si fuese necesario.

## Pruebas de Validación

El Agente Navegador ha validado que el flujo está operativo y responde adecuadamente. Aquí presento una demostración y capturas del producto final en uso:

### Grabación de Demostración del Agente
![Demostración en uso](C:\Users\Gustavo\.gemini\antigravity\brain\134203bb-34bf-4e80-b829-e64893424f23\onboarding_and_generate_1774601128949.webp)

### Capturas del Entorno de Redacción
![Vista del Formulario y Previa](C:\Users\Gustavo\.gemini\antigravity\brain\134203bb-34bf-4e80-b829-e64893424f23\note_preview_top_1774601442199.png)

![Renderizado del Saludo final](C:\Users\Gustavo\.gemini\antigravity\brain\134203bb-34bf-4e80-b829-e64893424f23\generated_note_preview_1774601429234.png)

*Para acceder al entorno de forma inmediata, abra el archivo `c:/Users/Gustavo/Desktop/ProQualis/Proyectos SRP/Agente Redacc Admin/app/index.html` en su navegador.*
