class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        V I S U A L I Z E  IMAGES IN UR HEAD
        - the interview is me just teaching anay smth
        TALK QUIETLY dont speak presentation voice
        DONT DO THE PROBLEM WITH PLAIN ENGLISH IN UR HEAD
        

        valid tree:
        1. no cycles - visited
        2. connected - one dfs can reach all

        1. use edge list to create adj list
        2. dfs(0) through adj list
         - visited --> check connected graph by seeing that all nodes in visited
         - dfs all neighbors except parent node u j came from
            - if hit another visited, then return False. assume True everywhere

        make sure you visit all nodes
        """
        # UNDIRECTED adj list graph
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        visited = set() # all nodes added so checks if graph connected
        
        def dfs(node, parent):
            # base cases - visited
            if node in visited:
                return False # cycle detected
            
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False
            
            return True
        
        # check whether all nodes visited by single dfs
        return dfs(0, None) and len(visited) == len(adj_list.keys())




