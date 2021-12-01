

class DFS:
    def __init__(self):
        self.graph={}
        self.visited=[]
    def insert(self,initial,node):
        if initial not in self.graph.keys():
            self.graph[initial]=[node]
        else:
            self.graph[initial].append(node)
    def print_graph(self):
        print(self.graph)
    def traverse_dfs(self,node):
        if node not in self.graph.keys():
            return
        for k in self.graph[node]:
            if (node,k) not in self.visited:
                self.visited.append((node,k))
                #print(k,self.visited)
                self.traverse_dfs(k)
def main():
    obj = DFS()
    obj.insert(1,2)
    obj.insert(2,3)
    obj.insert(1,3)
    obj.insert(3,2)
    obj.insert(1,5)
    obj.insert(3,4)
    #obj.print_graph()
    obj.traverse_dfs(1)

if __name__=="__main__":
    main()
