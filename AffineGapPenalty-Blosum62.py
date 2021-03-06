
# coding: utf-8

# In[3]:


import math
global a
global b
global MIN
a = -11
b = -1
MIN = -(math.inf)


# In[4]:


def matching(s, t, i, j):
    blosum62 = [[4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0, -4],
                [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1, -4],
                [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1, -4],
                [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1, -4],
                [0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2, -4],
                [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1, -4 ],
                [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1, -4], 
                [0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1, -4] ,
                [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1, -4], 
                [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1, -4], 
                [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1, -4], 
                [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1, -4], 
                [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1, -4], 
                [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1, -4], 
                [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2, -4], 
                [1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0, -4], 
                [0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0, -4], 
                [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2, -4], 
                [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1, -4], 
                [0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1, -4], 
                [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1,-1,-4],
                [-1, 0, 0, 1,-3, 3, 4,-2, 0,-3,-3, 1,-1,-3,-1, 0,-1,-3,-2,-2, 1, 4,-1,-4],
                [0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2, 0, 0,-2,-1,-1,-1,-1,-1,-4],
                [-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4, 1 ]]
    RNA_pair = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X', '*']
    x =RNA_pair.index(s[j-1])
    y =RNA_pair.index(t[i-1])
    score = blosum62[x][y] 
    return (score)


# In[5]:


def initialize_x(i, j):
    if i > 0 and j == 0:
        return MIN
    else:
        if j > 0:
            return a + (b * j)
        else:
            return 0

def initialize_y(i, j):
    if j > 0 and i == 0:
        return MIN
    else:
        if i > 0:
            return a + (b * i)
        else:
            return 0

def initialize_m(i, j):
    if j == 0 and i == 0:
        return 0
    else:
        if j == 0 or i == 0:
            return MIN
        else:
            return 0


# In[6]:


def AffineGapPenaly(s,t):
    print (s,t)
    m = len(s)
    n = len(t)
    best_score = 0    
    X = [[initialize_x(i, j) for j in range(0, m+1)] for i in range(0, n+1)]
    Y = [[initialize_y(i, j) for j in range(0, m+1)] for i in range(0, n+1)]
    M = [[initialize_m(i, j) for j in range(0, m+1)] for i in range(0, n+1)]
    for j in range(1, m+1):
        for i in range(1, n+1):
            X[i][j] = max((a  + M[i][j-1]), (b  + X[i][j-1]), (a  + Y[i][j-1]))
            Y[i][j] = max((a + M[i-1][j]), (a  + X[i-1][j]), (b + Y[i-1][j]))
            M[i][j] = max(matching(s, t, i, j) + M[i-1][j-1], X[i][j], Y[i][j])
    best_score = max(M[i][j], X[i][j], Y[i][j])
    xalgn=""
    yalgn=""
    i, j = n,m
    while (i>0 or j>0):
        if (i>0 and j>0 and M[i][j] == M[i-1][j-1] + matching(s, t, i, j)):
            xalgn += s[j-1]
            yalgn += t[i-1]
            i -= 1; j -= 1
        elif (i>0 and M[i][j] == Y[i][j]):
            xalgn += '_'
            yalgn += t[i-1]
            i -= 1
        elif (j>0 and M[i][j] == X[i][j]):
            xalgn += s[j-1]
            yalgn += '_'
            j -= 1
    print (best_score)
    print (xalgn[::-1])
    print (yalgn[::-1])


# In[8]:


AffineGapPenaly("DVKVDDRQHGRINCPCNSRPKPPLVLLPKWQAKGLFRPFPDPNHRPKDWSFGCFEFIRFRRWNRHTDYAIGSNLMHSYYIHMAWI", 
                "DVKVDDRQHGRINCAEYHTFCNSRPKPPLVLLPKWQAFLSLFRPFPWSFGCFEFIRFRRWNGSYYIHMAMI")

