# among-us-rules-blaster
Simple python script to blast rules into chat. Useful for old-style Hide & Seek mode.

## Requirements
- Windows 10/11
- Among Us
- Python 3

## Setup
```bash
# Clone the repository
git clone https://github.com/tejashah88/among-us-rules-blaster.git
cd among-us-rules-blaster

# Run the setup script to create & activate a virtual environment with the necessary dependencies (if needed)
# If it's already created, calling this will just activate the environment
call setup

# Run the rules blaster service with the specified rules file. You can change the path to your own rules
python rules_blaster.py rules/hide-and-seek.txt
```

## How to Use
1. Create a rules text file in `rules/` and place your rules you want to broadcast in chat rooms. Each line must be 100 characters or less.
2. Launch the script with the rules path specified.
3. Press `Ctrl + 1` with the chat open and the cursor blinking to type the rules line by line. Press `Ctrl + C` to stop the service
