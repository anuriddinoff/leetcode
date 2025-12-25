class Solution(object):
    def recoverOrder(self, order, friends):
        a = []
        for i in order:
            for j in friends:
                if i == j:
                    a.append(i)
        return a            