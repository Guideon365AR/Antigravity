# Plan de Implementación: Sección de Gestión de Inventario y EPP

## Descripción del Objetivo
Agregar una nueva sección principal al prototipo (`IGNEALIS_Prototipo_v3.html`) destinada a la gestión completa del inventario, equipamiento sensible y Elementos de Protección Personal (EPP), tal como se especifica en el documento `A Implementar.txt`.

## Cambios Propuestos

### Modificaciones en el HTML (`IGNEALIS_Prototipo_v3.html`)

1. **Barra de Navegación (Sidebar)**:
   - Se agregará un nuevo botón en la barra lateral izquierda, justo debajo de "Vehículos y Equipamiento", llamado **"Inventario y EPP"** que apuntará a un nuevo `div` con ID `s-inventario`.
   - Se le añadirá un icono acorde a inventario/seguridad (por ejemplo, un escudo o caja de herramientas).

2. **Nueva Pantalla (`s-inventario`)**:
   - Se creará un nuevo contenedor `<div id="s-inventario" class="screen max-w-7xl mx-auto p-8">` siguiendo la estética de diseño "Dark/Aura Edition" con gradientes, bordes translúcidos y desenfoque (backdrop-blur).
   - **Encabezado**: Título "Gestión de Inventario y EPP".
   - **Métricas Superiores**: Tarjetas mostrando estadísticas rápidas (ej. EPP Asignados, Equipos Sensibles en Mantenimiento, Total de Herramientas).
   - **Grid Principal**: El contenido se dividirá en módulos que cubrirán todos los aspectos mencionados en el documento:
     - **EPP - Equipo Estructural**: Control de stock y asignaciones de chaquetones, cascos, monjitas, guantes, etc. Se mostrará una tabla o lista con estados de vida útil. Incluirá la clasificación por Niveles de Protección (EPI Nivel 1, 2 y 3).
     - **Equipamiento Sensible**: Panel específico para equipos de alta tecnología (Cámaras térmicas, ERA, detectores de gases, equipos hidráulicos) con alertas de calibración/mantenimiento.
     - **Inventario Básico (Vehículo/Parque)**: Gestión de mangueras, lanzas, y herramientas de entrada forzada, permitiendo ver qué elemento pertenece a qué vehículo.

3. **Lógica JS**:
   - No se requiere JavaScript adicional complejo; la nueva pantalla se integrará de forma automática gracias al script de navegación por atributos `data-screen` ya existente en el final del archivo HTML.

## Plan de Verificación

### Verificación Manual
1. Abrir `IGNEALIS_Prototipo_v3.html` en un navegador web.
2. Hacer clic en el nuevo botón "Inventario y EPP" en el menú lateral.
3. Comprobar que la vista cambia correctamente a la nueva sección sin errores visuales.
4. Validar que la estética (colores, espaciados y tipografías) sea consistente con el resto del prototipo.
5. Comprobar que todas las categorías del documento original (`A Implementar.txt`) se vean representadas de forma clara y organizadas.
6. Probar la navegación hacia otra pestaña y volver a la nueva sección para asegurar que el sistema de pantallas SPA funcione sin problemas.
