# CartPole-v0, MountainCar-v0, MsPacman-v0 (requires the Atari dependency), or Hopper-v1
import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action