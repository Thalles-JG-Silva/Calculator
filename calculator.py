class Calculator:
    def __init__(self):
        self.current_input = ""

    def input(self, value):
        self.current_input += str(value)

    def clear(self):
        self.current_input = ""

    def calculate(self):
        try:
            result = eval(self.current_input)
            self.current_input = str(result)
            return result
        except Exception as e:
            self.current_input = ""
            return "Error"
