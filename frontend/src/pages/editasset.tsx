import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import NavBar from "../components/NavBar";

import { getAssetById, updateAsset, deleteAsset } from "../api/assets";

import { getUsers } from "../api/users";
import { getUserRole } from "../utils/auth";

export default function EditAsset() {
  const { id } = useParams();
  const navigate = useNavigate();

  const role = getUserRole();

  const [name, setName] = useState("");
  const [category, setCategory] = useState("");
  const [status, setStatus] = useState("");
  const [ownerId, setOwnerId] = useState("");

  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetchAsset();
    fetchUsers();
  }, []);

  const fetchAsset = async () => {
    const asset = await getAssetById(Number(id));

    setName(asset.name);
    setCategory(asset.category);
    setStatus(asset.status);
    setOwnerId(asset.owner_id);
  };

  const fetchUsers = async () => {
    if (role === "admin") {
      const data = await getUsers();
      setUsers(data);
    }
  };

  const handleSubmit = async (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();

    await updateAsset(Number(id), {
      name,
      category,
      status,
      owner_id: role === "admin" ? Number(ownerId) : undefined,
    });

    alert("Asset updated");
    navigate("/assets");
  };

  const handleDelete = async () => {
    if (role !== "admin") return;

    await deleteAsset(Number(id));

    alert("Asset deleted");
    navigate("/assets");
  };

  return (
    <>
      <NavBar />

      <main className="min-h-screen bg-pink-50 px-8 pt-28 pb-10">
        <div className="mx-auto max-w-2xl rounded-3xl border border-pink-200 bg-white/70 p-8">
          <h1 className="mb-2 text-3xl font-bold text-pink-900">Edit Asset</h1>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                Asset Name
              </label>
              <input
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
              />
            </div>

            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                Category
              </label>
              <input
                required
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
              />
            </div>

            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                Status
              </label>
              <select
                value={status}
                onChange={(e) => setStatus(e.target.value)}
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
              >
                <option value="active">Active</option>
                <option value="in repair">In Repair</option>
                <option value="retired">Retired</option>
              </select>
            </div>

            {role === "admin" && (
              <div>
                <label className="mb-2 block text-sm font-medium text-pink-800">
                  Assign Owner
                </label>
                <select
                  value={ownerId}
                  onChange={(e) => setOwnerId(e.target.value)}
                  className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
                >
                  {users.map((user: any) => (
                    <option key={user.id} value={user.id}>
                      {user.username}
                    </option>
                  ))}
                </select>
              </div>
            )}

            <button
              type="submit"
              className="w-full rounded-full bg-pink-400 py-3 font-medium text-white transition hover:bg-pink-500"
            >
              Update Asset
            </button>

            {role === "admin" && (
              <button
                type="button"
                onClick={handleDelete}
                className="w-full rounded-full border border-pink-300 bg-white py-3 font-medium text-pink-500 transition hover:bg-pink-50"
              >
                Delete Asset
              </button>
            )}
          </form>
        </div>
      </main>
    </>
  );
}
