# MECHATRONICS SKILLS CHALLENGE
# A simple Python quiz app for Mechatronics Engineering students.

import random

question_bank = {
    "1": {
        "topic": "Electronics",
        "questions": [
            {
                "question": "Which component is used to store electrical charge?",
                "options": ["A. Resistor", "B. Capacitor", "C. Fuse", "D. Switch"],
                "answer": "B",
                "explanation": "A capacitor stores electrical charge in an electric field."
            },
            {
                "question": "What is the unit of electrical resistance?",
                "options": ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"],
                "answer": "C",
                "explanation": "Electrical resistance is measured in ohms (Ω)."
            },
            {
                "question": "Which device protects a circuit from excessive current?",
                "options": ["A. Fuse", "B. LED", "C. Capacitor", "D. Sensor"],
                "answer": "A",
                "explanation": "A fuse breaks the circuit when current becomes too high."
            },
            {
                "question": "Which instrument is used to measure voltage?",
                "options": ["A. Ammeter", "B. Voltmeter", "C. Thermometer", "D. Tachometer"],
                "answer": "B",
                "explanation": "A voltmeter measures potential difference (voltage)."
            },
            {
                "question": "What does an LED produce when current flows through it correctly?",
                "options": ["A. Light", "B. Sound", "C. Pressure", "D. Motion"],
                "answer": "A",
                "explanation": "LED means Light Emitting Diode; it produces light."
            }
        ]
    },
    "2": {
        "topic": "Sensors and Actuators",
        "questions": [
            {
                "question": "What is the main job of a sensor?",
                "options": ["A. Detect a physical condition", "B. Store programs", "C. Supply fuel", "D. Increase resistance"],
                "answer": "A",
                "explanation": "A sensor detects a physical condition and provides a signal."
            },
            {
                "question": "Which sensor is commonly used to detect temperature?",
                "options": ["A. Thermistor", "B. LDR", "C. Microphone", "D. Limit switch"],
                "answer": "A",
                "explanation": "A thermistor changes resistance as temperature changes."
            },
            {
                "question": "Which component can convert electrical energy into rotational motion?",
                "options": ["A. Resistor", "B. Electric motor", "C. Fuse", "D. Diode"],
                "answer": "B",
                "explanation": "An electric motor converts electrical energy into mechanical rotation."
            },
            {
                "question": "What does an LDR respond to?",
                "options": ["A. Light intensity", "B. Sound level", "C. Water pressure", "D. Speed"],
                "answer": "A",
                "explanation": "An LDR is a light-dependent resistor; its resistance changes with light."
            },
            {
                "question": "In a control system, an actuator is mainly used to do what?",
                "options": ["A. Carry out a physical action", "B. Display a password", "C. Store data permanently", "D. Measure resistance only"],
                "answer": "A",
                "explanation": "An actuator produces an action, such as movement, from a control signal."
            }
        ]
    },
    "3": {
        "topic": "Automation and PLC",
        "questions": [
            {
                "question": "What is the full meaning of PLC?",
                "options": ["A. Power Line Circuit", "B. Programmable Logic Controller", "C. Program Load Control", "D. Process Level Computer"],
                "answer": "B",
                "explanation": "PLC stands for Programmable Logic Controller."
            },
            {
                "question": "Which part of a PLC receives signals from sensors and switches?",
                "options": ["A. Output module", "B. Input module", "C. Power shaft", "D. Display screen"],
                "answer": "B",
                "explanation": "The input module receives signals from field devices."
            },
            {
                "question": "Which PLC section sends control signals to motors or lamps?",
                "options": ["A. Output module", "B. Input module", "C. Memory card only", "D. Sensor casing"],
                "answer": "A",
                "explanation": "The output module sends signals to devices such as motors and lamps."
            },
            {
                "question": "What is the purpose of a ladder diagram?",
                "options": ["A. To draw building plans", "B. To program control logic", "C. To measure temperature", "D. To charge a battery"],
                "answer": "B",
                "explanation": "Ladder logic is a graphical programming language used with PLCs."
            },
            {
                "question": "In an automatic system, what does feedback help the controller do?",
                "options": ["A. Compare actual output with desired output", "B. Remove every sensor", "C. Stop all input signals", "D. Increase wire length"],
                "answer": "A",
                "explanation": "Feedback provides information about the output for comparison and correction."
            }
        ]
    },
    "4": {
        "topic": "Mechanical Systems",
        "questions": [
            {
                "question": "Which machine element is used to transmit rotary motion between shafts?",
                "options": ["A. Gear", "B. Fuse", "C. Thermistor", "D. Diode"],
                "answer": "A",
                "explanation": "Gears transmit rotary motion and torque between shafts."
            },
            {
                "question": "What is the SI unit of torque?",
                "options": ["A. Joule", "B. Newton metre", "C. Pascal", "D. Ampere"],
                "answer": "B",
                "explanation": "Torque is measured in newton metres (N m)."
            },
            {
                "question": "Which component supports a rotating shaft and reduces friction?",
                "options": ["A. Bearing", "B. Spring", "C. Piston ring", "D. Gasket"],
                "answer": "A",
                "explanation": "A bearing supports a shaft and helps reduce friction."
            },
            {
                "question": "What is the main function of a spring?",
                "options": ["A. Store mechanical energy", "B. Measure voltage", "C. Produce electrical signals", "D. Control current"],
                "answer": "A",
                "explanation": "A spring stores mechanical energy when it is deformed."
            },
            {
                "question": "Which transmission component connects and disconnects engine power from the gearbox?",
                "options": ["A. Clutch", "B. Radiator", "C. Alternator", "D. Spark plug"],
                "answer": "A",
                "explanation": "The clutch engages and disengages power transmission from the engine."
            }
        ]
    }
}

def get_choice(prompt, valid_choices):
    """Get and validate a menu choice from the user."""
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please select one of the options shown.")

def show_topics():
    print("\nCHOOSE A MECHATRONICS TOPIC")
    print("1. Electronics")
    print("2. Sensors and Actuators")
    print("3. Automation and PLC")
    print("4. Mechanical Systems")

def run_quiz():
    print("=" * 42)
    print("       MECHATRONICS SKILLS CHALLENGE")
    print("=" * 42)

    name = input("Enter your name: ").strip()
    if name == "":
        name = "Student"

    show_topics()
    topic_choice = get_choice(
        "\nEnter the number of your chosen topic: ",
        ["1", "2", "3", "4"]
    )

    selected_topic = question_bank[topic_choice]
    questions = selected_topic["questions"][:]
    random.shuffle(questions)

    score = 0
    missed_questions = []

    print("\nHello", name + "!")
    print("Topic:", selected_topic["topic"])
    print("You will answer 5 questions. Good luck!\n")

    for number, item in enumerate(questions, start=1):
        print("-" * 42)
        print("Question", number, "of", len(questions))
        print(item["question"])

        for option in item["options"]:
            print(option)

        answer = get_choice("Your answer (A/B/C/D): ", ["A", "B", "C", "D"])

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Not quite.")
            missed_questions.append(item)
            print("Correct answer:", item["answer"])

        print("Learning note:", item["explanation"])

    percentage = (score / len(questions)) * 100

    print("\n" + "=" * 42)
    print("             QUIZ RESULT")
    print("=" * 42)
    print("Student:", name)
    print("Topic:", selected_topic["topic"])
    print("Score:", str(score) + "/" + str(len(questions)))
    print("Percentage:", str(round(percentage, 1)) + "%")

    if percentage >= 80:
        print("Remark: Excellent work!")
    elif percentage >= 50:
        print("Remark: Good effort. Keep practising.")
    else:
        print("Remark: More practice will help you improve.")

    if missed_questions:
        print("\nTOPICS TO REVISE")
        for item in missed_questions:
            print("- " + item["question"])
    else:
        print("\nPerfect score! You answered every question correctly.")

    print("\nThank you for using Mechatronics Skills Challenge.")

def main():
    while True:
        run_quiz()
        again = get_choice("\nWould you like to try another topic? (Y/N): ", ["Y", "N"])
        if again == "N":
            print("Goodbye. Keep learning Mechatronics!")
            break

if __name__ == "__main__":
    main()
