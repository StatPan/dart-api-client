# CHANGELOG



## v1.0.6 (2025-11-29)

### Fix

* fix: update release workflow and semantic-release config ([`ca81f5e`](https://github.com/StatPan/dart-api-client/commit/ca81f5e232d3ffc9f7254de6d73cac8bdffe6a93))

### Unknown

* Merge pull request #6 from StatPan/fix/release-workflow

fix: update release workflow and semantic-release config ([`6c49277`](https://github.com/StatPan/dart-api-client/commit/6c492774032907377b15b10ba2336d53d8427ec5))


## v1.0.5 (2025-11-29)

### Fix

* fix: pull latest changes after release to ensure correct build version ([`2e3621b`](https://github.com/StatPan/dart-api-client/commit/2e3621b4d3b3d661fd9387ebdf9021304d74bb20))

### Unknown

* Merge pull request #5 from StatPan/fix/pull-after-release

fix: pull after release ([`9c18a20`](https://github.com/StatPan/dart-api-client/commit/9c18a205475ba8b9b46891f1bf2225f9d45e8dec))


## v1.0.4 (2025-11-29)

### Fix

* fix: separate build step from semantic-release to ensure correct versioning ([`6da22d5`](https://github.com/StatPan/dart-api-client/commit/6da22d5efc583c63d42d08e04b60576fada697bb))

### Unknown

* Merge pull request #4 from StatPan/fix/build-versioning

fix: separate build step ([`c62ff7d`](https://github.com/StatPan/dart-api-client/commit/c62ff7d6fd72ccfa12d0b1adfc39d92a5f7170b0))


## v1.0.3 (2025-11-29)

### Chore

* chore: use explicit pypi publish action ([`040cbe3`](https://github.com/StatPan/dart-api-client/commit/040cbe33468ee3d848c3dc9f43e188a162351460))

### Fix

* fix: trigger release to verify pypi publish ([`80e7173`](https://github.com/StatPan/dart-api-client/commit/80e717372f24a6ec338f2869c1905bd9d3ae12f4))

### Unknown

* Merge pull request #3 from StatPan/fix/trigger-release

fix: trigger release ([`d612194`](https://github.com/StatPan/dart-api-client/commit/d612194e81ffa97b0488cc89545201d9b4e65456))

* Merge pull request #2 from StatPan/chore/fix-pypi-publish

chore: fix pypi publish workflow ([`f073298`](https://github.com/StatPan/dart-api-client/commit/f0732981199697bf9479c34ab8991e98239938ac))


## v1.0.2 (2025-11-29)

### Chore

* chore: setup commitizen for conventional commits ([`93aedc8`](https://github.com/StatPan/dart-api-client/commit/93aedc853f75ce9bcc1d5bdc88da27a3878f59da))

### Documentation

* docs: add contributing guide with workflow rules ([`db9e7de`](https://github.com/StatPan/dart-api-client/commit/db9e7dedb776535816b810463b7c0a755523a3b5))

### Fix

* fix(client): use logging instead of warnings for unclosed client check ([`836e98d`](https://github.com/StatPan/dart-api-client/commit/836e98d50c77125bcd65e2ca91b2122e1f45fb02))

* fix: enhance robustness in request validation and cleanup

- Add __del__ hook to warn about unclosed client
- Explicitly check for &#39;status&#39; field in JSON response
- Raise DartAPIError if status is missing ([`eba20f7`](https://github.com/StatPan/dart-api-client/commit/eba20f71d710d7faa9e2c2d46ed9f2725c5c4609))

### Unknown

* Merge pull request #1 from StatPan/refactor/issue-2-robustness-improvements

fix: enhance robustness in request validation and cleanup ([`4ce9668`](https://github.com/StatPan/dart-api-client/commit/4ce9668d5a1596786cd1bf27bc195d2f250719c8))


## v1.0.1 (2025-11-28)

### Fix

* fix: correct exception arguments and restore py.typed

- Fix TypeError in exception raising (positional args mismatch)
- Add type guard for response data
- Restore py.typed marker for PEP 561 compliance ([`fb98177`](https://github.com/StatPan/dart-api-client/commit/fb9817706980c8fa44239d7810cd02507b3fc187))


## v1.0.0 (2025-11-28)

### Chore

* chore: configure automated versioning and PyPI metadata ([`62cbffa`](https://github.com/StatPan/dart-api-client/commit/62cbffa05ecdac1e33a291cfb5166808e004f6a2))

### Feature

* feat: enhance client usability and package structure

- Unify package namespace to &#39;dart_client&#39;
- Expose exceptions in __init__
- Support external rate limiter injection
- Strict error handling for non-000 status codes
- Return Pydantic models for get_company and get_list
- Add get_corp_codes helper ([`d0b0ecc`](https://github.com/StatPan/dart-api-client/commit/d0b0ecc71f4f928cd5f8f3b6ed730d8551bc1c11))

### Unknown

* Initial commit: dart-api-client v0.1.0

- 83개 DART API 자동 생성 (YAML 기반 코드젠)
- 비동기 우선 설계 (httpx + asyncio)
- Rate limiting 지원
- Pydantic 모델로 타입 안전성
- 실제 API 테스트 및 fixture 검증 완료
- 상세한 한글 문서화

Features:
- DS001: 기본 조회 (4 APIs)
- DS002: 정기보고서 (28 APIs)
- DS003: 재무제표 (7 APIs)
- DS004: 지분공시 (2 APIs)
- DS005: 주요사항 (36 APIs)
- DS006: 증권신고서 (6 APIs) ([`d993791`](https://github.com/StatPan/dart-api-client/commit/d993791560d66e09f2e8eb3a8975e51f38a650bb))
