# -*- coding: utf-8 -*-
"""Apply mobile-friendly legal shell (header + main + legal.css) to policy HTML files."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEGAL = ["terms.html", "privacy.html", "refund-policy.html", "legal-compliance.html"]

HEADER_EN = """<header class="legal-header sticky top-0 z-40 border-b border-[#E9EBF3] bg-white/95 backdrop-blur-md">
    <div class="mx-auto max-w-[880px] px-4 py-3 sm:px-6 sm:py-4 lg:px-8">
      <div class="flex items-center justify-between gap-3">
        <a href="/en/" class="min-w-0 shrink text-lg font-black tracking-[-.05em] text-[#0F172A] sm:text-xl">sendy</a>
        <details class="relative sm:hidden">
          <summary class="flex h-10 w-10 cursor-pointer list-none items-center justify-center rounded-xl border border-[#E9EBF3] bg-white text-[#0F172A] shadow-sm [&::-webkit-details-marker]:hidden" aria-label="Open menu">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
          </summary>
          <div class="absolute right-0 top-full z-50 mt-2 w-[min(calc(100vw-2rem),18rem)] rounded-2xl border border-[#E9EBF3] bg-white p-3 shadow-xl">
            <nav class="flex flex-col gap-1 text-[14px] font-semibold text-[#374151]" aria-label="Legal navigation">
              <a href="/en/terms.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Terms</a>
              <a href="/en/privacy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Privacy</a>
              <a href="/en/refund-policy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Refund</a>
              <a href="/en/legal-compliance.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Compliance</a>
              <a href="/en/report-abuse.html" class="rounded-lg px-3 py-2.5 font-semibold text-violet hover:bg-[#F8F9FB]">Report abuse</a>
            </nav>
          </div>
        </details>
        <nav class="hidden flex-wrap items-center justify-end gap-x-3 gap-y-2 text-[12px] font-semibold text-[#6E7380] sm:flex sm:text-[13px] lg:gap-x-4" aria-label="Legal navigation">
          <a href="/en/terms.html" class="transition hover:text-violet">Terms</a>
          <a href="/en/privacy.html" class="transition hover:text-violet">Privacy</a>
          <a href="/en/refund-policy.html" class="transition hover:text-violet">Refund</a>
          <a href="/en/legal-compliance.html" class="transition hover:text-violet">Compliance</a>
          <a href="/en/report-abuse.html" class="transition hover:text-violet">Report abuse</a>
        </nav>
      </div>
    </div>
  </header>"""

HEADER_RU = """<header class="legal-header sticky top-0 z-40 border-b border-[#E9EBF3] bg-white/95 backdrop-blur-md">
    <div class="mx-auto max-w-[880px] px-4 py-3 sm:px-6 sm:py-4 lg:px-8">
      <div class="flex items-center justify-between gap-3">
        <a href="/ru/" class="min-w-0 shrink text-lg font-black tracking-[-.05em] text-[#0F172A] sm:text-xl">sendy</a>
        <details class="relative sm:hidden">
          <summary class="flex h-10 w-10 cursor-pointer list-none items-center justify-center rounded-xl border border-[#E9EBF3] bg-white text-[#0F172A] shadow-sm [&::-webkit-details-marker]:hidden" aria-label="Открыть меню">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
          </summary>
          <div class="absolute right-0 top-full z-50 mt-2 w-[min(calc(100vw-2rem),18rem)] rounded-2xl border border-[#E9EBF3] bg-white p-3 shadow-xl">
            <nav class="flex flex-col gap-1 text-[14px] font-semibold text-[#374151]" aria-label="Юридическая навигация">
              <a href="/ru/terms.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Terms</a>
              <a href="/ru/privacy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Privacy</a>
              <a href="/ru/refund-policy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Refund</a>
              <a href="/ru/legal-compliance.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Compliance</a>
              <a href="/ru/report-abuse.html" class="rounded-lg px-3 py-2.5 font-semibold text-violet hover:bg-[#F8F9FB]">Сообщить о нарушении</a>
            </nav>
          </div>
        </details>
        <nav class="hidden flex-wrap items-center justify-end gap-x-3 gap-y-2 text-[12px] font-semibold text-[#6E7380] sm:flex sm:text-[13px] lg:gap-x-4" aria-label="Legal navigation">
          <a href="/ru/terms.html" class="transition hover:text-violet">Terms</a>
          <a href="/ru/privacy.html" class="transition hover:text-violet">Privacy</a>
          <a href="/ru/refund-policy.html" class="transition hover:text-violet">Refund</a>
          <a href="/ru/legal-compliance.html" class="transition hover:text-violet">Compliance</a>
          <a href="/ru/report-abuse.html" class="transition hover:text-violet">Report abuse</a>
        </nav>
      </div>
    </div>
  </header>"""

HEADER_ROOT = """<header class="legal-header sticky top-0 z-40 border-b border-[#E9EBF3] bg-white/95 backdrop-blur-md">
    <div class="mx-auto max-w-[880px] px-4 py-3 sm:px-6 sm:py-4 lg:px-8">
      <div class="flex items-center justify-between gap-3">
        <a href="/" class="min-w-0 shrink text-lg font-black tracking-[-.05em] text-[#0F172A] sm:text-xl">sendy</a>
        <details class="relative sm:hidden">
          <summary class="flex h-10 w-10 cursor-pointer list-none items-center justify-center rounded-xl border border-[#E9EBF3] bg-white text-[#0F172A] shadow-sm [&::-webkit-details-marker]:hidden" aria-label="Open menu">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
          </summary>
          <div class="absolute right-0 top-full z-50 mt-2 w-[min(calc(100vw-2rem),18rem)] rounded-2xl border border-[#E9EBF3] bg-white p-3 shadow-xl">
            <nav class="flex flex-col gap-1 text-[14px] font-semibold text-[#374151]" aria-label="Legal navigation">
              <a href="/terms.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Terms</a>
              <a href="/privacy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Privacy</a>
              <a href="/refund-policy.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Refund</a>
              <a href="/legal-compliance.html" class="rounded-lg px-3 py-2.5 hover:bg-[#F8F9FB] hover:text-violet">Compliance</a>
              <a href="/en/report-abuse.html" class="rounded-lg px-3 py-2.5 font-semibold text-violet hover:bg-[#F8F9FB]">Report abuse</a>
            </nav>
          </div>
        </details>
        <nav class="hidden flex-wrap items-center justify-end gap-x-3 gap-y-2 text-[12px] font-semibold text-[#6E7380] sm:flex sm:text-[13px] lg:gap-x-4" aria-label="Legal navigation">
          <a href="/terms.html" class="transition hover:text-violet">Terms</a>
          <a href="/privacy.html" class="transition hover:text-violet">Privacy</a>
          <a href="/refund-policy.html" class="transition hover:text-violet">Refund</a>
          <a href="/legal-compliance.html" class="transition hover:text-violet">Compliance</a>
          <a href="/en/report-abuse.html" class="transition hover:text-violet">Report abuse</a>
        </nav>
      </div>
    </div>
  </header>"""


def inject_legal_css(html: str, root_relative: bool) -> str:
    if "legal.css" in html:
        return html
    if root_relative:
        needle = '<link rel="stylesheet" href="assets/css/main.css">'
        insert = '<link rel="stylesheet" href="assets/css/main.css">\n  <link rel="stylesheet" href="assets/css/legal.css">'
    else:
        needle = '<link rel="stylesheet" href="/assets/css/main.css">'
        insert = '<link rel="stylesheet" href="/assets/css/main.css">\n  <link rel="stylesheet" href="/assets/css/legal.css">'
    if needle in html:
        return html.replace(needle, insert, 1)
    return html


def swap_header(html: str, header: str) -> str:
    return re.sub(r"<header\b[^>]*>.*?</header>", header.strip(), html, count=1, flags=re.DOTALL)


def patch_main(html: str) -> str:
    html = html.replace(
        '<main class="mx-auto max-w-[880px] px-5 py-12 sm:px-8">',
        '<main class="legal-main mx-auto max-w-[880px] min-w-0 px-4 pb-12 pt-6 sm:px-6 sm:pb-14 sm:pt-8 lg:px-8">',
        1,
    )
    html = html.replace(
        '<h1 class="mt-4 text-[32px] font-black tracking-[-.03em] text-[#0F172A]">',
        '<h1 class="mt-3 text-[26px] font-black leading-[1.15] tracking-[-.03em] text-[#0F172A] sm:mt-4 sm:text-[32px] sm:leading-tight">',
        1,
    )
    html = html.replace(
        '<article class="legal-body mt-8">',
        '<article class="legal-body mt-6 min-w-0 sm:mt-8">',
        1,
    )
    html = html.replace(
        '<p class="text-[13px] font-medium text-[#6E7380]"><a href="',
        '<p class="text-[12px] font-medium text-[#6E7380] sm:text-[13px]"><a href="',
        1,
    )
    return html


def process(path: Path, header: str, root_css: bool) -> None:
    html = path.read_text(encoding="utf-8")
    if 'class="legal-header"' in html and "legal.css" in html:
        return
    html = inject_legal_css(html, root_css)
    html = swap_header(html, header)
    html = patch_main(html)
    path.write_text(html, encoding="utf-8")


def main() -> None:
    for name in LEGAL:
        process(ROOT / name, HEADER_ROOT, root_css=True)
        process(ROOT / "en" / name, HEADER_EN, root_css=False)
        process(ROOT / "ru" / name, HEADER_RU, root_css=False)
    print("Patched legal pages: mobile header + legal.css + main spacing")


if __name__ == "__main__":
    main()
