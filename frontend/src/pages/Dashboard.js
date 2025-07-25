
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
