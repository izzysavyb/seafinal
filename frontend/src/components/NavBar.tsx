import { navLinks } from "./LoginBox";
export default function NavBar() {
  return (
    <nav className="fixed top-4 z-50 flex w-full justify-center">
      <div className="flex items-center gap-4">
        <ul className="flex items-center gap-4">
          {navLinks.map((link) => (
            <li key={link.name}>
              <a
                href={link.path}
                className="transition-colors hover:text-gray-400"
              >
                {link.name}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
}
