import Header from "../../components/Header";
import {getTranslations} from "next-intl/server";

function Stat({label, value}: {label: string; value: string}) {
  return (
    <div className="rounded-xl border border-gray-200 bg-white p-4">
      <div className="text-xs text-gray-500">{label}</div>
      <div className="mt-1 text-lg font-bold">{value}</div>
    </div>
  );
}

export default async function HomePage() {
  const t = await getTranslations("Home");

  return (
    <main className="min-h-screen bg-white">
      <Header />

      {/* HERO */}
      <section className="mx-auto max-w-6xl px-6 py-14">
        <div className="grid gap-10 lg:grid-cols-2 lg:items-center">
          <div>
            <p className="text-sm font-semibold tracking-wide text-yellow-600">
              {t("kicker")}
            </p>

            <h1 className="mt-3 text-4xl font-extrabold tracking-tight sm:text-5xl">
              {t("headline")}
            </h1>

            <p className="mt-4 text-lg text-gray-600">{t("tagline")}</p>

            <div className="mt-8 flex flex-wrap gap-3">
              <a
                href="#devis"
                className="rounded-md bg-yellow-500 px-5 py-3 text-sm font-semibold text-black hover:bg-yellow-400"
              >
                {t("cta")}
              </a>
              <a
                href="#services"
                className="rounded-md border border-gray-300 px-5 py-3 text-sm font-semibold hover:bg-gray-50"
              >
                {t("ctaSecondary")}
              </a>
            </div>

            <div className="mt-10 grid grid-cols-2 gap-4">
              <Stat label={t("stat1Label")} value={t("stat1Value")} />
              <Stat label={t("stat2Label")} value={t("stat2Value")} />
            </div>
          </div>

          {/* Right panel (placeholder) */}
          <div className="rounded-2xl bg-gray-50 p-8">
            <h2 className="text-lg font-bold">{t("panelTitle")}</h2>
            <p className="mt-2 text-sm text-gray-600">{t("panelDesc")}</p>

            <ul className="mt-6 space-y-3 text-sm">
              <li>✅ {t("panelItem1")}</li>
              <li>✅ {t("panelItem2")}</li>
              <li>✅ {t("panelItem3")}</li>
            </ul>
          </div>
        </div>
      </section>

      {/* SERVICES */}
      <section id="services" className="border-t border-gray-100">
        <div className="mx-auto max-w-6xl px-6 py-14">
          <h2 className="text-2xl font-extrabold">{t("servicesTitle")}</h2>
          <p className="mt-2 text-gray-600">{t("servicesDesc")}</p>

          <div className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            {[1, 2, 3, 4].map((i) => (
              <div
                key={i}
                className="rounded-2xl border border-gray-200 bg-white p-5"
              >
                <div className="text-base font-bold">{t(`service${i}Title`)}</div>
                <div className="mt-2 text-sm text-gray-600">
                  {t(`service${i}Desc`)}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* QUOTE */}
      <section id="devis" className="border-t border-gray-100">
        <div className="mx-auto max-w-6xl px-6 py-14">
          <h2 className="text-2xl font-extrabold">{t("quoteTitle")}</h2>
          <p className="mt-2 text-gray-600">{t("quoteDesc")}</p>

          <div className="mt-6 grid gap-3 md:grid-cols-2">
            <input className="rounded-md border px-4 py-3" placeholder={t("phName")} />
            <input className="rounded-md border px-4 py-3" placeholder={t("phPhone")} />
            <input className="rounded-md border px-4 py-3 md:col-span-2" placeholder={t("phService")} />
            <textarea className="rounded-md border px-4 py-3 md:col-span-2" rows={4} placeholder={t("phDetails")} />
            <button className="rounded-md bg-gray-900 px-5 py-3 text-sm font-semibold text-white hover:bg-black md:col-span-2">
              {t("send")}
            </button>
          </div>
        </div>
      </section>

      {/* FOOTER */}
      <footer id="contact" className="border-t border-gray-100">
        <div className="mx-auto max-w-6xl px-6 py-10 text-sm text-gray-600">
          {t("footer")}
        </div>
      </footer>
    </main>
  );
}