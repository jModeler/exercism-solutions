AMINO_LOOKUP = {
"Methionine": "AUG",
"Phenylalanine": ["UUU", "UUC"],
"Leucine": ["UUA", "UUG"],
"Serine": ["UCU", "UCC", "UCA", "UCG"],
"Tyrosine": ["UAU", "UAC"], 
"Cysteine": ["UGU", "UGC"],
"Tryptophan": "UGG",
"STOP": ["UAA", "UAG", "UGA"]
}

def inverse_dict(lookup):
    inv_lookup = {}
    for k, values in lookup.items():
        if isinstance(values, list):
            for v in values:
                inv_lookup[v] = k 
        else:
            inv_lookup[values] = k
    return inv_lookup

CODON_LOOKUP = inverse_dict(AMINO_LOOKUP)
STEP_SIZE = 3


def proteins(strand):
    result = []
    for ii in range(0, len(strand), STEP_SIZE):
        codon = strand[ii:(ii+STEP_SIZE)]
        if CODON_LOOKUP[codon] == "STOP":
            return result 
        else:
            result.append(CODON_LOOKUP[codon])
    return result

        

