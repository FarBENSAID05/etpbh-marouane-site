"use client";

import Link from "next/link";
import {usePathname} from "next/navigation";

const LOCALES = ["fr", "ar", "en"] as const;

export default function LanguageSwitcher() {
  const pathname = usePathname() || "/";
  const parts = pathname.split("/");
  const currentLocale = (parts[1] || "fr") as (typeof LOCALES)[number];
  const rest = "/" + parts.slice(2).join("/");
  const restPath = rest === "/" ? "" : rest;

  return (
    <div className="flex items-center gap-2 text-sm">
      {LOCALES.map((l) => {
        const href = `/${l}${restPath}`;
        const active = l === currentLocale;

        return (
          <Link
            key={l}
            href={href}
            className={
              "rounded px-2 py-1 " +
              (active ? "bg-gray-900 text-white" : "hover:bg-gray-100")
            }
          >
            {l.toUpperCase()}
          </Link>
        );
      })}
    </div>
  );
}