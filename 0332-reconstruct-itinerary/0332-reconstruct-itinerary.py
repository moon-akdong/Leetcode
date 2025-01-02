class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = [] 
        graph = collections.defaultdict(list)
        for srt,arv in sorted(tickets,reverse=True):
            graph[srt].append(arv)

        def dfs(srt):
            while graph[srt]:
                dfs(graph[srt].pop())
            result.append(srt)
        dfs("JFK")
        return result[::-1]