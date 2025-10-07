DNA_RNA = {
    'G':'C',
    'C':'G',
    'T':'A',
    'A':'U'
}

def to_rna(dna_strand):
    rna = ''
    for ds in dna_strand:
        rna = ''.join([rna, DNA_RNA.get(ds)])
    return rna

