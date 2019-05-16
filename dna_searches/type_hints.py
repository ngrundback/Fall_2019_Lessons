from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):  # don't run off end!
            return gene
        #  initialize codon out of three nucleotides
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)  # add codon to gene
    return gene


my_gene: Gene = string_to_gene(gene_str)
# print(my_gene)

def l_search(gene: Gene, key_codon: Codon) -> int:
    count = 0
    for codon in gene:
        if codon == key_codon:
            return 1, count
        count += 1
    return -1

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
print(l_search(my_gene, acg))

def b_search(gene: Gene, key_codon: Codon) -> bool:
    low: int = 0
    high: int = len(gene)-1

    while low <= high:
        mid: int = (low + high)//2 # no float
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True, mid
my_sorted_gene: Gene = sorted(my_gene)
print(b_search(my_sorted_gene, acg))
