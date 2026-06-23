import { useNavigate } from "react-router-dom";
import { navLinks } from "./navlinks";
import { getUserRole } from "../utils/auth";
export default function NavBar() {
  const navigate = useNavigate();
  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  const role = getUserRole();
  return (
    <nav className="fixed top-6 z-50 flex w-full justify-center">
      <div className="flex items-center gap-3 rounded-full bg-pink-400/70 backdrop-blur-md px-3 py-2 shadow-[0_8px_25px_rgba(236,72,153,0.35)] border border-pink-300">
        <ul className="flex items-center gap-6 px-4 text-white text-sm font-medium">
          {navLinks
            .filter((link) => {
              if (link.name === "Users" && role !== "admin") {
                return false;
              }

              return true;
            })
            .map((link) => (
              <li key={link.name}>
                <a
                  href={link.path}
                  className="transition-all duration-300 hover:text-pink-100 hover:scale-105"
                >
                  {link.name}
                </a>
              </li>
            ))}
          <li>
            <button
              onClick={handleLogout}
              className="rounded-full bg-white px-4 py-2 text-pink-500 text-sm font-medium shadow-md hover:bg-pink-100 transition"
            >
              Logout
            </button>
          </li>
        </ul>
      </div>
    </nav>
  );
}
