from fuzzywuzzy import fuzz


counter_similar = 0
counter_fuzzy = 0


class Label:
    def __init__(self, p_iteration, p_full_label):
        self.label = "{},{}".format(p_iteration, p_full_label)


class Alphabet:
    def __init__(self):
        self.alphabet = {}
        self.inverted_alphabet = {0: "0"}
        self.counter = 10000

    def get_fuzzy_label(self, p_iteration, p_full_label, p_fuzzy):
        p_label = "{},{}".format(p_iteration, p_full_label)
        if p_label not in self.alphabet:
            fuzzy_label = self.search_fuzzy_label(p_label, p_fuzzy)
            if fuzzy_label != "0":
                self.alphabet[p_label] = self.alphabet[fuzzy_label]
            else:
                self.alphabet[p_label] = self.counter
            self.inverted_alphabet[self.counter] = p_label
            self.counter += 1
        return str(self.alphabet[p_label])

    def get_label(self, p_iteration, p_full_label):
        p_label = "{},{}".format(p_iteration, p_full_label)
        if p_label not in self.alphabet:
            self.alphabet[p_label] = self.counter
            self.inverted_alphabet[self.counter] = p_label
            self.counter += 1
        return str(self.alphabet[p_label])

    def prnt(self):
        print(self.alphabet)

    def prnt_inverted_alph(self):
        print(self.inverted_alphabet)

    def search_fuzzy_label(self, p_label, p_fuzz):
        global counter_fuzzy
        global counter_similar
        tempvar, _ = p_label.split(',', 1)

        current_iteration_alphabet = {k for k, v in self.alphabet.items() if k.startswith(tempvar)}
        #print(current_iteration_alphabet)
        #print(tempvar)
        #print("---")
        for a in current_iteration_alphabet:
            similar = fuzz.ratio(a, p_label)
            #print(a+"---"+p_label)

            #print(similar)
            if similar > p_fuzz:
                counter_similar += 1
                return str(a)
        counter_fuzzy += 1
        return "0"

    def clear_alphabet(self):
        self.alphabet = {}
        self.inverted_alphabet = {0: "0"}


