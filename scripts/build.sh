#!/usr/bin/env bash
# paper/sections/*.md 와 paper/references.md 를 하나의 원고로 합친다.
# pandoc 이 있으면 Word(.docx)도 만든다. (templates/reference.docx 가 있으면 그 서식을 쓴다)
set -euo pipefail
cd "$(dirname "$0")/.."

mkdir -p output
out=output/manuscript.md
: > "$out"

for f in paper/sections/*.md; do
  [ -e "$f" ] || { echo "paper/sections/ 에 원고가 없습니다."; exit 1; }
  cat "$f" >> "$out"
  printf '\n\n' >> "$out"
done

if [ -f paper/references.md ]; then
  # 확인 상태 주석(<!-- ... -->)은 제거하고 붙인다.
  sed -E 's/[[:space:]]*<!--.*-->//' paper/references.md >> "$out"
fi

echo "원고: $out ($(wc -m < "$out") 자)"

if command -v pandoc >/dev/null 2>&1; then
  args=()
  [ -f templates/reference.docx ] && args+=(--reference-doc=templates/reference.docx)
  pandoc "$out" -o output/manuscript.docx "${args[@]}"
  echo "Word: output/manuscript.docx"
else
  echo "pandoc 이 없어 .docx 변환은 건너뜁니다. (설치: https://pandoc.org)"
fi

if grep -nE '\[(인용 필요|연구자 입력)' "$out" >/dev/null; then
  echo "주의: 아직 채우지 않은 [인용 필요]/[연구자 입력] 표시가 있습니다."
fi
