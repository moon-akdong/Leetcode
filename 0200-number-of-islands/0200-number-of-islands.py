class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(ind1,ind2):
            if ind1 < 0 or ind1 >= len(grid) or ind2 < 0 or ind2>=len(grid[ind1]) or grid[ind1][ind2] !='1':
                return 
            grid[ind1][ind2] = '0'
            dfs(ind1 +1,ind2)
            dfs(ind1-1,ind2)
            dfs(ind1,ind2+1)
            dfs(ind1,ind2-1)


        count= 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count +=1 

        return count

        