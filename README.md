# AffineAlignment
An overlap alignment between two strings s and t is a local alignment of a suffix of s with a prefix of t. An optimal overlap alignment will therefore maximize an alignment score over all such substrings of s and t.

The term "overlap alignment" has also been used to describe what Rosalind defines as a semiglobal alignment. See “Semiglobal Alignment” for details.

Given: Two DNA strings s and t in FASTA format, each having length at most 10 kbp.

Return: The score of an optimal overlap alignment of s and t, followed by an alignment of a suffix s′ of s and a prefix t′ of t achieving this optimal score. Use an alignment score in which matching symbols count +1, substitutions count -2, and there is a linear gap penalty of 2. If multiple optimal alignments exist, then you may return any one.
