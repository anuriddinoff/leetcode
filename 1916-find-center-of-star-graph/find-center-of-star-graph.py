class Solution(object):
    def findCenter(self, edges):
        count = len(edges)
        for i in edges:
            for j in i:
                a= 0
                for k in edges:
                    if j in k:
                        a +=1
                        if a ==count:
                            return j

