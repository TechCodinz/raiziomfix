import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    if (email === "admin@raiziom.com" && password === "1234") {
      localStorage.setItem("raiziomUser", email);
      navigate("/");
    } else {
      alert("Invalid credentials");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Raiziom Login</h2>
      <form onSubmit={handleLogin}>
        <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
        <br />
        <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}
