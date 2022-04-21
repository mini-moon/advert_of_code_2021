import os
from dataclasses import dataclass


@dataclass
class Point:
    """
    Class to represent a point in the Heightmap
    """

    row: int
    col: int
    height: int

    @property
    def risk_level(self):
        return 1 + self.height

    def __int__(self):
        return self.height

    def __lt__(self, other):
        if isinstance(other, Point):
            return self.height < other.height
        return self.height < other

    def __gt__(self, other):
        if isinstance(other, Point):
            return self.height > other.height
        return self.height > other

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.height == other.height
        return self.height == other

    def __hash__(self):
        return hash((self.row, self.col, self.height))


class Heightmap:
    """
    Class to represent a heightmap containing a grid of Points.
    """

    def __init__(self, data):
        self.points = [
            [Point(row, col, height) for col, height in enumerate(data[row])]
            for row in range(len(data))
        ]

    def __is_low_point(self, point: Point) -> bool:
        """
        Return whether all adjacent cells (up, down, left, right) are higher than the current row, col
        Args:
            point (Point): The point to check
        Returns:
            bool: Whether the point is a low point or not
        """
        row, col = point.row, point.col
        above = self[row - 1][col] if row > 0 else float("inf")
        below = self[row + 1][col] if row < len(self) - 1 else float("inf")
        left = self[row][col - 1] if col > 0 else float("inf")
        right = self[row][col + 1] if col < len(self[row]) - 1 else float("inf")
        return self[row][col] < min(above, below, left, right)

    def low_points(self):
        """
        Return a list of all low points in the heightmap
        Returns:
            list[Point]: A list of all low points in the heightmap
        """
        return [point for row in self for point in row if self.__is_low_point(point)]

    def __getitem__(self, key):
        return self.points[key]

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        for row in self.points:
            yield row

    def __repr__(self):
        return "".join(
            "".join(f"{point.height}" for point in row) + "\n" for row in self.points
        )


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        data = [list(map(int, row)) for row in f.read().splitlines()]

    heightmap = Heightmap(data)

    print(sum(point.risk_level for point in heightmap.low_points()))


if __name__ == "__main__":
    main()
