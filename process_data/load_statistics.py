import numpy as np
import os
from dopamine.agents.dqn import dqn_agent
from dopamine.discrete_domains import run_experiment
from dopamine.colab import utils as colab_utils
from absl import flags
import collections


def generate_stats_graph():
    game = 'Pong'
    baseline_data = colab_utils.load_baselines('/home/sethlinc/projects/honours-dopamine/dopamine_runs/baseline')
    data = colab_utils.read_experiment(
        '/home/sethlinc/projects/honours-dopamine/dopamine_runs',
        summary_keys=['train_episode_returns']
    )
    data['agent'] = 'Sample DQN'
    data['run_number'] = 1
    # experimental_data[game] = experimental_data[game].merge(
    #     sample_data[sample_data.game == game], how='outer')
    print(data)
    print(baseline_data)


if __name__ == '__main__':
    generate_stats_graph()
