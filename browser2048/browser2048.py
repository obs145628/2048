import gym
import numpy as np
from .serverenv import ServerEnv

class Browser2048Env(ServerEnv):
    def __init__(self):
        self.state_dtype = np.int32
        self.action_space = gym.spaces.Discrete(4)
        self.observation_space = gym.spaces.Box(np.array([0]*16),
                                                np.array([31]*16),
                                                dtype=np.int32)
        super().__init__()
