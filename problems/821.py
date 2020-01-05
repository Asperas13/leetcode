class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        c_poses = [i for i in range(len(S)) if S[i] == C]
        return [min([abs(j - i) for j in c_poses]) for i in range(len(S))]
