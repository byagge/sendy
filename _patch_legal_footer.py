from pathlib import Path

root = Path(__file__).resolve().parent
old = '<footer class="border-t border-[#E9EBF3] bg-[#FAFBFC] py-8 text-center text-[12px] text-[#6E7380]">'
new = '<footer class="border-t border-[#E9EBF3] bg-[#FAFBFC] px-4 py-8 text-center text-[11px] leading-snug text-[#6E7380] sm:text-[12px]">'
for p in root.rglob("*.html"):
    if p.name in ("index.html", "report.html"):
        continue
    t = p.read_text(encoding="utf-8")
    if old in t:
        p.write_text(t.replace(old, new), encoding="utf-8")
