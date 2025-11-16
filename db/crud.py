import sqlite3

DB_NAME = 'quizes.db'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

def close():
    global conn, cursor
    cursor.close()
    conn.close()


def create_tables():
    open()


    cursor.execute("""CREATE TABLE IF NOT EXISTS quiz (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR, 
    description TEXT              
    )""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question VARCHAR,
    answer VARCAR,
    wrong1 VARCHAR,
    wrong2 VARCHAR,               
    wrong3 VARCHAR              
    )""")


    cursor.execute("""CREATE TABLE IF NOT EXISTS quiz_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER,
    question_id INTEGER,
    FOREIGN KEY (quiz_id) REFERENCES quiz (id),
    FOREIGN KEY (question_id) REFERENCES questions (id)          
    )""")

    conn.commit()
    close()
  
def add_quizes():
    open()

    quizes = [
        ("Тварини", "Перевір знання про тварин."),
        ("Космос", "Питання про планети й зорі."),
        ("Україна", "Що ти знаєш про нашу країну?"),
        ("Історія", "Події минулого світу."),
        ("Фільми", "Впізнай героїв і стрічки.")
    ]

    cursor.executemany("""INSERT INTO quiz(title, description) VALUES (?, ?)""", quizes)
    conn.commit()
    close()

def add_questions():
    open()
    questions = [
        # Тварини
        ("Яка тварина найбільша у світі?", "Синій кит", "Слон", "Жираф", "Білий ведмідь"),
        ("Яка тварина вміє літати?", "Кажан", "Кіт", "Слон", "Крокодил"),
        ("Скільки лап у павука?", "8", "6", "10", "4"),
        ("Яка тварина спить зимою?", "Ведмідь", "Лисиця", "Вовк", "Олень"),
        ("Яка тварина має довгу шию?", "Жираф", "Зебра", "Кенгуру", "Кіт"),

        # Космос
        ("Яка планета найближча до Сонця?", "Меркурій", "Земля", "Марс", "Венера"),
        ("Як називається наша галактика?", "Чумацький Шлях", "Андромеда", "Молочна Туманність", "Оріон"),
        ("Яка планета червона?", "Марс", "Юпітер", "Нептун", "Венера"),
        ("Що є центром Сонячної системи?", "Сонце", "Земля", "Місяць", "Марс"),
        ("Як називається супутник Землі?", "Місяць", "Фобос", "Деймос", "Титан"),

        # Україна
        ("Столиця України?", "Київ", "Львів", "Харків", "Одеса"),
        ("Національна страва України?", "Борщ", "Піца", "Суші", "Кебаб"),
        ("Яке море омиває південь України?", "Чорне", "Азовське", "Балтійське", "Каспійське"),
        ("Символ України?", "Тризуб", "Хрест", "Зірка", "Сонце"),
        ("Найбільша річка України?", "Дніпро", "Дністер", "Прут", "Тиса"),

        # Історія
        ("Хто був першим президентом України?", "Леонід Кравчук", "Віктор Ющенко", "Леонід Кучма", "Петро Порошенко"),
        ("У якому році почалася Друга світова війна?", "1939", "1941", "1914", "1945"),
        ("Яке місто було столицею Київської Русі?", "Київ", "Чернігів", "Новгород", "Полоцьк"),
        ("Хто відкрив Америку?", "Христофор Колумб", "Магеллан", "Кук", "Васко да Гама"),
        ("Де винайшли піраміди?", "Єгипет", "Рим", "Греція", "Індія"),

        # Фільми
        ("Хто головний герой у 'Шрек'?", "Шрек", "Фіона", "Осел", "Дракон"),
        ("Як звуть хлопчика з 'Гаррі Поттер'?", "Гаррі", "Рон", "Драко", "Дамблдор"),
        ("У якому мультфільмі є Елза?", "Холодне серце", "Моана", "Рапунцель", "Бембі"),
        ("Як звали лева з 'Король лев'?", "Сімба", "Муфаса", "Скар", "Нала"),
        ("У якому мультфільмі є риба Немо?", "У пошуках Немо", "Русалонька", "Океан", "Рибки 3D")
    ]

    cursor.executemany("""INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)""", questions)
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute("PRAGMA foreign_keys=on")
    action = input("Додати зв'язок? (y\n)")
    while action != "n":
        quiz_id = int(input("Введіть номер вікторини"))
        questions_id = int(input("Введіть номер запитання"))
        cursor.execute("""INSERT INTO quiz_questions (quiz_id, question_id) VALUES (?, ?)""", [quiz_id, questions_id])
        conn.commit()
        action = input("Додати зв'язок? (y\n)")
    close()

def main():
    # create_tables()
    # add_quizes()
    # add_questions()
    add_links()


main()