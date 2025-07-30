// 🌱 Raiziomfix Core Engine – To be evolved into Raiziom
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { recordAction, getWallet, createCheckoutSession, getPlugins } from "../api/raiziom";

export default function Dashboard() {
  // 🧠 Core logic: part of Raiziom engine
  const email = localStorage.getItem("raiziomUser");
  const token = localStorage.getItem("raiziomToken");
  const [credits, setCredits] = useState(0);
  const [plugins, setPlugins] = useState([]);

  useEffect(() => {
    async function fetchData() {
      if (email) {
        const w = await getWallet(email);
        setCredits(w.credits || 0);
        recordAction(email, "dashboard-view");
      }
      if (token) {
        const list = await getPlugins(token);
        setPlugins(list);
      }
    }
    fetchData();
  }, [email, token]);

  const buyCredits = async () => {
    const data = await createCheckoutSession();
    if (data.url) window.location.href = data.url;
  };

  return (
    <div style={{ padding: "1rem" }}>
      <h1>Raiziom Dashboard</h1>
      <p>Credits: {credits}</p>
      <button onClick={buyCredits}>Buy Credits</button>
      <br />
      <Link to="/wallet">Go to Wallet</Link>
      <h3>Available Plugins</h3>
      <ul>
        {plugins.map((p, i) => (
          <li key={i}>{p.name} - v{p.version}</li>
        ))}
      </ul>
    </div>
  );
}
