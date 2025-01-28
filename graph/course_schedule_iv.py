from typing import List
from collections import defaultdict, deque


class SolutionTreeTraversalOnDemand:
    # Performs DFS and returns true if there's a path between src and target and false otherwise.
    def isPrerequisite(
        self, adjList: dict, visited: List[bool], src: int, target: int
    ) -> bool:
        visited[src] = True

        if src == target:
            return True

        for adj in adjList.get(src, []):
            if not visited[adj]:
                if self.isPrerequisite(adjList, visited, adj, target):
                    return True
        return False

    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])

        result = []

        for query in queries:
            # Reset the visited array for each query
            visited = [False] * numCourses
            result.append(self.isPrerequisite(adjList, visited, query[0], query[1]))

        return result


class SolutionTreeTraversalPreprocessed:
    # Iterate over each node and perform BFS starting from it.
    # Mark the starting node as a prerequisite to all the nodes in the BFS
    # traversal.
    def preprocess(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        adjList: dict[int, List[int]],
        isPrerequisite: List[List[bool]],
    ) -> None:
        for i in range(numCourses):
            q = deque([i])

            while q:
                node = q.popleft()

                for adj in adjList.get(node, []):
                    # If we have marked i as a prerequisite of adj it implies we
                    # have visited it. This is equivalent to using a visited
                    # array.
                    if not isPrerequisite[i][adj]:
                        isPrerequisite[i][adj] = True
                        q.append(adj)

    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = {}
        for edge in prerequisites:
            if edge[0] not in adjList:
                adjList[edge[0]] = []
            adjList[edge[0]].append(edge[1])

        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        self.preprocess(numCourses, prerequisites, adjList, isPrerequisite)

        answer = []
        for query in queries:
            answer.append(isPrerequisite[query[0]][query[1]])

        return answer


class SolutionTopologicalSortKahnAlgorithm:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for edge in prerequisites:
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodePrerequisites = defaultdict(set)

        while q:
            node = q.popleft()

            for adj in adjList[node]:
                # Add node and prerequisite of the node to the prerequisites of adj
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    nodePrerequisites[adj].add(prereq)

                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)

        answer = []
        for q in queries:
            answer.append(q[0] in nodePrerequisites[q[1]])

        return answer


class SolutionFloydWarshallAlgorithm:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]

        for edge in prerequisites:
            isPrerequisite[edge[0]][edge[1]] = True

        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    # If there is a path src -> intermediate and intermediate -> target, then src -> target exists as well
                    isPrerequisite[src][target] = isPrerequisite[src][target] or (
                        isPrerequisite[src][intermediate]
                        and isPrerequisite[intermediate][target]
                    )

        answer = []
        for query in queries:
            answer.append(isPrerequisite[query[0]][query[1]])

        return answer
