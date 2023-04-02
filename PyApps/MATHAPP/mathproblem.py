class MathProblem:
    def __init__(self, lhs, rhs, operator=''):
        self.lhs = lhs
        self.rhs = rhs
        self.operator = operator
        
    def getLHS(self):
        return self.lhs
    
    def getRHS(self):
        return self.rhs
    
    def getOperator(self):
        return self.operator
    
    def setLHS(self, value):
        if self.lhs  != value:
            self.lhs = value
            return True
        else:
            return False
    
    def setRHS(self, value):
        if self.rhs != value:
            self.rhs = value
            return True
        else:
            return False
    
    def setOperator(self, value):
        if self.operator != value:
            self.operator = value
            return True
        else:
            return False
        
    def getString(self):
        return ""
    def checkAnswer(self,ans):
        return False
