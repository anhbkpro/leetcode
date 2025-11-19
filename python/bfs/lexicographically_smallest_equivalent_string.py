class Solution:
    def __init__(self):
        self.min_char = 0

    def dfs(self, src, adj_matrix, visited, component):
        # Mark the character as visited
        visited[src] = True
        # Add it to the list
        component.append(src)
        # Update the minimum character in the component
        self.min_char = min(self.min_char, src)

        for i in range(26):
            # Perform DFS if the edge exists and the node isn't visited yet
            if adj_matrix[src][i] is not None and not visited[i]:
                self.dfs(i, adj_matrix, visited, component)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Adjacency matrix to store edges
        adj_matrix = [[None for _ in range(26)] for _ in range(26)]

        for i in range(len(s1)):
            char1_idx = ord(s1[i]) - ord("a")
            char2_idx = ord(s2[i]) - ord("a")
            adj_matrix[char1_idx][char2_idx] = 1
            adj_matrix[char2_idx][char1_idx] = 1

        # Array to store the final character mappings
        mapping_char = list(range(26))

        # Array to keep visited nodes during DFS
        visited = [False] * 26

        for c in range(26):
            if not visited[c]:
                # Store the characters in the current component
                component = []
                # Variable to store the minimum character in the component
                self.min_char = 27
                self.dfs(c, adj_matrix, visited, component)

                # Map the characters in the component to the minimum character
                for vertex in component:
                    mapping_char[vertex] = self.min_char

        # Create the answer string
        ans = ""
        for c in baseStr:
            ans += chr(mapping_char[ord(c) - ord("a")] + ord("a"))

        return ans
