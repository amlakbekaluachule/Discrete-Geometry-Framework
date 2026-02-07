def cyclic_lemma_check(facts):
    return any("lie on a common circle" in f.description for f in facts)


def cyclic_lemma_conclude():
    return Fact("Opposite angles subtend equal arcs")
