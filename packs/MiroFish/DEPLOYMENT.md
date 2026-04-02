# Guía de Despliegue — MiroFish

Documentación del servidor de producción y configuraciones aplicadas.

---

## Servidor

| Parámetro | Valor |
|-----------|-------|
| Host | `192.168.5.207` |
| Usuario | `evergara` |
| Zona horaria | `America/Santiago (UTC-3)` |

### Cambiar zona horaria (aplicado el 2026-04-02)

```bash
sudo timedatectl set-timezone America/Santiago
timedatectl status
```

---

## Servicios systemd

| Servicio | Puerto | Descripción |
|----------|--------|-------------|
| `mirofish-frontend.service` | `3000` | Servidor Vite (Vue 3) |
| `mirofish-backend.service` | `5001` | API Flask (Python) |

### Comandos útiles

```bash
# Estado
sudo systemctl status mirofish-frontend.service
sudo systemctl status mirofish-backend.service

# Reiniciar
sudo systemctl restart mirofish-frontend.service
sudo systemctl restart mirofish-backend.service

# Logs en tiempo real
sudo journalctl -u mirofish-frontend.service -f
sudo journalctl -u mirofish-backend.service -f
```

---

## Configuración de API (frontend)

El archivo `frontend/src/api/index.js` usa `baseURL: ''` (cadena vacía) para aprovechar el proxy de Vite:

```js
// frontend/src/api/index.js
baseURL: import.meta.env.VITE_API_BASE_URL || ''
```

El proxy en `vite.config.js` redirige `/api/*` → `http://localhost:5001`:

```js
// frontend/vite.config.js
proxy: {
  '/api': { target: 'http://localhost:5001', changeOrigin: true }
}
```

> **Importante**: no usar `http://localhost:5001` como `baseURL` ya que rompe el acceso desde navegadores remotos.

---

## Ruta de despliegue en servidor

```
/home/evergara/MiroFish/
├── frontend/src/   ← archivos Vue copiados vía scp
└── backend/        ← código Flask
```

### Comando de actualización rápida

```bash
# Desde la máquina local, copiar frontend y reiniciar
scp -r frontend/src evergara@192.168.5.207:/home/evergara/MiroFish/frontend/
ssh evergara@192.168.5.207 "sudo systemctl restart mirofish-frontend.service"
```

---

## Historial de cambios relevantes

| Commit | Descripción |
|--------|-------------|
| `d888c19` | Fix: redirigir `/process/new` a Home cuando no hay proyecto pendiente |
| `89db833` | Fix: baseURL de API para acceso remoto + textos de UI a español |
| `e04266d` | Traducción completa de frontend y mensajes de API backend a español |
| `79cfd51` | Traducción de Home.vue y componentes de simulación a español |
