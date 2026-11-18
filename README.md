# 논문작성 에이전트 (국문 학술지용)

Claude Code 안에서 국문 학술지 논문을 **기획 → 문헌조사 → 개요 → 집필 → 자체 심사 → 교정 → 초록**까지 단계별로 진행하는 에이전트 모음입니다.

## 사용법

이 저장소에서 Claude Code를 실행한 뒤:

```
/paper-write 대학생의 자기효능감이 학업지속의도에 미치는 영향
```

전 과정을 한 번에 진행합니다(각 단계마다 확인을 받습니다). 단계별로 직접 실행할 수도 있습니다.

| 명령 | 하는 일 |
|---|---|
| `/paper-init [주제]` | 주제·연구문제·대상 학술지 규정 설정 → `paper/project.md` |
| `/paper-research [키워드]` | 국내외 선행연구 조사 → `research/notes/`, `paper/references.md` |
| `/paper-outline` | 장·절 구성과 문단별 논증 흐름 → `paper/outline.md` |
| `/paper-draft <장\|전체>` | 장별 집필 → `paper/sections/` |
| `/paper-review [--fix]` | 심사위원 관점 심사 + 인용 검사 (→ 수정) |
| `/paper-polish [장\|전체]` | 맞춤법·띄어쓰기·학술 문체·번역투 교정 |
| `/paper-abstract` | 국문·영문 초록, 키워드, 영문 제목 |

## 에이전트 (`.claude/agents/`)

- `literature-researcher` — KCI·RISS·Google Scholar·Crossref 등에서 문헌 검색, 서지 확인, 문헌 노트
- `outline-architect` — 연구문제↔결과↔결론이 맞물리는 개요 설계
- `section-writer` — 장별 학술 문체 집필
- `peer-reviewer` — KCI 등재지 심사 기준으로 판정·수정 요구
- `citation-checker` — 본문 인용↔참고문헌 대응, 서지 실재 확인, 양식 점검
- `korean-editor` — 내용은 그대로 두고 표현만 교정

## 연구윤리 안전장치

- 확인하지 못한 문헌은 지어내지 않고 `[인용 필요: ...]`로 남깁니다.
- 연구자가 제공하지 않은 데이터·결과는 만들지 않고 `[연구자 입력: ...]`로 남깁니다.
- 참고문헌마다 확인 상태(✅/⚠️)와 출처 URL을 기록합니다.

연구 결과 수치, 분석 결과, 면담 자료 등은 `paper/project.md`의 "확보한 자료·결과"에 적거나 `research/` 폴더에 넣어 주세요. 소장한 논문 PDF는 `research/pdfs/`에 넣으면 정밀하게 읽고 인용합니다.

## 도구

```bash
python3 scripts/check_citations.py   # 인용 ↔ 참고문헌 대응, 미확인 문헌, 남은 표시 검사
bash scripts/build.sh                # output/manuscript.md (+ pandoc 있으면 .docx) 생성
```

학술지 Word 서식을 쓰려면 `templates/reference.docx`에 서식 파일을 넣으세요(pandoc reference-doc).

## 투고 전 연구자가 직접 확인할 것

표절 검사(KCI 문헌유사도검사 등), 모든 인용의 원문 대조, 저자 정보·소속, IRB 승인 번호, 학술지 연구윤리 서약서, 생성형 AI 사용 고지 규정.
