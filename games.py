#Hangman
import random

#const
HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O  |
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   |
|   |
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
|
--------
"""
)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("СТОЛОВАЯ", "РЕСТОРАН", "ШКОЛА", "СПРАВКА", "АНЕКДОТ", "ЗАВТРАК", "БИЗНЕС")
#инициализация переменных
word = random.choice(WORDS) #слово, которое нужно будет угадывать
so_far = "-" * len(word) #по дному дефису на каждую букву, которую нужно отгадать
wrong = 0 #количество ошибок, которые сделал игрок
used = [] #буквы, которые игрок уже отгадал
#основной цикл
print("\t\tДобро пожаловать в игру 'Виселица'!")
print(
"""
Сейчас я загадаю слово, а вы  должны будете по буквам его угадать.
Вы будете предлагать по одной букве, если эта буква есть в моем слове, то
я открою вам ее положение в слове. Если же нет, то я буду дорисовывать человечка
на виселица.
Игра будет длиться до тех пор, пока вы не отгадаете слово, либо пока человечек не
полностью повешен.
Итак, осталось, только пожелать вам удачи, ведь от вас зависит судьба, несчастного
рисованного человечка!
"""
)
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже предлагали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
    #пользовательский ввод
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Вы уже предлагали букву: ", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)
    #проверка наличия буквы в слове
    if guess in word:
        print("\nДа! Буква", guess, "есть в слове!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nК сожалению, буквы", guess, "нет в слове.")
        wrong += 1
#завершение игры
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nЧеловеска повесили!")
else:
    print("\nВы отгадали!")
print("\nБыло загаданно слово", word, ".")
input("\n\nPress ENTER to EXIT.")