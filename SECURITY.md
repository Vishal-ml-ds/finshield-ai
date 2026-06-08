# Security Policy

FinShield AI processes sensitive financial and personal data, so we take security
seriously. This document explains how to report vulnerabilities and what you can
expect from us in return.

## Supported Versions

The `main` branch always receives security fixes. Older tags are not maintained —
please run the latest version.

| Version | Supported          |
| ------- | ------------------ |
| `main`  | :white_check_mark: |
| older   | :x:                |

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues,
discussions, or pull requests.**

Instead, report privately through one of:

- **GitHub Security Advisories** — use the
  [private vulnerability reporting](https://github.com/Vishal-ml-ds/finshield-ai/security/advisories/new)
  form (preferred).
- **Email** — contact the maintainer, **Vishal Prasad**, via the address on the
  [GitHub profile](https://github.com/Vishal-ml-ds) with the subject line
  `SECURITY: FinShield AI`.

Please include as much of the following as you can:

- A description of the vulnerability and its impact.
- Steps to reproduce or a proof-of-concept.
- Affected component(s) (backend API, ML pipeline, frontend, infra).
- Any suggested remediation.

## What to Expect

- **Acknowledgement** within **3 business days**.
- An initial assessment and severity classification within **7 business days**.
- Regular updates as we work on a fix.
- Public credit for the report once a fix ships, unless you prefer to remain anonymous.

Please give us a reasonable window to remediate before any public disclosure
(coordinated disclosure). We will not pursue legal action against good-faith
researchers who follow this policy.

## Scope

In scope:

- The FinShield AI backend (FastAPI), ML scoring engine, frontend (Next.js), and
  infrastructure-as-code in this repository.

Out of scope:

- Third-party services (Supabase, AWS, etc.) — report those to the respective vendor.
- Findings that require a compromised host, physical access, or social engineering.
- Vulnerabilities in dependencies already tracked by Dependabot, unless you have a
  working exploit specific to FinShield's usage.

## Security Best Practices for Operators

If you deploy FinShield, please:

- Keep all secrets in environment variables or a secret manager — never in source.
- Rotate credentials regularly and after any suspected exposure.
- Enable HTTPS/TLS everywhere and never disable certificate validation.
- Apply least-privilege IAM and database roles.
- Keep dependencies current (Dependabot PRs are enabled in this repo).

Thank you for helping keep FinShield AI and its users safe. 🛡️
