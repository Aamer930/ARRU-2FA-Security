<div align="center">

# ARRU Security — Two-Factor Authentication (2FA) Desktop App

**A Python desktop application demonstrating Time-based One-Time Password (TOTP) authentication using Google Authenticator integration.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Security: TOTP](https://img.shields.io/badge/Security-TOTP%20%7C%20RFC%206238-orange?style=flat-square)](https://datatracker.ietf.org/doc/html/rfc6238)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=flat-square)]()

---

**Course:** Introduction to Cyber Security — CCY2001  
**Institution:** Arab Academy for Science, Technology and Maritime Transport (AASTMT)  
**Major:** Computer Science — Cyber Security Department  
**Supervisor:** Dr. Ehab Abo Seif

</div>

---

## Overview

ARRU Security is a cybersecurity demonstration project that implements **Two-Factor Authentication (2FA)** using the **TOTP (Time-based One-Time Password)** standard (RFC 6238). The application provides a graphical interface that generates a QR code for pairing with any TOTP-compatible authenticator app, then verifies the generated one-time passwords in real time.

This project was built to demonstrate core concepts in modern authentication security, including shared secret generation, QR-based provisioning, and time-windowed OTP validation.

---

## Features

| Feature | Description |
|---|---|
| QR Code Generation | Renders a TOTP provisioning QR code scannable by any authenticator app |
| TOTP Verification | Validates 6-digit OTPs against a 30-second rolling time window |
| Google Authenticator Compatible | Fully compliant with RFC 6238 — works with Google Authenticator, Authy, Microsoft Authenticator, and more |
| Offline Operation | No internet connection or external server required |
| Clean Desktop GUI | Built with Python's native Tkinter library — zero web dependencies |

---

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│                     TOTP Flow                           │
│                                                         │
│  1. App generates random Base32 secret                  │
│  2. Secret is encoded into a QR code (otpauth:// URI)   │
│  3. User scans QR with authenticator app                │
│  4. App and authenticator share the same secret         │
│  5. Both derive the same 6-digit OTP every 30 seconds   │
│  6. App verifies entered OTP against its own derivation │
└─────────────────────────────────────────────────────────┘
```

1. Click **Generate QR Code** — a cryptographically random Base32 TOTP secret is created and rendered as a QR code
2. Scan the QR code using Google Authenticator (or any compatible TOTP app)
3. Enter the 6-digit OTP displayed in your authenticator app
4. Click **Verify OTP** — the application confirms validity in real time

OTPs rotate every **30 seconds** per the TOTP standard.

---

## Tech Stack

| Technology | Role |
|---|---|
| Python 3 | Core language |
| Tkinter | Native desktop GUI framework |
| [pyotp](https://github.com/pyauth/pyotp) | TOTP secret generation and OTP verification |
| [qrcode](https://github.com/lincolnloop/python-qrcode) | QR code image generation |
| [Pillow](https://python-pillow.org/) | Image processing and Tkinter rendering |

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Aamer930/ARRU-2FA-Security.git
cd ARRU-2FA-Security

# Install dependencies
pip install pyotp qrcode[pil] Pillow
```

### Run

```bash
python LoginForm.py
```

---

## Project Structure

```
ARRU-2FA-Security/
├── LoginForm.py          # Main application — GUI, QR generation, OTP verification
├── temp_qr.png           # Auto-generated QR code image (runtime artifact)
├── README.md
├── LICENSE
└── Doc/
    ├── CyberSecurity Project presentation.pdf
    └── Intro To Cyber Security.pdf
```

---

## Security Design Notes

> This project is a **proof-of-concept** built for educational purposes.

The following considerations apply to any production deployment of this pattern:

- **Secret storage** — TOTP secrets must be generated once per user and stored in an encrypted, access-controlled database. This demo regenerates the secret on every launch.
- **QR code handling** — `temp_qr.png` is written to disk. In production, serve the QR image in-memory and never persist it to the filesystem.
- **Authentication layers** — 2FA is a second factor, not a first. A production system requires username/password authentication before TOTP verification.
- **Replay protection** — pyotp's `verify()` method handles the 30-second window; add server-side OTP replay caching for hardened deployments.

---

## Concepts Demonstrated

- Time-based One-Time Password (TOTP) — RFC 6238
- HMAC-based One-Time Password (HOTP) — RFC 4226 (underlying algorithm)
- QR code provisioning via `otpauth://` URI scheme
- Shared secret cryptography
- Multi-factor authentication (MFA) architecture

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

Built for CCY2001 — Introduction to Cyber Security · Arab Academy for Science, Technology and Maritime Transport (AASTMT)  
Computer Science — Cyber Security Department · Supervised by Dr. Ehab Abo Seif · Ahmed Aamer · 2026

</div>
