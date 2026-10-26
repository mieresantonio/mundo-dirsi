import { useEffect, useState } from 'react'

export default function App() {
  const [health, setHealth] = useState('comprobando…')

  useEffect(() => {
    fetch('/api/health')
      .then((r) => r.json())
      .then((d) => setHealth(d.status ?? 'sin respuesta'))
      .catch(() => setHealth('API no disponible (arranca el backend en :5000)'))
  }, [])

  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', maxWidth: 640, margin: '4rem auto', padding: '0 1rem' }}>
      <h1>¡Hola, mundo-dirsi! 👋</h1>
      <p>Esta es la plantilla base: React + Vite en el frontend y Flask en el backend.</p>
      <p>
        Estado de la API: <strong>{health}</strong>
      </p>
    </main>
  )
}
