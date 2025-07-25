const BASE_URL = ""; // relative to same domain

export async function register(email, password) {
  const res = await fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });
  return res.json();
}

export async function signup(email, password) {
  const res = await fetch(`${BASE_URL}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  return res.json();
}

export async function createCheckoutSession() {
  const res = await fetch(`${BASE_URL}/create-checkout-session`, {
    method: "POST",
  });
  return res.json();
}
export async function login(email, password) {
  const res = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
    body: JSON.stringify({ email, password })
  });
  return res.json();
}

export async function getWallet(email) {
  const res = await fetch(`${BASE_URL}/wallet/${email}`);
  return res.json();
}

export async function recordAction(email, action) {
  const res = await fetch(`${BASE_URL}/action`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, action }),
export async function sendIdeaToRaiziom(idea, token) {
  const res = await fetch(`${BASE_URL}/idea?token=${token}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ idea })
  });
  return res.json();
}

export async function addFunds(email, amount, provider = "mock") {
  const res = await fetch(`${BASE_URL}/add_funds`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, amount, provider }),
export async function askAI(message, token) {
  const res = await fetch(`${BASE_URL}/ai/respond?token=${token}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ input: message })
  });
  return res.json();
}

export async function getEarnings(email) {
  const res = await fetch(`${BASE_URL}/earnings/${email}`);
export async function getPlugins(token) {
  const res = await fetch(`${BASE_URL}/plugins?token=${token}`);
  return res.json();
}
