# 🦅 UNRT: Unified Network Reconnaissance Toolkit

> **Scan intelligently. Analyze deeply. Secure effectively.**

![Python](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge&logo=python)(www.python.org)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge&logo=linux)(https://www.microsoft.com/en-in/windows)(www.linux.orgg)
![License](https://img.shields.io/badge/License-Educational-orange?style=for-the-badge)(LICENSE)

---

## 📜 Overview

**UNRT** (Unified Network Reconnaissance Toolkit) is a powerful, all-in-one scanning framework designed by **Group 2 (CYBER SENTINELS)**. It aggregates industry-standard security tools into a single, cohesive interface, allowing security researchers and students to perform comprehensive network reconnaissance with ease.

Built with an emphasis on **automation** and **visual clarity**, UNRT handles the complexity of invoking multiple tools so you can focus on analyzing the results.

---

## 🚀 Features at a Glance

UNRT orchestrates the following engines to deliver a 360-degree view of your target:

| 🔧 Module | 📝 Function | 🔍 Description |
|:---:|:---:|:---|
| **Nmap** | Comprehensive Scanning | Performs aggressive scans for OS detection, versioning, and traceroute. |
| **Hping3** | Packet Crafting | Custom packet generation for advanced connectivity checks (TCP SYN). |
| **Dirsearch** | Web Enumeration | High-speed brute-forcing of web directories and hidden paths. |
| **Netcat** | Port Sweeping | Rapid, raw TCP connection scanning for service discovery. |
| **Unicornscan** | Asynchronous Scanning | Ultra-fast asynchronous TCP scanning (Linux optimized). |

---

## 🛠️ Prerequisites

Before launching UNRT, ensure your environment is prepped with the necessary engines.

### 1. Python Dependencies
Install the required python libraries:
```bash
pip install pyfiglet
```

### 2. External Tools
UNRT acts as a commander for these tools. Ensure they are installed and in your system PATH:
*   [**Nmap**](https://nmap.org/download.html) (Required)
*   **Dirsearch** (Required - `pip install dirsearch` or install locally)
*   **Netcat** (`nc` or `ncat`)
*   *(Optional)* **Hping3** & **Unicornscan** (Linux recommended)

> **Note for Windows Users:** Some tools like Hping3 and Unicornscan are native to Linux. UNRT will intelligently skip them or attempt fallbacks (like standard `ping`) if they are absent.

---

## 💻 How to Use

### Step 1: Clone or Download
Get the toolkit to your local machine:
```bash
git clone https://github.com/your-repo/UNTR.git
cd UNTR
```

### Step 2: Run the Toolkit
Execute the main script using Python:
```bash
python college_project.py
```

### Step 3: Engage
1.  **Enter Target**: When prompted, input your target IP, Hostname, or URL (e.g., `scanme.nmap.org`).
2.  **Sit Back**: UNRT will automatically resolve endpoints and sequentially launch its scanning modules.
3.  **Analyze**: Watch the real-time, color-coded output for results.

---

## 📸 Usage Example

```text
=============================================================================
   __  ___   ______  ______
  / / / / | / / __ \/_  __/
 / / / /  |/ / /_/ / / /   
/ /_/ / /|  / _, _/ / /    
\____/_/ |_/_/ |_| /_/     
                           
=============================================================================

       Unified Network Reconnaissance Toolkit (UNRT)
       Developed solely for Educational & Ethical Testing Purposes
       Developer: Raj kumar
       By Group: CYBER SENTINELS
       Running on: Windows

=============================================================================

[+] Please enter the target (IP, Hostname, or URL): scanme.nmap.org
```

---

## ⚠️ Disclaimer

**EDUCATIONAL USE ONLY.**

This tool is developed by **Raj kumar** and **CYBER SENTINELS** for academic and ethical testing purposes. 
*   **Do not** use this tool against networks or systems you do not own or have explicit permission to test.
*   The developers assume **no liability** for misuse or damage caused by this toolkit.

---

<p align="center">
  Developed with ❤️ by <b> RAJ06-C </b>
</p>

