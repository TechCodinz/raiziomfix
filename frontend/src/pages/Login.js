import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login as apiLogin, signup } from "../api/raiziom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await apiLogin(email, password);
    } catch (err) {
      await signup(email, password);
    }
    localStorage.setItem("raiziomUser", email);
    navigate("/");
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
