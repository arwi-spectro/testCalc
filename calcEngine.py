"""Stores Backend engines for the calculator"""


class BasicEngine:
    """Evaluates the string using BODMAS"""

    def __init__(self):
        """Create mappings to operators and methods"""
        self.expressions = ["+", "-", "*", "/"]
        self.exp_dict = {
            "+": self.solve_add,
            "-": self.solve_subtract,
            "/": self.solve_div,
            "*": self.solve_multiply,
        }

    def solve_div(self, val1, val2):
        """divides two arguments"""
        return float(val1) / float(val2)

    def solve_add(self, val1, val2):
        """adds two arguments"""
        return float(val1) + float(val2)

    def solve_multiply(self, val1, val2):
        """Multiply two arguments"""
        return float(val1) * float(val2)

    def solve_subtract(self, val1, val2):
        """Subtract two arguments"""
        return float(val1) - float(val2)

    def evaluate_div(self, list_exp):
        """Parse and evaluate expressions based on signs"""
        while True:
            if "/" in list_exp:
                list_exp = self.remove_exp(list_exp, "/")
            else:
                break
        while True:
            if "*" in list_exp:
                list_exp = self.remove_exp(list_exp, "*")
            else:
                break
        while True:
            if "+" in list_exp:
                list_exp = self.remove_exp(list_exp, "+")
            else:
                break
        while True:
            if "-" in list_exp:
                list_exp = self.remove_exp(list_exp, "-")
            else:
                break

        return list_exp

    def remove_exp(self, list_exp, exp):
        """Remove the expressions by overwriting"""
        for count in range(len(list_exp)):
            if list_exp[count] == exp:
                val1 = list_exp[count - 1]
                val2 = list_exp[count + 1]
                res = self.exp_dict[exp](val1, val2)
                return self.overwrite_string(list_exp, res, count)

    def overwrite_string(self, list_exp, result, count):
        """Overwrite the expressions"""
        first_half = list_exp[: (count - 1)]
        second_half = list_exp[(count + 2) :]
        first_half.append(result)
        return first_half + second_half

    def make_list(self, exp_str):
        """convert the expression string into a list of operands
        and operators
        """
        temp = ""
        output = []
        for item in exp_str:
            if item in self.expressions:
                output.append(temp)
                output.append(item)
                temp = ""
            else:
                temp += item
        value = ""
        for item in reversed(exp_str):

            if item in self.expressions:
                value = value[::-1]
                break
            else:
                value += item
        output.append(value)
        return output

    def evaluate(self, exp_string):
        """Evaluate the string"""
        a = self.make_list(exp_string)
        exp_string = self.evaluate_div(a)

        return str(exp_string[0])


if __name__ == "__main__":
    engine = BasicEngine()
