import { useEffect, useState } from "react";
import { getWallet, getEarnings, addFunds } from "../api/raiziom";

export default function Wallet() {
  const email = localStorage.getItem("raiziomUser");
  const [credits, setCredits] = useState(0);
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const wallet = await getWallet(email);
      setCredits(wallet.credits || 0);
      const e = await getEarnings(email);
      setLogs(e.logs || []);
    }
    fetchData();
  }, [email]);

  const handleAdd = async () => {
    await addFunds(email, 5, "paystack");
    const wallet = await getWallet(email);
    setCredits(wallet.credits || 0);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Wallet</h2>
      <p>Credits: {credits}</p>
      <button onClick={handleAdd}>Add 5 Credits</button>
      <h3>Logs</h3>
      <ul>
        {logs.map((l, i) => (
          <li key={i}>{l.description}: {l.amount}</li>
        ))}
      </ul>
    </div>
  );
}
