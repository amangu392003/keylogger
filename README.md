# Keylogger Detection System using Keystroke Dynamics

## Overview

This project implements a behavioral biometric keylogger detection system using Python. It records user typing patterns, analyzes keystroke dynamics (flight time, dwell time), and detects suspicious activity using anomaly detection. The visualization module displays typing behavior and highlights anomalies.

---

## Quick Start

### 1. Prerequisites

- Python 3.x installed ([Download Python](https://python.org))
- All scripts and this README are in the same project folder.

### 2. Install all dependencies

Open a command prompt in your project directory and run:
pip install -r requirements.txt


### 3. Module Structure

| File                     | Purpose                           |
|--------------------------|-----------------------------------|
| keylogger.py             | Records keystrokes                |
| feature_extraction.py    | Extracts timing features          |
| anomaly_detection.py     | Detects behavioral anomalies      |
| visualization_alerting.py| Plots and alerts anomalies        |
| requirements.txt         | All Python libraries needed       |
| Makefile                 | Automates running all scripts     |

---

## Step-by-Step Usage

**A. Record Keystrokes**  
python keylogger.py

- Start typing as usual; all keys will be logged.
- Press ESC to stop recording.
- Output: `keystroke_data.csv`

**B. Extract Features**  
python feature_extraction.py

- Extracts flight/dwell time from raw data.
- Output: `features.csv`; prints baseline typing profile.

**C. Detect Anomalies**
python anomaly_detection.py

- Flags unusual typing speeds/times.
- Output: terminal list of anomalies or "No anomalies detected".

**D. Visualize & Alert**
python visualization_alerting.py

- Plots typing behavior and marks suspicious events in red.
- Output: window with graph and alert printout.

---

## Automate with Makefile

If you have GNU Make installed:
make
Runs all steps in sequence: keylogging, feature extraction, anomaly detection, visualization.

---

## Troubleshooting

- If a script fails, check for missing dependencies and run `pip install -r requirements.txt`.
- Ensure all `.py` files and data files are in the **same directory**.
- For Windows:  
  Use the standard command prompt or Git Bash to run scripts and Makefile.
- If the plot doesn't appear, ensure `matplotlib` is installed.
- Always export notebooks as `.py` files before using Makefile automation.

---

## Credits

Developed for the Keylogger Detection using Keystroke Dynamics project.

---

