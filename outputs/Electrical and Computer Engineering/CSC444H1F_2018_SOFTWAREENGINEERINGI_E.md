## Page 1

![Page 1](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_001.png)

University of Toronto 
Faculty of Applied Science and Engineering 
Final Exam - December, 2018 
Duration: 2 and V2 hours 
C5C444111 --- Software Engineering I 
Examiner: Michael Stunim 
Work independently. No aids allowed. No books. No notes. No calculators. No 
computers. No communicating devices. 
Do not remove any sheets from this test book. Answer all questions in the space 
provided. No additional sheets are permitted. 
Please write clearly so we can read what you write, and please use proper 
English so we can understand what you write. 
If any of the questions appear unclear or ambiguous to you, then make any 
assumptions you need, state them and answer the question that way. 
Write your name and student number in the space below. Do the same on the top 
of each sheet of this exam book. 
Last Name: 
Student Number: 
Do not write below this line: 
2 
3 
4 
5 
6 
7 
3


## Page 2

![Page 2](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_002.png)

Name: 
Student Number 
1. Warmup: Your class project 
(10/100 marks) 
a. What is the name of your group project? 
h. What is the name of the group's Github repository? 
What were you responsible for and what were your key contributions to the 
project? 
d. Identify each other group member (by name or email address) and identify 
which part of the project they were primarily responsible for. 
Team member 
Responsibilities 
CSC444H1 
Final Exam 2018 
Page 2 of 17


## Page 3

![Page 3](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_003.png)

Name: 
Student Number 
2. Ruby Programming 
(10 /100 marks) 
a. Write Ruby code that will define a method partition that can be invoked on 
collections like arrays. hashes, sets or ranges. The partition method should invoke 
a block on each element of the collection and return two arrays. The first array 
should return all of the elements for which the block evaluated to true, and the 
second should contain all of the other elements. For example: 
[1, 5, 96, 43, 88, ].7].partition {IiI (i&1) != O} 
should return 
[[1, 5, 43, 17], [96, 88, ]] 
To help you out a bit, you can append an element to an array with 
array << element 
Please write your code below. 
CSC444H1 
Final Exam 2018 
Page 3 of 17


## Page 4

![Page 4](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_004.png)

Name: 
Student Number 
h. What Output is generated when methodi is called in the code below? If no output 
is generated, please answer with "none". 
def methodi 
x = 11 
method2 do lxi 
puts ,c 
end 
end 
def method2 
x = 22 
yield 33 
end 
def method3 
x = 11 
method2 do lyl 
puts x 
end 
end 
c. What output is generated when method3 is called in the code above: 
CSC444H 1 
Final Exam 2018 
Page 4 of 17


## Page 5

![Page 5](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_005.png)

Name: 
Student Number 
3. Routing 
(O marks) 
The following code generates routes so that incoming HTTP requests are routed to 
specific actions belonging to specific controllers: 
Rails.application.routes draw do 
root 
'welcome/index 
resources 
:toys, , 
except: [:destroy] 
get 'profile', action: :show, 
controller: 'users' 
end 
In the table below, list the controller actions that would need to be implemented and 
for each action give the URI that might cause the action to he invoked. 
Controller 
Action 
URI 
CSC444HI 
Final Exam 2018 
Page 5 of 17


## Page 6

![Page 6](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_006.png)

Name: 
Student Number_________________ 
4. Associations 
(10/100 marks) 
a. We are working on MovieSite, and we'd like to add functionality such that a user 
can buy a ticket for a particular movie. The following use cases apply: 
- 
Over time, a user will buy many tickets to different movies. 
- 
Given a user, we want to be able to ask what tickets she has bought. 
- 
Any given movie will have many tickets associated with it. 
- 
Given a movie, we want to be able to ask what tickets have been bought for 
that movie. 
- 
Given a ticket, we want to be able to ask which movie it's for. 
- 
Given a ticket, we want to be able to ask what user bought it. 
Given the three models User, Ticket, and Movie, fill in the necessary associations 
to implement the above. 
class User < ActiveRecord: :Base 
end 
class Ticket < ActiveRecord: :Base 
end 
class Movie < ActiveRecord: :Base 
end 
C5C444H1 
Final Exam 2018 
Page 6 of 17


## Page 7

![Page 7](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_007.png)

Name: 
Student Number 
b. The above models correspond to three database tables for users, tickets and 
movies, respectively. What foreign key(s), if any. need to be included in which 
table(s) to support the above relationships. 
Given a user, we also want to ask what movies that user has bought tickets to. 
Specify the foreign key(s) that must be added to which table(s), if any, and what 
additional line(s) of code must be added to which class(es), if any, to support this 
operation. 
d. In a different application, suppose Student and Advisor are both ActiveRecord 
subclasses. In the Advisor class, the line has—many students appear. 
However, belongs to : advisor does not appear in the Student class. 
Circle the correct answer to each of the following questions: 
True or False: The database schema required to support the association is 
different from what it would he ifbelongsto : advisor had been 
present. 
True or False: In the Rails app, given an advisor @a we can write 
@a. students to get that advisor's students. 
True or Falso: In the Rails app, given a student @s we can write 
@ s . advisor to get that student's advisor. 
CSC444Hi 
Final Exam 2018 
Page 7 of 17


## Page 8

![Page 8](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_008.png)

Name: 
Student Number 
5. Software development 
(10 / 100 marks) 
a. True or False: Reusing previously tested and deployed software components 
always leads to higher software quality. Explain your answer 
river F or 
/pl000000: 
b. In method-level refactoring, the 
code smell is likely to be present if 
any of the other three are present. 
long method 
nse,': 
. 
method does more than 1 thing 
method has too many arguments 
method jumps back and forth between levels of abstraction 
c. What is the main difference between BDD and TDD? 
BDD focuses on validation while TDD focuses on verification 
BDD focuses on verification while TDD focuses on validation 
BDD is better attesting methods independently than TDD 
BDD generally uses mocks and stubs more than TDD 
d. Which of the features below is SMART? 
Users can search for a movie by title 
As a customer, I want to see the top 10 movies sold sorted by price so 
that I can buy the cheapest ones first 
MovieSite should have a good User Interface 
4n.r 4. i ( "r 1) , 
 
MovieSite should have a good User Interface with a good 
response time. 
e. Which of the following is NOT true about TDD? 
Views cannot be tested with TDD 
4ei:4, R r 11' 
You write a test case before writing the code to be tested 
You can use TDD in conjunction with BDD 
TDD can help make your code more tested, modular, and readable 
CSC444Hl 
Final Exam 2018 
Page 8 of 17


## Page 9

![Page 9](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_009.png)

Name: 
Student Number 
6. Testing 
(10/100 marks) 
Fill out the following table for each of the different types of tests. If there is a list 
of possible answers (in parentheses), use one of those answers. 
Unit 
Functional 
Integration 
What is tested? 
Running time: 
(v.fast, fast, slow) 
Error localization: 
(good, OK, poor) 
Coverage: 
(good, OK, poor) 
Use of mocks & 
stubs: 
(heavy, yes, little) 
Name of 
appropriate tool for 
these tests: 
Explain the difference between mutation testing and fuzz testing. 
CSC444Hi 
Final Exam 2018 
Page 9 of 17


## Page 10

![Page 10](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_010.png)

Name: 
Student Number 
Sally wants her website to have a special layout on the first Tuesday of every month. 
She has the following controller and test code. What FIRST principle is clearly not 
being followed? 
# HomeController 
def index 
if Time now. tuesday? 
render 'special index' 
else 
render 'index' 
end 
end 
# HomeControllerSpec 
it 'should render special template on Tuesdays' do 
get 'index' 
if Time now. tuesday? 
response. should render_template ( 'specialindex') 
else 
response should render template (' 
end 
end 
Which is stronger: 100% branch coverage or 100% statement coverage? 
Explain your answer with a (pseudo-)code example. 
CSC444H 1 
Final Exam 2018 
Page 10 of 17


## Page 11

![Page 11](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_011.png)

A 
B 
C 
D 
E 
IBC 
JD 
E 
Name: 
Student Number__________________ 
7. Responsive Web Design 
(10/100 marks) 
Provide layout code SO that the elements shown in the following images are 
automatically adjusted and laid out as shown for the three device types: desktop 
screen, tablet, and srnartphone. Element C is an image, and one of three different 
images instances (C-large. ipg, C-tablet. jpg, or C-small . jpg) should he 
shown depending on the size of the screen. You may find this a bit tricky. Make 
whatever reasonable assumptions you need to make, but please state them. There is 
extra space on the following page. 
CSC444F11 
Final Exam 2018 
Page 11 of 17


## Page 12

![Page 12](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_012.png)

Name: 
Student Number 
Page for Responsive Web Design code. 
CSC444HI 
Final Exam 2018 
Page 12 of 17


## Page 13

![Page 13](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_013.png)

Name: 
Student Number 
8. Full Web application 
(20/100 marks) 
Assume you have a very large database available containing exam questions and 
answers to those questions. You wish to make those available to students through a 
website to help them prepare for their exams. 
You can assume two database tables already exist that are full of data. First, a 
Questions table that has two columns: question and answer. Second, a Keyword table 
that also has two columns: keyword and list of indices. Each question and answer 
contains entry consists of HTML text. 
When you think about the design of this application, you'd like a home page that 
states the purpose of the site with a form so that the user can type in a keyword. After 
pressing a submit button, a new page comes up with a randomly selected exam 
question that was indexed to the submitted keyword. That page will have a "show 
answer" button at the bottom. If the user presses that button, then a new page comes 
Lip with both the question and the answer. Each page should have a link back to the 
home page. 
Please provide a Lo-Fi user interface sketch that depicts the expected user experience, 
and then implement this application on the following pages. You can make any 
assumptions you like, but please state them clearly. The following structure would he 
appropriate 
a. Assumptions (including specifics about the database) 
h. UI sketches 
Controller code 
Routes 
Model code 
Ii View code 
CSC444H1 
Final Exam 2018 
Page 13 of 17


## Page 14

![Page 14](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_014.png)

Name: 
Student Number 
Page for application 
CSC444H 1 
Final Exam 2018 
Page 14 of 17


## Page 15

![Page 15](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_015.png)

Name: 
Student Number 
Page for application 
CSC444H1 
Final Exam 2018 
Page 15 of 17


## Page 16

![Page 16](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_016.png)

Name: 
Student Number 
Page for application 
CSC444H1 
Final Exam 2018 
Page 16 of 17


## Page 17

![Page 17](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_017.png)

Name: 
Student Number 
Page for application 
CSC444HI 
Final Exam 2018 
Page 17 of 17

