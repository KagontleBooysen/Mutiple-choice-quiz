from Question import Question

question_prompts = [
    "How soon after an accident must it be reported?\n(a) At end of shift/tommorrow\n(b) On when you have the time\n(c) Immediately\n\n",
    "Who must the operator respond to when hand signals are given?\n(a) Anyone available\n(b) Nobody\n(c) Banksman\n\n",
    "How often must a competent person inspect the lifting tackle used in lifting operations?\n(a) Every six months\n(b) Every one month\n(c) Every three months\n\n",
    "Corrosion on a steel wire rope (SWR) is normally caused by?\n(a) Metal fatigue\n(b) Broken wires\n(c) Lack of lubrication\n(d) High speed operation\n\n",
    "What is the maximum sling angle permitted in lifting operations?\n(a) 180 deg\n(b) 60 deg\n(c) 120 deg\n(d) 30 deg\n\n",
    "How can the safe working load (SWL) of a sling be determined?\n(a) Ask the supervisor\n(b) On the info tags or stamped on the ferrule\n(c) Contact the manufacturer\n\n",
    "When constructing a Tripod what is distance from the center to load and the lowbed?\n(a) 770mm\n(b) 650mm\n(c) 400mm\n(d) 385mm\n\n",
    "How is the Portuguese knot constructed in A-Frame?\n(a) Becket hitch two round turns and figure of eight\n(b) rolling bowline seven half hitches and two round turns\n(c) Glove hitch three half hitches outside 14-18 turns and inside 5-9 turns and then glove hitch and three half hitches\n\n",     
    "What is the space created by two snatch blocks when lowering the load from the tower to the ground is called?\n(a) Idle of the spaces\n(b) Thimble spheres\n(c) Vertex of the paradox\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "c"),
    Question(question_prompts[5], "b"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " Correct")

run_test(questions)
