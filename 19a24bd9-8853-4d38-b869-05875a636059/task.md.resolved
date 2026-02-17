# Configuración de Docker para Firehouse

## Tareas

- [x] Analizar el repositorio y dependencias actuales
- [x] Actualizar Dockerfile para Ruby 3.2 (Actualizado a 2.7 por compatibilidad)
- [x] Crear docker-compose.yml con PostgreSQL
- [x] Actualizar configuración de base de datos
- [x] Intentar ejecutar el build con Docker
- [x] Verificar que la aplicación funciona correctamente


## Problemas Encontrados

❌ **Incompatibilidad irreconciliable**: Rails 4.2 requiere Bundler < 2.0, pero Bundler 1.x no soporta Ruby 3.2 (usa método `untaint` eliminado).

❌ **SyntaxError en Devise 3.5.10**: Ruby 2.7 es más estricto con bloques después de hashes sin paréntesis. Se requiere parchear la gema.

