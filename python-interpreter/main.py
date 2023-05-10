stack = list()
memory_stack = list()
for i in range(0, 256):
    memory_stack.append('')


def pushi(n):

    while True:
        try:
            if len(stack) <= 15:
                n = float(n)
                stack.append(n)
                print(f'Value < {n} > added to the stack successfully.')
                break
            else:
                print(f'\nSTACK OVERFLOW ERROR! Remove an item from the stack.\n')
                break
        except ValueError:
            print(f'{instruction[1]} is not a valid value.')
            break


def push(address):

    try:
        dec_address = int(address, base=16)
        if len(stack) <= 15:
            if memory_stack[dec_address] == '':
                print('Empty memory slot.')
            else:
                stack.append(memory_stack[dec_address])
                memory_stack[dec_address] = ''
                print(f'Value <{stack[-1]}> added to the stack successfully.')
        else:
            print(f'\nSTACK OVERFLOW ERROR! Remove an item from the stack.\n')
    except IndexError:
        print('This address does not exist in the memory.')
    except ValueError:
        print(f'{instruction[1]} is not a valid hexadecimal value.')


def _pop(address):
    while True:
        try:
            dec_address = int(address, base=16)
            if len(memory_stack) <= 256:
                memory_stack[dec_address] = stack[-1]
                del stack[-1]
                print(f'Value <{memory_stack[dec_address]}> added to {hex(dec_address)} memory slot.')
                break
            else:
                print(f'\nSTACK OVERFLOW ERROR! Remove an item from the memory.\n')
                break
        except ValueError:
            print(f'{instruction[1]} is not a valid hexadecimal value')
            break
        except IndexError:
            if len(stack) == 0:
                print('The stack is empty.')
                break
            else:
                print('Address not found in memory.')
                break


while True:

    print(stack)
    print(memory_stack)
    print(len(memory_stack))
    instruction = list(map(str, input('\n>>').upper().split()))

    if len(instruction) == 2:

        if instruction[0] == 'PUSHI':
            pushi(instruction[1])
            instruction.clear()

        elif instruction[0] == 'PUSH':
            push(instruction[1])
            instruction.clear()

        elif instruction[0] == 'POP':
            _pop(instruction[1])
            instruction.clear()

        else:
            print(f'ERROR. Invalid operation.')

    elif len(instruction) == 1:

        if instruction[0] == 'INPUT':
            value = str(input('>>> '))
            try:
                value = float(value)
                stack.append(value)
                print(f'Value {value} added to the stack successfully.')
            except ValueError:
                print(f'{value} is not a valid value.')

        elif instruction[0] == 'PRINT':
            try:
                print(stack[-1])
                stack.pop()
            except IndexError:
                print('The stack is empty.')

        elif instruction[0] == 'ADD':
            try:
                value = stack[len(stack) - 2] + stack[len(stack) - 1]
                if len(stack) > 1:
                    del stack[len(stack) - 1]
                    del stack[len(stack) - 1]
                    stack.append(value)
                else:
                    print('Not enough values in the stack.')
            except IndexError:
                print('Not enough values in the stack.')

        elif instruction[0] == 'SUB':
            try:
                value = stack[len(stack) - 2] - stack[len(stack) - 1]
                if len(stack) > 1:
                    del stack[len(stack) - 1]
                    del stack[len(stack) - 1]
                    stack.append(value)
                else:
                    print('Not enough values in the stack.')
            except IndexError:
                print('Not enough values in the stack.')

        elif instruction[0] == 'MUL':
            try:
                value = stack[len(stack) - 2] * stack[len(stack) - 1]
                if len(stack) > 1:
                    del stack[len(stack) - 1]
                    del stack[len(stack) - 1]
                    stack.append(value)
                else:
                    print('Not enough values in the stack.')
            except IndexError:
                print('Not enough values in the stack.')

        elif instruction[0] == 'DIV':
            try:
                value = stack[len(stack) - 2] / stack[len(stack) - 1]
                if len(stack) > 1:
                    del stack[len(stack) - 1]
                    del stack[len(stack) - 1]
                    stack.append(value)
                else:
                    print('Not enough values in the stack.')
            except IndexError:
                print('Not enough values in the stack.')
            except ZeroDivisionError:
                print('ZERO_DIVISION_ERROR')

        elif instruction[0] == 'SWAP':
            if len(stack) >= 2:
                stack[len(stack) - 2], stack[len(stack) - 1] = stack[len(stack) - 1], stack[len(stack) - 2]
            else:
                print('Not enough values in the stack.')

        elif instruction[0] == 'DROP':
            if len(stack) >= 1:
                print(f'Value < {stack[-1]} > removed from the stack.')
                stack.pop()
            else:
                print('Not enough values in the stack.')

        elif instruction[0] == 'DUP':
            if len(stack) > 0:
                stack.append(stack[-1])
            else:
                print('Not enough values in the stack.')

        elif instruction[0] == 'HLT':
            print('CLOSING APPLICATION...')
            break
        else:
            print('ERROR. Invalid operation.')
            instruction.clear()
