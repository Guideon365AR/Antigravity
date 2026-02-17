# Dockerización de Firehouse: Guía Final

¡La aplicación **Firehouse** ya está operativa en Docker! Se han resuelto múltiples desafíos de compatibilidad para asegurar que una aplicación Rails 4.2 de 2015 funcione correctamente en un entorno moderno.

## 🚀 Estado Actual
- **Ruby**: 2.7.8 (Alpine)
- **Rails**: 4.2.11
- **Base de Datos**: PostgreSQL 14
- **Servidor Web**: Thin (v1.7.2)
- **Estado**: **Operativo** en [http://localhost:3000](http://localhost:3000)

---

## 🛠️ Soluciones Técnicas Aplicadas

### 1. Retro-compatibilidad de Ruby
Se intentó inicialmente Ruby 3.2, pero Rails 4.2 requiere Bundler 1.x, el cual utiliza métodos eliminados en Ruby 3.0 (`untaint`).
- **Solución**: Se seleccionó **Ruby 2.7** como la versión más moderna y estable compatible con Rails 4.2.

### 2. Parche BigDecimal
Ruby 2.7/3.0 eliminaron `BigDecimal.new`. Rails 4.2 aún lo usa internamente.
- **Solución**: Se aplicó un parche en [boot.rb](file:///c:/Users/Gustavo/firehouse/config/boot.rb) que restaura la funcionalidad de `BigDecimal.new` llamando al constructor moderno.

### 3. Configuración de Secretos
La aplicación fallaba al iniciar por falta de archivos de configuración.
- **Solución**: Se creó [secrets.yml](file:///c:/Users/Gustavo/firehouse/config/secrets.yml) basado en el ejemplo del repositorio, permitiendo que Rails cargue las claves necesarias.

### 4. Optimización de Docker
Se ajustó el [docker-compose.yml](file:///c:/Users/Gustavo/firehouse/docker-compose.yml) para evitar conflictos entre las gemas instaladas en la imagen y el volumen de código fuente.

---

## 📖 Instrucciones de Uso

### Levantar la aplicación
Si los contenedores están detenidos, ejecútalos con:
```bash
docker-compose up -d
```

### Acceso
- **Web**: [http://localhost:3000](http://localhost:3000)
- **Base de Datos**: `localhost:5432` (User/Pass: `docker`/`docker`)

### Comandos de Utilidad
```bash
# Ver logs en tiempo real
docker-compose logs -f web

# Entrar a la consola de Rails
docker-compose exec web bundle exec rails console

# Ejecutar migraciones manualmente
docker-compose exec web bundle exec rake db:migrate
```

---

## ✅ Lista de Cambios
- [x] **Dockerfile**: Actualizado a Ruby 2.7 con todas las dependencias (Postgres, Magick, Node).
- [x] **docker-compose.yml**: Configurado con persistencia de datos y salud de servicios.
- [x] **config/boot.rb**: Parcheado para compatibilidad con Ruby moderno.
- [x] **config/database.yml**: Adaptado para conectar al servicio `db` de Docker.
- [x] **config/secrets.yml**: Creado y configurado.
