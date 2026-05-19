# Secrets & Confidential Information Reference — Severity Classification

Confidential information includes credentials, cryptographic secrets, API keys, and
any data intended to remain private for security or business reasons. The categories
below guide severity classification. The examples are **illustrative, not exhaustive**
— apply judgment to any value that appears intended to be secret, even if it doesn't
match these examples exactly.

## Severity Levels

### Critical

Active credentials that, if exposed, grant broad or unrestricted access to systems,
infrastructure, or sensitive data. Exposure typically enables immediate unauthorized
access with little or no additional information needed.

Types that commonly fall at this level include (but are not limited to):
- Cloud provider root or master access keys (e.g., AWS root account keys, GCP
  service account keys with Owner or Editor role)
- Private cryptographic keys (RSA, EC, DSA private keys in PEM or DER format)
- SSH private keys (including `id_rsa`, `id_ed25519`, and similar)
- Database root or administrative passwords
- Symmetric encryption master keys (AES master keys, KMS customer master keys)
- TLS/SSL certificate private keys
- Full-disk or backup encryption keys

### High

Credentials or tokens with significant but scoped access; exposure may allow
unauthorized API calls, data access, or service impersonation.

Types that commonly fall at this level include (but are not limited to):
- Third-party service API keys (payment processors, communication APIs, analytics)
- OAuth 2.0 client secrets
- JWT signing secrets or symmetric JWT keys
- Personal access tokens (GitHub, GitLab, Bitbucket, Azure DevOps PATs)
- Webhook shared secrets
- SMTP credentials or email delivery service API keys
- Cloud IAM keys with non-root but significant roles
- CI/CD pipeline secrets and deploy keys

### Medium

Internal secrets that may expose internal services, configuration, or limited-scope
data. Severity increases if combined with network access to internal systems.

Types that commonly fall at this level include (but are not limited to):
- Internal service passwords or API keys with restricted, scoped access
- Database connection strings containing embedded credentials (non-root accounts)
- Internal API endpoints combined with authentication tokens
- Encryption keys for non-critical or non-production data
- Session signing keys for web applications (limited blast radius)
- Configuration file secrets for internal tooling

### Low

Secrets with very limited scope, already expired or revoked, or clearly intended only
for testing or local development environments.

Types that commonly fall at this level include (but are not limited to):
- Credentials explicitly marked as `test`, `demo`, `example`, or `fake` in nearby
  comments or variable names
- Keys that context clearly shows have been revoked, rotated, or are no longer valid
- Local development credentials for isolated, non-production systems
- Credentials for sandbox or demo environments with no real user data

## Applying These Categories

These categories are starting points for judgment, not rigid rules. Context matters:

- **Entropy as a signal, not proof**: High-entropy random strings may be API keys or
  may be legitimately random non-secret values (e.g., generated UUIDs, nonces, salts).
  Look at the surrounding variable name, comment, or usage context.
- **Variable name context**: Assignment to a variable named `api_key`, `secret`,
  `token`, `password`, `credential`, `private_key`, `auth`, or similar raises
  suspicion significantly, regardless of the value format.
- **Placeholder detection**: Values like `YOUR_API_KEY`, `<your-token>`, `REPLACE_ME`,
  `xxxxxxxxxxxxxxxx`, or `changeme` are not secrets themselves, but may mark locations
  where real secrets should be substituted — note them as informational findings.
- **Version control exposure**: A secret committed to a git repository should be
  treated as compromised even if the commit was later removed, because git history
  is typically recoverable.
- **Production vs. non-production**: The same credential type is more severe in a
  production environment than in an isolated development sandbox.
