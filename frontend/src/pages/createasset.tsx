import { useState } from "react";
import NavBar from "../components/NavBar";

import { createAsset } from "../api/assets";
import axios from "axios";

export default function CreateAsset() {
  const [name, setName] = useState("");
  const [category, setCategory] = useState("");
  const [serialNumber, setSerialNumber] = useState("");
  const [status, setStatus] = useState("");

  const handleSubmit = async (e: React.SubmitEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!name || !category || !serialNumber || !status) {
      alert("Please fill in all fields before submitting!");
      return;
    }

    try {
      await createAsset({
        name,
        category,
        serial_number: serialNumber,
        status,
      });
      alert("Asset created successfully!");
      setName("");
      setCategory("");
      setSerialNumber("");
      setStatus("");
    } catch (error: unknown) {
      if (axios.isAxiosError(error)) {
        console.log("Full error:", error.response?.data);

        const detail = error.response?.data?.detail;

        if (detail) {
          alert(JSON.stringify(detail, null, 2));
        } else {
          alert(error.message);
        }
      } else {
        alert("Unknown error");
      }
    }
  };

  return (
    <>
      <NavBar />

      <main className="min-h-screen bg-pink-50 px-8 pt-28">
        <div className="mx-auto max-w-2xl rounded-3xl border border-pink-200 bg-white/70 p-8 ">
          <h1 className="mb-6 text-3xl font-bold text-pink-900">
            Create Asset
          </h1>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                Asset Name
              </label>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
                placeholder="Laptop 11"
              />
            </div>
            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                Category
              </label>
              <input
                type="text"
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
                placeholder="Laptop"
              />
            </div>
            <div>
              <label className="mb-2 block text-sm font-medium text-pink-800">
                Serial Number
              </label>
              <input
                type="text"
                value={serialNumber}
                onChange={(e) => setSerialNumber(e.target.value)}
                className="w-full rounded-xl border border-pink-200 px-4 py-3 outline-none focus:border-pink-400"
                placeholder="ABC123"
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
                <option value="">Select status</option>
                <option value="active">Active</option>
                <option value="in repair">In Repair</option>
                <option value="retired">Retired</option>
              </select>
            </div>

            <button
              type="submit"
              className="w-full rounded-full bg-pink-400 py-3 font-medium text-white transition hover:bg-pink-500"
            >
              Create Asset
            </button>
          </form>
        </div>
      </main>
    </>
  );
}
