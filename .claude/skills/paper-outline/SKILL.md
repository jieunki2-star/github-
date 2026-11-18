---
name: paper-outline
description: 연구문제와 문헌조사를 바탕으로 논문의 장·절 구성과 문단별 논증 흐름(개요)을 만든다.
argument-hint: "[구성에 대한 요청 사항]"
---

1. `paper/project.md`와 `research/notes/`가 있는지 확인한다. 노트가 없으면 `/paper-research`를 먼저 권하되, 연구자가 원하면 그대로 진행한다.
2. `outline-architect` 에이전트에게 `paper/outline.md` 작성을 맡긴다. 요청 사항: $ARGUMENTS
3. 개요를 연구자에게 요약해 보여주고 확인받는다: 제목 후보, 핵심 주장, 장 구성, 근거가 부족한 지점.
4. 연구자의 수정 의견을 반영해 개요를 고친 뒤, `/paper-draft 서론`부터 장별 집필을 안내한다.
