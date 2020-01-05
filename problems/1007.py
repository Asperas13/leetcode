class Solution:
    def minDominoRotations(self, A, B) -> int:
        def _rotate(x, A, B):
            A_rotations, B_rotations = 0, 0
            for i in range(len(A)):
                if A[i] != x and B[i] != x:
                    return -1
                elif A[i] != x:
                    A_rotations += 1
                elif B[i] != x:
                    B_rotations += 1

            return min(A_rotations, B_rotations)

        rotations = _rotate(A[0], A, B)
        if rotations != -1 or A[0] == B[0]:
            return rotations
        else:
            return _rotate(B[0], A, B)