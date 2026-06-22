import { useEffect, useState } from 'react';
import { getAssets } from '../api/assets';

import NavBar from '../components/NavBar';

export default function Assets() {
  const [assets, setAssets] = useState([]);

  useEffect(() => {
    fetchAssets();
  }, []);

  const fetchAssets = async () => {
    const data = await getAssets();
    setAssets(data);
  };

  return (
    <>
      <NavBar />
      <main className=" bg-pink-50 px-8 pt-28 pb-10">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-pink-900">Assets</h1>
          <p className="text-pink-600">Manage The IT LTD Assets</p>
        </div>
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
          {assets.map((asset: any) => (
            <div
              key={asset.id}
              className="overflow-hidden rounded-3xl border border-pink-200 bg-white/70  shadow-lg transition hover:scale-[1.02]"
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
              </div>
            </div>
          ))}
        </div>
      </main>
    </>
  );
}
