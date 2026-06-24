import { Navigate } from "react-router-dom";
import { getUserRole, isAuthenticated } from "../utils/auth";

type Props = {
  children: React.ReactNode;
  allowedRoles?: string;
};

export default function ProtectedRoute({ children, allowedRoles }: Props) {
  if (!isAuthenticated()) {
    return (
      <Navigate to="/" state={{ message: "Please log in to continue." }} />
    );
  }
  const role = getUserRole();

  if (allowedRoles && role && !allowedRoles.includes(role)) {
    alert("Not authorised");
    return <Navigate to="/dashboard" />;
  }
  return children;
}
