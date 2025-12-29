from logistic_hub import LogisticHub
from matplotlib import pyplot as plt
start_data = "data.json"

if __name__ == "__main__":
    hub = LogisticHub(start_data)
    hub.draw_graph()
    plt.show()
