# Secret Scanning Integrations

Read this file when selecting or configuring a secret scanner. The project lifecycle
reference defines where the scanner belongs in pre-commit; this file supplies scanner
commands and copyable integration blocks. Pin versions and update them through the
project's dependency policy.

## Choose One Default

- Use **Gitleaks** by default for local blocking and Git repository or history scans.
- Use **TruffleHog** when active credential verification or non-repository sources are
  required. Verification contacts external services; enable it only when network and
  privacy policy allow the scanned values to be tested.
- Use **detect-secrets** when the team wants a committed, audited baseline and tunable
  Python detectors and filters.

Add a second scanner only when it covers a documented source or verification need that
the default does not.

## Gitleaks

Install and run locally:

```sh
brew install gitleaks
gitleaks git --redact
```

Add this repository entry to `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/gitleaks/gitleaks
  rev: v8.30.1
  hooks:
    - id: gitleaks
```

GitHub Actions job:

```yaml
permissions:
  contents: read

jobs:
  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

GitLab CI job:

```yaml
secret-scan:
  image:
    name: ghcr.io/gitleaks/gitleaks:v8.30.1
    entrypoint: [""]
  variables:
    GIT_DEPTH: "0"
  script:
    - gitleaks git --redact --verbose .
```

## TruffleHog

Install and run locally:

```sh
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh \
  | sh -s -- -b /usr/local/bin
trufflehog git file://. --results=verified,unknown --fail
```

Install the binary first, then add this local hook to `.pre-commit-config.yaml`:

```yaml
- repo: local
  hooks:
    - id: trufflehog
      name: TruffleHog
      entry: bash -c 'trufflehog git file://.'
      language: system
      stages: [pre-commit, pre-push]
```

GitHub Actions job:

```yaml
jobs:
  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: trufflesecurity/trufflehog@v3.95.6
        with:
          extra_args: --results=verified,unknown --fail
```

GitLab CI job:

```yaml
secret-scan:
  image: alpine:latest
  before_script:
    - apk add --no-cache git curl jq
    - curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin
  script:
    - trufflehog filesystem . --results=verified,unknown --fail --json | jq
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
```

## detect-secrets

Install, create the baseline, audit it, and scan tracked files:

```sh
uv add --dev detect-secrets
uv run detect-secrets scan > .secrets.baseline
uv run detect-secrets audit .secrets.baseline
git ls-files -z | xargs -0 uv run detect-secrets-hook --baseline .secrets.baseline
```

Add this repository entry to `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/Yelp/detect-secrets
  rev: v1.5.0
  hooks:
    - id: detect-secrets
      args: [--baseline, .secrets.baseline]
```

GitHub Actions job for a uv project:

```yaml
jobs:
  secret-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v8
      - run: uv sync --locked --dev
      - run: git ls-files -z | xargs -0 uv run detect-secrets-hook --baseline .secrets.baseline
```

GitLab CI job for a uv project:

```yaml
secret-scan:
  image: ghcr.io/astral-sh/uv:0.11.22-python3.12-trixie-slim
  variables:
    UV_LINK_MODE: copy
  before_script:
    - apt-get update && apt-get install -y --no-install-recommends git
  script:
    - uv sync --locked --dev
    - git ls-files -z | xargs -0 uv run detect-secrets-hook --baseline .secrets.baseline
```

## Handling Findings

- Never hide a real secret with an allowlist or baseline. Revoke it, remove it from the
  repository, and clean history when required.
- Use baselines only for reviewed historical findings. Audit and commit baseline
  updates separately so additions remain visible in review.
- Keep allowlists narrow and document why each match is a false positive.
- Secret scanners are heuristic controls, not proof that a repository has no secrets.

## Sources

- https://raw.githubusercontent.com/gitleaks/gitleaks/refs/heads/master/README.md
- https://github.com/gitleaks/gitleaks-action
- https://raw.githubusercontent.com/trufflesecurity/trufflehog/refs/heads/main/README.md
- https://raw.githubusercontent.com/trufflesecurity/trufflehog/refs/heads/main/PreCommit.md
- https://raw.githubusercontent.com/Yelp/detect-secrets/refs/heads/master/README.md
