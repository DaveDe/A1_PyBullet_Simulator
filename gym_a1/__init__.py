from gym.envs.registration import register

register(
    id='a1-v0',
    entry_point='gym_a1.envs:A1Env',
)