const BASE_URL = "https://raiziomfix.onrender.com"; // replace with actual

export async function sendIdeaToRaiziom(idea) {
  const res = await fetch(`${BASE_URL}/idea`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ idea }),
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

export async function login(email, password) {
  const res = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
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
  });
  return res.json();
}

export async function addFunds(email, amount, provider = "mock") {
  const res = await fetch(`${BASE_URL}/add_funds`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, amount, provider }),
  });
  return res.json();
}

export async function getEarnings(email) {
  const res = await fetch(`${BASE_URL}/earnings/${email}`);
  return res.json();
}
