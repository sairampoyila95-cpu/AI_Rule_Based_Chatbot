# ==================================================
# Rule-Based AI Chatbot
# DecodeLabs AI Project 1
# Developed by Keerthi Ranga
# ==================================================

print("=" * 60)
print("🤖 WELCOME TO RULE-BASED AI CHATBOT")
print("=" * 60)
print("Type 'help' to see available commands.")
print("Type 'exit' to close the chatbot.")
print("=" * 60)

while True:

    user = input("\nYou: ").lower().strip()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # Good Morning
    elif "good morning" in user:
        print("Bot: Good Morning! Have a productive day.")

    # Good Night
    elif "good night" in user:
        print("Bot: Good Night! Sweet dreams.")

    # Asking Name
    elif "your name" in user:
        print("Bot: My name is RuleBot.")

    # Who Are You
    elif "who are you" in user:
        print("Bot: I am a Rule-Based AI Chatbot created using Python.")

    # How Are You
    elif "how are you" in user:
        print("Bot: I am doing great. Thank you for asking!")

    # Creator
    elif "who created you" in user:
        print("Bot: I was created using Python and rule-based logic.")

    # AI
    elif user == "ai":
        print("Bot: AI stands for Artificial Intelligence.")

    # Machine Learning
    elif "machine learning" in user:
        print("Bot: Machine Learning is a branch of AI that allows systems to learn from data.")

    # Data Science
    elif "data science" in user:
        print("Bot: Data Science involves analyzing and interpreting data to gain insights.")

    # Python
    elif user == "python":
        print("Bot: Python is one of the most popular programming languages used in AI.")

    # Programming
    elif "programming" in user:
        print("Bot: Programming is the process of writing instructions for computers.")

    # Skills
    elif "skills" in user:
        print("Bot: Important skills include Python, Communication, Problem Solving, and AI concepts.")

    # Course
    elif "course" in user:
        print("Bot: Python, Artificial Intelligence, Machine Learning, and Data Science are excellent courses.")

    # Internship
    elif "internship" in user:
        print("Bot: Internships help you gain practical experience and improve your resume.")

    # Career
    elif "career" in user:
        print("Bot: Build projects, learn new skills, and stay consistent to grow your career.")

    # Weather
    elif "weather" in user:
        print("Bot: Sorry, I cannot check live weather information.")

    # Date
    elif "date" in user:
        print("Bot: Sorry, I cannot access the current date.")

    # Time
    elif "time" in user:
        print("Bot: Sorry, I cannot access real-time information.")

    # Favourite Color
    elif "favorite color" in user:
        print("Bot: My favorite color is blue.")

    # Favourite Food
    elif "favorite food" in user:
        print("Bot: Robots don't eat food, but I like data!")

    # Joke
    elif "joke" in user:
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    # Motivation
    elif "motivate me" in user:
        print("Bot: Success comes from continuous learning and practice. Keep going!")

    # Fun Fact
    elif "fun fact" in user:
        print("Bot: Ada Lovelace is considered the world's first computer programmer.")

    # Thank You
    elif "thank you" in user or "thanks" in user:
        print("Bot: You're welcome! 😊")

    # Help Command
    elif user == "help":
        print("""
================ AVAILABLE COMMANDS ================

Greetings:
- hi
- hello
- hey

General:
- who are you
- your name
- how are you
- who created you

Technology:
- ai
- machine learning
- data science
- python
- programming

Career:
- skills
- course
- internship
- career

Fun:
- joke
- motivate me
- fun fact
- favorite color
- favorite food

Utilities:
- weather
- date
- time

Others:
- good morning
- good night
- thank you

Exit:
- exit
- bye
- quit

====================================================
        """)

    # Exit Commands
    elif user in ["exit", "bye", "quit"]:
        print("Bot: Goodbye! Have a great day. 👋")
        break

    # Default Response
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")