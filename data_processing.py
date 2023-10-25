import numpy as np
import os
from dopamine.agents.dqn import dqn_agent
from dopamine.discrete_domains import run_experiment
from dopamine.colab import utils as colab_utils
from absl import flags

BASE_PATH = 'tmp/dopamine_run'
GAMES = ['Pong']
experimental_data = colab_utils.load_baselines('/baselines')
