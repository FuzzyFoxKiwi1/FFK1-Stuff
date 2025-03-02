import random
import operator

# Define math operations
operations = {
    "add": ("+", operator.add),
    "sub": ("-", operator.sub),
    "mul": ("*", operator.mul),
    "div": ("/", operator.truediv),
    "any": ["+", "-", "*", "/"]
}

def generate_question(operation_choice, outcome_restriction):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    if operation_choice == "any":
        operation_symbol = random.choice(operations["any"])
        operation_func = operations[next(k for k, v in operations.items() if v[0] == operation_symbol)][1]
    else:
        operation_symbol, operation_func = operations[operation_choice]
    
    if outcome_restriction is not None:
        while True:
            result = operation_func(num1, num2)
            if outcome_restriction(result):
                break
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)

    question = f"What is {num1} {operation_symbol} {num2}?"
    answer = operation_func(num1, num2)
    return question, answer

def use_calculator():
    print("Calculator is available. Type 'exit' to leave the calculator.")
    while True:
        expression = input("Enter calculation: ")
        if expression.lower() == "exit":
            break
        try:
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

def settings_menu():
    print("Settings Menu:")
    operation_choice = input("Choose the type of math (add, sub, mul, div, any): ").lower()
    while operation_choice not in operations.keys():
        operation_choice = input("Invalid choice. Please choose (add, sub, mul, div, any): ").lower()

    outcome_restriction = None
    outcome_input = input("Do you want to restrict the outcome? (yes/no): ").lower()
    if outcome_input == "yes":
        min_value = float(input("Enter the minimum value: "))
        max_value = float(input("Enter the maximum value: "))
        outcome_restriction = lambda x: min_value <= x <= max_value

    num_questions_choice = input("Set the number of questions (random, minimum, maximum, fixed): ").lower()
    if num_questions_choice == "random":
        num_questions = random.randint(5, 20)
        print(f"Random number of questions: {num_questions}")
    elif num_questions_choice == "minimum":
        num_questions = 5
    elif num_questions_choice == "maximum":
        num_questions = 20
    elif num_questions_choice == "fixed":
        num_questions = int(input("Enter the fixed number of questions: "))
    else:
        num_questions = 10  # Default to 10 if invalid choice

    max_calculator_uses = int(input("Set the maximum number of calculator uses (0 for no limit): "))

    num_skips_choice = input("Set the number of skips (random, minimum, maximum, fixed): ").lower()
    if num_skips_choice == "random":
        num_skips = random.randint(1, num_questions)
        print(f"Random number of skips: {num_skips}")
    elif num_skips_choice == "minimum":
        num_skips = 1
    elif num_skips_choice == "maximum":
        num_skips = num_questions
    elif num_skips_choice == "fixed":
        num_skips = int(input("Enter the fixed number of skips: "))
    else:
        num_skips = 3  # Default to 3 if invalid choice

    return operation_choice, outcome_restriction, num_questions, max_calculator_uses, num_skips

def main():
    print("Welcome to the Math Quiz Game!")
    user_name = input("Enter your name: ")

    total_score = 0
    while True:
        operation_choice, outcome_restriction, num_questions, max_calculator_uses, num_skips = settings_menu()
        
        score = 0
        skipped = 0
        calculator_uses = 0
        
        for _ in range(num_questions):
            if skipped >= num_skips:
                print("No more skips left.\n")
                break

            question, answer = generate_question(operation_choice, outcome_restriction)
            print(question)
            user_answer = input("Your answer (type 'SKIP' to skip or 'CALC' to use the calculator): ")

            if user_answer.lower() == "skip":
                if skipped < num_skips:
                    print("Question skipped.\n")
                    skipped += 1
                    continue
                else:
                    print("No more skips allowed.\n")
                    continue

            elif user_answer.lower() == "calc":
                if max_calculator_uses == 0 or calculator_uses < max_calculator_uses:
                    use_calculator()
                    calculator_uses += 1
                    user_answer = input("Your answer (after using calculator): ")
                else:
                    print("Maximum calculator uses reached.\n")
                    continue

            try:
                user_answer = float(user_answer)
                if round(user_answer, 2) == round(answer, 2):
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer was {round(answer, 2)}.\n")
            except ValueError:
                print("Invalid input. Please enter a number.\n")
        
        total_score += score
        print(f"Quiz over! {user_name}'s final score for this quiz is {score}/{num_questions - skipped}. Questions skipped: {skipped}.")
        print(f"Total correct answers across all quizzes: {total_score}")
        print(f"Calculator was used {calculator_uses} times.")

        continue_input = input("Type 'Continue' to start a new quiz or anything else to exit: ").lower()
        if continue_input != "continue":
            break

    print("Thank you for playing! Goodbye!")

if __name__ == "__main__":
    main()
