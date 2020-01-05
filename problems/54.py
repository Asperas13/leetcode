class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result_list = []
        visited = {}
        n = len(matrix)
        m = len(matrix[0])
        size = n * m
        cur_direction = 'r'
        cur_x, cur_y = 0, 0
        delta_x, delta_y = 1, 0
        directions_mapping = {'r': ('d', 0, 1), 'd': ('l', -1, 0), 'l': ('u', 0, -1), 'u': ('r', 1, 0)}
        while len(result_list) < size:
            if cur_x < 0 or cur_x == m or cur_y < 0 or cur_y == n or (cur_y, cur_x) in visited:
                cur_x -= delta_x
                cur_y -= delta_y
                cur_direction, delta_x, delta_y = directions_mapping[cur_direction]
                cur_x += delta_x
                cur_y += delta_y

            result_list.append(matrix[cur_y][cur_x])
            visited[(cur_y, cur_x)] = 1
            cur_y += delta_y
            cur_x += delta_x

        return result_list