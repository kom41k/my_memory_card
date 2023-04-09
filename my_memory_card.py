import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle, randint
from colorama import init, Fore
from colorama import Back
from colorama import Style

class Question():
    def __init__(
     self, question, right_answer,
     wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
red = '<span style="color:red;">{}</span>'
green = '<span style="color:green;">{}</span'
violet = '<span style="color:violet;">{}</span'
blue = '<span style="color:blue;">{}</span>'
lime = '<span style="color:lime;">{}</span'
orange = '<span style="color:orange;">{}</span'

questions_list = []
q1 = Question('Ты кто такой?','плахой','хароший','ну да','ну есть такое')
questions_list.append(q1)
q2 = Question('Ты плахой?','нет','да','кукушка','корова')
questions_list.append(q2)
q3 = Question('уверен?','неа','возможно','ну да','ну есть такое')
questions_list.append(q3)
q4 = Question('А я хароший?','нет','ага','кика','почка')
questions_list.append(q4)
q5 = Question('ARE YOU NORMAL?','да','нет','ну да','ну есть такое')
questions_list.append(q5)
q6 = Question('уверен?','неа','возможно','ну да','ну есть такое')
questions_list.append(q6)
q7 = Question('Ты кто такой?','плахой','хароший','ну да','ну есть такое')
questions_list.append(q7)
q8 = Question('Ты плахой?','да','нет','ну да','ну есть такое')
questions_list.append(q8)
q9 = Question('уверен?','неа','возможно','ну да','ну есть такое')
questions_list.append(q9)

init(autoreset=True)
app = QApplication([])





main_win = QWidget()
main_win.setWindowTitle('Memory card')
main_win.resize(600, 400)
button = QPushButton('Ответить')

lol = QLabel(orange.format('Правильно/Неправильно'))
lel = QLabel('')
lul = QLabel('')
question_ = QLabel('<b>Какой национальности не существует?</b>')
btn_answer1 = QRadioButton('вариант 1')
btn_answer2 = QRadioButton('вариант 2')
btn_answer3 = QRadioButton('вариант 3')
btn_answer4 = QRadioButton('вариант 4')
radiogroupbox = QGroupBox('Варианты ответов')
layout_main = QVBoxLayout()
h_line1 = QVBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line2.addWidget(btn_answer1)
h_line2.addWidget(btn_answer2)
h_line3.addWidget(btn_answer3)
h_line3.addWidget(btn_answer4)
h_line1.addLayout(h_line2)
h_line1.addLayout(h_line3)
radiogroupbox.setLayout(h_line1)
labelgroupbox= QGroupBox('Результат теста')
l_line1 = QVBoxLayout()
l_line2 = QHBoxLayout()
l_line3 = QHBoxLayout()
l_line2.addWidget(lol)
l_line2.addWidget(lul)
l_line3.addWidget(lel, alignment=Qt.AlignCenter)
l_line1.addLayout(l_line2)
l_line1.addLayout(l_line3)
labelgroupbox.setLayout(l_line1)
buttongroup = QButtonGroup()
buttongroup.addButton(btn_answer1)
buttongroup.addButton(btn_answer2)
buttongroup.addButton(btn_answer3)
buttongroup.addButton(btn_answer4)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(question_, alignment=Qt.AlignCenter)

layout_line2.addWidget(labelgroupbox)
layout_line2.addWidget(radiogroupbox)
layout_line3.addWidget(button, alignment=Qt.AlignCenter)
labelgroupbox.hide()
layout_main.addLayout(layout_line1)
layout_main.addLayout(layout_line2)
layout_main.addLayout(layout_line3)
def show_result():
    radiogroupbox.hide()
    labelgroupbox.show()
    button.setText('Следующий вопрос')

def show_question():
    labelgroupbox.hide()
    radiogroupbox.show()
    button.setText('Ответить')
    buttongroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer1.setChecked(False)
    btn_answer1.setChecked(False)
    btn_answer1.setChecked(False)
    buttongroup.setExclusive(True)


answers=[btn_answer1, btn_answer2, btn_answer3, btn_answer4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_.setText(q.question)
    lel.setText(blue.format(q.right_answer))
    show_question()



def show_correct(to):
    lul.setText(to)
    show_result()


def check_answer():
    if answers[0].isChecked():
        main_win.score += 1
        print(Fore.GREEN  +  'Статистика:')
        print(Fore.GREEN  + '-Всего вопросов',main_win.total)
        print(Fore.GREEN +  '\n-Правильных ответов',main_win.score)
        print(Fore.GREEN  +  'Рейтинг:',(main_win.score / main_win.total) * 100,'%')
        show_correct(green.format('<i><b>Правильный ответ</i></b>')) 
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct(red.format('<i><b>Неправильный ответ</i></b>'))
            print(Fore.RED + 'Рейтинг:',(main_win.score / main_win.total) * 100,'%')

def next_question():
    main_win.total += 1
    print(Fore.YELLOW  +  'Статистика:')
    print(Fore.YELLOW  +  '-Всего вопросов',main_win.total)
    print(Fore.YELLOW  +  '\n-Правильных ответов',main_win.score)
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
main_win.total = 0
main_win.score = 0
button.clicked.connect(click_OK)
next_question()
main_win.setLayout(layout_main)
main_win.show()
app.exec_()
