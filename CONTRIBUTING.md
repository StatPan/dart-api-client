# 기여 가이드 (Contributing Guide)

`dart-api-client` 프로젝트에 기여해주셔서 감사합니다! 효율적인 협업과 자동화된 배포를 위해 아래 규칙을 준수해주세요.

## 1. 브랜치 전략 (Branching Strategy)

우리는 **PR(Pull Request) 기반 워크플로우**를 따릅니다. `master` 브랜치에 직접 푸시하는 것은 금지됩니다.

### 브랜치 네이밍 규칙
이슈 번호와 작업 유형을 포함하여 브랜치 이름을 생성합니다.

- 기능 추가: `feat/issue-{number}-{description}`
- 버그 수정: `fix/issue-{number}-{description}`
- 문서/기타: `chore/issue-{number}-{description}`

예시:
- `feat/issue-12-add-rate-limiter`
- `fix/issue-15-typo-in-readme`

## 2. 커밋 메시지 (Commit Convention)

우리는 **Conventional Commits** 규칙을 따릅니다. 이는 자동 버전 관리와 릴리즈 노트 생성을 위해 필수적입니다.

형식: `<type>(<scope>): <subject>`

- `feat`: 새로운 기능 (Minor version up)
- `fix`: 버그 수정 (Patch version up)
- `docs`: 문서 변경
- `style`: 코드 포맷팅, 세미콜론 누락 등 (로직 변경 없음)
- `refactor`: 코드 리팩토링
- `test`: 테스트 코드 추가/수정
- `chore`: 빌드 태스크, 패키지 매니저 설정 등

예시:
- `feat: add get_corp_codes helper method`
- `fix(client): resolve type error in exception handling`

## 3. 개발 절차 (Workflow)

1. **이슈 생성**: 작업할 내용에 대한 이슈를 생성합니다.
2. **브랜치 생성**: `git checkout -b feat/issue-123-description`
3. **작업 및 커밋**: `git commit -m "feat: ..."`
4. **Push**: `git push origin feat/issue-123-description`
5. **PR 생성**: GitHub에서 `master` 브랜치로 PR을 생성합니다.
6. **Review & Merge**: 리뷰 후 머지되면, GitHub Actions가 자동으로 버전을 올리고 PyPI에 배포합니다.

## 4. 로컬 개발 환경 설정

```bash
# 의존성 설치
uv sync

# 프리커밋 훅 설치 (커밋 메시지 검사 등)
uv run pre-commit install
```
