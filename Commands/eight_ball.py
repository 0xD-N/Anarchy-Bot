import random

def eight_ball() -> str:
    answers = ["no", "yes", "maybe", "depends", "doubtful", "it seems so", "it appears so", "certainly", "without a doubt",
               "unfortunately", "it is certain", "you may rely on it", "signs point to yes", "Reply hazy try again", "Better not tell you now",
               "Ask again later", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "My sources say no", "Very doubtful", "My reply is no"]

    return answers[random.randrange(0, len(answers))]