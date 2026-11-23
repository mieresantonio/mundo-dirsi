// Blockali-lite v1.1 — bundle de la demo (build simulado para P-03)
const ROUTES = {
  "/inicio": () => renderHome(),
  "/modulos": () => renderModules(),
  "/laboratorio": () => renderLab()
};
const API_BASE = "https://BC123.pythonanywhere.com";
async function fetchProgress(userId) {
  const r = await fetch(`${API_BASE}/api/progreso?user=${userId}`);
  return r.json();
}
async function askTutor(question) {
  const r = await fetch("/api/tutor/preguntar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  });
  return r.json();
}
function renderHome() { document.getElementById("app").textContent = "Inicio"; }
function renderModules() { document.getElementById("app").textContent = "Módulos"; }
function renderLab() { document.getElementById("app").textContent = "Laboratorio"; }
window.__routes = Object.keys(ROUTES);
