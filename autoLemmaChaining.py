class Fact:
    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return self.description


class Lemma:
    def __init__(self, name, check, conclude):
        self.name = name
        self.check = check
        self.conclude = conclude


class ProofEngine:
    def __init__(self):
        self.facts = []
        self.lemmas = []

    def add_fact(self, fact):
        if fact.description not in [f.description for f in self.facts]:
            self.facts.append(fact)

    def add_lemma(self, lemma):
        self.lemmas.append(lemma)

    def run(self):
        changed = True
        while changed:
            changed = False
            for lemma in self.lemmas:
                if lemma.check(self.facts):
                    new_fact = lemma.conclude()
                    if new_fact.description not in \
                       [f.description for f in self.facts]:
                        self.add_fact(new_fact)
                        changed = True
