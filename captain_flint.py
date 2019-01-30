import subprocess

filename = "pieces_of_eight.wav"
command = 'afplay'

subprocess.call(['afplay', filename])
