from typing import List, Tuple

class First:
    file_path = "input.txt"

    def solve(self) -> int:
        first_col, second_col = self.read_in_file()
        distance = self.calculate_distance(first_col, second_col)
        return distance

    def read_in_file(self) -> Tuple[List[int], List[int]]:
        first_column = []
        second_column = []

        with open(self.file_path, 'r') as file:
            lines = file.read().strip().split("\n")
        for line in lines:
            first_column.append(int(line.split()[0]))
            second_column.append(int(line.split()[1]))
        return first_column, second_column

    @staticmethod
    def calculate_distance(first_col: List[int], second_col: List[int]) -> int:
        distance = 0
        sorted_first = sorted(first_col)
        sorted_second = sorted(second_col)

        for i in range(len(sorted_first)):
            distance += abs(sorted_first[i] - sorted_second[i])
        return distance


first = First()
print(first.solve())
