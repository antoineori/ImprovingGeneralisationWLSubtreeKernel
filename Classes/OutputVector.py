class VectorList:
    def __init__(self):
        self.vectors = []

    def add_vector(self, vector):
        self.vectors.append(vector)

    def remove_vector(self, vector):
        self.vectors.remove(vector)

    def get_vector(self, index):
        return self.vectors[index]

    def get_all_vectors(self):
        return self.vectors
