import { useState, useEffect, type SubmitEvent } from "react";
import NavBar from "../components/NavBar";
import { updateMyAccount, getCurrentUser } from "../api/users";

export default function EditAccount() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    fetchUser();
  }, []);

  const fetchUser = async () => {
    try {
      const userId = Number(localStorage.getItem("userId"));

      const data = await getCurrentUser(userId);

      setUsername(data.username);
      setEmail(data.email);
    } catch (error) {
      console.error(error);
      alert("Failed to load account");
    }
  };

  const handleSubmit = async (e: SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!username.trim() || !email.trim()) {
      alert("Username and email are required");
      return;
    }

    try {
      await updateMyAccount({
        username,
        email,
        password: password.trim() ? password : undefined,
      });

      alert("Account updated");
    } catch (error) {
      console.error(error);
      alert("Update failed");
    }
  };

  return (
    <>
      <NavBar />

      <main className="min-h-screen bg-pink-50 px-8 pt-28 pb-10">
        <div className="mx-auto max-w-2xl rounded-3xl border border-pink-200 bg-white/70 p-8 backdrop-blur-md shadow-lg">
          <h1 className="mb-2 text-3xl font-bold text-pink-900">
            Edit Account
          </h1>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                Username
              </label>
              <input
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
              />
            </div>

            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                Email
              </label>
              <input
                required
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
              />
            </div>

            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                New Password
              </label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Leave blank to keep current password"
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
              />
            </div>

            <button
              type="submit"
              className="w-full rounded-full bg-pink-400 py-3 font-medium text-white transition hover:bg-pink-500"
            >
              Save Changes
            </button>
          </form>
        </div>
      </main>
    </>
  );
}
