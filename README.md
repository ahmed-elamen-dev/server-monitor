# Server Health Monitor

## Project Description

A Python-based Linux server monitoring tool that collects important system information and generates a server health report automatically.

## Features

- Hostname monitoring
- Current user monitoring
- Current date and time
- Operating system detection
- Kernel version detection
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Primary IPv4 address detection
- System uptime monitoring
- Automatic server health report generation

## Technologies Used

- Linux
- Python 3
- Git
- GitHub
- psutil

## Project Structure

```text
server-monitor/
├── monitor.py
├── reports/
│   └── server_report.txt
├── screenshots/
├── README.md
├── .gitignore
└── requirements.txt


## Installation

1. Clone the repository:
```bash
git clone <your-github-repository-url>
cd server-monitor


pip3 install -r requirements.txt
 ```
## How to Run


Run the monitoring script using:

```bash
python3 monitor.py



The script automatically generates a server health report inside:

```text
reports/server_report.txt
