from gym.envs.registration import register

register(
    id='Browser2048-v0',
    entry_point='browser2048.browser2048:Browser2048Env'
)
