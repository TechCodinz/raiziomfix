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