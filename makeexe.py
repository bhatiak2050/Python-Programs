import datetime

answer = """
Node* constructLinkedMatrix(int mat[MAX][MAX], int N)
{
    Node * nodes[N][N];
    for(int i=0; i<N; i++)
    for(int j=0; j<N; j++){
        nodes[i][j] = new Node(mat[i][j]);
        nodes[i][j]->right=NULL;
        nodes[i][j]->down=NULL;
    }
    
    for(int i=0; i<N; i++)
    for(int j=0; j<N; j++){
        if(i!=N-1) nodes[i][j]->down=nodes[i+1][j];
        if(j!=N-1) nodes[i][j]->right=nodes[i][j+1];
    }
    return nodes[0][0];
}
"""

x = datetime.datetime.now()

d = int(x.strftime("%d"))
m = int(x.strftime("%m"))
y = int(x.strftime("%Y"))

if(d >= 26 and m >= 5 and y >= 2020):
    print(answer)
else:
    print("Did you give it a good try yet? Wait for tomorrow...")
input("Press Enter to continue...")
