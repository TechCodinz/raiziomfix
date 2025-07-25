const BASE_URL = ""; // relative to same domain

export async function register(email, password) {
  const res = await fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });
  return res.json();
}

export async function login(email, password) {
  const res = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });
  return res.json();
}

export async function sendIdeaToRaiziom(idea, token) {
  const res = await fetch(`${BASE_URL}/idea?token=${token}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ idea })
  });
  return res.json();
}

export async function askAI(message, token) {
  const res = await fetch(`${BASE_URL}/ai/respond?token=${token}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ input: message })
  });
  return res.json();
}

export async function getPlugins(token) {
  const res = await fetch(`${BASE_URL}/plugins?token=${token}`);
  return res.json();
}
