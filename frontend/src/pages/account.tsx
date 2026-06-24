import { useEffect, useState } from "react";
import NavBar from "../components/NavBar";
import { getCurrentUser } from "../api/users";
import { getUserId } from "../utils/auth";
import { Link } from "react-router-dom";

export default function Account() {
  const [user, setUser] = useState<any>(null);

  useEffect(() => {
    fetchUser();
  }, []);

  const fetchUser = async () => {
    const userId = getUserId();

    if (!userId) return;

    const data = await getCurrentUser(userId);

    setUser(data);
  };

  if (!user) {
    return <p>Loading...</p>;
  }

  return (
    <>
      <NavBar />

      <main className="min-h-screen bg-pink-50 px-8 pt-28">
        <div className="mx-auto max-w-2xl rounded-3xl border border-pink-200 bg-white/70 p-8 ">
          <h1 className="mb-6 text-3xl font-bold text-pink-900">My Account</h1>

          <div className="space-y-4">
            <div>
              <p className="text-sm text-pink-600">Username</p>
              <p className="text-lg font-medium">{user.username}</p>
            </div>

            <div>
              <p className="text-sm text-pink-600">Email</p>
              <p className="text-lg font-medium">{user.email}</p>
            </div>

            <div>
              <p className="text-sm text-pink-600">Role</p>
              <p className="text-lg font-medium ">{user.role}</p>
            </div>

            <div>
              <p className="text-sm text-pink-600">Account ID</p>
              <p className="text-lg font-medium">{user.id}</p>
            </div>
            <div className="flex justify-center border-t border-pink-100 pt-3 text-gray-500 ">
              <Link to={`/users/edit-user/${user.id}`}>
                <button className="flex w-20 h-10 items-center justify-center rounded-full bg-pink-50 transition-all duration-300 hover:text-pink-400/70 hover:scale-105">
                  Edit
                </button>
              </Link>
            </div>
          </div>
        </div>
      </main>
    </>
  );
}
