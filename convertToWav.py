import os
import pathlib
from pydub import AudioSegment

"""
reads in m4a files from specified directory
and outputs them as wavs in new directory
"""

"""
inFile = "pieces_of_eight.m4a"
track = AudioSegment.from_file(inFile, format='m4a')
outFile = track.export("test.wav", format='wav')
"""

# create path objects to audio files directory
audioDir = str(pathlib.Path.cwd()) + "/audio/"
audioDir = pathlib.Path(audioDir)
# convert to list and store audio file strings
audioFiles = list(audioDir.iterdir())
audioFiles = [file for file in audioFiles if not file.is_dir()]

# mkdir for output wavs
outDir = "audio/wavs/"
os.makedirs(outDir, exist_ok=True)

for m4a in audioFiles:
    # strip path to filename
    fn = os.path.basename(m4a)
    # remove extension
    fn = fn.split(".")[0]
    print(fn)
    # convert to audio segment
    track = AudioSegment.from_file(m4a, format='m4a')
    # make output filename
    outFile = outDir + fn + ".wav"
    # now export
    track.export(outFile, format="wav")
