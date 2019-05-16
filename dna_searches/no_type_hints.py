# Genes are commonly represented in computer software as a sequence of the
# characters A, C, G, and T. Each letter represents a nucleotide, and the
# combination of three nucleotides is called a codon.
# A codon codes for a specific amino acid that together with other amino acids
# can form a protein. A classic task in bioinformatics software is to find a
# particular codon within a gene.

Nucleotide = ('A', 'C', 'G', 'T')
Codon = []  # type alias for codons
Gene = []  # type alias for genes

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"


def string_to_gene(s):
    gene = []
    for i in range(0, len(s)-3, 3):
        if (i + 2) >= len(s):  # don't run off end!
            return gene
        #  initialize codon out of three nucleotides
        codon = (s[i],s[i + 1], s[i + 2])
        gene.append(codon)  # add codon to gene
    return gene


my_gene = string_to_gene(gene_str)
print(my_gene)
