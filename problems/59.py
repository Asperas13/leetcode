class Solution:
    def generateMatrix(self, n: int):
        matrix = [[None for _ in range(n)] for _ in range(n)]

        numb = 1
        corner_numb = n ** 2 + 1
        cur_direction = 'r'
        cur_x, cur_y = 0, 0
        delta_x, delta_y = 1, 0
        directions_mapping = {'r': ('d', 0, 1), 'd': ('l', -1, 0), 'l': ('u', 0, -1), 'u': ('r', 1, 0)}
        while True:
            if numb == corner_numb:
                break

            if cur_x < 0 or cur_x == n or cur_y < 0 or cur_y == n or matrix[cur_y][cur_x] is not None:
                cur_x -= delta_x
                cur_y -= delta_y
                cur_direction, delta_x, delta_y = directions_mapping[cur_direction]
                cur_x += delta_x
                cur_y += delta_y

            matrix[cur_y][cur_x] = numb
            numb += 1
            cur_y += delta_y
            cur_x += delta_x

        return matrix