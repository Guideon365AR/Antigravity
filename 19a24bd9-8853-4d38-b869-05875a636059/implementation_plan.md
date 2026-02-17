# Plan de Implementación: Configuración Docker para Firehouse

Actualizar la aplicación Rails 4.2 para ejecutarse con Ruby 3.2 en Docker, con PostgreSQL como base de datos.

## User Review Required

> [!WARNING]
> **Compatibilidad con Rails 4.2**: Rails 4.2 es muy antiguo y puede tener problemas de compatibilidad con Ruby 3.2. La versión oficial más alta soportada por Rails 4.2 es Ruby 2.4. Esto puede requerir actualizar Rails en el futuro.

> [!IMPORTANT]
> **Bundler Version**: El Gemfile.lock está usando Bundler 1.17.3, que puede no ser compatible con Ruby 3.2. Actualizaré a una versión más moderna.

## Proposed Changes

### Infraestructura Docker

#### [MODIFY] [Dockerfile](file:///c:/Users/Gustavo/firehouse/Dockerfile)

Actualizar el Dockerfile existente para:
- Cambiar base image de `ruby:2.4-alpine` a `ruby:3.2-alpine`
- Actualizar instalación de bundler a versión 2.x
- Mejorar el orden de capas para mejor caching
- Asegurar que todas las dependencias del sistema estén presentes

#### [NEW] docker-compose.yml

Crear archivo docker-compose.yml con:
- Servicio `web` para la aplicación Rails
- Servicio `db` para PostgreSQL 14
- Volúmenes para persistencia de datos
- Red compartida entre servicios
- Variables de entorno necesarias

---

### Configuración de Base de Datos

#### [MODIFY] [database.yml](file:///c:/Users/Gustavo/firehouse/config/database.yml)

Actualizar la configuración de development para:
- Usar el hostname del servicio Docker (`db` en lugar de `localhost`)
- Mantener credenciales consistentes con docker-compose

---

### Scripts de Inicio

#### [MODIFY] [start.sh](file:///c:/Users/Gustavo/firehouse/start.sh)

Revisar y posiblemente actualizar el script de inicio para asegurar compatibilidad con el entorno Docker.

## Verification Plan

### Automated Tests
```bash
# Build de la imagen Docker
docker-compose build

# Iniciar los servicios
docker-compose up
```

### Manual Verification
- Verificar que la base de datos PostgreSQL se inicia correctamente
- Verificar que la aplicación Rails puede conectarse a la base de datos
- Reportar cualquier error encontrado durante el build o ejecución
