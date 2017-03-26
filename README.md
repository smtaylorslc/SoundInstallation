# jacksonSoundInstallation
Installation art piece -- written in Python.
Creates multiple sine waves and then adjusts them given input from a PIR sensor (the more consecutive motion detected, the more dissonant the sine waves become).

Currently this project works well as a standalone project, but the Pi's audio output is less than satisfactory -- planning to create a socket connection between the Pi and a client computer that will output the sound to a stereo system.

Adding buzzer controls and video to the project in the near future.

## Setup
**Prereqs:**
* Python 2.7
* Pip
* Virtualenv

If you don't already have virtualenv installed, run `pip install virtualenv` from the command line.

Start a virtualenvironment inside the project folder and install the requirements listed in requirements.txt.

`virtualenv venv` 

`source venv/bin/activate` 

`pip install -r requirements.txt` 


After this, you should be ready to run the attached standalonePiFile.py from the command line using:

`python standalonePiFile.py`

The console will prompt you for the number of sine wave threads you'd like to start, after which you can quit the program by hitting the Return key.

Built off of Davy Wybiral's "python-musical".
https://github.com/wybiral/python-musical
