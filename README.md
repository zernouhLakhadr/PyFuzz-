# PyFuzz-
A lightweight fuzzer built in Python to discover vulnerabilities through automated malformed input generation.
---

## 📌 About The Project

**PyFuzz** is my cybersecurity student project that demonstrates the fundamentals of **fuzz testing** — a powerful technique used by security researchers and penetration testers to find vulnerabilities in software.

The project includes:
- A **fuzzer script** that generates and sends unexpected/malformed inputs
- A **target script** (also in Python) that simulates a vulnerable application
- Automated detection of how targets respond to edge-case inputs

---

## 🛠️ Built With

- **Python 3**
- No external dependencies — pure stdlib

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Installation
```bash
git clone https://github.com/YOUR_USERNAME/pyfuzz.git
cd pyfuzz
```

### Usage
```bash
# Run the target (vulnerable app)
python target.py

# Run the fuzzer against the target
python fuzzer.py
```

---

## 🎯 How It Works

1. The **target** application accepts input and processes it
2. The **fuzzer** generates a wide range of malformed, oversized, or unexpected inputs
3. It sends them automatically to the target and monitors the response
4. Crashes, errors, or unexpected behavior reveal potential vulnerabilities

---

## 🔐 What This Demonstrates

- Core fuzzing methodology used in real-world security testing
- How input validation failures lead to vulnerabilities
- Python scripting for offensive security tooling
- The attacker mindset when probing applications

---

## ⚠️ Disclaimer

This tool is built for **educational purposes only**. Only use it against systems you own or have explicit permission to test. Unauthorized use is illegal.

---

## 👤 Author

**Your Name**
- LinkedIn: www.linkedin.com/in/aymen-zernouh-1b690925b
- GitHub: https://github.com/zernouhLakhadr

---

---

⭐ If you found this useful, give it a star!
