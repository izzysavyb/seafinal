"use client";
import { useEffect, useState } from "react";
import NavBar from "../components/NavBar";
import { getCurrentUser } from "../utils/auth";
import type { AssetTypes } from "../api/types";
import { getAssets } from "../api/assets";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const [assets, setAssets] = useState<AssetTypes[]>([]);
  const user: any = getCurrentUser();

  useEffect(() => {
    fetchAssets();
  }, []);
  const fetchAssets = async () => {
    const data = await getAssets();

    setAssets(data);
  };

  const totalAssets = assets.length;
  const activeAssets = assets.filter(
    (asset) => asset.status === "active"
  ).length;
  const retiredAssets = assets.filter(
    (asset) => asset.status === "retired"
  ).length;

  return (
    <>
      <NavBar />
      <main className="min-h-screen bg-pink-50  px-8 pt-28 pb-10">
        <div>
          <h1 className="pb-5">Hi there, {user?.sub}!</h1>
          <div className="flex justify-center">
            <div className="bg-white p-8 rounded-xl w-80">
              <h2>Account Details:</h2>
              <ul>
                <li className="text-black">- Role: {user?.role}</li>
                <li className="text-black">- User ID: {user?.id}</li>
              </ul>
            </div>
          </div>
        </div>

        <h1 className="py-4">Stats</h1>
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          <div className="rounded-2xl bg-white p-6 ">
            <h2 className="text-gray-500">Total Assets</h2>
            <p className="text-3xl font-bold">{totalAssets}</p>
          </div>

          <div className="rounded-2xl bg-white p-6 ">
            <h2 className="text-gray-500">Active Assets</h2>
            <p className="text-3xl font-bold">{activeAssets}</p>
          </div>

          <div className="rounded-2xl bg-white p-6 ">
            <h2 className="text-gray-500">Retired Assets</h2>
            <p className="text-3xl font-bold">{retiredAssets}</p>
          </div>

          <div className="rounded-2xl bg-white p-6 ">
            <h2 className="text-gray-500">Admin Access</h2>
            <p className="text-3xl font-bold">
              {user?.role === "admin" ? "Enabled" : "Disabled"}
            </p>
          </div>
        </div>

        <h1 className="py-4">Quick Actions</h1>
        {user?.role == "admin" ? (
          <div className="grid gap-6 lg:grid-cols-2">
            <Link to={"/assets/create-asset"}>
              <button className="rounded-full bg-white px-4 py-2 text-2xl">
                Create an Asset
              </button>
            </Link>

            <Link to={"/users"}>
              <button className="rounded-full bg-white px-4 py-2 text-2xl">
                Manage Users
              </button>
            </Link>
          </div>
        ) : (
          <div className="grid gap-6 lg:grid-cols-2">
            <Link to={"/assets"}>
              <button className="rounded-full bg-white px-4 py-2 text-2xl transition-all duration-300 hover:text-pink-400/70 hover:scale-105">
                View my Assets
              </button>
            </Link>
            <Link to={"/account"}>
              <button className="rounded-full bg-white px-4 py-2  text-2xl transition-all duration-300 hover:text-pink-400/70 hover:scale-105">
                Account Settings
              </button>
            </Link>
          </div>
        )}
      </main>
    </>
  );
}
