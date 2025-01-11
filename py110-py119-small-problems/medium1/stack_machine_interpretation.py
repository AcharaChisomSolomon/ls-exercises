def minilang(commands):
    stack = []
    register = 0

    commands = commands.split(' ')

    for command in commands:
        if command.lstrip('-').isnumeric():
            register = int(command)
        elif command == 'PUSH':
            stack.append(register)
        elif command == 'ADD':
            popped_value = stack.pop()
            register += popped_value
        elif command == 'SUB':
            popped_value = stack.pop()
            register -= popped_value
        elif command == 'MULT':
            popped_value = stack.pop()
            register *= popped_value
        elif command == 'DIV':
            popped_value = stack.pop()
            register //= popped_value
        elif command == 'REMAINDER':
            popped_value = stack.pop()
            register %= popped_value
        elif command == 'POP':
            register = stack.pop()
        elif command == 'PRINT':
            print(register)


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)