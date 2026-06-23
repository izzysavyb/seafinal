import { useEffect, useState } from "react";
import { deleteAsset, getAssets } from "../api/assets";
import { getUserRole } from "../utils/auth";
import NavBar from "../components/NavBar";
import { type AssetTypes } from "../api/types";
import { Link } from "react-router-dom";

export default function Assets() {
  const [assets, setAssets] = useState<AssetTypes[]>([]);

  useEffect(() => {
    fetchAssets();
  }, []);

  const fetchAssets = async () => {
    const data = await getAssets();
    setAssets(data);
  };
  const handleDelete = async (id: number) => {
    try {
      await deleteAsset(id);
      alert("Asset Deleted");

      setAssets(assets.filter((assets) => assets.id !== id));
    } catch (error) {
      console.error(error);
      alert("Delete failed");
    }
  };
  const role = getUserRole();
  return (
    <>
      <NavBar />
      <main className="min-h-screen bg-pink-50 px-8 pt-28 pb-10">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-pink-900">Assets</h1>
          <p className="text-pink-600 pb-4">Manage The IT LTD Assets</p>
          <Link to={"/assets/create-asset"}>
            <button className="rounded-full bg-white p-4 py-2 text-md">
              Create a new asset?
            </button>
          </Link>
        </div>
        {assets.length === 0 ? (
          <div className="flex justify-center">
            <div className="bg-white p-8 rounded-xl shadow-md w-80">
              <p className="pb-4">You don't own any Assets :(</p>
              <div className="flex justify-center border-t border-pink-100 pt-3 text-gray-500 ">
                <Link
                  className="flex w-50 h-10 items-center justify-center rounded-full bg-pink-50 shadow-md cursor-pointer"
                  to="/assets/create-asset"
                >
                  Click to Create an Asset!
                </Link>
              </div>
            </div>
          </div>
        ) : (
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
            {assets.map((asset: any) => (
              <div
                key={asset.id}
                className="overflow-hidden rounded-3xl border border-pink-200 bg-white/70  "
              >
                <div className="space-y-4 p-5">
                  <div>
                    <h3 className="text-lg font-semibold text-gray-800">
                      {asset.name}
                    </h3>
                    <p className="text-sm text-gray-500">
                      Serial: {asset.serial_number}
                    </p>
                  </div>

                  <div className="border-t border-pink-100 pt-3 text-sm text-gray-500">
                    Asset ID: {asset.id}
                  </div>

                  {role === "admin" && (
                    <div className="flex justify-center border-t border-pink-100 pt-3 text-gray-500 ">
                      <button
                        className="flex w-20 h-10 items-center justify-center rounded-full bg-pink-50"
                        onClick={() => handleDelete(asset.id)}
                      >
                        Delete
                      </button>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </main>
    </>
  );
}
