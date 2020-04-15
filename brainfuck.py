"""
 A simple brainfuck interpreter

"""


class BrainFuckVM:
    """The interpreter."""

    def __init__(self):
        self.blocks = [0] * 10
        self.pointer = 0
        self.jump_table = {}

    def parse(self, string):
        """Single pass parser to catch loops."""
        stack = []
        self.jump_table = {}
        for ip, ch in enumerate(string):
            if ch == '[':
                stack.append(ip)
            elif ch == ']':
                pos = stack.pop()
                self.jump_table[ip] = pos
                self.jump_table[pos] = ip

    def eval(self, string):
        """Evaluates a string."""

        self.parse(string)
        ip = 0

        while ip < len(string):
            ch = string[ip]
            ip += 1

            if ch == '+':
                self.blocks[self.pointer] += 1
            elif ch == '-':
                self.blocks[self.pointer] -= 1
            elif ch == '>':
                self.pointer += 1
            elif ch == '<':
                if self.pointer > 0:
                    self.pointer -= 1
            elif ch == '.':
                char = self.blocks[self.pointer]
                print(chr(char), end='')
            elif ch == ',':
                char = input()
                self.blocks[self.pointer] = ord(char)
            elif ch == '[':
                if self.blocks[self.pointer] == 0:
                    ip = self.jump_table[ip - 1] + 1
            elif ch == ']':
                ip = self.jump_table[ip - 1]

    def state(self):
        """Shows the state of the VM."""
        print()
        for i, val in enumerate(self.blocks):
            if self.pointer == i:
                print('[%s] ' % val, end='')
            else:
                print('%s ' % val, end='')


if __name__ == '__main__':
    bf = BrainFuckVM()
    bf.eval('++++>+++[<[->>+>+<<<]>>>[-<<<+>>>]<<-]')
    bf.state()
