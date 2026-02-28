
# AI Red Team Lab

This repository contains a **home AI red team lab** designed for educational purposes. It demonstrates **attacks on LLMs and AI agents** in a safe, offline environment.

## Features

- 10+ attack vectors: prompt injection, memory poisoning, tool misuse, behavioral drift
- Multi-step emergent behavior simulation
- Automated red team execution
- CSV and HTML reporting
- Interactive Matplotlib dashboard showing:
  - Attack categories
  - Success rates
  - Drift levels
- Fully sandboxed and safe for home lab

## Files

- `attacks_library.py` - structured attack vectors
- `ai_redteam_lab.py` - interactive lab with behavioral drift
- `ai_redteam_report_export.py` - automated execution with CSV & HTML export
- `ai_redteam_dashboard.py` - final version with visual dashboard
- `README.md` - project overview and instructions

## Usage

1. Install dependencies: `pip install matplotlib`
2. Run `python ai_redteam_dashboard.py` to execute all attacks and view dashboard
3. View reports: `redteam_report.csv` and `redteam_report.html`

## Notes

- Safe for educational purposes only
- Fully offline sandbox environment
- Easily extensible with new attacks and tools
