# Cloud Deployment Walkthrough

This guide explains how to deploy the Firehouse application to a cloud provider. I recommend **Railway** or **Render** as they are beginner-friendly and support Docker/Rails well.

## Prerequisites
- A GitHub account with this repository pushed (you should have this ready).
- A Railway.app or Render.com account.

## Option A: Deploying to Railway (Recommended)

1.  **Sign Up/Login**: Go to [Railway.app](https://railway.app/) and log in with GitHub.
2.  **New Project**: Click "New Project" > "Deploy from GitHub repo".
3.  **Select Repository**: Choose your `firehouse` repository.
4.  **Add Database**:
    -   Right-click the collection (or click "New") > Database > "Add PostgreSQL".
    -   Railway will automatically inject `DATABASE_URL` into your app service.
    -   **Important**: Wait for the Redis database if your app needs it (secrets.yml mentions Redis), or remove Redis dependency if unused. (I noticed Redis config in secrets.yml, add Redis service if needed).
5.  **Configure Environment Variables**:
    -   Click on your App service card.
    -   Go to the "Variables" tab.
    -   Add `SECRET_KEY_BASE`. You can generate one by running `rake secret` locally or typing a long random string.
    -   Add `RAILS_ENV` = `production`.
    -   Add `RAILS_LOG_TO_STDOUT` = `true`.
    -   Add `RAILS_SERVE_STATIC_FILES` = `true`.
6.  **Build & Deploy**:
    -   Railway should automatically detect the `Dockerfile` and build.
    -   Watch the "Deployments" logs.
7.  **Access App**:
    -   Once deployed, go to "Settings" > "Networking" and "Generate Domain" to get a public URL.

## Option B: Deploying to Render

1.  **Sign Up/Login**: Go to [Render.com](https://render.com/).
2.  **New Web Service**: Click "New +" > "Web Service".
3.  **Connect Repo**: Select your `firehouse` repo.
4.  **Configure**:
    -   **Runtime**: Docker.
    -   **Region**: Pick close to you.
    -   **Branch**: `master` (or `main`).
5.  **Environment Variables**:
    -   Add `DATABASE_URL` (You need to create a "PostgreSQL" service in Render first and copy the "Internal Connection URL").
    -   Add `SECRET_KEY_BASE`.
    -   Add `RAILS_ENV` = `production`.
    -   Add `RAILS_LOG_TO_STDOUT` = `true`.
    -   Add `RAILS_SERVE_STATIC_FILES` = `true`.
6.  **Create Service**: Click "Create Web Service".

## Verification
-   Visit the generated URL.
-   Login to the app (if you have seeded users or register a new one).

> [!NOTE]
> The `start.sh` script runs `rake db:migrate` on every boot. This is convenient for demos but ensures your DB schema is always up to date.
