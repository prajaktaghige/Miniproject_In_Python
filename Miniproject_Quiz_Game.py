def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    answer = int(input("Choose an option (number): "))
    return answer == correct_option

def main():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Madrid"],
            "correct_option": 1
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_option": 2
        }
    ]
    
    score = 0
    for q in questions:
        if ask_question(q['question'], q['options'], q['correct_option']):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    
    print(f"Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
