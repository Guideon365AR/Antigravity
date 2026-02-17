# Script de Sincronización Automática del Cerebro (AntiGravity Brain)
# Este script actualiza tu copia local con los cambios remotos y sube tus nuevos cambios.

$BrainPath = "C:\Users\Gustavo\.gemini\antigravity\brain"
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$LogPath = Join-Path $BrainPath "sync_log.txt"

Start-Transcript -Path $LogPath -Append


Write-Host "Iniciando sincronización del Cerebro en: $BrainPath" -ForegroundColor Cyan

# Navegar al directorio
Set-Location -Path $BrainPath

# 1. Traer cambios remotos (Pull)
Write-Host "1. Descargando cambios remotos (git pull)..." -ForegroundColor Yellow
git pull origin main

if ($LASTEXITCODE -ne 0) {
    Write-Host "Error al descargar cambios. Por favor, resuelve los conflictos manualmente." -ForegroundColor Red
    exit
}

# 2. Agregar cambios locales
Write-Host "2. Agregando cambios locales..." -ForegroundColor Yellow
git add .

# 3. Confirmar cambios (Commit)
$Status = git status --porcelain
if ($Status) {
    Write-Host "3. Confirmando cambios..." -ForegroundColor Yellow
    git commit -m "Auto-sync: $Timestamp"

    # 4. Subir cambios (Push)
    Write-Host "4. Subiendo cambios a GitHub (git push)..." -ForegroundColor Yellow
    git push origin main

    if ($LASTEXITCODE -eq 0) {
        Write-Host "¡Sincronización completada exitosamente!" -ForegroundColor Green
    }
    else {
        Write-Host "Error al subir los cambios." -ForegroundColor Red
    }
}
else {
    Write-Host "No hay cambios locales para subir." -ForegroundColor Green
}

Write-Host "Proceso finalizado."
Start-Sleep -Seconds 3
Stop-Transcript
