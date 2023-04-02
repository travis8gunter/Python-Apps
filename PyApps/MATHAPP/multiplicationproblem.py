from mathproblem import MathProblem


class MultiplicationProblem(MathProblem):
    def __init__(self, lhs, rhs):
        super().__init__(lhs, rhs)
        self.setOperator("*")
        
    def getString(self):
        return f"{self.lhs} * {self.rhs}"

    def checkAnswer(self, ans):
        return ans == self.lhs * self.rhs


