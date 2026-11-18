---
name: paper-review
description: 투고 전 자체 심사. 심사위원 관점의 내용 심사와 인용·참고문헌 검사를 동시에 수행하고, 원하면 수정까지 진행한다.
argument-hint: "[--fix]"
---

1. `paper/sections/`에 원고가 없으면 멈추고 `/paper-draft`를 안내한다.
2. 다음 두 에이전트를 **동시에** 실행한다.
   - `peer-reviewer`: 내용 심사 → `paper/reviews/review-<오늘 날짜>.md`
   - `citation-checker`: 인용 검사 → `paper/reviews/citations-<오늘 날짜>.md`
3. 두 보고서를 합쳐 연구자에게 보여준다: 판정, 반드시 고칠 것(우선순위순), 인용 문제 요약.
4. 인자에 `--fix`가 있거나 연구자가 동의하면, 주요 수정 요구를 장별로 묶어 `section-writer`에게 수정을 맡긴다. 연구 설계·해석을 바꾸는 요구는 연구자 결정이 필요하므로 수정하지 말고 질문으로 남긴다.
