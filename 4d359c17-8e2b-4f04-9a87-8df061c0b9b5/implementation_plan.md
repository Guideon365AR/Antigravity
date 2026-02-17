# Cloud Deployment Preparation Plan

The goal is to deploy the Firehouse Rails 4.2 application to a cloud provider (Railway or Render) using Docker. We need to ensure the application listens on the correct port, connects to the managed database via `DATABASE_URL`, and serves static assets correctly.

## User Review Required
> [!IMPORTANT]
> **Database Configuration**: I will modify `config/database.yml` to prioritize `DATABASE_URL` environment variable, which is standard for cloud providers.
> **Static Files**: I will verify `config.serve_static_files` is enabled so the Docker container can serve assets directly.
> **Secrets**: You must provide `SECRET_KEY_BASE` in the deployment platform's environment variables. I will ensure `secrets.yml` or `application.rb` reads this.

## Proposed Changes

### Configuration
#### [MODIFY] [database.yml](file:///c:/Users/Gustavo/firehouse/config/database.yml)
- Update `production` environment to use `url: <%= ENV['DATABASE_URL'] %>` if present, falling back to existing separate fields.

#### [MODIFY] [production.rb](file:///c:/Users/Gustavo/firehouse/config/environments/production.rb)
- Ensure logging goes to STDOUT (`RAILS_LOG_TO_STDOUT`).

#### [MODIFY] [Dockerfile](file:///c:/Users/Gustavo/firehouse/Dockerfile)
- Move asset precompilation to the build stage if possible, or leave in start script but ensure `SECRET_KEY_BASE` is available (dummy value for build).

### Scripting
#### [MODIFY] [start.sh](file:///c:/Users/Gustavo/firehouse/start.sh)
- Ensure it handles database migration on startup.
- Ensure Unicorn listens on `$PORT` or default to 3000.

#### [MODIFY] [unicorn.rb](file:///c:/Users/Gustavo/firehouse/config/unicorn.rb)
- Update code to listen on `ENV['PORT']`.

## Verification Plan

### Manual Verification
1.  **Local Production Build**:
    -   Run `docker build -t firehouse-prod .`
    -   Run `docker run --env-file .env.prod -p 3000:3000 firehouse-prod`
    -   Verify app boots and serves assets.
2.  **Deployment**:
    -   User follows the generated walkthrough to connect GitHub and deploy.
