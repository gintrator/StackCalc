import readline

VALID_OPS = ['=', '+', '-', '*', '/', 'c', 'p']


class StackCalcException(Exception):    
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


class StackCalculator(object):

    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return " ".join(str(i) for i in self.stack)

    def evaluate(self, command):
        item = self.coerce_to_num(command)
        if item is not None:
            self.stack.append(item)
        else:
            self.evaluate_op(command)
        	
    def evaluate_op(self, op):
        if op not in VALID_OPS:
            raise StackCalcException("Unknown op: {0}.".format(op))
        if len(self.stack) == 0:
            raise StackCalcException("Empty stack.")
        if op == '=':
            print(self.stack.pop())
            return
        if op == 'c':
            self.stack = []
            return
        if op == 'p':
            print("Stack: {0}".format(self))
            return
        if len(self.stack) < 2:
            raise StackCalcException("Not enough operands.")
        if op == '+':
            self.stack.append(self.stack.pop() + self.stack.pop())
        if op == '-':
            self.stack.append(self.stack.pop() - self.stack.pop())
        if op == '*':
            self.stack.append(self.stack.pop() * self.stack.pop())
        if op == '/':
            self.stack.append(self.stack.pop() / self.stack.pop())

    def coerce_to_num(self, item):
        try:
            return int(item)
        except ValueError:
            try:
                return float(item)
            except ValueError:
                return None


def main():
    try:
        calc = StackCalculator()
        print("Stack Calculator. Valid ops: {0}.".format(' '.join(VALID_OPS)))
        while True:
            try:
                calc_input = input("calc> ")
                calc_input = calc_input.split()
                for command in calc_input:
                    output = calc.evaluate(command)
                    #print("stack: {0}".format(calc))
            except StackCalcException as e:
                print(e.value)
    except EOFError:
        print("\nGoodbye")

main()

        
