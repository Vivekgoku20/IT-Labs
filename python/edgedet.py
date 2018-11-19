e=[[0 for i in range(100)] for j in range(0,100)]
visited=[0 for i in range(0,100)]
time=0
ts=[-1 for i in range(100)]
level=[0 for i in range(100)]
te=[-1 for i in range(100)]
dfsp=[]
def dfs(u,l):
    global time
    if(visited[u]==0):
        ts[u] = time
        time = time + 1
        dfsp.append(u)
        visited[u]=1
    else:
        te[u]=time
        time+1
    for i in range(0,int(n)):
        if(e[u][i]==1):
            if(visited[i]==0):
            	print(u," ",i," tree egde")
            	level[i]=l+1
            	dfs(i,l+1)
            elif((te[i]==-1) and (ts[i]!=-1)):
                print(u," ",i," back edge")
            else:
            	if(ts[i]>ts[u]):
            		print(u," ",i," front edge")
            	else:
            		print(u," ",i," cross edge")	
    te[u]=time
    time=time+1
v1=[0 for i in range(100)]
time=0
def dfsde(u):
    global time

def main():
    global n
    n = input("Enter the number of vertices")
    global w, h
    w,h =int(n),int(n)
    m=input("Enter the number of edges")
    #visited=[0 for i in range(0,int(n))]
    q=[]
    #e = [[0 for x in range(w)] for y in range(h)]
    for i in range(0,int(m)):
        k=input("Enter edge ")
        c=k.split()
        e[int(c[0])][int(c[1])]=1
        #e[int(c[1])][int(c[0])]=1
    count=0
    l=input("Enter the dfs source vertex ")
    dfs(int(l),0)
    ts[0]=0
    print("dfs traversal")
    for i in range(0,int(n)):
    	print(dfsp[i])
    for i in range(0,int(n)):
        print("v ",i,"st ",ts[i],"et ",te[i])
    #for i in range(0,int(n)):
        #for j in range(0,int(n)):
            #if(e[i][j]==1):
                #if(level[i]==level[j])
    print("Levels of dfs tree of each vertex")
    for i in range(0,int(n)):
        print(level[i])
if __name__=='__main__':
    main()

