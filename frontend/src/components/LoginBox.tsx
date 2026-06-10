import { useState } from "react";
export const navLinks = [
  { name: "Dashboard", path: "/dashboard" },
  { name: "Asset List", path: "/assets" },
  { name: "User List", path: "/users" },
  { name: "Account", path: "/account" },
];
export default function LoginBox() {
  const [mode, setMode] = useState("login");

  return (
    <div
      className="min-h-screen flex items-center justify-center bg-cover bg-center"
      style={{ backgroundImage: "url('/backgroundimage.jpg')" }}
    >
      <div className="bg-white p-8 rounded-xl shadow-md w-80">
        <div className="flex flex-col gap-3 mb-6 overflow-hidden rounded-lg">
          <button
            onClick={() => setMode("login")}
            className={`flex-1 p-2 rounded-lg ${
              mode === "login" ? "bg-pink-500 text-white" : "bg-gray-200"
            }`}
          >
            Login
          </button>

          <button
            onClick={() => setMode("register")}
            className={`flex-1 p-2 rounded-lg ${
              mode === "register" ? "bg-pink-500 text-white" : "bg-gray-200"
            }`}
          >
            Register
          </button>
        </div>
        <h2 className="text-2xl font-bold mb-6 text-center text-black-500">
          {mode === "login" ? "Login" : "Register"}
        </h2>

        {mode === "register" && (
          <input
            type="text"
            placeholder="Email"
            className="w-full p-2 mb-4 border rounded"
          />
        )}

        <input
          type="text"
          placeholder="Username"
          className="w-full p-2 mb-4 border rounded"
        />

        <input
          type="text"
          placeholder="Password"
          className="w-full p-2 mb-4 border rounded"
        />

        <button className="w-full bg-pink-500 text-white p-2 rounded">
          {mode === "login" ? "Log In" : "Create Account"}
        </button>
      </div>
    </div>
  );
}
