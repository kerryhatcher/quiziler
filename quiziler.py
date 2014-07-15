__author__ = 'khatch'


import quizlib
import pango
import gtk
import random

quiz = quizlib.StartQuiz()

quiz.randomquestion()
#print "answer: " + quiz.answer + " - " + quiz.answers[quiz.answer]


class QuizilerGUI:

    builder = gtk.Builder()

    def set_answer(self):
        #random.shuffle(quiz.answers)
        for answer in quiz.answers:
            print answer + ":  " + quiz.answers[answer]
            print "button" + answer
            answer_btn = self.builder.get_object("button" + answer)
            answer_btn.set_label(quiz.answers[answer])

    def on_button_answer_clicked(self, data):
        print quiz.answers[quiz.answer]
        print data.get_label()
        if quiz.answers[quiz.answer] == data.get_label():
            self.question_text_view.modify_base(gtk.STATE_NORMAL,gtk.gdk.color_parse('#0000ff'))
            print("correct!")
        else:
            self.question_text_view.modify_base(gtk.STATE_NORMAL,gtk.gdk.color_parse('#ff0000'))
            print("wrong...")

    def on_Main_Window_destroy(self, widget, data=None):
        gtk.main_quit()

    def gtk_main_quit(self, widget, data=None):
        gtk.main_quit()

    def on_button_next_pressed(self, widget, data=None):
        self.next_question()

    def next_question(self):
        quiz.randomquestion()
        self.question_text_view = self.builder.get_object("question_text_view")
        question_buffer = gtk.TextBuffer()
        question_buffer.set_text(quiz.question)
        self.question_text_view.set_buffer(question_buffer)
        self.set_answer()
        self.question_text_view.modify_base(gtk.STATE_NORMAL,gtk.gdk.color_parse('#ffffff'))
        self.question_text_view.modify_font(pango.FontDescription("Monospace 20"))


    def __init__(self):


        self.builder.add_from_file("main.glade")
        self.window = self.builder.get_object("Main_Window")
        self.builder.connect_signals(self)
        #self.next_question()



    def __repr__(self):
        return "Type what do you want to see here."

if __name__ == "__main__":
    quiziler = QuizilerGUI()
    quiziler.window.show()
    quiziler.window.fullscreen()
    gtk.main()







