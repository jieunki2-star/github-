#!/usr/bin/env python3
"""본문 인용과 참고문헌 목록(paper/references.md)의 대응을 검사한다.

검사 내용
- 본문에 있으나 참고문헌에 없는 인용
- 참고문헌에 있으나 본문에서 인용하지 않은 문헌
- 참고문헌의 미확인(⚠️) 항목
- 남아 있는 [인용 필요] / [연구자 입력] 표시

인식하는 본문 인용 형식 (APA 계열)
  (홍길동, 2020) (홍길동·김철수, 2021) (홍길동 외, 2022) (홍길동, 2020: 15)
  (Smith, 2019) (Smith & Lee, 2020) (Smith et al., 2021) (Smith, 2019, p. 3)
  여러 개: (홍길동, 2020; Smith, 2019)
  서술형: 홍길동(2020), Smith(2019), Smith와 Lee(2020), 홍길동 외(2022)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ROOT / "paper" / "sections"
REFS = ROOT / "paper" / "references.md"

YEAR = r"(?:19|20)\d{2}[a-z]?"
NAME = r"[가-힣]{2,5}|[A-Z][A-Za-z'\-]+"

PAREN_RE = re.compile(r"\(([^()]*?" + YEAR + r"[^()]*)\)")
ITEM_RE = re.compile(r"^\s*(?P<auth>.+?),\s*(?P<year>" + YEAR + r")\b")
NARR_RE = re.compile(
    r"(?P<auth>(?:" + NAME + r")(?:\s*(?:·|&|와|과|and)\s*(?:" + NAME + r"))*(?:\s*(?:외|et al\.))?)\s*\((?P<year>" + YEAR + r")\)"
)
MARK_RE = re.compile(r"\[(인용 필요|연구자 입력)[^\]]*\]")


def first_author(auth: str) -> str:
    auth = re.sub(r"\s*(외|et al\.)\s*$", "", auth.strip())
    first = re.split(r"\s*(?:·|&|,|와|과|\band\b)\s*", auth)[0]
    return first.strip()


def citations_in_text() -> dict[tuple[str, str], list[str]]:
    found: dict[tuple[str, str], list[str]] = {}
    for path in sorted(SECTIONS.glob("*.md")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            loc = f"{path.name}:{lineno}"
            for m in PAREN_RE.finditer(line):
                for part in m.group(1).split(";"):
                    im = ITEM_RE.match(part)
                    if im:
                        key = (first_author(im.group("auth")), im.group("year"))
                        found.setdefault(key, []).append(loc)
            for m in NARR_RE.finditer(line):
                key = (first_author(m.group("auth")), m.group("year"))
                found.setdefault(key, []).append(loc)
    return found


def reference_entries() -> tuple[dict[tuple[str, str], str], list[str]]:
    entries: dict[tuple[str, str], str] = {}
    unverified: list[str] = []
    if not REFS.exists():
        return entries, unverified
    for line in REFS.read_text(encoding="utf-8").splitlines():
        text = line.strip().lstrip("-*0-9. ").strip()
        m = re.match(r"(?P<auth>.+?)\s*\((?P<year>" + YEAR + r")\)", text)
        if not m:
            continue
        surname = re.split(r"[,·\s]", m.group("auth").strip())[0]
        entries[(surname, m.group("year"))] = text
        if "⚠️" in line or "미확인" in line:
            unverified.append(text[:100])
    return entries, unverified


def main() -> int:
    if not SECTIONS.exists() or not any(SECTIONS.glob("*.md")):
        print("paper/sections/ 에 원고가 없습니다.")
        return 0
    cited = citations_in_text()
    refs, unverified = reference_entries()

    missing = {k: v for k, v in cited.items() if k not in refs}
    unused = [v for k, v in refs.items() if k not in cited]

    print(f"본문 인용 {len(cited)}건 / 참고문헌 {len(refs)}건\n")

    print(f"## 참고문헌에 없는 본문 인용 ({len(missing)})")
    for (a, y), locs in sorted(missing.items()):
        print(f"- {a}, {y}  ← {', '.join(locs[:5])}")

    print(f"\n## 본문에서 인용하지 않은 참고문헌 ({len(unused)})")
    for t in unused:
        print(f"- {t[:100]}")

    print(f"\n## 미확인(⚠️) 참고문헌 ({len(unverified)})")
    for t in unverified:
        print(f"- {t}")

    marks = []
    for path in sorted(SECTIONS.glob("*.md")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for m in MARK_RE.finditer(line):
                marks.append(f"{path.name}:{lineno}  {m.group(0)}")
    print(f"\n## 남은 표시 ({len(marks)})")
    for m in marks:
        print(f"- {m}")

    return 1 if (missing or unverified) else 0


if __name__ == "__main__":
    sys.exit(main())
