import { useState } from 'react';
import { loginUser, registerUser } from '../api/auth';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const [mode, setMode] = useState('login');

  const [username, setUsername] = useState('');

  const [email, setEmail] = useState('');

  const [password, setPassword] = useState('');

  const navigate = useNavigate();

  const handleSubmit = async () => {
    try {
      if (mode === 'login') {
        const data = await loginUser(username, password);

        localStorage.setItem('token', data.access_token);

        navigate('/dashboard');
      } else {
        await registerUser(username, email, password);

        alert('Registration successful');

        setMode('login');
      }
    } catch (error) {
      console.error(error);

      alert('Authentication failed');
    }
  };
  return (
    <div className="min-h-screen bg-pink-50 flex items-center justify-center bg-cover bg-center ">
      <div className="bg-white p-8 rounded-xl shadow-md w-80">
        <div className="flex flex-col gap-3 mb-6 overflow-hidden rounded-lg">
          <button
            onClick={() => setMode('login')}
            className={`flex-1 p-2 rounded-lg ${
              mode === 'login' ? 'bg-pink-500 text-black' : 'bg-gray-200'
            }`}
          >
            Login
          </button>

          <button
            onClick={() => setMode('register')}
            className={`flex-1 p-2 rounded-lg ${
              mode === 'register' ? 'bg-pink-500 text-black' : 'bg-gray-200'
            }`}
          >
            Register
          </button>
        </div>
        <h2 className="text-2xl font-bold mb-6 text-center text-black-500">
          {mode === 'login' ? 'Login' : 'Register'}
        </h2>

        {mode === 'register' && (
          <input
            type="text"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full p-2 mb-4 border rounded"
          />
        )}

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full p-2 mb-4 border rounded"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 mb-4 border rounded"
        />

        <button
          className="w-full bg-pink-500 text-black p-2 rounded hover:scale-[1.02]"
          onClick={handleSubmit}
        >
          {mode === 'login' ? 'Log In' : 'Create Account'}
        </button>
      </div>
    </div>
  );
}
