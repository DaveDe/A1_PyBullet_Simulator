import gym
from gym import error, spaces, utils
from gym.utils import seeding

#Use PyBullet to simulate the A1 robot
import pybullet as p

class A1Env(gym.Env):

	def __init__(self):

		print("In init")

	def step(self, action):

		print("In Step")

	def reset(self):

		print("In reset")

