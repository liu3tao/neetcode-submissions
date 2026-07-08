class Solution:
    def checkDup(self, currNums: Set[str], newNums: List[str]) -> bool:
        for n in newNums:
            if n == '.':
                continue
            if n in currNums:
                # print(currNums, newNums, n)
                return True
            else:
                currNums.add(n)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(3)]
        for i in range(9):
            if self.checkDup(set(), board[i]):
                # print(i, 'row')
                return False
            if i == 3 or i == 6:
                for b in boxes:
                    b.clear()
            if self.checkDup(boxes[0], board[i][0:3]):
                # print(i, 'box0', boxes[0])
                return False
            if self.checkDup(boxes[1], board[i][3:6]):
                # print(i, 'box1', boxes[1])
                return False
            if self.checkDup(boxes[2], board[i][6:9]):
                # print(i, 'box2', boxes[2])
                return False
            for j in range(9):
                if self.checkDup(cols[j], [board[i][j]]):
                    # print(i, j, 'col', cols[j])
                    return False
        return True