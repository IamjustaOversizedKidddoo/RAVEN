# 🐦‍⬛ RAVEN

> A curated collection of OSINT, hacking, and dark-web intelligence tools.

---

## 📁 Repository Structure

| Directory | Source | Description |
|-----------|--------|-------------|
| [`hackingtool/`](./hackingtool) | [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool) | All-in-one Hacking Tool for Linux |
| [`ahmia-site/`](./ahmia-site) | [ahmia/ahmia-site](https://github.com/ahmia/ahmia-site) | Ahmia — Tor hidden services search engine (Django) |
| [`ahmia-crawler/`](./ahmia-crawler) | [ahmia/ahmia-crawler](https://github.com/ahmia/ahmia-crawler) | Ahmia crawler for indexing .onion sites (Scrapy) |
| [`ahmia-index/`](./ahmia-index) | [ahmia/ahmia-index](https://github.com/ahmia/ahmia-index) | Ahmia Elasticsearch indexing infrastructure |
| [`emailosint/`](./emailosint) | [krishpranav/emailosint](https://github.com/krishpranav/emailosint) | Email OSINT tool for gathering account intelligence |

---

## 🔍 Tools Overview

### 🛠 hackingtool
All-in-one hacking tool featuring anonymous surfing, information gathering, web attack, phishing, exploitation frameworks, and more.

### 🌐 Ahmia (site + crawler + index)
Ahmia is a search engine for Tor's onion services. The three components together form the full stack:
- **ahmia-site** — The public-facing Django web app
- **ahmia-crawler** — Scrapy-based crawler that discovers `.onion` sites
- **ahmia-index** — Elasticsearch backend for indexing and serving results

### 📧 emailosint
Python-based OSINT tool for gathering information about email accounts — checks breaches, social presence, and more.

---

> ⚠️ **Disclaimer**: These tools are for educational and authorized penetration testing purposes only. Misuse is strictly prohibited.
