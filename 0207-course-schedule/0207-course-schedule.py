class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프로 구성 변경 
        graph = collections.defaultdict(list)
        for x,y in prerequisites:
            graph[x].append(y)

        # 순환구조를 판별하기 위해 이미 방문했던 노드를 traced 변수에 저장 
        traced = set()
        def dfs(k):
            if k in traced:
                return False
            if k in visited:
                return True
            traced.add(k)
            for y in graph[k]:
                if not dfs(y):
                    return False 
            # 형제노드 지만 기록이 남으면 순환으로 잘 못 판단할 수도 있기 때문에
            traced.remove(k)
            visited.add(k)
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False

        return True 