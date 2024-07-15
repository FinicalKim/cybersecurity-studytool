# app/main.py
from services import generate_quiz_question, save_quiz_question, get_tutorials, get_labs
from models import User, session

def main_menu():
    print("Welcome to the Cybersecurity Study App!")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = session.query(User).filter_by(username=username, password_hash=password).first()

    if user:
        print(f"Welcome, {user.username}!")
        user_menu()
    else:
        print("Invalid credentials. Please try again.")
        login()

def register():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    user = User(username=username, email=email, password_hash=password)
    session.add(user)
    session.commit()

    print("Registration successful. You can now log in.")
    main_menu()

def user_menu():
    print("1. Take a Quiz")
    print("2. View Tutorials")
    print("3. View Labs")
    print("4. Logout")

    choice = input("Enter your choice: ")

    if choice == "1":
        take_quiz()
    elif choice == "2":
        view_tutorials()
    elif choice == "3":
        view_labs()
    elif choice == "4":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        user_menu()

def take_quiz():
    question = generate_quiz_question()
    print(f"Question: {question}")
    options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    correct_option = 1  # Placeholder for the correct option
    explanation = "Explanation of the answer."

    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    user_answer = int(input("Enter your answer (1-4): "))

    if user_answer == correct_option + 1:
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_option + 1}. {explanation}")

    save_quiz_question(question, options, correct_option, explanation)
    user_menu()

def view_tutorials():
    tutorials = get_tutorials()
    for tutorial in tutorials:
        print(f"Title: {tutorial.title}\nContent: {tutorial.content}\n")
    user_menu()

def view_labs():
    labs = get_labs()
    for lab in labs:
        print(f"Title: {lab.title}\nInstructions: {lab.instructions}\n")
    user_menu()

if __name__ == "__main__":
    main_menu()
