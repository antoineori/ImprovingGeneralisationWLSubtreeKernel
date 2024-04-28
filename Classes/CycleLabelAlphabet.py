class CycleLabelAlphabet:
    def __init__(self, max_cycle_length=None):
        self.alphabet = {(): 'c0'}
        self.counter = 1
        self.max_cycle_length = max_cycle_length

    def get_cycle_label(self, lst):
        # Filter the list based on max_cycle_length
        if self.max_cycle_length is not None:
            lst = [x for x in lst if x <= self.max_cycle_length]
        # sort and then convert the list to a tuple to make it hashable
        lst = sorted(lst)
        lst = tuple(lst)
        # if the list is not in the alphabet, add it and increment the counter
        if lst not in self.alphabet:
            self.alphabet[lst] = 'c' + str(self.counter)
            self.counter += 1
        # return the label for the list
        return self.alphabet[lst]

    def prnt(self):
        print(self.alphabet)



"""class CycleLabelAlphabet:
    def __init__(self):
        self.cycle_labels = {}
        self.cycle_combinations = {}

    def get_cycle_label(self, cycle_lengths):
        cycle_lengths = tuple(sorted(cycle_lengths))
        if cycle_lengths in self.cycle_labels:
            return self.cycle_labels[cycle_lengths]
        else:
            cycle_label = "C" + str(len(self.cycle_labels) + 1)
            self.cycle_labels[cycle_lengths] = cycle_label
            self.cycle_combinations[cycle_label] = cycle_lengths
            return cycle_label

    def get_cycle_combinations(self):
        return self.cycle_combinations
"""
