import Link from "next/link";
import {getLocale, getTranslations} from "next-intl/server";
import LanguageSwitcher from "./LanguageSwitcher";

export default async function Header() {
  const locale = await getLocale();
  const t = await getTranslations("Nav");

  return (
    <header className="border-b border-gray-100">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
        <Link href={`/${locale}`} className="font-extrabold tracking-tight">
          ETPBH MAROUANE
        </Link>

        <nav className="hidden items-center gap-6 text-sm md:flex">
          <a className="hover:underline" href="#services">
            {t("services")}
          </a>
          <a className="hover:underline" href="#projects">
            {t("projects")}
          </a>
          <a className="hover:underline" href="#contact">
            {t("contact")}
          </a>
        </nav>

        <LanguageSwitcher />
      </div>
    </header>
  );
}