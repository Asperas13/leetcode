# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        visited = set()
        directions = {'up': 'left', 'left': 'down', 'down': 'right', 'right': 'up'}

        def map_direction_to_coord_delta(direction):
            if direction == 'up':
                return 0, 1
            elif direction == 'left':
                return -1, 0
            elif direction == 'down':
                return 0, -1
            else:
                return 1, 0

        def get_next_direction(direction):
            return directions[direction]

        def go_back(robot):
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnLeft()
            robot.turnLeft()

        def _dfs(robot, x, y, visited, current_direction):
            if (x, y) in visited:
                return

            robot.clean()
            visited.add((x, y))

            for i in range(4):
                dx, dy = map_direction_to_coord_delta(current_direction)
                if robot.move():
                    _dfs(robot, x + dx, y + dy, visited, current_direction)
                    go_back(robot)

                robot.turnLeft()
                current_direction = get_next_direction(current_direction)

        _dfs(robot, 0, 0, visited, 'up')