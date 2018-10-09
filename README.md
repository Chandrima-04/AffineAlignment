# AffineAlignment

An affine gap penalty is written as a+b⋅(L−1), where L is the length of the gap, a is a positive constant called the gap opening penalty, and b is a positive constant called the gap extension penalty.

We can view the gap opening penalty as charging for the first gap symbol, and the gap extension penalty as charging for each subsequent symbol added to the gap.

For example, if a=11 and b=1, then a gap of length 1 would be penalized by 11 (for an average cost of 11 per gap symbol), whereas a gap of length 100 would have a score of 110 (for an average cost of 1.10 per gap symbol).

Consider the strings "PRTEINS" and "PRTWPSEIN". If we use the BLOSUM62 scoring matrix and an affine gap penalty with a=11 and b=1, then we obtain the following optimal alignment.
