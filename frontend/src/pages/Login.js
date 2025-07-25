import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login, register } from "../api/raiziom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isRegister, setIsRegister] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isRegister) {
        await register(email, password);
        alert("Registered. Please log in.");
        setIsRegister(false);
        return;
      }
      const data = await login(email, password);
      if (data.token) {
        localStorage.setItem("raiziomToken", data.token);
        navigate("/");
      } else {
        alert("Login failed");
      }
    } catch (err) {
      alert("Error");
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>{isRegister ? "Register" : "Raiziom Login"}</h2>
      <form onSubmit={handleSubmit}>
        <input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
        <br />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
        <br />
        <button type="submit">{isRegister ? "Register" : "Login"}</button>
        <button type="button" onClick={() => setIsRegister(!isRegister)} style={{ marginLeft: 8 }}>
          {isRegister ? "Go to Login" : "Need an account?"}
        </button>
      </form>
    </div>
  );
}
