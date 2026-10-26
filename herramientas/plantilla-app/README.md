# plantilla-app

Plantilla mínima fullstack para mundo-dirsi: React + Vite (frontend) y Flask (backend).

## Arrancar

```bash
# Backend (puerto 5000)
pip install -r requirements.txt
python3 app.py

# Frontend (en otra terminal)
npm install
npm run dev
```

El frontend hace proxy de `/api` hacia `http://localhost:5000`.

## Endpoints

- `GET /api/health` → `{"status": "ok", "app": "plantilla-app"}`

Solo código fuente: sin `node_modules`, `venv`, `dist` ni artefactos generados.
