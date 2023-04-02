import random
from additionproblem import AdditionProblem
from multiplicationproblem import MultiplicationProblem

def make_problems(min_value, max_value, num_problems):
    problems = []
    for i in range(num_problems):
        op = random.choice([AdditionProblem, MultiplicationProblem])
        lhs = random.randint(min_value, max_value)
        rhs = random.randint(min_value, max_value)
        problems.append(op(lhs, rhs))
    return problems
def check_problems(problems, answers):
    num_correct = 0
    for i, problem in enumerate(problems):
        if problem.checkAnswer(answers[i]):
            num_correct += 1
    return num_correct
