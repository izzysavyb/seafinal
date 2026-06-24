import { useEffect, useState } from "react";
import NavBar from "../components/NavBar";
import { getUserByID, updateUser } from "../api/users";
import { getUserRole } from "../utils/auth";

import { useParams } from "react-router-dom";

export default function EditUser() {
  const currentRole = getUserRole();
  const { id } = useParams();

  const [user, setUser] = useState<any>(null);

  const [username, setUsername] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [role, setRole] = useState("");

  useEffect(() => {
    fetchUser();
  }, []);

  const fetchUser = async () => {
    const data = await getUserByID(Number(id));

    setUser(data);
    setUsername(data.username);
    setEmail(data.email);
    setRole(data.role);
  };

  if (!user) {
    return <p>Loading...</p>;
  }
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      await updateUser(Number(id), {
        username,
        email,
        password: password || undefined,
        role: currentRole === "admin" ? role : undefined,
      });

      alert("User updated successfully!");
    } catch (error) {
      console.error(error);
      alert("Update failed");
    }
  };
  return (
    <>
      <NavBar />

      <main className="min-h-screen bg-pink-50 px-8 pt-28">
        <div className="mx-auto max-w-2xl rounded-3xl border border-pink-200 bg-white/70 p-8">
          <h1 className="mb-6 text-3xl font-bold text-pink-900">Edit User</h1>

          <form onSubmit={handleSubmit} className="space-y-6">
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full rounded-xl border px-4 py-3"
            />

            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full rounded-xl border px-4 py-3"
            />

            <input
              type="password"
              placeholder="New password (optional)"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full rounded-xl border px-4 py-3"
            />

            {currentRole === "admin" && (
              <select
                value={role}
                onChange={(e) => setRole(e.target.value)}
                className="w-full rounded-xl border px-4 py-3"
              >
                <option value="user">user</option>
                <option value="admin">admin</option>
              </select>
            )}

            <button
              type="submit"
              className="w-full rounded-full bg-pink-400 py-3 text-white"
            >
              Update User
            </button>
          </form>
        </div>
      </main>
    </>
  );
}
