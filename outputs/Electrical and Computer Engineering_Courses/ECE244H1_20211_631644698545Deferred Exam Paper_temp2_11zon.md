## Page 1

ECE 244F - Programming Fundamentals (Fall 2021)
Deferred Final Examination
Examiners: T. Mizan Rahman and Sadegh Yazdanshenas
Duration: ISO minutes to solve + 30 minutes to scan and upload answer sheets
Late uploads will receive a mark of zero
Instructions — Read Carefully
You have minutes to solve thc Once the I SO minutes are over, you must Stop solving
questions and begin scanning your answers and uploading them to Crowdmark. You have 30 minutes to
do so. If your answers are not uploaded by the end of the 30 minutes. your will receive a mark of
Zero the
You may print questions and in the provided. Alternatively, you may write your
answers On blank sheets of paper. or use Word. Google Docs. ctC. Clearly each answer With the
question number. Write your nank and student number at the top right comer of each sheet.
You may take photos Of your answer sheets or use a scanning app (e.g., SwiftScan). Once you have the
Scans you Can upload them to Crowdmark. have written your answers in Word, Google DOCS, a
similar program, Save your work as PDF file, Which you can directly upload. Crowdmark does not
accept .doex files.
This test is OPEN Textbook and OPEN notes. You MAY NOT Other aids (e.g., web on
programming, a C++ compiler. etc.). You are to solve the exam by yourself, Without thc aid of others.
The Of each is indicated. The total value Of is
In answering the questions, you must assume the C+II standard and the use of the g++ compiler
available on the Linux machines in the ECF labs.
Some questions marked as Challenging or You Should these questions to the end.
If you have any doubts, write your assumption do•.vn. If sensible, they will bc considered.
If you must ask an instructor a question, please use the (clickable) Zoom link below •
it there Will a Jong wait time. In any Case, the Common
answer given to your questions will "write down your assumption".
Best Of



## Page 2

Consider the Class definition below. it is correctly and though
the IS given.
public:
ine
get
void see length(int n) ;
print() ;
Ine 1 en ;
float fraction ;
A main function uses this class and makes the following variable declaration:
in t length ;
nare
string alias ;
For each Of the following code fragments that appear in main. indicate by placing and x in the
column the generates a compile-time error Ot error-free.
Assume that
and the definition are and that the namespace is
Mystery m;
m. see length (O) ;
My g Eery m (name) ;
coue m. gee lengthO endl;
Mystery m (alias) ;
Mystery m (name) ;
m. len 3
m (alias) ;
set length (increment) ;
are on (e.g„ A. B.) give
answer as enher "No Errors" or "Errors".



## Page 3

Write a C" futK:tiCMi void readintSt that repeatedly reads integers from the standard input
(using and then immediately outpuls thc input integer (using cout), onc integer per line,
When a • Character is the function prints Done on a by itself and
returns , if any than digits or • . • thc the
Error on a line hy itself You may the Will never enter
700
However, ifthc user enters 101 21 13 abc 444, the function prints:
Write your code in the box below.
*include
using namespace std;
your given in



## Page 4

Question (3 pointers.
Consider the following Code snippet that manipulates rxtinters in a main function Ofa C++ program.
penullptr;
int• q=nullptr;
r—nullptr;
int•• t 'p;
p
q
•p
new int;
new int ;
Which Of the following statements (that come after above snippet executes) print 5 to the standard
output? You may is the is Correct
. cout
b
. cout
e.
Coue
cout
you are answering on your own sheets, write the labels Of the correct answers (e.g„ go.



## Page 5

(4 Memory
We would like to create a dynamically allocated array called a. which has six* n. the value Of
which is olgained frotn user inpuL Each of n elements of thc array points to a dymunically
allocated pointer to a Shape object Each of these pointers points to a dymunically allocated
Shape object.
that the definition and implementation Of the Shape is available and is COtTCCt.
uhich of the following code snippets allocates the data stmaure. as described above? Circle only
and
a new Shape'* ( m ;
for (int i
a = Shape • ;
nev ;
Shape* • * a
nev Shape*'
* (au J) new Shape();
C.
p.
Shape* a
for (int
Shape••• a
nev
Shape ;
nev Shape* • ;
a Shape•;
'(nev ;
Ifyou on your own sheets. write the label of the correct answer (e. A. or BO.



## Page 6

S. (X Memory.
Consider following definitions and implementations as the that
utilizes them. You may assume the code is rree Ofcompile-time errors.
class A
private :
int data ;
A(int V) (data V: Y
int getDataO conse {return data;}
private :
publ c :
BO (a = nev A(O)
B' rhs) • a); return •this; )
d seeA
helper one b)



## Page 7

p — nev BO ;
// This is Point W
return (p) :
int main (
// This is Point X
•helper (X) ;
// This Is Poine Z
z •helper two (y) ;
return (O) ;
Indicate Of Objects Of type A in program
Indicate the in the number of objects oftypc that exist in memory and that occurs
during program For example, if 5 more
exist, write Iftwe exist. write •2.
Indicate the in the number of objects of type A that exist in memory and that occurs
during program V Z. For example. 5
exist, write If two fcmr objects exist. write -2.



## Page 8

(d) Indicate thc in the number orobjeetS or type A that exist in mcmory and that ocVurS
during example, if objects
exist. write fewer objects exist. write -2,
(e) Indicate thc in thc number of objects oftypc A that exist in memory and
during program execution For example, if objects
exist. write +5. If two fewer objects exist. write •2.
Draw a
If yew an answering own she«s, write the of each pad followed by



## Page 9

6. Linked
following is the definition Of thc Which a node in a linked
public for simplicity, head linked list is pointed to by head
class List-Node
in key ;
Li3tNode• next
ListNode• head;
following is a function to traverse the linked list. However. Some from the
figlction is remmed. as shown by the comments, What are the removed lines?
(head)
void traverse (ListNodei h)
(h return ;
IÅstNode•• per ;
While (eondition
/ / Line 2
/ / Line 3
A. Whal should 1 be? Circle one answer.
1.
2.
3.
4.
cout
eoue
Line 1 or a
endl ;
end;
( —>key endl ;
( •per) — >key ;



## Page 10

B. Should the be?
2.
3.
4.
5.
per nuliper
*per
nuilptr
•per h
C. What should Line 2 be? Circle one answer.
2.
3.
4.
5.
gout
cout
endi ;
( •per) endi
D. What should Line 3 ræved be? Circle one answer.
Nothing. Line 3 or a
2.
3.
4.
S.
per
per
( •per) — ;
= (•per) . next;
If you are answering on your Own sheets, write the label of each question part by the



## Page 11

Question 7. (6 marks).
It is desired to implement an efficient deletion function in a linked list You are given a linked list
Ikiinted to by head and a pointer per to a node in a linked list, which is guaranteed not to be the
last node On the list (i e, not the tail ncKdey Wiite a function runoveNodo that removes this
from the list,
Below is an example Of What
You may the following is the definition Of Class. The head node Of
linked list is pointed to by head
class ListNode
pub I f c :
int key;
Li s tNodo• next
head ;
Write Y o u are not allowed to Change the arguments or
node) (
you are answering on your own sheets, write your function. including the header given in
the question.



## Page 12

are With an implementation Of a Clasg as a Class.
-me I inkedLIse class is shown below, you may assume every function is correctly implemente•l
pcl vaee :
publ :
linkedIÄst() ;
Other) ;
& rhS)
/*ereates a new head Vith key k and updates the
void insert.KeyatTaiI(ine k) ;
/ / if the list is the following functions return
// false and do nothing, otherwise they perform the
// xntioned easks, update their argumnts Che key
/ / Of deleted node, and true
k) ; / the node
k) ; Ehe node head
We Wish to implement a class that represents a queue. A queue is a data Sttuture in
Which insertions are done on one end, called the an deletions done on another end
called thc front. myQue•ue looks has the following definition;
class myQueue
linkedLise data; / • linked list * /
k) ; Vith k at /
in E fronE() ; node A E
front(); /• return key of ae Ezone • /
/ * return true if queue
are required to implement thc following Of to
fimctionality. Note that the only private data member of myQueue is a LinkedList named



## Page 13

a) the pugh_back k) In this a With
value of is added at the back of the queue.
b) Implement thc front ( ) function. In this function. thc value of the key of the front
node in the queue is returned and no updates happen to queue. If qucLE is empty —1 is
e front O
c) function returns true if are no nodes in
queue and false
d) the function. In this function. the value of the key of the
front of the queue is returned and the node at front is removed from the queue. If the queue
e pop_frone O
If you are answering on your sheets, write your fimetions, including the headers given the



## Page 14

Question 9. (5 marks). Recursion.
Write a function that replaces each element Of an array or positive integers with its prefix
Sum. The prefix sum of an element is the sum of thc element and all the elements that are at smaller
indices than it. For example. for the 4-elcmcnt array a shown below on the left. thc function
repQs the elenvents of the array as shown below on right.
a 1 3 6 10
The function has the following prototype:
and is initially invoked an array A as follows: prefix-sum (A, O, n—i. O) ;
void prefixsun tint* arr ,
int left ,
int right
, int psun) (
you are answering on your own sheets. write your function. including the header given in
the question.



## Page 15

10. (3
Consider the following binary tree. •Ille keys ofthe nodes are shown inside the nodes.
What is the preorder traversal of the tree ? Write Ymir answer here:
is the inorder traversal of the tree? Write your answer here.
is Of the tree? Write here:
and
J (3 Trees.
A binary search tree (BSV) has 7 nodes. as shown belcnv. 'Ille key Of each node is not shown.
thc keys; 73, 30, 36 24.
the key for each node in the tree and
above tree
each node.



## Page 16

12. (5 marks).
Consider the defined represents a in a binary root Of
tree is pointed to by root, which is also declared below.
left ;
TreeNode• ghe ;
Write a function E OE Counts the Of
nodes in a Y Ou Can thc necessary are included.
function is invoked as follows:
cout nuu±er of interior nodes in Ehe tree is:
count interior (root)
Write your answer below.
the
endl ;



## Page 17

13. (5 marks). TreeS_
Consider the two and to a binary
Class Treeyode
in t key ;
( ) key ;
TreeNode• geezeEt() conse (return
Amid post O ;
Tree Mree; // Create a tree
/ / Code
the tree rooted at EOOt traversal. It is
invoked as myTree. post O ; and prints the keys of the nodes to cout. The method
Write your answer below.
header in



## Page 18

(3 marks)
A stu&nt, John, asked to write a 'Unction that given a pointer to the root or a binary tree,
checks if thc binary tree is a binary scareh It returns ifthc tree is a binary search tree and
false if 'Rhenvisc. John wrote thc following function:
node) (
NULL) reeurn ecue;
/ / for left node
NULL
fal so ;
NULL
return false;
/ / recursively to children
(i SEST )
true ;
//ve the end, so a BSC!
re turn true :
Hcnvever. to John's surprise hc received a mark of O ror the above timetion John did not accept that
the above a fundamental flaw and Objected to the mark of O. Y Ou nccd to find and show a
binary show John that his doe the your You Can
the dAtn Of ig an integer _ Depict tree write integer
each node thal ghould an your
tree can have a maximum of S nodes. Draw your tree below.



## Page 19

•Ihe following program memo"' issues. •Ille linc numbers to the left are not part or the code,
they arc added to facilitate your answer.
2 using na—spaae std;
4 class Shape I
pub I c :
private :
size n;
Shape* ;
delete arr ;
geesaze() eonse (return size; )
24 i;
26 int main O
27 Mystery m (10) ;
29
•Ilme output ofvaigrind is shown and indicates the issues.
Shape ( ) ;
—181 s 9—
—18159—
ght
—18159—
—18159—
copyright (C) 2002-2015, and GNU GPL'd, by Julian se*ard
Using Valgrind—3.11. O and LibVEX; rerun Vith —h for
info
OX400BOA: : (in t) 17)
by Ox4009EE : 2 7)



## Page 20

alloc • d
c : 4 21 )
e 159— by OX40 : : .
by ox4009EF: main (myseery.cpp: 27)
—18159— Mismatched free ( ) / delete / delete (J
at Ox4A0673E : delete
c : 574 )
—I B 159= by Ox400B4F: Hystery : : —Mystery (mystery.
—lei 59— by ox400A00 : maln (mystery. cpp: 27)
—181S9— OX4e46040 IS O bytes a block Of Size BO
ae Ox4A078FO : long)
(vg_replaee c: 421)
—1B 159— by O*400AB7 : (in E) 16)
by Ox4009EF: main (mystery. QF, : 27)
—18159—
—1 E159— stJWARY:
—18159—
ted
total heap usage :
12 allocs, i frees, 168 bytes
88 bytes in II blocks are definitely lost in loss record
—1 e 159—
OX4Ä07D73: long)
( vg_replace c : 332 )
—i e 159=
—1 BIS9—
—18159—
—1 e159—
—1B 159—
—1 e 159—
—1 B 15 y—
frcm 4 )
by OX400AE2:
by Ox4009EF: main (mystery. 2 7)
SUWARY :
definitely lost:
possibly lose:
suppressed
88 bytes in II blocks
O bytes in O blocks
O bytes in O blocks
For counts of and suWressed errors , rerun
hulicatc thc changes required to thc code fix thc issues.
all bc With to Shape and



## Page 21

A Change indicated by a number, followed by one Of: Ot
and finally Change Here are some examples:
To indicate that a comment is to bc inserted before definition of class Shape, you
4 // This is c I Shape
• to indicate that the z c method Of be you
Finally, to indicate that the getShapeArray method of Hystery *Itould be conse,
23 Repl'w•e
Shape• • getShapeArray O fretum am.)
Write your answers in the table below. You may ormay not need all rows.
are answering on your sheets, write your in a liKe the above.



## Page 22

For each code snippet, specify the Wust-case complexity, using the Big-O notation. Write the
answer in thc box provided ancr cach code snippet.
for (int
for i<n; 1+4) (
code with O (I)
for (int 1—0; i<n;
/ / sotæ Vith O (I)
B. or and



## Page 23

17. (6 marks) A
TWO Students Were to write a recursive function that given a integer n, computes
Amy Wrote the following function;
return I ;
return (Amy (n—l) + ;
John wrote the fo Ilowing function:
John n)
return ;
Answer the following questions about eode written by Amy and John.
a) Is Amy's function Correct (docs it compute and return or No. (circle Onc answer)
b) Is John's function correct (does it compute and return 2 Yes or (circle one answer)
c) What is the worst-case complexity Of Amy's function using Big O notation?
d) is the complexity Of John ' s function Big O notation ?
you r answer.



## Page 24

18. (6
the following definitions Of and derived Assume the implementation Of
is Correct though the code is not Shown here.
Base
Base ( ) ;
—Base() :
int ;
print ( )
class DerivedA :
int R;
public:
public Base
—Derived* ;
void set* (int r) ;
pub I i e :
DerivedAA ( ) ;
float getPO const;
void print() conge;



## Page 25

public:
getc() conge. •
void seec r) ;
print C)
class
float P;
public:
DerivedBE O :
get-P() conse;
setP(fIoat p) ;
const ;
In the table below. indicate whether each group of statements (i.e.. a row in the table) generates a
compiler error or not by placing an X i" thc approprialc column.
C.
Statement
Base e;
DerivedA r;
DerivedAA pr;
pr r;
DerivedA r;
DerivedAA p";
r — pr;
Deri r ;
DerivedB c;
DerivedBB pc
int x — pc.get1D();
Base• elm_p;
r ror?
Error?



## Page 26

H.
DerivedA+ r_p•
— new DerivedA();
Rase' eIn_p CQ rivedA();
Der ivedAAt pr—p;
DerivedA• new DerivedAÖ;
pr_p — r-p;
i pr_p
DerivedA' r_p;
Der i vedAA0 pr—p
DerivedA• r_p;
r_p — pr_p•
= Derivedm();
new DerivedAA()
If you an ans•erüug on your own sheets, write the label (e.g„ A. or B.) and your



## Page 27

19. (6
Consider the following classes.
u sing
string ;
public :
person ) (
— "EMPTY" ; address — "EMPTY"; id — 0 ; 1
person (sering 1 _na_m, sexing 1 _ addresz,
name I address
I address; — id;)
Virtual void printlnfo()
eoue CQ Person ID lives
void setAddress (string I address) {address I address;
String getName ( ) return naæ ;
void seeld I i
float GPA;
0.0;)
student(string I String I address, int I id,
noat 1 _öpA)
void setGPA(f10at 1 — 1 CPA;)
( Student' s iS
Coue ID has a gpA
following in a function. followed by the expressions in the table



## Page 28

p_one
123", 1)
p_per 5p_g-ne ;
, 2, 3.9);
"456"
What is 1Mintcd by cach ofthe
following? If it results in a compile
write ' •compile
each row of the table independently.
p_one. ( ) ;
p_one. printName ;
s one.printlnfo() :
'_one. ;
p_ptr 's one
are A. or B.)



## Page 29

Qinstion 20. (6 jnarks). Binary Treem (Wam$ng• Difficult)
the same definition of a that appears in 12 Given a pointer to the
root of a tülary find a subscr of thc ncm:Es of thc tree to both of the following cogbtraints:
I) If a node is included in this its parent cannot be included in the sutset.
2) There sholdd other Ihal meets the first constraint and sum orthekeys orthe
1K'd:s of the other subset is larger than üte sum ofthe keys ofthe nodes of this subset,
YOLE code should return the sum of the key values of in a subset that meets the above
requirements Three examples are provided tR210w to help you better understand the problem. You
are allowed and encouraged to write one heller function(s).
Olay
Write y our answer below arxl on Ihe overflow page irnecessary.
// Write any global variables and helper functi«xts here
ine seleceAndSum (TreeNode* root)
are anmeringon your own sheets, anmer, incluüng the futrtkm header given


