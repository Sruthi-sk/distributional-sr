import pickle

import matplotlib.pyplot as plt
import seaborn as sns


# Loading
with open('dsm_returns.pkl', 'rb') as f:
    dsm_returns = pickle.load(f)
    # for task, reward_distributions in dsm_returns.items():
    #     plt.figure()
    #     plt.title(f'Return Distribution for {task}')
    #     plt.hist(reward_distributions, bins=20, alpha=0.5)
    #     plt.legend()
    #     plt.xlabel('Return')
    #     plt.ylabel('Frequency')
    #     plt.show()
            
    num_plots = len(dsm_returns)
    num_cols = min(3, num_plots) 
    num_rows = (num_plots + num_cols - 1) // num_cols  # Calculate rows needed
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(4*num_cols, 5*num_rows), sharey=True)
    fig.suptitle('Return Distribution Predictions - DSM', fontsize=14)
    # print(dsm_returns.items())
    for i, (title, returns) in enumerate(dsm_returns.items()):
        ax = axes.flatten()[i] if num_plots > 1 else axes # Handle single subplot case
        sns.histplot(returns, kde=True, color='blue', ax=ax)
        ax.set_title(title)
        ax.set_xlabel('Return')
        ax.set_ylabel('Density')
        ax.get_legend().remove()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust for title 
    plt.show()
    