class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 구현 
        graph = collections.defaultdict(list)
        for u,w,v in times:
            graph[u].append((w,v))

        # 우선순위큐 변수 지정
        Q = [(0,k)]
        dist = collections.defaultdict(int)

        # 우선수위큐 최솟값 기준으로 정점까지 최단 경로 삽입 
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time 
                for v,w in graph[node]:
                    alt = time + w 
                    heapq.heappush(Q,(alt,v))

        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == n:
            return max(dist.values())
        return -1 