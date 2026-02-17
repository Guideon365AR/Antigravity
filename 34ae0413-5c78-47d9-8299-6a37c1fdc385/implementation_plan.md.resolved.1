# Plan de Migración: Firehouse a Rails 8 (Docker First)

## Problema
No existe una instalación local de Ruby en Windows, lo cual impide ejecutar `rails new` nativamente. Instalar Ruby en Windows puede ser propenso a errores.

## Solución
Utilizar **Docker** para:
1.  Instalar Rails temporalmente en un contenedor.
2.  Generar la estructura de archivos de la nueva aplicación en el sistema anfitrión (Windows) mediante volúmenes.
3.  Ejecutar el entorno de desarrollo.

## User Review Required
> [!NOTE]
> **Docker como Herramienta Principal**: Todo comando de rails (`rails g migration`, `rails c`, etc.) se ejecutará a través de `docker-compose run web ...` o similar.

## Proposed Changes

### 1. Reestructuración de Directorios
Moveremos el código actual para limpiar el área de trabajo:
- `c:\Users\Gustavo\firehouse` -> `c:\Users\Gustavo\firehouse-legacy`
- Crear `c:\Users\Gustavo\firehouse` (VACÍO)

### 2. Bootstrapping (Generación Inicial)
Ejecutaremos un comando Docker único para generar la app:
```bash
docker run --rm -v "c:\Users\Gustavo\firehouse:/app" -w /app ruby:3.3.0-slim /bin/bash -c "gem install rails && rails new . --database=postgresql --css=tailwind"
```
*Nota: Usaremos PostgreSQL y Tailwind CSS por ser estándares modernos robustos.*

### 3. Configuración de Docker Permanente
Crearemos un `docker-compose.yml` moderno para Rails 8:
- **Web**: Ruby 3.3
- **DB**: PostgreSQL 16
- **Redis**: Última versión

### 4. Portabilidad
Una vez generada la estructura, copiaremos manualmente los modelos esenciales desde `firehouse-legacy`.

## Verification Plan
1.  **Generación de Archivos**: Verificar que la carpeta `firehouse` contenga `app`, `config`, `Gemfile`, etc.
2.  **Inicio del Servidor**: Ejecutar `docker-compose up` y acceder a `http://localhost:3000` para ver la pantalla de bienvenida de Rails.
