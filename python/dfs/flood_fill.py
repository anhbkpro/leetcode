from typing import List, Tuple


class Solution:
    def __init__(self) -> None:
        self.DIRECTIONS: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        for r in range(len(image)):
            for c in range(len(image[0])):
                if r == sr and c == sc:
                    old_color = image[r][c]
                    new_color = color
                    if old_color == new_color:
                        return image
                    self._dfs(image, r, c, new_color, old_color)

        return image

    def _dfs(
        self, image: List[List[int]], sr: int, sc: int, new_color: int, old_color: int
    ):
        if not self._is_valid_cell(image, sr, sc, new_color, old_color):
            return

        image[sr][sc] = new_color
        for dx, dy in self.DIRECTIONS:
            self._dfs(image, sr + dx, sc + dy, new_color, old_color)

    def _is_within_grid_bounds(self, image: List[List[int]], sr: int, sc: int) -> bool:
        return sr >= 0 and sc >= 0 and sr < len(image) and sc < len(image[0])

    def _is_visited(self, image: List[List[int]], sr: int, sc: int, color: int) -> bool:
        return image[sr][sc] == color

    def _is_same_region_with_starting_point(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> bool:
        return image[sr][sc] == color

    def _is_valid_cell(
        self, image: List[List[int]], sr: int, sc: int, new_color: int, old_color: int
    ) -> bool:
        return (
            self._is_within_grid_bounds(image, sr, sc)
            and not self._is_visited(image, sr, sc, new_color)
            and self._is_same_region_with_starting_point(image, sr, sc, old_color)
        )
