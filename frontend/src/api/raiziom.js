const BASE_URL = "https://raiziomfix.onrender.com"; // replace with actual

export async function sendIdeaToRaiziom(idea) {
  const res = await fetch(`${BASE_URL}/idea`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ idea }),
  });
  return res.json();
}
