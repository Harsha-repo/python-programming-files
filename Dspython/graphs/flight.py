# problem statement we have set of places as nodes for ex we  have mumbai , dubai , paris , newyork , torneto 
# we need to find shortes path between mumbai and new york  with the min numof stops 

# and the graph is link given png

class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict={}                   # this is an empty dict that is used to store the start point city and all connected nodes to that 
        for start,end in self.edges:         # this loops helps to achive that 
            if start in self.graph_dict:    
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print('graph dict',self.graph_dict)
    
    # now lets find all the possible routes that are there between our start and end nodes 

    def get_paths(self,start,end,path=[]):
        path = path+[start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths
    
    # to find the shortest dist flight from mumbai to newyork is that list witht he lowest elements adh
    

    def get_shortest_path(self,start,end,path=[]):
        path = path+[start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None
        
        shortest_path=None

        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)< len(shortest_path):
                        shortest_path=sp
                        
        return shortest_path
    
if __name__=='__main__':
    routes=[
        ("mumbai","paris"),
        ('mumbai','dubai'),
        ('paris', 'dubai'),
        ('paris','newyork'),
        ('dubai','newyork'),
        ('newyork','toronto')
    ]

    route_graph = Graph(routes)
    start = 'mumbai'
    end = 'newyork'
    print(f'the paths between {start} and {end}:',route_graph.get_paths(start,end))
    print(f'the shortest paths between {start} and {end}:',route_graph.get_shortest_path(start,end))
    sp = route_graph.get_paths(start,end)
    l=[]
    for i in sp:
        min = len(i)
        if len(i)<min:
            min=len(i)
        index=i
    print(index) 
        
    