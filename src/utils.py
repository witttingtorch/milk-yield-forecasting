import matplotlib.pyplot as plt

def save_plot(fig, filename):
    fig.savefig(f"../outputs/{filename}.png")
