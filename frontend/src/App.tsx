import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Login from './pages/login';
import Dashboard from './pages/dashboard';
import ProtectedRoute from './components/ProtectedRoute';
import Assets from './pages/assets';
import CreateAsset from './pages/createasset';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />

        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/assets"
          element={
            <ProtectedRoute>
              <Assets />
            </ProtectedRoute>
          }
        />
        <Route
          path="/assets/create-asset"
          element={
            <ProtectedRoute allowedRoles="admin">
              <CreateAsset />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
