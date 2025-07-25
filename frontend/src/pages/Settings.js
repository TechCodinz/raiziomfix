export default function Settings() {
  const logout = () => {
    localStorage.removeItem("raiziomToken");
    window.location.href = "/login";
  };
  return (
    <div style={{ padding: "1rem" }}>
      <h1>Settings</h1>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
