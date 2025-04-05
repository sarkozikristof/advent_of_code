from typing import List, Dict, Tuple

class Second:
    file_path = "input.txt"

    def solve(self) -> int:
        first_col, second_col = self.read_in_file()
        similarity_score = self.get_similarity_score(first_col, second_col)
        return similarity_score

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
    def refactor_list_to_dict(value_list) -> Dict[int, int]:
        dic = {}
        for value in value_list:
            if value in dic:
                dic[value] += 1
            else:
                dic[value] = 1
        return dic

    def get_similarity_score(self, fist_col: List[int], second_col: List[int]) -> int:
        similarity_score = 0
        second_dict = self.refactor_list_to_dict(second_col)

        for value in fist_col:
            if value in second_dict:
                similarity_score += value * second_dict[value]
        return similarity_score


second = Second()
print(second.solve())
