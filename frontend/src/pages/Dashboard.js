
// Dashboard.js
import { useEffect } from "react";
import { recordAction, getWallet } from "../api/raiziom";
import { useState } from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const email = localStorage.getItem("raiziomUser");
  const [credits, setCredits] = useState(0);

  useEffect(() => {
    async function fetchCredits() {
      const w = await getWallet(email);
      setCredits(w.credits || 0);
    }
    fetchCredits();
    recordAction(email, "dashboard-view");
  }, [email]);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Welcome to Raiziom Dashboard</h1>
      <p>Credits: {credits}</p>
      <Link to="/wallet">Go to Wallet</Link>

import { createCheckoutSession } from "../api/raiziom";

export default function Dashboard() {
  const buyCredits = async () => {
    const data = await createCheckoutSession();
    if (data.url) {
      window.location.href = data.url;
    }
  };

  return (
    <div>
      <h1>Welcome to Raiziom Dashboard</h1>
      <button onClick={buyCredits}>Buy Credits</button>
    </div>
  );
}
import { useEffect, useState } from "react";
import { getPlugins } from "../api/raiziom";

export default function Dashboard() {
  const [plugins, setPlugins] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("raiziomToken");
    if (!token) return;
    getPlugins(token).then(setPlugins);
  }, []);

  return (
    <div style={{ padding: "1rem" }}>
      <h1>Raiziom Dashboard</h1>
      <h3>Available Plugins</h3>
      <ul>
        {plugins.map((p, i) => (
          <li key={i}>{p.name} - v{p.version}</li>
        ))}
      </ul>
    </div>
  );
}
