import urllib.request

from pydub import AudioSegment
from pydub.playback import play

# download an audiofile
urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")

# load into pydub
loop = AudioSegment.from_wav("metallic-drums.wav")

# play the result
play(loop)
