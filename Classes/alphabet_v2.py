from fuzzywuzzy import fuzz


class Alphabet2:
    def __init__(self):
        self.alphabet = []
        self.inverted_alphabet = []
        self.counter = 1

    def get_fuzzy_label(self, p_iteration, p_full_label, p_fuzzy):
        if int(p_iteration) >= len(self.alphabet):
            self.alphabet.extend({})
        d = self.alphabet[int(p_iteration)]
        if p_full_label not in d:
            fuzzy_label = self.search_fuzzy_label(p_full_label, p_fuzzy)
            if fuzzy_label != "0":
                d[p_full_label] = self.alphabet[int(p_iteration)][fuzzy_label]
            else:
                d[p_full_label] = self.counter
                self.counter += 1
        if int(p_iteration) >= len(self.inverted_alphabet):
            self.inverted_alphabet.extend({})
        self.inverted_alphabet[int(p_iteration)][d[p_full_label]] = p_full_label
        return str(d[p_full_label])

    def get_label(self, p_iteration, p_full_label):
        if int(p_iteration) >= len(self.alphabet):
            self.alphabet.extend([])
        d = self.alphabet[int(p_iteration)]
        if p_full_label not in d:
            d[p_full_label] = self.counter
            self.counter += 1
        if int(p_iteration) >= len(self.inverted_alphabet):
            self.inverted_alphabet.extend({})
        self.inverted_alphabet[int(p_iteration)][d[p_full_label]] = p_full_label
        return str(d[p_full_label])

    def prnt(self):
        print(self.alphabet)

    def prnt_inverted_alph(self):
        print(self.inverted_alphabet)

    def search_fuzzy_label(self, p_label, p_fuzz):
        tempvar, _ = p_label.split(',', 1)
        current_iteration_alphabet = self.alphabet[int(tempvar)]
        for a in current_iteration_alphabet:
            similar = fuzz.ratio(a, p_label)
            if similar > p_fuzz:
                return str(a)
        return "0"


