stack = list()
memory = list()
memory_addresses = list()
memory_values = list()                                                                  # list initialization
instruction_tuple = ('PUSHI value', 'PUSH address', 'POP address', 'PRINT', 'ADD',
                     'SUB', 'MUL', 'INPUT', 'DIV', 'SWAP', 'DROP', 'DUP', 'HLT')
for i in range(0, 256):    # fill up the memory
    memory.append('')


def pushi(n):    # add values to stack

    try:  # if the value is not float/int
        if len(stack) <= 15:   # check if the stack is full
            n = float(n)
            stack.append(n)
            print(f'Value < {n} > added to the stack successfully.')
        else:
            print(f'\nSTACK OVERFLOW ERROR! Remove an item from the stack.\n')   # if the list is full
    except ValueError:
        print(f'{instruction[1]} is not a valid value.')


def push(address):  # move values from the memory to the stack

    try:
        dec_address = int(address, base=16)
        if len(stack) <= 15:
            if memory[dec_address] == '':
                print('Empty memory slot.')
            else:
                memory_addresses.append(hex(dec_address))
                memory_values.append(0)
                stack.append(memory[dec_address])
                memory[dec_address] = ''
                print(f'Value <{stack[-1]}> added to the stack successfully.')
        else:
            print(f'\nSTACK OVERFLOW ERROR! Remove an item from the stack.\n')
    except IndexError:  # non existent address
        print('This address does not exist in the memory.')
    except ValueError:  # not hexadecimal
        print(f'{instruction[1]} is not a valid hexadecimal value.')


def _pop(address):  # move values from the stack to the memory

    try:
        dec_address = int(address, base=16)
        if len(memory) <= 256:
            memory[dec_address] = stack[-1]
            del stack[-1]
            print(f'Value <{memory[dec_address]}> added to {hex(dec_address)} memory slot.')
            memory_addresses.append(hex(dec_address))
            memory_values.append(memory[dec_address])
        else:
            print(f'\nSTACK OVERFLOW ERROR! Remove an item from the memory.\n')

    except ValueError:  # if is not hexadecimal
        print(f'{instruction[1]} is not a valid hexadecimal value')

    except IndexError:
        if len(stack) == 0:  # if the stack is empty
            print('The stack is empty.')
        else:  # no existent address
            print('Address not found in memory.')


while True:  # main program

    instruction = list(map(str, input('\n>>').upper().split()))

    if len(instruction) == 2:

        if instruction[0] == 'PUSHI':  # add values to stack
            pushi(instruction[1])
            instruction.clear()

        elif instruction[0] == 'PUSH':  # move values from the memory to the stack
            push(instruction[1])
            instruction.clear()

        elif instruction[0] == 'POP':  # move values from the stack to the memory
            _pop(instruction[1])
            instruction.clear()

        else:
            print(f'ERROR. Invalid operation.')  # if user type non-existent operation
            print('Type help to show operations list\n')
    elif len(instruction) == 1:

        if instruction[0] == 'INPUT':  # read float value
            value = str(input('>>> '))
            try:  # check if value is float
                value = float(value)
                stack.append(value)
                print(f'Value {value} added to the stack successfully.')
            except ValueError:
                print(f'{value} is not a valid value.')

        elif instruction[0] == 'PRINT':  # remove and show the top of the stack
            try:  # check if the stack is empty
                print(stack[-1])
                stack.pop()
            except IndexError:
                print('The stack is empty.')

        elif instruction[0] == 'ADD':  # sum the two last elements of the stack and remove them
            try:  # check if the stack have more than 1 value
                value = stack[len(stack) - 2] + stack[len(stack) - 1]
                if len(stack) > 1:
                    del stack[len(stack) - 1]
                    del stack[len(stack) - 1]
                    stack.append(value)
                else:
                    print('Not enough values in the stack.')
            except IndexError:
                print('Not enough values in the stack.')

        elif instruction[0] == 'SUB':  # subtract the two last elements of the stack and remove them
            try:  # check if the stack have more than 1 value
                value = stack[len(stack) - 2] - stack[len(stack) - 1]
                if len(stack) > 1:
                    del stack[len(stack) - 1]
                    del stack[len(stack) - 1]
                    stack.append(value)
                else:
                    print('Not enough values in the stack.')
            except IndexError:
                print('Not enough values in the stack.')

        elif instruction[0] == 'MUL':  # multiply the two last elements of the stack and remove them
            try:  # check if the stack have more than 1 value
                value = stack[len(stack) - 2] * stack[len(stack) - 1]
                if len(stack) > 1:
                    del stack[len(stack) - 1]
                    del stack[len(stack) - 1]
                    stack.append(value)
                else:
                    print('Not enough values in the stack.')
            except IndexError:
                print('Not enough values in the stack.')

        elif instruction[0] == 'DIV':  # divide the two last elements of the stack and remove them
            try:  # check if the stack have more than 1 value and if the divisor is 0
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

        elif instruction[0] == 'SWAP':  # swap the two last elements of the stack
            if len(stack) >= 2:  # check if the stack have more than 1 value
                stack[len(stack) - 2], stack[len(stack) - 1] = stack[len(stack) - 1], stack[len(stack) - 2]
            else:
                print('Not enough values in the stack.')

        elif instruction[0] == 'DROP':  # remove the last element of the stack
            if len(stack) >= 1:  # check if the stack is empty
                print(f'Value < {stack[-1]} > removed from the stack.')
                stack.pop()
            else:
                print('Not enough values in the stack.')

        elif instruction[0] == 'DUP':  # duplicates the last element of the stack
            if len(stack) > 0:  # check if the stack is empty
                stack.append(stack[-1])
            else:
                print('Not enough values in the stack.')

        elif instruction[0] == 'HLT':  # close application
            print(f'\nSTACK')  # prints the stack
            for element in stack:
                print(f'| {element} |', end='')
            print('\n\nMEMORY OPERATIONS'  # prints memory operations
                  '\n------------------------')
            for i, addresss in enumerate(memory_addresses):
                print(f'{addresss}', end='')
                index = memory_addresses.index(addresss, i)
                print(f'               {memory_values[index]}')
            break
        elif instruction[0] == 'HELP':  # help operation
            for instruction in instruction_tuple:
                print(instruction)
        else:
            print('ERROR. Invalid operation.')  # check if is a valid operation
            instruction.clear()
