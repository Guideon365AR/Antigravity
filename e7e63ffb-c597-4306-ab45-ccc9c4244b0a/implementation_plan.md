# Plan de Implementación: Gestión Móvil SRP (Fase 1 - MVP)

Este documento detalla el diseño técnico e implementación del MVP (Fase 1) para **Gestión Móvil SRP**, una aplicación móvil nativa (diseñada en React Native / Expo) orientada al Servicio de Resguardo Patrimonial de la Universidad Nacional de Rosario (UNR). 

La aplicación se construirá bajo la metodología **Offline-First**, permitiendo a los encargados registrar inasistencias, novedades generales y gestionar equipos de trabajo en campo sin necesidad de conectividad permanente, sincronizándose de forma inteligente al recuperar la señal.

---

## 🌟 Enfoque de Diseño y Experiencia de Usuario Premium
Para garantizar un producto de nivel profesional que asombre al usuario, implementaremos una estética premium inspirada en las mejores prácticas de diseño contemporáneo:
*   **Esquema de Colores HSL Armonioso:** Utilizaremos un modo oscuro profundo por defecto (sleek dark mode) combinado con tonos de azul UNR y acentos vibrantes de verde (para estados en línea/sincronizados), amarillo (cola de sync pendiente) y rojo (errores o ausencias).
*   **Efectos de Vidrio Esmerilado (Glassmorphism):** Menús, tarjetas de agentes y modales flotantes contarán con sutiles transparencias con desenfoque de fondo y bordes pulidos.
*   **Micro-animaciones Fluidas:** Transiciones suaves al cambiar de pantalla, indicadores de sincronización animados y efectos dinámicos al presionar botones y tarjetas de agentes.
*   **Tipografía Moderna:** Integración de fuentes limpias y profesionales (como Inter o Roboto) para garantizar una legibilidad excelente en campo.

---

## 🛠️ Stack Tecnológico Propuesto
De acuerdo con las especificaciones técnicas recomendadas en la SDD:
1.  **Framework Base:** React Native con **Expo** (permite ejecución cruzada en Android, iOS y Web).
2.  **Gestión de Estado:** **Zustand** para el estado global de la app, estado del turno, cola de sincronización y logs.
3.  **Persistencia Local:** Simulación y persistencia local mediante `AsyncStorage` / SQLite mock integrado en Zustand para asegurar un comportamiento offline 100% fiable y testeable.
4.  **Iconografía:** Lucide React Native / Expo Vector Icons para controles limpios y modernos.
5.  **Entorno de Ejecución:** Contenedor de **Docker** montado sobre el espacio de trabajo para evitar la necesidad de instalar dependencias de Node.js de manera local en Windows. Se proporcionará un script `run.bat` para iniciar el servidor de desarrollo de Expo con un solo clic.

---

## 📋 Arquitectura de Pantallas (Flujo Completo del MVP)

Construiremos un flujo continuo que recorre las **13 pantallas del diseño** (SCR-01 a SCR-13):

1.  **SCR-01 (Login Premium):** Formulario con credenciales de encargado, validación interactiva, logo estilizado de SRP-UNR e indicador de carga fluida.
2.  **SCR-02 (Selector de Áreas):** Si el encargado está asignado a múltiples secciones, una rejilla de tarjetas con efecto "glassmorphic" permite seleccionar la sección activa.
3.  **SCR-03 (Inicio de Turno - Turn Start Screen):** **¡PANTALLA OBLIGATORIA!** Al ingresar en el horario de un turno (o 15 minutos antes), esta pantalla bloquea el resto de la aplicación (tanto online como offline) hasta que el equipo sea aprobado o modificado. Muestra los detalles del turno base y el listado de agentes asignados.
4.  **SCR-03b (Modificación de Equipo):** Permite al encargado:
    *   Marcar a un agente como "no se presentó" (lo cual autogenera un registro de inasistencia injustificada editable).
    *   Reasignar objetivos operativos (para las secciones matriciales: CUR, Área Salud, Veterinarias y Agrarias) como puntos de control, funciones específicas y prioridades.
    *   Agregar agentes de refuerzo ad-hoc a partir de un listado de disponibles.
    *   Remover temporalmente agentes del turno.
5.  **SCR-04 (Dashboard de Sección):** Panel principal del encargado que muestra la sección activa, el turno actual y el listado interactivo de agentes de guardia.
    *   **Barra de Estado de Conectividad Superior Permanente:** 
        *   🟢 **Verde:** Conectado y Sincronizado.
        *   🟡 **Amarillo:** Sin conexión, con registros pendientes en la cola local de sincronización.
        *   🔴 **Rojo:** Error de sincronización o conflicto pendiente.
6.  **SCR-05 & SCR-06 (Nueva Inasistencia y Confirmación):** Formulario guiado donde al seleccionar un agente ausente se elige el tipo (Justificada, Injustificada o Irregularidad con sus respectivos subtipos y justificaciones de texto obligatorio con validación de caracteres), y una pantalla final de confirmación antes de guardar.
7.  **SCR-07 & SCR-08 (Historial y Detalle de Inasistencias):** Historial filtrable de los últimos 30 días con indicadores visuales del estado de sincronización (PENDING / SYNCED / ERROR) y vista al detalle de cada registro.
8.  **SCR-12 & SCR-13 (Nueva Novedad e Historial de Novedades):** Registro de novedades operativas (Asunto, Objetivo, Descripción) con persistencia offline, confirmación mediante mecanismo **ACK** (HTTP 201 o HTTP 409 para duplicados) y cola de reintentos (máximo 5).
9.  **SCR-11 (Panel de Control y Ajustes):** Pantalla especial que incluye:
    *   **Simulador de Conectividad Avanzado:** Un interruptor interactivo para simular pérdida de red, forzar latencia o inducir errores del servidor (HTTP 500 o HTTP 409). ¡Ideal para probar y demostrar el comportamiento offline-first!
    *   **Gestor de Cola de Sincronización:** Muestra en tiempo real los elementos en cola (`PENDING_SYNC`) y permite forzar una sincronización manual mediante un botón de acción.
    *   **Visor de Logs de Sync:** Registro detallado de operaciones de red y confirmaciones ACK en tiempo real.

---

## 🔌 Motor Offline-First y Mecanismo de Sincronización (Sync Engine)

Implementaremos un módulo centralizado (`SyncEngine`) para gestionar la cola de operaciones:
1.  **Cola de Operaciones Local (`sync_queue`):** Cada inasistencia, aprobación de turno o novedad guardada se registra inmediatamente en la persistencia local con estado `PENDING` y se encola.
2.  **Mecanismo de Sincronización Automática:** Un proceso en segundo plano monitorea el estado de la red. Al recuperar la conectividad (`ONLINE`), procesa la cola de manera secuencial (FIFO):
    *   Envía la operación al backend simulado.
    *   **Confirmación por ACK:** Si el servidor responde exitosamente (HTTP 201 + `ack: true`), el registro local se actualiza a `SYNCED` / `CONFIRMED`.
    *   **Manejo de Duplicados (Idempotencia):** Si se recibe un error de duplicado (HTTP 409), se interpreta como un ACK positivo previo y el registro se marca como sincronizado para evitar la duplicidad de datos en la central.
    *   **Control de Reintentos:** En caso de fallas temporales de red, el reintento se pospone e incrementa el contador (`retry_count` hasta un máximo de 5).

---

## 📂 Estructura del Código del Proyecto

Se creará una estructura modular y escalable para la aplicación React Native:

```
SrpMovil/
├── docker-compose.yml       # Orquestación del contenedor de Node/Expo
├── run.bat                  # Script de inicio rápido en Windows para Docker
├── package.json             # Dependencias del proyecto Expo
├── App.tsx                  # Punto de entrada de la aplicación
└── src/
    ├── theme/               # Diseño visual premium (colores HSL, tipografía, estilos base)
    ├── store/               # Estados globales Zustand (Auth, Turno, SyncQueue, Logs, Conectividad)
    ├── services/            # Clientes de API, Mock Database y Motor de Sincronización (SyncEngine)
    ├── components/          # Componentes visuales reutilizables (Botones, GlassCard, StatusBar, Modales)
    └── screens/             # Implementación de las 13 pantallas requeridas (SCR-01 a SCR-13)
```

---

## 🧪 Plan de Verificación y Pruebas

Para asegurar la máxima calidad y robustez, realizaremos pruebas en los siguientes escenarios:

### 1. Pruebas de Flujo Funcional (Aceptación)
*   **Inicio de Turno Obligatorio:** Verificar que la app bloquea el acceso a cualquier otra pantalla hasta aprobar o modificar el equipo de guardia (tanto en modo online como offline).
*   **Flujo de Inasistencias:** Comprobar que registrar una inasistencia de tipo *Justificada* requiere obligatoriamente una descripción de mínimo 5 caracteres, mientras que una *Irregularidad* despliega correctamente el selector de subtipos.
*   **Gestión de Equipos Matriciales:** Verificar que en las secciones especiales (CUR, Salud, Vet, Agr) se habilitan las opciones para reasignar objetivos y prioridades.

### 2. Pruebas de Resiliencia Offline (Offline-First)
*   **Simulación de Pérdida de Conectividad:** Usando el **Simulador de Conectividad** en los Ajustes, desactivar la red y registrar inasistencias y novedades. Verificar que:
    1. La barra superior cambia a amarillo (Offline).
    2. Los registros se guardan instantáneamente de forma local (<200 ms).
    3. La lista del historial muestra el estado en "Pendiente".
*   **Sincronización Automática al Reconectar:** Activar la red en el simulador. Confirmar que la app procesa la cola de inmediato, la barra superior se ilumina en verde (Sincronizado) y los registros cambian a estado "Sincronizado / Confirmado".
*   **Prueba de Idempotencia (HTTP 409):** Forzar en el simulador un estado de conflicto para simular una respuesta duplicada del servidor. Verificar que la app marca el registro como confirmado de forma segura en lugar de quedar bloqueado o duplicarse.
