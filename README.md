# 🛡️ CyberOps v2.0

CyberOps is an open-source Python command-line toolkit built for system monitoring, process inspection, network analysis, password utilities, and file integrity verification.

Built as a learning project while exploring Python, software development, and cybersecurity concepts.

---

## 📸 Screenshots

### Main Interface

![CyberOps Main Interface](screenshot1.png)

### Commands & Features

![CyberOps Commands](screenshot2.png)

---

## 🚀 Features

### 💻 System Information

* Hostname
* Operating System
* Processor Details
* CPU Usage
* RAM Usage

### 🌐 Network Information

* Hostname Detection
* IP Address Lookup

### ⚙️ Process Viewer

* View active user processes
* Process ID (PID) display
* RAM usage information

### 🔒 SHA256 File Hashing

* Generate SHA256 hashes
* Verify file integrity

### 🔐 Password Generator

* Generate secure passwords
* Custom password length

### ✅ Password Strength Checker

* Analyze password strength
* Weak / Medium / Strong rating

### 📊 System Monitor

* CPU Usage Monitoring
* RAM Usage Monitoring
* Disk Usage Monitoring

### 🎨 Rich Terminal UI

* Colored output
* Rich tables
* Clean command interface

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/ansh385/CyberOps.git
```

Move into the project folder:

```bash
cd CyberOps
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run CyberOps:

```bash
python main.py
```

---

## 📖 Available Commands

| Command   | Description                 |
| --------- | --------------------------- |
| help      | Show all commands           |
| sysinfo   | Display system information  |
| network   | Display network information |
| processes | View active processes       |
| hash      | Generate SHA256 hash        |
| password  | Generate strong password    |
| checkpass | Check password strength     |
| monitor   | System monitor              |
| clear     | Clear screen                |
| exit      | Exit CyberOps               |

---

## 🛠️ Built With

* Python
* Rich
* Psutil
* PyFiglet

---

## 📂 Project Structure

```text
CyberOps
│
├── main.py
├── requirements.txt
├── README.md
│
└── modules
    ├── sysinfo.py
    ├── network.py
    ├── processes.py
    ├── hashing.py
    ├── password_generator.py
    ├── password_checker.py
    └── monitor.py
```

---

## 🤝 Contributing

Contributions, suggestions, and feature ideas are welcome.

Feel free to fork the project and submit improvements.

---

## ⭐ Support

If you find CyberOps useful, consider giving the repository a star.

---

## 📌 Project Status

CyberOps v2.0 is the final planned feature release.

The project will remain available as an open-source learning project and may receive occasional maintenance updates.

---

Built with ❤️ by The Coding Yatra
