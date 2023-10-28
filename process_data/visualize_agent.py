from dopamine.utils import example_viz_lib
import base64
from IPython.display import HTML


def generate_video():
    num_steps = 1000  # @param {type:"number"}
    example_viz_lib.run(agent='dqn', game='Pong', num_steps=num_steps,
                        root_dir='/home/sethlinc/projects/honours-dopamine/dopamine',
                        restore_ckpt='/home/sethlinc/projects/honours-dopamine/dopamine_runs/checkpoints/tf_ckpt-199'
                        )

if __name__ == '__main__':
    generate_video()
