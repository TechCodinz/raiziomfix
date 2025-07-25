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
    </div>
  );
}
