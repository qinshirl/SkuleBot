## Page 1

![Page 1](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_001.png)

ECE 244F - Programming Fundamentals (Fall 2021)
Deferred Final Examination
Examiners: T.S. Abdelrahman, Mizan Rahman and Sadegh Yazdanshenas
Duration: 150 minutes to solve + 30 minutes to scan and upload answer sheets
Late uploads will receive a mark of zero
Instructions - Read Carefully
You have 150 minutes to solve the exam. Once the 150 minutes are over, you must stop solving
questions and begin scanning your answers and uploading them to Crowdmark. You have 30 minutes to
do so. If your answers are not uploaded by the end of the 30 minutes, your will receive a mark of
zero for the exam.
You may print the questions and answer in the space provided. Alternatively, you may write your
answers on blank sheets of paper, or use Word, Google Docs, etc. Clearly label each answer with the
question number. Write your name and student number at the top right corner of each sheet.
You may take photos of your answer sheets or use a scanning app (e.g., SwiftScan). Once you have the
scans you can upload them to Crowdmark. If you have written your answers in Word, Google Does, or a
similar program, save your work as PDF file, which you can directly upload. Crowdmark does not
accept doex files.
This test is OPEN Textbook and OPEN notes. You MAY NOT use other aids (e.g., web resources on
programming, a Ct compiler, etc.). You are to solve the exam by yourself, without the aid of others.
The value of cach question is indicated. The total value of all questions is 100.
In answering the questions, you must assume the Ct+11 standard and the use of the gt+ compiler
available on the Linux machines in the ECF labs.
Some questions marked as challenging or difficult. You should leave these questions to the end.
If you have any doubts, write your assumption down. If sensible, they will be considered.
If you must ask an instructor a question, please use the (clickable) Zoom link below. Please do so only
if it is absolutely necessary! Otherwise, there will be a long wait time. In any case, the most common
answer given to your questions will be "write down your assumption".
https://us02web.zoom.us/j/89670882172
Best of luck!!


## Page 2

![Page 2](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_002.png)

Question 1. (3 marks). Classes and Methods.
Consider the class definition below. Assume it is correetly defined and implemented, even though
the implementation is not given.
class Mystery {
public:
Mystery (string& s) :
int ID:
Int get length) const;
void set length (int n) ;
void print () :
private:
int len:
float fraction;
vold up_length (float f) ;
void round (float f);
) :
A main function uses this class and makes the following variable declaration:
int length = 5:
string name = "Tom";
For each of the following code fragments that appear in main, indicate by placing and X in the
appropriate column whether the fragment generates a compile-time error or compiles error-free.
You should consider each fragment in isolation from the other fragments. Assume that lostream
string and the Mystery class definition are included and that the std namespace is used.
Compiles
Code Fragment
with no
Errors
Generates
Compile-time
errors
A.
Mystery m;
m. set length (0):
Mystery m(name) ;
B.
cout ‹ m.get length() < endl;
c.
Mystery m(alias) :
m. up length (increment) :
D.
Mystery m(name):
m. len = 3;
E.
Mystery m(alias) :
m. ID = 0;
Mystery m(name) :
r.
set length (increment):
If you are answering on your own sheets, write
answer as either "No Errors" or "Errors"
stion label
B.) and


## Page 3

![Page 3](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_003.png)

Question 2. (4 marks). C++ DO.
Write a C++ function void readInts) that repeatedly reads integers from the standard input
(using cin) and then immediately outputs the input integer (using cout), one integer per line.
When a ' character is encountered, the function prints the message Done on a line by itself and
returns. if the user enters any characters other than integer digits or the .
*the function prints the
message Error on a line by itself and returns. You may assume the user will never enter eof
Thus, for example if the user enters 51 16 700 ., the function prints:
700
Done
However, if the user enters 101 21 13 abc 444, the function prints:
101
21
13
Error
Write your code in the box below.
#include <iostream›
using namespace std;
void readints) /
are answering on your own sheets, write your function, including thi
Ler give
question.


## Page 4

![Page 4](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_004.png)

Question 3. (3 marks). Pointers.
Consider the following code snippet that manipulates pointers in a maîn function of'a C++ program.
int* p=nullptr;
int* q=nullptr;
int* r=nullptri
int** t = &p;
int** s = &q;
I = Pi
p = new int;
g = new int;
*p = 5;
*g = 2;
**s = (*p) + (**t);
Which of the following statements (that come after the above snippet executes) print 5 to the standard
output? You may assume iostream is included and the std namespace is used. Circle all correct
answers. Keep in mind that incorrect answers carry a penalty.
a. cout ‹< I;
b. cout << *t;
c. cout << *g:
d. cout «< *p:
e. cout < **t;
f. cout «< *I;
g. cout « *s;
h. cout << (**s) / 2;
If you are answering on your own sheets, write the labels of the correct answers (e.g., a., b.


## Page 5

![Page 5](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_005.png)

Question 4. (4 marks), Dynamic Memory Allocation.
We would like to create a dynamically allocated array called a, which has size n, the value of
which is obtained from usor input. Each of the n elements of the array points to a dynamically
allocated pointer to a Shape object. Each of these pointers points to a dynamically allocated
Shape object.
Assume that the definition and implementation of the Shape class is available and is correct.
Which of the following code snippets allocates the data structure, as described above? Circle only
one answer and note that some incorrect answers carry part marks
A.
Shape*** a = new Shape** [n];
for (int i = 0; 1 < n; ++1) €
a [i] = new Shape*:
* (a[i]) = new Shape () ;
B.
Shape*** a = new Shape** [n]:
for (int 1 = 0; 1 ≤ n; ++1)
* (a[i]) = new Shape () ;
U
Shape*** a = new Shape** [n]:
for (int i = 0; 1 < n; ++1)
a[i] = new Shape () :
{
D.
Shape*** a = new Shape** [n];
for (int i = 0; 1 < n; ++i) €
ali] = new Shape*;
* (a [i]) = & (new Shape()):
If you are answering on your own sheets, write the label of the correct answer (eg, A. or E


## Page 6

![Page 6](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_006.png)

Question 5. (8 marks), Dynamic Memory.
Consider the following class definitions and implementations as well as the main function that
ütilizes them. You may assume the code is free of compile-time errors.
class A l
private:
int data:
public:
A (int V) {data = v:)
int getData () const freturn data;)
void setData (int v) (data = v;)
* :
class BI
private:
A* a;
public:
BO) fa = new A(0) :)
B (const B& other) (a = new Al (*other.a) getdata ()) ;}
B6 operator= (const B6 =hs)
{*a= * (rhs.a): return *this;)
A* getA() const (return a;)
void seta (A* v) (a = vil
B* helper_one (B& b) |
A a (5):
A x (4):
B g:
B* p:
q = b;
p = &b:
This
Poin
return (p) ;


## Page 7

![Page 7](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_007.png)

B* helper_two (B b) {
в а;
B g:
B* p:
9 = b;
P = new BO) :
11 This
1S
Point
return (p):
int main () (
В х:
B Y:
B zi
I This 1s Point X
z = *helper one (x) ;
// This 1s Point 2
z = *heiper_two (y) :
11 This is Point V
return (0);
(a) Indicate the number of'objects of' type A that exist in memory when the program execution
reaches Point X.
Answer:
(b) Indicate the change in the number of objects of type A that exist in memory and that occurs
during program execution between Point X and Point Y. Forexample, il 5 more objects
exist, write +5, If'two fewer objects exist, write -2.
Answer:
(c) Indicate the change in the number of objects of type A that exist in memory and that occurs
during program execution between Point Y and Point Z. For example, if 5 more objects
exist, write +5. If twe fewer objects exist, write -2.
Answer:


## Page 8

![Page 8](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_008.png)

(d) Indicate the change in the number of objects of type A that exist in memory and that occurs
during program execution between Point Y and Point W. For example, if 5 more objects
exist, write +5. Iftwo fewer objects exist, write -2.
Answer:
(e) Indicate the change in the number of objects of type A that exist in memory and that occurs
during program exccution between Point Wand Point V. For example, if 5 more objects
exist, write +5. If two fewer objects exist, write -2.
Answer:
Hint: Draw a picture!
If you are answering on your own she
(e.g., (a) +8, (b) -18,
bel of ea
red by your


## Page 9

![Page 9](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_009.png)

Question 6. (7 marks). Linked Lists:
The following is the definition of the class ListNode which represents a node in a linked list. All
the members are public for simplicity. The head node of the linked list is pointed to by head.
class ListNode (
public:
int key:
ListNode*
next;
} :
ListNode* head:
The following is a non-member function to traverse the linked list. However, some content from the
function is removed, as shown by the comments. What are the removed lines?
// Non-member function invoked as traverse (head)
void traverse (ListNode* h) f
if (h = nullptr) return;
ListNode** ptr = 6(h->next) :
/ Line 1 removed
while (condition removed) {
// Line 2 removed
// Line 3 removed
}
A. What should Line 1 removed he? Circle one answer.
1. Nothing, Line 1 is empty or is a comment
2. cout ‹< h->key « endl;
3. cout < ptr->key «< end;
4. cout << (*h) ->key < end1;
5. cout << (*pti) ->key:


## Page 10

![Page 10](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_010.png)

B. What should the condition removed be? Circle one answer.
1. true
2. ptr 1= nullptr
3. *ptr -= nullptr
4. *ptr 1= h
5. ptr != *h
C. What should Line 2 removed be? Circle one answer.
1. Nothing, Line 2 is empty or is a comment
2. cout «< ptr->key ‹< endl;
3. cout < (*ptr) key < endl;
4. cout < & (*ptr) ->key «< endl;
5. cout < (*ptr) -›key << endl
D. What should Line 3 removed he? Circle one answer.
1. Nothing, Line 3 1s empty or 1s a conment
2. ptr = &( (*ptr) ->next) ;
3. ptr = (*ptr) ->next;
4. ptr = ptr->next;
5. ptr = (*ptr) - next;
I you are answering on your own she
answer label (e.g., A. 1 or B. 3, etc.).


## Page 11

![Page 11](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_011.png)

Question 7. (6 marks). Linked Lists and Complexity (Challenging)
It is desired to implement an efficient deletion function in a linked list. You are given a linked list
pointed to by head and a pointer ptr to a node in a linked list, which is guaranteed not to be the
last node on the list (i.e., not the tail node). Write a function removeNode that removes this node
from the list. The function must have a complexity of OL Below is an example of what
removeNode does
Before
ptr /
After:
head-
3
1
You may assume the following is the definition of the class, ListNode. The head node of the
linked list is pointed to by head
class ListNode 1
public:
int key:
ListNode* next;
ListNode* head;
Write your answer below. You are not allowed to change the function's arguments or return
type.
void removeNode (listNode* node) {
you are answering on your own sheets, write you
question.
function, including the header
given


## Page 12

![Page 12](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_012.png)

Question 8. (8 marks). Linked Lists
You are provided with an implementation of a 11nkedlist class as well as a 11stNode class.
The 11nkedList class is shown helow, you may assume every function is correctly implemented.
class linkedlist (
private:
listNode* head;
public:
linkedList () ;
linkedList (const linkedlist& other) ;
~1inkedList () :
linkedlist & operator= (const linkedlists rhs) ;
/*creates a new head with key k and updates the
linked list accordingly */
void insertkeyatHead (int k) :
/*creates a new node at tail with value k*/
void insertkeyatTail (int k) ;
W if the list is empty the following functions return
// false and do nothing, otherwise they perform the
/l mentioned tasks, update their arguments with the key
11 of deleted node, and return true
bool deleteTail (int& k); //deletes the node at tail
bool deletelead (int& k); //deletes the node at head
We wish to implement a myQueue class that represents a queue. A queue is a data structure in
which all insertions are done on one end, called the back and all deletions are done on another end
called the front. The myQueue class looks has the following definition:
class myQueue t
private:
linkedlist data; /* linked list */
public:
myQueue () :
/* create an empty queue */
void push back (int k):/* insert node with key k at back */
int pop_front () :/* remove node at front, return its key */
int front (); /* return key of node at front */
bool isempty(); /* return true if queue is empty */
You are required to implement the following functions of the queue class to have the mentioned
functionality. Note that the only private data member of myQueue is a linkedlist named
data.


## Page 13

![Page 13](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_013.png)

4) Implement the void push_back (int k) fumetion. In this fumetion, a new node with
value of 'k is added at the back of the queue.
void push_back (int k) i
b) Implement the int front () function. In this function, the value of the key of the front
node in the queue is returned and no updates happen to the queue. If queue is empty -1 is
returned.
int front () i
c) Implement the bool isempty () function which returns true if there are no nodes in the
queue and false otherwise.
bool isempty 0) T
d) Implement the int pop_front 0) function. In this function, the value of the key of the
front of the queue is returned and the node at front is removed from the queue. If the queue
is empty, -1 is returned.
int pop_front () (


## Page 14

![Page 14](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_014.png)

Question 9. (5 marks). Recursion.
Write a recursive function that replaces cach element of' an array of positive integers with its prefix
sum. The prefix sum of an element is the sum of the element and all the clements that are at smaller
indices than it. For example, for the 4-element array a shown below on the left. the function
replaces the elements of the array as shown below on the right.
a
2 3
3
6
10]
The function has the following prototype:
void prefixsum (int* arr, int left, int right, int psum) ;
and is initially invoked for an array A as follows: prefixsum (A, 0, n-1, 0):
void prefixsum (int* arr, int left, int right, int psum) (


## Page 15

![Page 15](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_015.png)

Question 10. (3 marks), Tree Traversals.
Consider the following binary tree. The keys of the nodes are shown inside the nodes.
)
What is the preorder traversal of the tree? Write your answer here:
What is the inorder traversal of the tree? Write your answer here:
What is the postorder traversal of the tree? Write your answer here:
If you are answering on your own shee
give the traversal of each.
preoder
"inorder:™
postorde
Question I1. (3 marks). Binary Search Trees.
A binary search tree (BST) has 7 nodes, as shown below. The key of each node is not shown.
However, we know that the nodes have the following keys; 50. 35, 75, 30, 20, 36 and 24. Identity
the key for each node in the tree and write it inside each node.
If you are answering on your own sheets, draw the above tree and write your answers insi
cach node.


## Page 16

![Page 16](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_016.png)

Question 12. (5 marks), Recursion.
Consider the class TreeNode defined below. It represents a node in a binary tree. The root of the
tree is pointed to by root, which is also declared below.
class TreeNode (
public:
int key:
TreeNode* left;
TreeNode* right;
) :
TreeNode* root;
Write a non-member recursive function count_interior that counts the number of interior
nodes in a binary tree. You can assume all the necessary headers are included.
The function is invoked as follows:
cout ‹< "Number of interior nodes in the tree is: "
« count_interior (root) < endl;
Write your answer below.
int count_interior (TreeNode* *) {
n vour own sheets
write your function, including the header given it


## Page 17

![Page 17](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_017.png)

Question 13. (5 marks). Binary Trees.
Consider the two classes TreeNode and Tree used to implement a binary tree.
alass TreeNode 1
private:
int key:
TreeNode* left;
TreeNode* right;
public:
int getKey () const (return key:)
TreeNode* getleft() const (return left;)
TreeNode* getRight () const (return right;)
class Tree f
private:
TreeNode* root;
public:
void post () :
) :
Tree myTree; // Create a tree
1/ Code to add nodes to mytree
The method post () recursively traverses the tree rooted at root using post-order traversal. It is
invoked as myTree.post (); and prints the keys of the nodes to cout. The method must take
no arguments and must return void. Write vour answer below
ou are answering on your own sheets, write your function, including the header given i


## Page 18

![Page 18](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_018.png)

Question 14. (3 marks) Binary Search Trees.
A student, John, was asked to write a function that given a pointer to the root of' a binary tree,
checks if the binary tree is a binary search tree. It returns true if the tree is a binary search tree and
false if otherwise. John wrote the following function:
bool isBST (TreeNode* node) (
if (node == NULL) return true;
1/condition for left node
if (node->left 1= NULL && node->left-›data >= node-›data)
return false;
//condition for right node
if (node->right |= NULL && node->right-›data <= node-›data)
return false:
// Apply recursively to children
if (1sBST (node->left) &6 1sBST (node->right))
return true;
1/we made it to the end, so this 1s a BST!
return true:
However, to John's surprise he received a mark of 0 for the above function. John did not accept that
the above code has a fundamental flaw and objected to the mark of 0. You need to find and show a
binary tree to show John that his code does not retum the correct answer for your tree. You can
assume the data of each TreeNode is an integer. Depict your tree below and write integer values
for each node. Remember that John's code should retur an incorrect answer for your tree. Your
tree can have a maximum of 5 nodes. Draw your tree below.


## Page 19

![Page 19](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_019.png)

Question 15. (6 marks), Valgrind.
The following program has memory issues. The line numbers to the left are not part of' the code,
they are added to facilitate your answer.
1 #include <iostream›
2 using namespace std;
3
4 class Shape f
5
public:
string
name;
7}:
8
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24 ł:
25
27
28
29 }
9 class Mystery {
private:
int size;
Shape** arr;
public:
Mystery (int n) (
size = n;
arr = new Shape* [sizel:
for (int 1 = 0; 1 <= n; ++1) arr[1]=new Shape() :
-Mystery () {
delete arr;
int getsize() const (return size;]
Shape** getShapeArray () const (return arr;}
26 int main () {
Mystery m (10) :
return 0;
The output of valgrind is shown below and indicates the issues.
==18159== Mencheck, a memory error
detector
=18159= Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward
et al.
==18159== Using Valgrind-3.11.0 and LibVEX; rerun with -h for
copyright
info
==18159==
Command: mystery.exe
==18159=
=18159
=18159==
--18159==
Invalid write of size 8
at 0x400BOA: Mystery:: Mystery (int) (mystery.cpp:17)
by 0x4009EE: main (mystery. cpp: 27)
=18159= Address 0x4c46090 is 0 bytes after a block of size 80


## Page 20

![Page 20](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_020.png)

alloc d
==18159==
at 0x4A078FO: operator new[] (unsigned long)
(vg_replace_malloc.c: 421)
==18159=
by 0x400AB7: Mystery:: Mystery (int) (mystery.cpp: 16)
=18159-
by 0x4009EF: main (mystery. cpp: 27)
18159=
=18159== Mismatched free() / delete / delete []
18159=
at 0x4A06738: operator delete (void*)
(vg_replace_malloc.c:574)
==18159 by 0x400B4F: Mystery:: Mystery () (mystery. cpp: 20)
==18159==
by 0x400A00: main (mystery. cpp: 27)
==18159== Address 0x4c46040 is 0 bytes inside a block of size 80
alloc'd
==18159=
at 0x4A078FO: operator new[] (unsigned long)
(vg_replace_malloc.c:421)
==18159-
by 0x400AB7: Mystery:: Mystery (int) (mystery.cpp:16)
=18159=
by 0x4009EF: main (mystery. cpp: 27)
=18159-
==18159=
==18159=
HEAP SUMMARY:
==18159==
in use at exit: 88 bytes in 11 blocks
==18159=
total heap usage: 12 allocs, 1 frees, 168 bytes
allocated
==18159~
==18159=
88 bytes in 11 blocks are definitely lost in loss record
1 of 1
==18159~
at 0x4A07D73: operator new (unsigned long)
(vg_replace_malloc.c: 332)
==18159=
by 0x400A2: Mystery:: Mystery (int) (mystery.app: 17)
18159-
=18159—
by 0x4009EF: main (mystery.cpp:27)
-18159=
=18159=
#=18159~
=18159==
==18159=
==18159~
LEAK SUMMARY:
definitely lost: 88 bytes in 11 blocks
indirectly lost: 0 bytes in 0 blocks
possibly lost: 0 bytes in 0 blocks
still reachable: 0 bytes in 0 blocks
suppressed: 0 bytes in 0 blocks
==18159-
=18159== For counts of detected and suppressed errors, rerun
with: -v
==18159= ERROR SUMMARY: 3 errors from 3 contexts (suppressed: 4
from 4)
Indicate the changes required to the code to fix the issues. No changes should be made to the
main () function: all fixes must be made with changes to the class Shape and Mystery.


## Page 21

![Page 21](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_021.png)

A change must be indicated by a line number, followed by one of: Remove, Replace with or Insert
Before and finally the change itself (if applicable). Here are some examples:
• To indicate that a comment is to be inserted before the definition of class Shape, you
write:
4
Insert Before
/ This is class Shape
• Similarly, to indicate that the getsize method of Mystery should be removed, you
wrile:
22
Remove
• Finally, to indicate that the getShapeArray method of Mystery should not be const,
you write:
23
Replace
Shape** getShape Array O [return arr:)
Write your answers in the table below. You may or may not need all rows.


## Page 22

![Page 22](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_022.png)

Question 16. (3 marks). Complexity Analysis.
For each code snippet, specily the worst-case complexity, using the Big-O notation. Write the
answer in the box provided after cach code snippet.
A.
for (int 1=0; 1<n; 1++) |
for (int j=0;j*j<n; J++){
/some code with 0(1)
}
в.
for (int 1=0; 1<n; 1++) t
for (int j=0:)*j<10000000; İ++) [
/some code with 0(1)
}
c.
for (int 1=0; 1<n; 1=i*2) |
for (int j=0;j<n; j++) {
/some code with 0(1)
}
I you are answering on your own sheets, write the part label (A., B. or C.) and provide yor
answer


## Page 23

![Page 23](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_023.png)

Question 17. (6 marks) Complexity Analysis.
Two students were asked to write a recursive function that given a positive integer n, computes 2ª.
Amy wrote the following function:
int Amy (int n) {
1f (n == 0)
return 1;
else
return (Amy (n-1) + Amy (n-1)) :
}
John wrote the following function:
int John (int n) {
if (n == 0)
return 1;
else
return (2*John (n-1)) ;
Answer the following questions about code written by Amy and John.
a) Is Amy's function correct (does it compute and return 2a)? Yes or No. (circle one answer)
b) Is Jolm's function correct (does it compute and return 2")? Yes or No. (circle one answer)
c) What is the worst-case complexity of Amy's function using Big O notation?
d) What is the worst-case complexity of John's function using Big O notation?
If you are answering on your own sheets, write the part label (e.g., a), b) or c)) and provide
your answer.


## Page 24

![Page 24](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_024.png)

Question 18. (6 marks), Inheritance.
Consider the following definitions of base and derived classes. Assume the implementation of these
classes is correct even though the implementation code is not shown here.
class Base f
private:
int ID:
public:
Base () :
~Base () ;
int getID () :
virtual void print() const = 0;
class DerivedA : public Base {
private:
int R;
public:
DerivedA () ;
~DerivedA () :
int getRO
const;
void setR (int I) :
virtual void print () const;
class DerivedAA: public Deriveda (
private:
float P;
public:
DerivedAA () :
~DerivedAA () :
float getP() const;
void setP (float p) ;
virtual void print () const;
class DerivedE : public Base (
private:
int c;


## Page 25

![Page 25](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_025.png)

public:
DerivedB () :
~DerivedB () :
int getc () const:
void set (int =);
virtual void print () const;
) :
class DerivedBB : public Deriveds (
private:
float P:
public:
DerivedBB () :
~DerivedBB () :
int get () const;
void setP (float p) :
virtual void print () const:
1:
In the table below, indicate whether each group of statements (i.e., a row in the table) generates a
compiler error or not by placing an X in the appropriate column. All statements appear in the main
function of a program. Consider cach group of statements (i.c.. row in the table) by itself.
Statement
Error?
NO
Error?
A.
B.
C.
Base e;
Deriveda pri
pr = r;
Deriveda r:
Derivedaa pri
r = pr;
eriveda r
erivede c
r = c;
E.
F.
Base* elm_p:


## Page 26

![Page 26](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_026.png)

G.
H.
I.
J.
K.
DerivedA* r_P:
r_P = new DerivedAO:
Base* elm_p = new DerivedA();
DerivedAA* pr_p;
Deriveda* r_p = new DerivedAO;
pr-P = Г.Р;
DerivedAA* pr_p = new DerivedAAO:
DerivedA* r-P:
1D = pro:
r_p->getPO;
DerivedAA* pr_p = new DerivedAAO:
Deriveda* r_P;
r_P = pr_p:
r_p-›printO:
If you are answering on your own sheets, write the question label (e.g
answer as either "No Error" or "Error'
) and gi


## Page 27

![Page 27](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_027.png)

Question 19. (6 marks), Inheritance.
Consider the following classes.
#include <iostream›
#include ‹string>
using namespace std;
class person|
private:
string name;
string
address;
protected:
int id;
public:
person () (name = "EMPTY": address = "EMPTY"; id = 0;)
person (string 1 name, string 1_address, int 1_id) |
name = 1 name; address = 1 address; id = 1 id;)
vold printName () (cout «"The person's name 15 "
« name‹<endl; )
virtual void printInfo() {
cout "Person with ID "<id<<" lives at "
« address<<endl;)
void setName (string 1_name) (name = 1_ name:)
void setAddress (string 1_address) faddress = -_address;)
string getName () (return name:)
string getAddress () (return address;)
void setid (int 1id) (1d = 1_1d;)
1 :
class student: public person!
private:
float GPA:
public:
student () (GPA = 0.0;)
student (string 1 name, string address, int id,
float 1 GPA) {GPA = 1
void setGA (float 1_GPA) (GPA = 1_GPA:)
void printName () {cout ‹‹"The student's name is "
« person: : getName () ‹endl; 1
virtual void printInfo() (
cout «"Student with ID "<<1dK< " has a GPA Of "
< GPA<Cendl; }
The following expressions appear in a main function, followed by the expressions in the table
below.


## Page 28

![Page 28](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_028.png)

person P_one ("A", "123", 1) ;
person* P_ptr = 6p_one;
student s_one ("B",
"456", 2, 3.9) :
student* s_pti = as_one:
A.
B.
C.
D.
E.
F.
expression(s)
P_
one, printinto?);
P_one. printName () :
s_one printInfo () :
s_one. printName () :
p_ptr-›printName () :
p_ptr = as_one;
P_ptr-SprintName () :
p_ptr = as_one;
p_ptr-›printInfo ();
s_ptr = ap_one;
s_ptr->printName () :
If you are answering on your own sheet
answer.
What is printed by each of the
following? If it results in a compile
error, write "compile error". Evaluate
each row of the table independently.


## Page 29

![Page 29](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_029.png)

Question 20. (6 marks). Binary Trees. (Warning: Difficult)
Assume the same definition of a TreeNode that appears in Question 12. Given a pointer to the
root of a binary tree, find a subset of the nodes of the tree to meet both of the following constraints:
I) If'a node is included in this subset, its parent cannot be included in the subset.
2) There should be no other subset that meets the first constraint and the sur of the keys of the
nodes of the other subset is larger than the sum of the keys of the nodes of this subset.
Your code should return the sum of the key values of the nodes in a subset that meets the above
requirements. Three examples are provided below to help you better understand the problem. You
are allowed and encouraged to write one or more helper functions).
Both nodes with
key value of 3 as
well as the node
with key of 5 are
included in this
subset, the code
returns 11.
Only the node with
key of 5 is induded
in this subset, the
code returns 5.
Nodes with key
value of 4 and 2 are
included in this
aubet, the code
returns 6.
Write your answer below and on the overflow page if necessary.
/ Write any global variables and helper functions here
// Write the selection function here
int selectAndSun (TreeNode* root) |
If you are answering on your own sheets, write your answer, including the function header given
above.

