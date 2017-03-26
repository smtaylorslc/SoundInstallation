import numpy
from gpiozero import MotionSensor
from musical.theory import Note, Scale
from musical.audio import source, playback
from threading import *
import time


# Plays sine wave, adjusted via adjustAudio method.
class sinePlayer(Thread):
  def __init__(self, event):
    Thread.__init__(self)
    # Define "stop" trigger
    self.stopped = event
    # Define key
    self.key = Note('C3')
    # Define scale
    self.scale = Scale(self.key, 'harmonic minor')
    self.note = self.key
    self.chunks = []
    self.chunks.append(source.sawtooth(self.note, 0.5))
    self.data = numpy.concatenate(self.chunks)
    self.data = self.data * 0.5
  
  # Adjust audio by x steps in scale defined above
  def adjustAudio(self,adjustment):
    self.note = self.scale.transpose(self.key, 0)
    self.chunks = []
    self.chunks.append(source.sawtooth(self.note, .5))
    self.data_adjusted = numpy.concatenate(self.chunks)
    self.data_adjusted = self.data_adjusted * 0.5
    self.data = self.data_adjusted

  # Runs indefinitely until passed "stop" trigger
  def run(self):
    while not self.stopped.wait(0.001):
      playback.play(self.data)


# Detects motion from PIR sensor. Sends motion info to
# sinePlayers.
class motionDetectController(Thread):
  def __init__(self, event, numPlayers):
    Thread.__init__(self)
    self.players = {}
    self.num_players = numPlayers
    for i in range(self.num_players):
      self.players[i] = sinePlayer(stopFlag)
    self.stopped = event
    self.motion_counter = 0
    self.pir = MotionSensor(4)
  def run(self):
    while not self.stopped.wait(0.001):
      if pir.motion_detected:
        if self.motion_counter <= self.num_players:
          self.motion_counter += 1
          self.players[
            self.motion_counter
          ].adjustAudio(self.motion_counter)
      else:
        if self.motion_counter > 0:
          self.players[
            self.motion_counter
          ].adjustAudio(0)
          self.motion_counter -= 1
      if self.motion_counter >= 1
      


stopFlag = Event()
stopFlag.set()

x = motionDetectController(stopFlag,7)
