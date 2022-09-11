import matplotlib.pyplot as plt
import numpy as np


def plot_rewards_timestamp(rewards,reward_mean_baseline=None, model_name="",smothing_win=200):
    # graficar los rewards por cada timestamp

    plt.figure(figsize=(10,7))
    
    start_at = 0

    x = list(range(start_at, len(rewards)))
    y = [np.nanmean(rewards[max(i - smothing_win, 0):i + 1]) for i in range(start_at, len(rewards))]
    plt.plot(x, y,label=model_name)
    plt.title(f"Mean reward {model_name}")
    plt.xlabel("Time/Training steps")

    if reward_mean_baseline is not None:
        # Añadimos mean reward comparativo (generalmente del random walk)
        plt.axhline(y=reward_mean_baseline, color="r", linestyle="-",label="baseline")
    plt.legend()
    plt.show()