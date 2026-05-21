# Walkthrough: Gestión Móvil SRP — MVP Fase 1

## ✅ Resumen del Proyecto

**Gestión Móvil SRP** es una aplicación móvil (React Native/Expo) desarrollada para el *Servicio de Resguardo Patrimonial (SRP)* de la Universidad Nacional de Rosario. Permite a los encargados de guardia registrar inasistencias, novedades operativas y gestionar equipos de trabajo, **100% offline-first**, sincronizando con el servidor central al recuperar señal.

---

## 🏗️ Arquitectura Técnica

| Capa | Tecnología |
|---|---|
| Framework | React Native (Expo SDK 51) — modo Web |
| Estado Global | Zustand 4.5 |
| Tipado | TypeScript 5.3 (strict mode) |
| Iconos | Lucide React |
| Entorno | Docker (node:20-alpine) vía `docker compose` |
| Acceso | Navegador web → `http://localhost:8081` |

### Estructura del Proyecto

```
SrpMovil/
├── App.tsx                   # Router central basado en estado Zustand
├── package.json              # Dependencias Expo 51
├── docker-compose.yml        # Contenedor Node:20-alpine (port 8081)
├── run.bat                   # Inicio con un clic en Windows
├── tsconfig.json             # TypeScript strict
└── src/
    ├── theme/index.ts        # Sistema de diseño premium (HSL dark mode)
    ├── store/
    │   ├── appStore.ts       # Auth, sección activa, aprobación de turno
    │   └── syncStore.ts      # Cola FIFO, inasistencias, novedades, logs
    ├── services/
    │   ├── mockData.ts       # BD mock: 13 secciones, 30+ agentes, turnos
    │   └── syncEngine.ts     # Motor de sincronización offline-first
    └── screens/              # 10 pantallas completas
```

---

## 📱 Pantallas Implementadas

### SCR-01 — Login Premium
- Credenciales de acceso con validación interactiva
- Indicador de carga fluido (spinner 800ms)
- Demo helper embebido con usuarios de prueba
- **Usuarios demo:** `encargado` (multi-área), `casilda` (área única)

### SCR-02 — Selector de Áreas
- Rejilla glassmorphic de secciones asignadas
- Solo aparece cuando el encargado tiene múltiples secciones

### SCR-03 — Inicio de Turno ⚠️ (OBLIGATORIO)
- **Bloquea el acceso** hasta que el equipo sea aprobado
- Muestra el turno activo auto-detectado según la hora del sistema
- Lista de agentes con sus objetivos asignados
- Botón "Modificar Equipo" → SCR-03b

### SCR-03b — Modificación de Equipo
- Marcar agentes como "No se presentó"
- Reasignación de objetivos (secciones matriciales: CUR, Salud, Vet, Agr)
- Agregar agentes de refuerzo ad-hoc desde listado de disponibles
- "Aprobar Equipo" desbloquea el resto de la app

### SCR-04 — Dashboard de Sección
- Barra superior tri-estado de conectividad:
  - 🟢 **Verde:** Conectado y sincronizado
  - 🟡 **Amarillo:** Offline, registros pendientes
  - 🔴 **Rojo:** Error de sincronización
- Lista de agentes activos con acceso rápido a registrar ausencia
- Menú de accesos rápidos (4 módulos)

### SCR-05 / SCR-06 — Nueva Inasistencia (Wizard 2 pasos)
- **Paso 1 (SCR-05):** Selección de agente, tipo y validaciones:
  - `JUSTIFICADA` → requiere descripción ≥5 chars, ≤500 chars
  - `IRREGULARIDAD` → despliega selector de subtipo obligatorio
- **Paso 2 (SCR-06):** Resumen con sello de tiempo inalterable y confirmación

### SCR-07 / SCR-08 — Historial de Inasistencias
- Lista filtrable por tipo y agente
- Badges de estado de sync: PENDING / SYNCED / ERROR / ANULADA
- Modal de detalle (SCR-08) con:
  - Edición de justificación (agrega a cola de sync)
  - Anulación (soft-delete)

### SCR-12 — Nueva Novedad
- Formulario: Asunto, Objetivo, Descripción (mínimo 10 chars)
- Guardado inmediato local con estado PENDING / CONFIRMED

### SCR-13 — Historial de Novedades
- ACK Server ID mostrado en tarjetas
- Contador de reintentos (`retry_count`)
- Badges de estado: PENDING / CONFIRMED / ERROR

### SCR-11 — Panel de Control / Simulador
- **Toggle de red:** Online ↔ Offline (simula pérdida de señal)
- **Selector de latencia:** 100ms / 500ms / 2000ms / 5000ms
- **Forzar errores:** HTTP 500 (reintento) / HTTP 409 (idempotencia)
- **Gestor de cola:** Vista de items, botón sync manual, vaciar cola
- **Bitácora en tiempo real:** Logs coloreados de todos los eventos de sync
- Botón de Cerrar Sesión

---

## 🔌 Motor Offline-First — SyncEngine

El motor se ejecuta en segundo plano cada 3 segundos:

```
Al recuperar red:
  → Toma items PENDING de la cola (FIFO)
  → Simula latencia configurada
  → Respuesta del servidor:
       HTTP 201 + ACK: true  → marca SYNCED ✅
       HTTP 409 (Duplicado) → ACK positivo por idempotencia ✅
       HTTP 500 (Error)     → incrementa retry_count, max 5 → ERROR ❌
```

### Flujo de Datos

```
Registro local (siempre instantáneo)
    ↓
SyncQueue [PENDING]
    ↓ (cuando isConnected = true)
SyncEngine.processQueue() — FIFO
    ↓
SyncItem → SYNCED | ERROR
    ↓
Absence/Novedad → sync_status actualizado
    ↓
UI reactiva (Zustand) → badges actualizados
```

---

## 🧪 Cómo Probar el MVP

### Inicio Rápido (Docker)

1. Ejecutar `run.bat` desde el directorio del proyecto, o:
   ```powershell
   docker compose up -d
   docker logs -f srp-movil-app
   ```
2. Abrir **http://localhost:8081** en el navegador

### Guía de Verificación

| Escenario | Pasos |
|---|---|
| Login multi-área | Usuario `encargado`, contraseña `123456` → va a SCR-02 |
| Login área única | Usuario `casilda`, contraseña `123456` → va a SCR-03 |
| Flujo completo | Login → Selección → Inicio Turno → Aprobar → Dashboard |
| Registro offline | Ajustes → Red OFF (barra amarilla) → Registrar inasistencia → ver PENDING |
| Sync automático | Ajustes → Red ON → esperar 3s → ver barra verde y badges SYNCED |
| Idempotencia 409 | Ajustes → Forzar Error 409 → hacer sync → verificar que igual pasa a SYNCED |
| Error 500 | Ajustes → Forzar Error 500 → ver retry_count subir hasta 5 → ERROR |

---

## ✅ Validación TypeScript

```
> npm run ts:check
> tsc

(sin errores) ✅
```

---

## 📦 Estado Final del Proyecto

- **Pantallas:** 10/10 implementadas y compilando ✅
- **Motor de Sync:** Operativo con manejo de 409/500 ✅
- **TypeScript:** 0 errores en modo estricto ✅
- **Docker:** Contenedor corriendo en puerto 8081 ✅
- **Diseño:** Dark mode premium con glassmorphism ✅
