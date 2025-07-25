import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Settings from "./pages/Settings";
import Wallet from "./pages/Wallet";
import Login from "./pages/Login";
import RaiziomAssistant from "./components/RaiziomAssistant";

function PrivateRoute({ children }) {
  const loggedIn = localStorage.getItem("raiziomUser");
  return loggedIn ? children : <Navigate to="/login" />;
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
        <Route path="/settings" element={<PrivateRoute><Settings /></PrivateRoute>} />
        <Route path="/wallet" element={<PrivateRoute><Wallet /></PrivateRoute>} />
      </Routes>
      <RaiziomAssistant />
    </Router>
  );
}

export default App;
