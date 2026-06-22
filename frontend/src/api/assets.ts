import api from './client';
import type { AssetTypes } from './types';

export const getAssets = async () => {
  const response = await api.get('/assets');

  return response.data;
};

export const createAsset = async (assetData: AssetTypes) => {
  const response = await api.post('/assets', assetData);

  return response.data;
};

export const updateAsset = async (assetId: number, assetData: any) => {
  const response = await api.put(`/assets/${assetId}`, assetData);

  return response.data;
};

export const deleteAsset = async (assetId: number) => {
  const response = await api.delete(`/assets/${assetId}`);

  return response.data;
};
