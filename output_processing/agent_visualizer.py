import os

from dopamine.utils import example_viz_lib


def generate_video():
    num_steps = 1000
    example_viz_lib.run(agent='dqn', game='Pong', num_steps=num_steps, root_dir='/dopamine')


if __name__ == '__main__':
    print(os.getcwd())
