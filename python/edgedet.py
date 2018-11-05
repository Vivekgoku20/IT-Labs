e=[[0 for i in range(100)] for j in range(0,100)]
visited=[0 for i in range(0,100)]
time=0
ts=[-1 for i in range(100)]
pred=[-1 for i in range(100)]
k=0
level=[0 for i in range(100)]
te=[-1 for i in range(100)]
dfsp=[]
def dfs(u,l):
    global time
    global k
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
            	pred[i]=u
            	print(u," ",i," tree egde")
            	k=k+1
            	level[i]=l+1
            	dfs(i,l+1)
            elif((te[i]==-1) and (ts[i]!=-1)):
                print(u," ",i," ","back edge")
            else:
            	k=pred[i]
            	po=0
            	while(k!=-1):
            		if(k==u):
            			print(u," ",i," front edge")
            			po=1
            			break;
            		else:
            			k=pred[k]
            	if(po==0):
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
    print("Levels of dfs tree")
    for i in range(0,int(n)):
        print(level[i])
    '''for i in range(0,i,nt(n)):
        if visited[i]==0:
            q.append(i)
            visited[i]=1
            count=count+1
            print("Component ",count)
            print(i)
        while q:
            x=q.pop(0)
            if(visited[x]==0):
                visited[x]=1
            for i in range(0,int(n)):
                if(e[x][i]==1):
                    if(visited[i]==0):
                        print(i)
                        visited[i]=1
                        q.append(i)
    print("Total number of components")
    print(count)'''
if __name__=='__main__':
    main()

