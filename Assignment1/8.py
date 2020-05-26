MAX = 100

def lu_decomposition(mat, n):
    lower = [[0 for x in range(n)]
            for y in range(n)]
    upper = [[0 for x in range(n)]
            for y in range(n)];

    for i in range(n):
        for k in range(i, n):
            sum = 0;
            for j in range(i):
                sum += (lower[i][j] * upper[j][k]);
            upper[i][k] = mat[i][k] - sum;

        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1; # Diagonal as 1
            else:
                sum = 0;
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
                lower[k][i] = int((mat[k][i] - sum) /
                        upper[i][i]);
    
    print("Lower Triangular"); 
    for i in range(n): 
        for j in range(n): 
            print(lower[i][j], end = "\t");  
        print("", end = "\n"); 
    
    print("Upper Triangular");
    for i in range(n): 
        for j in range(n):
            print(upper[i][j], end = "\t");
        print(""); 
    

mat = [[1, 1, -1], [-3, 5, 4], [-2, -4, 7]];

lu_decomposition(mat, 3);
