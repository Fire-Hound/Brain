import numpy as np
class Cell:
    def __init__(self):
        self.set_random_data()
        self.set_random_connections()
    def _get_random_connections(self):
        connections = np.array(["n", "ne", "e", "se", "s", "sw", "w", "nw"])
        num_of_connections = np.random.randint(0,9)
        random_connections = np.random.choice(connections, size=num_of_connections, replace=False)
        return random_connections
    def set_random_connections(self):
        self.connections = self._get_random_connections()
    def _get_random_data(self):
        return (np.random.random() * 2) - 1
    def set_random_data(self):
        self.data =  self._get_random_data()

class Brain(Cell):
    def __init__(self, rows, cols):
        self.Cells = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(Cell())
            self.Cells.append(row)
    def __getitem__(self, i):
        return self.Cells[i]