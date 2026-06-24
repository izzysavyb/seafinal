import { useEffect, useState } from "react";
import NavBar from "../components/NavBar";
import { deleteUser, getUsers } from "../api/users";
import type { User } from "../api/types";
import { Link } from "react-router-dom";
import { getUserRole } from "../utils/auth";

export default function Users() {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    const data = await getUsers();

    setUsers(data);
  };
  const role = getUserRole();
  const handleDelete = async (id: number) => {
    try {
      await deleteUser(id);

      setUsers(users.filter((user) => user.id !== id));

      alert("User deleted");
    } catch (error: any) {
      alert(error.response?.data?.detail);
    }
  };
  return (
    <>
      <NavBar />

      <main className="min-h-screen bg-pink-50 px-8 pt-28 pb-10">
        <h1 className="text-3xl font-bold mb-8">Users</h1>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {users.map((user) => (
            <div key={user.id} className="rounded-2xl bg-white p-6 ">
              <h2 className="text-xl font-bold">{user.username}</h2>
              <div className="flex justify-center border-t border-pink-100 pt-3 text-gray-500 ">
                <p className="py-2">Email: {user.email}</p>
              </div>
              <div className="flex justify-center border-t border-pink-100 pt-3 text-gray-500 ">
                <p className="py-2">Role: {user.role}</p>
              </div>
              <div className="flex justify-center border-t border-pink-100 pt-3 text-gray-500 ">
                <p className="py-2">ID: {user.id}</p>
              </div>
              <div className="flex justify-center border-t border-pink-100 pt-3 pb-3 text-gray-500 ">
                <Link to={`/users/edit-user/${user.id}`}>
                  <button className="flex w-20 h-10 items-center justify-center rounded-full bg-pink-50">
                    Edit User
                  </button>
                </Link>
              </div>
              <div className="flex justify-center border-t border-pink-100 pt-3 text-gray-500 ">
                {role === "admin" && (
                  <button
                    onClick={() => handleDelete(user.id)}
                    className="rounded-full bg-pink-50 px-4 py-2"
                  >
                    DELETE User
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      </main>
    </>
  );
}
