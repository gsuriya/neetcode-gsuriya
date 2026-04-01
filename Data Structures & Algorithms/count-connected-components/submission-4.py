class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        1. create adj_list from edge list
        2. dfs start on every node n
           - mark as visited so on later iterative dfs doesn't doublecount

        dfs from start node
        - if all nodes hit --> return True else False
        - if False: component_count += 1
        - if True: return component_count + 1

        """

        # create adj list
        adj_list = defaultdict(list)
        for src, dst in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        # dfs to increment components_count
        # - criteria for component?
             #comp 1: dont hit all nodes
             #comp 2: dont hit all nodes
             #comp 3: hit all nodes
                     # len(visited) == n
        # - criteria for NOT component?
        # return True if all nodes hit else return False

        # 1 -- 2 -- 3

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor != parent:
                    if dfs(neighbor, node):
                        return True

            if len(visited) == n:
                return True
            
            return False

        # dfs start on every node
        component_count = 0
        for i in range(n):
            if i not in visited:
                if not dfs(i, None):
                    component_count += 1
                else:
                    return component_count+1

        return component_count