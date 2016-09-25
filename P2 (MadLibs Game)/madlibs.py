#This is MadLibs Game!!!
#Project 2
#You can directly execute this file to play the MadLibs Game.
#This game consists of 4 levels.Every level contains 4 questions.
levels=["beginner","normal","intermediate","expert"]
#levels list is created so that user can enter the levels 
string=["Hello!My name is Nikhil Bansal.This is project  number _1_.This project is part of Intro To _2_ Nanodegree.In this project we learn basics of _3_ language.This Nanodegree has total of _4_ projects.","HTML stands for _1_. It is used to build basic _2_ of webpage._3_ is used to enhance the appearance of webpage.HTML files are saved with _4_ extention","len function is use to get the _1_ of the string or list._2_ function is used to transfrom string into list._3_ function is used to transform the list into single string._4_ language is used to make webpage dynamic.",
"Inside _1_ HTML tag we put the JavaScript._2_ tag besides <i> is used to make the font italics._3_ tag is used to make a vertical line in html.Full form of css is _4_.",""]
#string list contains the questions for each level.
answers=[["2","programming","python","5"],["hyper text markup language","structure","css",".html"],["length","split","join","java script"],["script","em","hr","cascading style sheets"]]
#answers list contains the answers to the questions.
print "\t"*5+"Welcome to MadLibs Game!!\n"
print "\t"*3+"1.beginner\t2.normal\t3.interediate\t\t4.expert\n"

def replace(index,element,string):
    """ This function is made to replace the empty blanks with the correct answers """
    string=string.replace("_"+str(element+1)+"_",answers[index][element])
    #replace function is an inbuilt function used to replace some text with another.
    return string

def madlib_process(index,string):
    """ This funtion is made to print the questions and call the replace function so that empty blank can be replaced with the corect answer. """ 
    print string
    current_blank = 1
    total_blanks = 5
    # current_blank is used as a loop control variable and total_blanks is used to store 1+the number of blanks for the level.
    while current_blank<total_banks:
        blank=raw_input("What is answer for blank "+str(current_blank)+" ").lower()
        #blank variable is used to store the input of the user for the particular question.lower function is used so that user can input the answer both in uppercase and lowercase. 
        if blank==answers[index][current_blank-1]:
            string = replace(index,current_blank-1,string)
            print string
            current_blank = current_blank + 1
        else:
            print "WRONG ANSWER! What is answer for blank "+str(current_blank)
        

def level_check(level):
    index=0
    # index is used as a loop control variable.
    # This function is used to call the madlib_process function 
    while index<len(levels):
        if levels[index]==level:
            madlib_process(index,string[index])
        index+=1
        
def play_madlibs():
    #This function is used to take input for level and check whether the level entered is correct or not.
    level=raw_input("Please choose your level : ").lower()
    #level variable is used to store the value of level entered by the user. 
    if(level==levels[0] or level==levels[1] or level==levels[2] or level==levels[3]):
        level_check(level)
    else:
        print "Enter valid Level"
        play_madlibs()  
    user_input=raw_input("Enter yes if you want to play again or enter no to quit ").lower()
    if user_input=="yes":
        print "\n"
        play_madlibs()
    else:
        print "ThankYou for playing"

play_madlibs()
