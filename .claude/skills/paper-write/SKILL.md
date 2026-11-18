---
name: paper-write
description: 논문 작성 전 과정(기획 → 문헌조사 → 개요 → 집필 → 심사·수정 → 교정 → 초록 → 원고 합치기)을 단계별로 진행한다. 각 단계 사이에 연구자 확인을 받는다.
argument-hint: "[논문 주제]"
---

논문 작성 전 과정을 진행한다. 주제: $ARGUMENTS

현재 진행 상황을 먼저 파악해, 이미 끝난 단계는 건너뛰고 이어서 진행한다.
- `paper/project.md` 없음 → 1단계부터
- `research/notes/` 비어 있음 → 2단계부터
- `paper/outline.md` 없음 → 3단계부터
- `paper/sections/`에 개요의 장이 다 없음 → 4단계부터

단계 (각 단계 끝에 결과를 요약하고 연구자의 확인이나 수정 의견을 받은 뒤 다음으로 넘어간다):
1. 기획: `/paper-init`의 절차를 따른다.
2. 문헌조사: `/paper-research`의 절차를 따른다.
3. 개요: `/paper-outline`의 절차를 따른다. **개요 확정은 반드시 연구자 승인을 받는다.**
4. 집필: `/paper-draft 전체`의 절차를 따른다.
5. 심사·수정: `/paper-review --fix`의 절차를 따른다. 수정 후 한 번 더 심사해 "수정 후 게재" 이상인지 확인한다 (최대 2회).
6. 교정: `/paper-polish 전체`의 절차를 따른다.
7. 초록: `/paper-abstract`의 절차를 따른다.
8. 마무리: `bash scripts/build.sh`로 원고를 `output/`에 합치고, `python3 scripts/check_citations.py`로 최종 점검한다.
   남은 `[인용 필요]`·`[연구자 입력]` 목록과 투고 전 연구자가 직접 확인할 체크리스트(표절 검사, 저자 정보, IRB, 연구윤리 서약 등)를 제시한다.
