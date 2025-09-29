HISTORY_FILE = "history.txt"

# Show the calculation history
def show_history():
    with open(HISTORY_FILE, 'r') as file:
        lines = file.readlines()
    if len(lines) == 0:
        print("No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())

# Clear all history
def clear_history():
    with open(HISTORY_FILE, 'w'):
        pass
    print('History Cleared')

# Save one calculation to history
def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()

    if len(parts) != 3:
        print('Invalid input. Use format: number operator number (e.g. 8 + 8)')
        return

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers entered.")
        return

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("You can't divide any number by 0")
            return
        result = num1 / num2
    elif op == "%":
        if num2 == 0:
            print("You can't modulo by 0")
            return
        result = num1 % num2
    else:
        print("Invalid Operator. USE ONLY +, -, *, /, %")
        return

    if result == int(result):
        result = int(result)

    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print('---- SIMPLE CALCULATOR ----')
    print('Type a calculation like: 8 + 2')
    print('Type "history" to see past results')
    print('Type "clear" to erase history')
    print('Type "exit" to quit')

    while True:
        user_input = input("Enter calculation or command: ").strip().lower()
        
        if user_input == 'exit':
            print('Goodbye!')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()
