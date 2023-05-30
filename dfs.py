# dfs
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
visited=[];
stack=[];
def dfs(visited,graph,start,goal):
    visited.append(start);
    stack.append(start);
    while stack:
        m = stack[-1];
        stack.pop();
        print(m);
        if m==goal:
            print("Goal node Found");
            break;
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n);
                    stack.append(n);


print("DFS Traversal");
dfs(visited,graph,'A','F');