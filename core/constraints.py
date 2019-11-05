class Constraints:
    """Object constraints"""

    def __init__(self):
        self.isResult = False

    def evaluateExpression(self, expression):
        """Evaluate an expression."""
        try:
            result = str(eval(expression, {}, {}))
        except Exception as err:
            result = err

        return result
