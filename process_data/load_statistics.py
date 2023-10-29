from dopamine.colab import utils as colab_utils
import seaborn as sns
import matplotlib.pyplot as plt


def generate_stats_graph():
    game = 'Pong'
    data = colab_utils.read_experiment(
        '/home/sethlinc/projects/honours-dopamine/dopamine_runs',
        summary_keys=['train_episode_returns']
    )
    data['agent'] = 'agent'
    data['run_number'] = 1

    fig, ax = plt.subplots(figsize=(16,8))
    sns.lineplot(x='iteration', y='train_episode_returns', hue='agent',
                 data=data, ax=ax)
    plt.title(game)
    plt.show()


if __name__ == '__main__':
    generate_stats_graph()
