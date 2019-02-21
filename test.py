import gym
import browser2048

env = gym.make('Browser2048-v0')
env.seed(469)
env.reset()

while True:
    action = env.action_space.sample()
    state, reward, done, _ = env.step(action)
    #print('state:', state, 'reward: ', reward)
    if done: break
