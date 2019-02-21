import gym
import numpy as np

import requests

URL = 'http://0.0.0.0:8080/'
REQ_URL = URL + 'req'
GETRES_URL = URL + 'getres'

def post(url, data):
    res = requests.post(url, json=data)
    if not res.ok:
            raise Exception('Request error')
    return res.json()

def req(data):
    idx = post(REQ_URL, data)
    
    while True:
        res = post(GETRES_URL, idx)
        if res[0] == 'ok':
            break

    return res[1]

class ServerEnv(gym.Env):

    def __init__(self):
        self.reset()

    def seed(self, seed):
        req(['SEED', seed])
        return [seed]

    def step(self, action):
        if not self.action_space.contains(action):
            raise Exception('Invalid action')
        if self.done:
            raise Exception('Env session finished, need to reset')
        
        res =  req(['S', action])
        if len(res) == 3:
            res.append(dict())
        res[0] = np.array(res[0], dtype=self.state_dtype)
        self.done = res[2]
        return res

    def reset(self):
        self.done = False
        res = req(['R'])
        res = np.array(res, dtype=self.state_dtype)
        return res
