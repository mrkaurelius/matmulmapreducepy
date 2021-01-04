import scipy.io
import numpy as np

# TODO
# mapreduce un verdigi cevai kontrol edebilecek kodu gelistir


def parse_mat(mat):
    csc_mat = None
    for i in mat['Problem'][0][0]:
        if isinstance(i, scipy.sparse.csc.csc_matrix):
            pmat = i
    return pmat.tocoo()

def write_matrix(amat,bmat):
    with open(amat_file + bmat_file + '.txt', 'w') as f:
        for ind in range(len(amat.row)):
            f.write(str("a,{},{},{}\n".format(
                amat.row[ind], amat.col[ind], amat.data[ind])))

    with open(amat_file + bmat_file + '.txt', 'a') as f:
        for ind in range(len(bpmat.row)):
            f.write(str("b,{},{},{}\n".format(
                bmat.row[ind], bmat.col[ind], bmat.data[ind])))


# mat_file = 'bcspwr01.mat'
amat_file = 'Trec4.mat'
bmat_file = 'Trec4.mat'

# mat_file = 'Trec6.mat'
amat = scipy.io.loadmat(amat_file)
bmat = scipy.io.loadmat(bmat_file)

apmat = parse_mat(amat)
bpmat = parse_mat(bmat)
write_matrix(apmat, bpmat.transpose())

amat_dense = apmat.todense()
bmat_dense = bpmat.todense()
print(amat_dense)
print(bmat_dense)
print(np.matmul(amat_dense,  bmat_dense.transpose()))