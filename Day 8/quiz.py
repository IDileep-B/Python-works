

def run_quiz():
    questions = [
        {
            "question": "1. What is the output of: print(type([]))?",
            "options": ["A. <class 'list'>", "B. <class 'tuple'>", "C. <class 'dict'>", "D. <class 'set'>"],
            "answer": "A"
        },
        {
            "question": "2. Which of the following is immutable in Python?",
            "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
            "answer": "C"
        },
        {
            "question": "3. What will be the output of: bool('False')?",
            "options": ["A. True", "B. False", "C. None", "D. Error"],
            "answer": "A"
        },
        {
            "question": "4. Which keyword is used to create a function in Python?",
            "options": ["A. func", "B. def", "C. function", "D. lambda"],
            "answer": "B"
        },
        {
            "question": "5. What is the correct file extension for Python files?",
            "options": ["A. .pyth", "B. .pt", "C. .py", "D. .pyt"],
            "answer": "C"
        },
        
            "question" : "6.What is a correct syntax to output Hello World in Python?",
            "options":["A.echo Hello World","B.p(Hello world)","C.print Hello world","4.echo(Hello world)"]
            "answer": "C"
         
        {
            "question":"7.How do you insert COMMENTS in Python code?"
            "options":["A./*This is comment*/","B.#This is a comment","C.//This is a comment"]
            "answer":"B"

        }
    ]

    score = 0

    print("\n=== Python Quiz ===\n")
    for q in questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)

      
        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice. Please enter A, B, C, or D.")

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")

    print(f"Your final score: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Excellent! You got all correct!")
    elif score >= len(questions) // 2:
        print("👍 Good job! Keep practicing.")
    else:
        print("📚 You need more practice.")

if __name__ == "__main__":
    run_quiz()
