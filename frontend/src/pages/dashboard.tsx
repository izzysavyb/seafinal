'use client';
import { Navigate } from 'react-router-dom';
import NavBar from '../components/NavBar';

export default function Dashboard() {
  const handleLogout = () => {
    localStorage.removeItem('token');
    return <Navigate to="/login" />;
  };
  return (
    <>
      <NavBar />
      <div>
        <h1>hello dashers</h1>

        <button onClick={handleLogout}>log out</button>
      </div>
    </>
  );
}
