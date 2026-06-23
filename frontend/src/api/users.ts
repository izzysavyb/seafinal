import api from "./client";

export const getUsers = async () => {
  const response = await api.get("/users");

  return response.data;
};

export const updateUser = async (id: number, userData: any) => {
  const response = await api.put(`/users/${id}`, userData);

  return response.data;
};

export const getUserByID = async (id: number) => {
  const response = await api.get(`/users/${id}`);
  return response.data;
};
