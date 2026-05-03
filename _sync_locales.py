"""Copy legal pages into ru/ and en/ with absolute asset paths and locale-prefixed links."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEGAL = ["terms.html", "privacy.html", "refund-policy.html", "legal-compliance.html"]

RU_TITLES = {
    "terms.html": "Условия использования — Sendy",
    "privacy.html": "Политика конфиденциальности — Sendy",
    "refund-policy.html": "Возвраты и оплата — Sendy",
    "legal-compliance.html": "Правовая информация и комплаенс — Sendy",
}

RU_HEADINGS = {
    "terms.html": "Условия использования",
    "privacy.html": "Политика конфиденциальности",
    "refund-policy.html": "Политика возвратов и оплаты",
    "legal-compliance.html": "Правовая информация и комплаенс",
}

RU_DATE_LINE = "Последнее обновление: 2 мая 2026 г."

LEGAL_BODIES_RU = ROOT / "legal-bodies" / "ru"


def inject_ru_article(html: str, filename: str) -> str:
    frag = LEGAL_BODIES_RU / filename.replace(".html", ".article.html")
    if not frag.is_file():
        return html
    inner = frag.read_text(encoding="utf-8").strip()
    return re.sub(
        r'<article class="legal-body mt-6 min-w-0 sm:mt-8">[\s\S]*?</article>',
        f'<article class="legal-body mt-6 min-w-0 sm:mt-8">\n{inner}\n</article>',
        html,
        count=1,
    )


def patch_legal_nav_labels_ru(html: str, prefix: str) -> str:
    pairs = [
        (
            f'<a href="{prefix}/terms.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Terms</a>',
            f'<a href="{prefix}/terms.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Условия</a>',
        ),
        (
            f'<a href="{prefix}/terms.html" class="transition hover:text-violet">Terms</a>',
            f'<a href="{prefix}/terms.html" class="transition hover:text-violet">Условия</a>',
        ),
        (
            f'<a href="{prefix}/privacy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Privacy</a>',
            f'<a href="{prefix}/privacy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Конфиденциальность</a>',
        ),
        (
            f'<a href="{prefix}/privacy.html" class="transition hover:text-violet">Privacy</a>',
            f'<a href="{prefix}/privacy.html" class="transition hover:text-violet">Конфиденциальность</a>',
        ),
        (
            f'<a href="{prefix}/refund-policy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Refund</a>',
            f'<a href="{prefix}/refund-policy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Возврат</a>',
        ),
        (
            f'<a href="{prefix}/refund-policy.html" class="transition hover:text-violet">Refund</a>',
            f'<a href="{prefix}/refund-policy.html" class="transition hover:text-violet">Возврат</a>',
        ),
        (
            f'<a href="{prefix}/legal-compliance.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Compliance</a>',
            f'<a href="{prefix}/legal-compliance.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Комплаенс</a>',
        ),
        (
            f'<a href="{prefix}/legal-compliance.html" class="transition hover:text-violet">Compliance</a>',
            f'<a href="{prefix}/legal-compliance.html" class="transition hover:text-violet">Комплаенс</a>',
        ),
        (
            f'<a href="{prefix}/report-abuse.html" class="rounded-lg px-3 py-2.5 font-semibold text-violet hover:bg-[#F8F9FB]">Report abuse</a>',
            f'<a href="{prefix}/report-abuse.html" class="rounded-lg px-3 py-2.5 font-semibold text-violet hover:bg-[#F8F9FB]">Сообщить о нарушении</a>',
        ),
        (
            f'<a href="{prefix}/report-abuse.html" class="transition hover:text-violet">Report abuse</a>',
            f'<a href="{prefix}/report-abuse.html" class="transition hover:text-violet">Сообщить о нарушении</a>',
        ),
    ]
    for en, ru in pairs:
        html = html.replace(en, ru)
    return html


def patch_legal_fixed(html: str, lang: str, filename: str) -> str:
    prefix = f"/{lang}"
    home = "/en/" if lang == "en" else "/ru/"
    html = html.replace('href="assets/', 'href="/assets/')
    html = html.replace('src="assets/', 'src="/assets/')
    html = html.replace('href="index.html"', f'href="{home}"')
    for name in LEGAL:
        html = html.replace(f'href="{name}"', f'href="{prefix}/{name}"')
        html = html.replace(f'href="/{name}"', f'href="{prefix}/{name}"')
    html = html.replace("href='/en/report-abuse'", f"href='{prefix}/report-abuse.html'")
    html = html.replace("href='/en/report-abuse.html'", f"href='{prefix}/report-abuse.html'")
    html = re.sub(
        r'href="/(en|ru)/report-abuse(?:\.html)?"',
        f'href="{prefix}/report-abuse.html"',
        html,
    )
    html = html.replace(
        'href="/" class="min-w-0 shrink text-lg font-black tracking-[-.05em] text-[#0F172A] sm:text-xl">sendy</a>',
        f'href="{home}" class="min-w-0 shrink text-lg font-black tracking-[-.05em] text-[#0F172A] sm:text-xl">sendy</a>',
    )
    html = html.replace('href="report.html"', f'href="{prefix}/report-abuse.html"')
    html = html.replace(">Report</a>", ">Report abuse</a>")

    if lang == "ru":
        html = html.replace('aria-label="Open menu"', 'aria-label="Открыть меню"')
        html = html.replace('aria-label="Legal navigation"', 'aria-label="Юридическая навигация"')
        html = html.replace(
            f'<a href="{home}" class="text-violet hover:underline">Home</a>',
            f'<a href="{home}" class="text-violet hover:underline">Главная</a>',
        )
        html = patch_legal_nav_labels_ru(html, prefix)
        if filename in RU_TITLES:
            html = re.sub(r"<title>.*?</title>", f"<title>{RU_TITLES[filename]}</title>", html, count=1)
            html = html.replace('<html lang="en">', '<html lang="ru">', 1)
        if filename in RU_HEADINGS:
            html = re.sub(
                r'(<h1 class="mt-3 text-\[26px\] font-black leading-\[1\.15\] tracking-\[-\.03em\] text-\[#0F172A\] sm:mt-4 sm:text-\[32px\] sm:leading-tight">)[^<]*(</h1>)',
                rf"\1{RU_HEADINGS[filename]}\2",
                html,
                count=1,
            )
            html = html.replace(
                '<p class="mt-2 text-[14px] text-[#6E7380]">Last updated: 2 May 2026</p>',
                f'<p class="mt-2 text-[14px] text-[#6E7380]">{RU_DATE_LINE}</p>',
            )

    return html


def main() -> None:
    for lang in ("ru", "en"):
        (ROOT / lang).mkdir(exist_ok=True)
    for lang in ("ru", "en"):
        for name in LEGAL:
            raw = (ROOT / name).read_text(encoding="utf-8")
            text = patch_legal_fixed(raw, lang, name)
            if lang == "ru":
                text = inject_ru_article(text, name)
            (ROOT / lang / name).write_text(text, encoding="utf-8")

    idx = (ROOT / "index.html").read_text(encoding="utf-8")
    ru_idx = idx.replace(
        '<a href="/" class="rounded-md px-2 py-0.5 text-violet" hreflang="ru">RU</a>',
        '<a href="/ru/" class="rounded-md px-2 py-0.5 text-violet" hreflang="ru">RU</a>',
    )
    ru_idx = ru_idx.replace(
        '<a class="rounded-xl px-4 py-2 text-violet" href="/">RU</a>',
        '<a class="rounded-xl px-4 py-2 text-violet" href="/ru/">RU</a>',
    )
    (ROOT / "ru" / "index.html").write_text(ru_idx, encoding="utf-8")
    print("Synced legal pages into ru/ and en/")


if __name__ == "__main__":
    main()
