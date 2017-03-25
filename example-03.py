import numpy

from musical.theory import Note, Scale
from musical.audio import source, playback
from threading import *
import time


# Define key and scale



class sinePlayer(Thread):
  def __init__(self, event):
    Thread.__init__(self)
    self.stopped = event
    self.key = Note('C2')
    self.scale = Scale(self.key, 'harmonic minor')
    self.note = self.key
    self.chunks = []
    self.chunks.append(source.sawtooth(self.note, 0.5))
    self.data = numpy.concatenate(self.chunks)
    self.data = self.data * 0.5
    #while True:
    #  self.repeatPlay()

  def adjustAudio(self,adjustment):
    self.note = self.scale.transpose(self.key, adjustment)
    self.chunks = []
    self.chunks.append(source.sawtooth(self.note, 0.5))
    self.data_adjusted = numpy.concatenate(self.chunks)
    self.data_adjusted = self.data_adjusted * 0.5
    self.data = self.data_adjusted
  def run(self):
    while not self.stopped.wait(0.001):
      print("playing!")
      playback.play(self.data)
      print(self.data)


stopFlag = Event()
players = {}
for i in range(6):
  players[i] = sinePlayer(stopFlag)
  players[i].start()
  time.sleep(.5)

for i in range(5):
  print "%s seconds!" % i
  time.sleep(i)

for i in range(6):
  players[i].adjustAudio(i)
  time.sleep(.5)
#player.adjustAudio()

time.sleep(2)

for i in range(6):
  players[i].adjustAudio(0)
  time.sleep(.5)


time.sleep(2)
stopFlag.set()
