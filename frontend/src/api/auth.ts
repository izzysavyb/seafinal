import api from './client';

export const loginUser = async (username: string, password: string) => {
  const formData = new URLSearchParams();

  formData.append('grant_type', 'password');
  formData.append('username', username);
  formData.append('password', password);

  const response = await api.post('/auth/login', formData, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });

  return response.data;
};

export const registerUser = async (
  username: string,
  email: string,
  password: string
) => {
  const response = await api.post('/auth/register', {
    username,
    email,
    password,
  });

  return response.data;
};
