import seaborn as sns
import matplotlib.pyplot as plt

def plot_seaborn_example():
    data = sns.load_dataset("iris")
    sns.pairplot(data)
    plt.show()

if __name__ == "__main__":
    plot_seaborn_example()
