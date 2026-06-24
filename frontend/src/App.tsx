import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/login";
import Dashboard from "./pages/dashboard";
import ProtectedRoute from "./components/ProtectedRoute";
import Assets from "./pages/assets";
import CreateAsset from "./pages/createasset";
import Users from "./pages/users";
import EditUser from "./pages/edituser";
import Account from "./pages/account";
import EditAsset from "./pages/editasset";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />

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
            <ProtectedRoute>
              <CreateAsset />
            </ProtectedRoute>
          }
        />
        <Route
          path="/assets/edit-asset/:id"
          element={
            <ProtectedRoute>
              <EditAsset />
            </ProtectedRoute>
          }
        />
        <Route
          path="/users"
          element={
            <ProtectedRoute allowedRoles="admin">
              <Users />
            </ProtectedRoute>
          }
        />
        <Route
          path="/users/edit-user/:id"
          element={
            <ProtectedRoute allowedRoles="admin">
              <EditUser />
            </ProtectedRoute>
          }
        />
        <Route
          path="/account"
          element={
            <ProtectedRoute>
              <Account />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}
