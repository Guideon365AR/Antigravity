# Plan de Implementación: Aplicación Lista de Tareas Pendientes

Este plan describe los pasos para construir una aplicación web que replica fielmente el diseño gráfico del archivo "Tareas pendientes 1.pdf".

## Objetivo
Crear una aplicación funcional de lista de tareas que mantenga la estética visual del PDF (estilo "brutalista" o geométrico, bordes gruesos, paleta de colores crema/negro/acentos).

## Diseño Visual
Basado en el análisis del PDF:
- **Paleta de Colores**:
  - Fondo Global: Crema (#F5EFE6)
  - Acentos: Rojo (#FF0000 - Alta), Naranja (#FFB347 - Media), Verde (#00C853 - Baja)
  - Texto/Bordes: Negro (#000000)
  - Color de fondo fechas: Negro (#000000) con texto blanco.
- **Tipografía**: Sans-serif, geométrica y audaz (p.ej., Montserrat, Roboto o Futura).
- **Estilo**: Bordes negros gruesos, alto contraste, diseño de cuadrícula.

## Estructura de Archivos

### Frontend
- [ ] `index.html`: Estructura semántica.
- [ ] `style.css`: Estilos personalizados (Vanilla CSS) para control total del diseño.
- [ ] `script.js`: Lógica para manejar tareas (agregar, marcar como completada, notas).

## Tareas Detalladas

### 1. Estructura HTML (`index.html`)
- Contenedor principal con borde punteado (simulando el diseño).
- Encabezado "LISTA DE TAREAS PENDIENTES".
- Leyenda de prioridades.
- Tabla/Lista de tareas con columnas: Fecha, Prioridad, Tarea, Quién, En Curso, Listo.
- Sección de Notas al pie.

### 2. Estilos CSS (`style.css`)
- Implementar el fondo crema.
- Crear las clases de utilidad para los puntos de prioridad (rojo, naranja, verde).
- Estilizar la tabla de tareas:
  - Primera columna (Fecha) con fondo negro y texto blanco.
  - Bordes negros sólidos entre celdas.
- Estilizar los checkboxes personalizados (estilo visual del PDF: checks grandes).
- Tipografía fuerte para los encabezados.

### 3. Funcionalidad JS (`script.js`)
- Array de datos inicial con los datos del PDF (como ejemplo).
- Renderizado dinámico de la lista de tareas.
- (Opcional) Funcionalidad para marcar checks.

## Verificación
- Comparar visualmente el resultado con el PDF original.
- Verificar que la responsividad sea adecuada (o mantener diseño fijo tipo "papel" si se prefiere fidelidad al PDF).
