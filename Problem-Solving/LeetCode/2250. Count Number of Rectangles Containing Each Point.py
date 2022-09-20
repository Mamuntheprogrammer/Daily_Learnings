class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key = lambda x: x[0])
        dict1 = defaultdict(list)

        for l, h in rectangles:
            dict1[h].append(l)



        def dfs(x,y): 
            count = 0

            for h in range(y,101):
                count += len(dict1[h]) - bisect.bisect_left(dict1[h],x)

            return count

        return [dfs(x,y) for x,y in points]