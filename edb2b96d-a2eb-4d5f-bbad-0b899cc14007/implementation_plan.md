# Eliminar Pantallas Secundarias

El objetivo es simplificar la interfaz dejando únicamente el "Centro de Control" (Dashboard), eliminando las pantallas de "Nueva Intervención", "Personal" y "Novedades".

## Proposed Changes

### Interfaz Principal
#### [MODIFY] ultmo ignealis.html
- Eliminar de `<nav id="nav">` los botones correspondientes a `s-intervencion`, `s-personal` y `s-novedades`.
- Eliminar los bloques HTML completos de `<div id="s-intervencion">`, `<div id="s-personal">` y `<div id="s-novedades">`.
- Simplificar el bloque de Javascript final (`<script>`), eliminando las animaciones que hacían referencia a los `id` de la pantalla de intervención que será eliminada, y manteniendo solo la lógica de animación para el Dashboard.

## Verification Plan

### Manual Verification
- Cargar el archivo en el navegador y verificar que la barra lateral solo muestre la opción del "Centro de Control".
- Verificar visualmente que no queden rastros de las pantallas eliminadas y que la pantalla actual se vea completa.
- Comprobar la consola del navegador (`F12`) para asegurar que el Javascript no tire errores por elementos no encontrados (ej. animaciones referenciando elementos borrados).
