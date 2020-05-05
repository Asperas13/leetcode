from heapq import heappush, heappop
from collections import defaultdict, Counter


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_to_dishes = defaultdict(Counter)
        columns = []
        dishes = set()
        id_heap = []
        for order in orders:
            if order[2] not in dishes:
                columns.append(order[2])
                dishes.add(order[2])

            if int(order[1]) not in table_to_dishes:
                heappush(id_heap, int(order[1]))

            table_to_dishes[int(order[1])][order[2]] += 1

        columns.sort()
        columns.insert(0, "Table")
        answer = [columns]
        while id_heap:
            min_table = heappop(id_heap)
            table_order = [str(min_table)]
            for column in columns[1:]:
                table_order.append(str(table_to_dishes[min_table][column]))
            answer.append(table_order)

        return answer