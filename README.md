# State Machine Visualization
This program connects to a server and simulates a state machine by sending and receiving data and finally create a pdf file called "state_machine.pdf".

>This program utilizes a random number generator to produce actions randomly ranging from 1 to 3.

## Requirements
- Python 3.6 and above installed on your local machine
- Graphviz installed on your local machine

## Installation
1. Install venv
   ```bash
   python3 -m venv venv
   ```
2. Activate venv
   ```bash
   source ./venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## How to run the program?
After activating the venv, run the command
```bash
python state_machine.py
```

#### Output:
- state_machine
- state_machine.pdf