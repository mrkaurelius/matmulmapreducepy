import scipy.io

# TODO
# kullanilacak matrisleri standardize et
# mat = scipy.io.loadmat('Trec4.mat')

def parse_mat(mat):
    csc_mat = None
    for i in mat['Problem'][0][0]:
       if isinstance(i, scipy.sparse.csc.csc_matrix): 
           pmat = i 
    return pmat.tocoo() 

# mat_file = 'bcspwr01.mat'
mat_file = 'Trec4.mat'
# mat_file = 'Trec6.mat'
mat = scipy.io.loadmat(mat_file)

pmat = parse_mat(mat)

with open(mat_file + '.txt', 'w') as f:
    for ind in range(len(pmat.row)):
        f.write(str("{},{},{}\n".format(pmat.row[ind], pmat.col[ind], pmat.data[ind])))

# print(pmat)
