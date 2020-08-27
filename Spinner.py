def transpose(matrix):                                         # membuat function dengan nama transpose
    for i in range(len(matrix)):                               # kemudian membuat looping terhadap row dan columns pada matrix, dimana data matrix 3x3, row(3),column(3)
        for j in range(i,len(matrix)):                         # kemudian membuat for loop column terhadap row. dengan range(row dan length dari matrix(3))
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
# ITERASI - 1 : i in range (2), awalnya i adalah 0, kemudian looping j, kondisi j saat i= 0, tidak berjalan

# ITERASI - 2 : saat i adalah 0,  j =1,
# >>>> data[0][1],data[1][0] = data[1][0], data[0][1]
# row 0, col 1 = (swap) ke row 1 col 0 -->> posisi '2' ke '4'

# ITERASI - 3 : i = 0, j = 2
# >>>> data[0][2],data[2][0] = data[2][0], data[0][2]
# row 0, col 2 = (swap) ke row 2 col 0 -->> posisi '3' ke '7'

# ITERASI - 4 : kondisi range(3) terpenuhi pertama, kembali ke for loop -1 saat i =1, j =1 
# tidak ada yang berubah karena posisi yang sama row 1 col 1 terhadap row 1 col 1

# ITERASI - 5 : kondisi i=1 , j=2
# >>>> data[1][2],data[2][1] = data[2][1], data[1][2]
# row 1, col 2 = (swap) ke row 2 col 1 -->> posisi '6' ke '8'


def RevTranspose(matrix):                       # membuat fungsi kedua untuk dengan nama RevTranspose dimana fungsi ini akan dijalankan guna me-reverse hasil transpose matrix pertama
    for i in range (len(matrix)):               # kemudian membuat looping terhadap row dan columns pada matrix, dimana data matrix 3x3, row(3),column(3)
        k = len(matrix) - 1
        for j in range(0,k):                    
            matrix[j][i], matrix[k][i] = matrix[k][i], matrix[j][i] 
            k = k - 1                           
    return matrix                   #memanggil hasil matrix

matrix = [[1,2,3], [4,5,6], [7,8,9]] #data matrix yang akan di transpose dan di reverse transpose

transpose(matrix)
print(RevTranspose(matrix))

