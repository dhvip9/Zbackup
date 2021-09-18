opt = ['+', '-', '*', 'x', '/', '^', '**', 'X', '_', '=', '(', ')', '[', ']', '%']   # | Opterators |
single_opt = ['!']                                                                   # |    List    |

print("""| | | | | |     | | | | |   | | | | |
  | |     | |   | |         | |      
  | |     | |   | | | |     | | | |  
  | |     | |   | |         | |      
| | | | | |     | | | | |   | | | | |""")
print("""-------------------------------------------------
 | Wellcome! To [ DEE ], The World Of MATHS    | 
 | Exit from 'DEE' Write [ exit ] in Lower Case|
-------------------------------------------------""")
print("1 . [ write Here ]")
count = 1  # for Sequence count

while True:
    user_input = str(input(">> "))

    # -----------------------------
    # for Exit
    if user_input == "exit":
        print("| ThankYou! For Visiting [ DEE Maths ] |")
        break
    else:
        # -----------------------------
        # Separate values and opterators
        numbers = [[], []]  # [0] for opterators, [1] for value
        for i in user_input:
            if i in single_opt:
                numbers[0].append(i)

            elif i in opt:
                numbers[0].append(i)
                numbers[1].append(" ")

            else:
                numbers[1].append(i)

        opterator = numbers[0]

        # -----------------------------
        # L.H.S. Number
        raw_value1 = ""
        for i in numbers[1]:
            if i != " ":
                raw_value1 += i
            else:
                break

        # -----------------------------
        # R.H.S Number
        raw_value2 = ""
        if opterator[0] in opt:
            rhs_num = numbers[1]
            reves_value2 = ""
            index = -1
            reves_index = -1

            for j in reversed(rhs_num):
                if j != " ":
                    reves_value2 += rhs_num[index]
                    index -= 1
                else:
                    break

            for i in reves_value2:
                raw_value2 += reves_value2[reves_index]
                reves_index -= 1

            value = [int(raw_value1), int(raw_value2)]

        else:
            value = [int(raw_value1)]

    # ------------------------------
    # working of operation
    while True:
        # Addition[+]
        if opterator[0] == "+":
            final_value_add = value[0] + value[1]
            print("=", final_value_add)
            print()
            count += 1  # for Sequence count
            print(count, ". [ Write Here ]")
            break

            # Subtraction[-]
        elif opterator[0] == "-":
            final_value_sub = value[0] - value[1]
            print("=", final_value_sub)
            print()
            count += 1  # for Sequence count
            print(count, ". [ Write Here ]")
            break

        if opterator[0] == "_":
            print("| WARNING! :- Use this [ - ]            |")
            print("| NOTE :- Write only operator not Number|")
            opterator[0] = str(input("]> "))

            # multiplication[*]
        if opterator[0] == "*" or opterator[0] == "x":
            final_value_multi = value[0] * value[1]
            print("=", final_value_multi)
            print()
            count += 1  # for Sequence count
            print(count, ". [ Write Here ]")
            break

        if opterator[0] == "X":
            print("| WARNING! :- Use [*] or Lower Case [x] |")
            print("| NOTE :- Write only operator not Number|")
            opterator[0] = str(input("]> "))

            # Division[/]
        if opterator[0] == "/":
            if value[1] == 0 or (value[0] == 0 and value[1] == 0):
                final_value_div = 0
                print("=", final_value_div)
                print("| WARNING! :- Zero [0] Cannot Divisible Any Number |")
                print()
                count += 1  # for Sequence count
                print(count, ". [ Write Here ]")
                break
            else:
                final_value_div = value[0] / value[1]
                print("=", final_value_div)
                print()
                count += 1  # for Sequence count
                print(count, ". [ Write Here ]")
                break

            # power or exponent[^]
        if opterator[0] == "^" or opterator[0] == "**":
            final_value_pow = value[0] ** value[1]
            print("=", final_value_pow)
            print()
            count += 1  # for Sequence count
            print(count, ". [ Write Here ]")
            break

            # factorial[!]
        if opterator[0] == "!":
            f = 1
            value_copy = value[0]
            final_value_fac = value[0]
            while f < value_copy:
                final_value_fac = final_value_fac * f
                f += 1
            print("=", final_value_fac)
            print()
            count += 1  # for Sequence count
            print(count, ". [ Write Here ]")
            break
