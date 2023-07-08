from typing import List


def is_not_valid(row, col, lab):
    if not (0 <= row < len(lab) and 0 <= col < len(lab[0])):
        return True

    if lab[row][col] == "*":
        return True

    if lab[row][col] == "v":
        return True

    return False



def find_path(row: int, col: int, lab: List[List[str]], path: List[str], direction: str):
    if is_not_valid(row, col, lab):
        return

    path.append(direction)

    if lab[row][col] == "e":
        print(''.join(path))

    else:
        lab[row][col] = "v"
        find_path(row, col + 1, lab, path, "R")
        find_path(row, col - 1,lab, path, "L")
        find_path(row + 1, col, lab, path, "D")
        find_path(row - 1, col, lab, path, "U")
        lab[row][col] = "-"

    path.pop()


n = int(input())
m = int(input())
labyrinth = [list(input()) for _ in range(n)]
find_path(0, 0, labyrinth , [], "")
