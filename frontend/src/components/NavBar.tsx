import { navLinks } from './navlinks';
export default function NavBar() {
  return (
    <nav className="fixed top-6 z-50 flex w-full justify-center">
      <div className="flex items-center gap-3 rounded-full bg-pink-400/70 backdrop-blur-md px-3 py-2 shadow-[0_8px_25px_rgba(236,72,153,0.35)] border border-pink-300">
        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-white text-pink-500 shadow-md cursor-pointer">
          H
        </div>

        <ul className="flex items-center gap-6 px-4 text-white text-sm font-medium">
          {navLinks.map((link) => (
            <li key={link.name}>
              <a
                href={link.path}
                className="transition-all duration-300 hover:text-pink-100 hover:scale-105"
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
