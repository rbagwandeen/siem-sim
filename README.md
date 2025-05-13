# SIEM-SIM: Splunk-Inspired SIEM Simulation

**Project Status:** In Progress  
This project is a simulated Security Information and Event Management (SIEM) system designed to visualize, analyze, and monitor log data in a format inspired by enterprise tools like Splunk.

---

## Overview

**SIEM-SIM** is a Python-powered dashboard that simulates the core functionality of a SIEM tool. It ingests AWS-style CloudTrail logs and displays threat actor profiles, event breakdowns, and threat severity insights in a structured, GUI-based interface.

---

## Tech Stack

- **Python 3**  
- **Tkinter** (for GUI interface)  
- **SQLite** (planned integration for log storage)  
- **Matplotlib** (for visual analytics – planned)  
- **CSV data simulation** (CloudTrail logs, threat actors, threat types)  
- **Canva** (for visual assets/UI icons)

---

## Features

- Simulated CloudTrail log ingestion  
- GUI layout with threat breakdowns  
- Attacker profiles and threat type mapping  
- Modular design with expandable frames  
- Visual analytics and charts (coming soon)  
- Log filtering/search functionality (coming soon)  
- Exportable incident summaries (planned)

## Future Plans

- Add visual data breakdown using matplotlib
- Implement log search/filtering by IP, user, or status
- Connect to SQLite for persistent log storage
- Export incident reports with summaries