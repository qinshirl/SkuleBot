## Page 1

![Page 1](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_001.png)

UNIVERSITY OF TORONTO 
FACULTY OF APPLIED SCIENCE AND ENGINEERING
FINAL EXAMINATION, December 2022 
Duration: 2.5 hours 
Second Year - ECE
ECE244H1 - Programming Fundamentals 
Examiner - D. Yuan, SK Rahman, S. Bhadra
This exam is open book, open note.
If any of the questions appear unclear or ambiguous to you, then make any assumptions you 
need, state them and answer the question that way. If you believe there is an error, state what 
the error is, fix it, and respond as if fixed.
Be brief and specific. Clear, concise answers will be given higher marks than vague, wordy 
answers. Marks will be deducted for incorrect statements.
You will receive 20% of the marks for each (sub) question if you leave the answer blank.
There are 29_ total numbered pages, 10 Questions.
Name:
Student Number:
Total Marks
Marks Received
Question 1
5
Question 2
8
Question 3
5
Question 4
12
Question 5
10
Question 6
12
Question 7
10
Question 8
5
Question 9
9
Question 10
24
Page 1 of 29 pages


## Page 2

![Page 2](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_002.png)

In this exam, you can assume the new operator will always succeed (the system won't run out 
of memory).
Question 1 [5 marks, 1 mark each]: Multiple choice (provide all correct answers), no 
explanation needed.
(1) Which of the following is good practice for developing a high-quality and maintainable 
program?
(a) Never write comments to shorten coding time.
(b) Using shortest names (1 or 2 characters) for variable namings to improve code 
cleanness.
(c) Thoroughly test the program after coding.
(2) True or False? The derived class will always contain all the member variables from the base 
class.
(a) True
(b) False
(3) True or False? Every class has a copy constructor, even though it might not be explicitly 
defined.
(a) True
(b) False
(4) Which of the following is not true about quick sort?
(a) The average time complexity of quick sort is 0{nlogn).
(b) The worst-case time complexity of quick sort is 0(nlogn).
(c) Quick sort is the fastest general sorting algorithm used by modern computer programs.
(5) Assume algorithm X has a time complexity of 0(n), and algorithm Y has a time complexity 
of 0(nlogri). Given a sufficiently large input size (i.e., n>100000), which of the following 
behavior is expected?
(a) X and Y are equally efficient.
(b) X is more efficient than Y.
(c) Y is more efficient than X.
Page 2 of 29 pages


## Page 3

![Page 3](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_003.png)

Question 2 [8 marks]: Class
Sarah, a new intern in Macrosoft, is asked to debug the following program.
#include <iostream >
using nam espace std;
class Superint { 
int* p; 
public:
Superlnt(int i) { 
p = new int;
*p = i;
};
~Super'Int() { 
delete p;
}
void set_val(int i) { *p = i; } 
int get_val() { return *p; }
};
int m ain() { 
Superint x(3); 
Superint y(x);
cout << "x: " << x.get_val() << endl; 
cout << "y: " << y.get_val() << endl;
y.set_val(5);
cout << "x: " << x.get_val() << endl; 
cout << "y: " << y.get_val() << endl;
return 0;
}
a. [2 marks] What will be printed into stdout (i.e., terminal) before the program crashes?
Page 3 of 29 pages


## Page 4

![Page 4](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_004.png)

b. [2 marks] Sarah also realized the program crashes with a segmentation fault (i.e., segfault) 
after it executes all the print statements. What is the root cause behind the crash?
c. [4 marks] Will, a senior programmer in Macrosoft, tells Sarah that all the bugs in this program 
can be fixed by adding one additional public member function to the Superint class. Please write 
the implementation of this member function, including both header and its body. Your 
implementation should be no more than 5 lines of code.
Page 4 of 29 pages


## Page 5

![Page 5](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_005.png)

Question 3 [5 marks]: Given the following program that calls a recursive function. Write the 
output printing to stdout. You may not need to fill the entire table.
#include <iostreani> 
using namespace std;
void fonk_bom b(int n) { 
if (n <= 0) { 
return;
}
cout << n << endl; 
for (int i = 0; i < n; ++i) { 
forl<_bom b(n - 1);
}
}
int main() { 
fork_bomb(3); 
return 0;
}
Line
Output
1
2
3
4
5
6
7
8
9
10
11
12
13
Page 5 of 29 pages


## Page 6

![Page 6](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_006.png)

Question 4 [12 marks, 4 marks each]: Pointer and Reference
Read the following three functions and answer the following questions:
int foo(int a) { 
a += 1; 
return a;
}
int bar(int* a) { 
*a += 1; 
return *a;
}
int zoo(int& a) { 
a += 1; 
return a;
}
a. Given the following function m1(), what is the output if it executes?
void m l() { 
int X = 0; 
int y = 0; 
int* p = &XJ 
int* q = &y;
*p += foo(x) + zoo(y);
*q += foo(y) + zoo(x); 
cout << "Check point 1:" << endl; 
cout << "x: " << X << endl; 
cout << "y: " << y << endl;
}
Line
Output
1
2
3
Page 6 of 29 pages


## Page 7

![Page 7](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_007.png)

b. Given the following function nn2(), what is the output if it executes?
void m 2() { 
int X = 0; 
int y = 0; 
int* p = &x; 
int* q = &y;
X += foo(*q) + bar(p);
y += foo(*p) + bar(q);
cout << "Check point 2:" << endlj
cout << "x: " << X << endl;
cout << "y: " << y << endl;
}
Line
Output
1
2
3
c. Given the following function m3(), what is the output if it executes?
void m 3() { 
int X = 0; 
int y = 0; 
int* p = &x; 
int* q = &y;
*p += zoo(y) + bar(q);
*q += zoo(x) + bar(p); 
cout << "Check point 3:" << endl; 
cout << "x: " << X << endl; 
cout << "y: " << y << endl;
}
Line
Output
1
2
3
Page 7 of 29 pages


## Page 8

![Page 8](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_008.png)

Question 5 [10 marks]: Inheritance
The University of Toronto wants to manage students from different departments using a C++ 
program. Students from all the departments will share the following base class:
class student { 
protected: 
string nam e; 
int id; 
public:
student(const strings nam e_, int id_) : 
nam e(nam e_), id(id_)
{
cout << "student" << endl;
};
virtual void print_server() = 0; 
virtual void print_departm ent() = 0;
string get_nam e() { return nam e; }
int get_id() { return id; }
};
Derived from student class, the programmers then write another class for engineering students. 
All engineering students have access to the ECF server:
class eng_student : public student { 
protected:
int ecf_id; 
public:
eng_student(const strings nam e_j int id_, int ecf_id_) : 
student(nam e_, id_)j ecf_id(ecf_id_)
{
cout << "eng student" << endl;
};
virtual void print_server() {
cout << nam e << " logs into ecf." << endl;
}
int get_ecf_id() { 
return ecf_id;
}
};
Page 8 of 29 pages


## Page 9

![Page 9](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_009.png)

Derived from eng_student, programmers then write two classes for ECE students and MIE 
students. Unlike MIE students, ECE students have their designated server called UG server:
class ttiie_student : public eng_student { 
public:
mie_student(const strings name_j int id_, int ecf_id_) : 
eng_student(name_, id_, ecf_id_)
{
cout << "m ie student" << endl;
};
virtual void print_departm ent() {
cout << nam e << " is a m ie student." << endl;
}
};
class ece_student : public eng_student { 
private:
int ug_id; 
public:
ece_student(const strings nam e_, int id_, int ecf_id_, int ug_id_) : 
eng_student(nam e_j id_j ecf_id_)j ug_id(ug_id_)
{
cout << "ece student" << endl;
};
virtual void print_server() {
cout << nam e << " logs into ug." << endl;
}
virtual void print_departm ent() {
cout << nam e << " is an ece student." << endl;
}
int get_ug_id() { 
return ug_id;
}
}J
In addition, programmers write a new derived class for Computer Science (CS) students. Unlike 
engineering students, they use Markus servers instead of ECF servers:
Page 9 of 29 pages


## Page 10

![Page 10](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_010.png)

class cs_student : public student { 
protected:
int m arkus_id; 
public:
cs_student(const strings nam e_, int id_j int m arkus_id_) : 
student(nam e_j id_)j m arkus_id(m arkus_id_)
{
cout << "cs student" << endl;
virtual void print_server() {
cout << nam e << " logs into m arkus." << endl;
}
virtual void print_departm ent() {
cout << nam e << " is an cs student." << endl;
}
int get_m arkus_id() { 
return m arkus_id;
}
};
Read the implementations of these five classes carefully and answer the following questions.
a. [2 marks] You write the following piece of code to declare four students. However, you get a 
compile-time error. Why doesn't it compile? (Note: you don’t need to fix anything in the class 
declarations and implementations given above.)
cs_student A("A", 0^ 10); 
ece_student B("B", 1, 11, 0); 
eng_student H("H", 3, 13);
Page 10 of 29 pages


## Page 11

![Page 11](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_011.png)

b. [4 marks] Now, an array named student_list is declared and initialized as follows. Write 
the output generated by std::cout. (You might not need to fill the whole table.)
student* student_list[4] = {
new cs_student("Leo"j 0, 10)^ 
new ece_student("Bill"j 1, llj 0)^ 
new m ie_student("Ellie", 2, 12), 
new ece_student("Haley", 3, 13, 1)
};
Line
Output
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
Page 11 of 29 pages


## Page 12

![Page 12](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_012.png)

c. [4 marks] After the student_list initialized in question b, the following for' loops will be 
executed. What will be the output generated by these two loops? Fill in your answers in the 
following table. Again, you might not need all the rows.
cout << "Depar'tment; " << endl; 
for (int i = 0; i < 4; ++i) {
student_list[i]->print_departm ent();
}
cout << "Server: " << endl; 
for (int i = 0; i < 4; ++i) { 
student_list[i]->print_server();
}
Line
Output
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
Page 12 of 29 pages


## Page 13

![Page 13](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_013.png)

Question 6 [12 marks]: Complexity Analysis
Determine the worst-case time complexity (expressed in big-0 notation) for each of the program 
segments below as a function of the size of the input n. Write the details of your analysis and 
clearly indicate your final result.
a. [3 marks]
void foo(int n) {
for (int i = 0; i < nj ++i) {
for (int j=i-4;j<i+4; ++j) { 
for (int k = 0; k < n * n; ++k) { 
cout << i + j + k << endl;
}
}
}
}
b. [3 marks] 
void ban(int n) {
for (int i = 0; i < nj ++i) {
for (int j = 0; j < i * n; ++j) { 
0(1);
}
}
}
Page 13 of 29 pages


## Page 14

![Page 14](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_014.png)

c. [6 m arks]
void expelliarnius(int n) { 
if (n <= 0) return; 
int sum = 0;
for (int i = 0; i < n; ++i) { 
sum += i;
}
cout << sum << endl; 
expelliarm us(n - 1); 
expelliarm us(n - 1);
}
Page 14 of 29 pages


## Page 15

![Page 15](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_015.png)

Question 7 [10 marks]: Linked List
A sorted linked list is sorted if the value of nodes monotonically increases from the head. For 
example, the following list is sorted:
2
5
7
10
15
Given two sorted linked lists with their head pointers, write a function to merge two lists into 
one and return the head of the new list. To get a full mark, your function needs to be recursive. 
The merged list should be made by splicing together the nodes of the first two lists, meaning 
that you should not create any new nodes. The definition of ListNode is given below. You 
can assume the list ends with NULL.
class ListNode { 
ListNode* next; 
int data; 
public:
ListNode(int data_) { 
data = data_; 
next = NULL;
}
ListNode* get_next() { return next; }
void set_next(ListNode* next_) { next = next_; }
int get_data() { return data; }
};
// Return the head of the m erged list.
// Feel free to use the next page.
ListNode* m erge(ListNode* a, ListNode* b) {
Page 15 of 29 pages


## Page 16

![Page 16](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_016.png)

Page 16 of 29 pages


## Page 17

![Page 17](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_017.png)

Question 8 [5 marks]: Binary Search Tree and Tree Traversal
Draw a binary search tree that results in the following post-order traversal: [ 1,4, 3, 5, 2 ]
Page 17 of 29 pages


## Page 18

![Page 18](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_018.png)

Question 9 [9 marks]. Binary Tree and Recursion
A binary tree is symmetric if the root node’s left subtree is exactly a mirror reflection of the right 
subtree. For example, the tree on the left is symmetric, but the tree on the right is not.
This tree is symmetric
Now, you are asked to complete the function is_symmetric. It should return true if and only if 
the root is a symmetric tree. You should fill out the recursive helper function 
is_syttimetr'ic_helper' to make is_symmetric work as expected. Hint: you should write less 
than 15 lines of code.
This tree is not symmetric
/* Definition of the tree node */
class TreeNode {
public:
int data; 
TreeNode* left; 
TreeNode* right;
};
/* Recursive helper */
bool is_symtnetric_helper(TreeNode* left, TreeNode* right);
bool is_sym m etric(TreeNode* root) { 
if (root == NULL) { 
return true;
}
return isSym m etricHelper(root->left, root->right);
}
Complete the helper in the next page.
Page 18 of 29 pages


## Page 19

![Page 19](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_019.png)

// Com plete this recursive helper.
bool is_sym m etric_helper(TreeNocle* left^ TreeNode* right) {
Page 19 of 29 pages


## Page 20

![Page 20](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_020.png)

Question 10 [24 marks]. Hash Table and Programming
Thanks to your previous implementation of the VTuber, it became an instant modern classic. 
With great popularity comes greater responsibility. Now there are more than 300,000 VTubers 
streaming on the MeTube, and your engineering manager asks you to implement a data 
structure that allows users to quickly lookup whether a specific Vtuber is currently 
live-streaming.
A naive solution would be using an array of 300,000 entries, with each entry holding a boolean 
variable indicating whether the corresponding Vtuber is live-streaming or not. However, there 
are two major problems:
1. Users can only query the database with Vtubers’ names, not some internal ids.
2. Only -20% of total Vtubers are streaming at any given time, so most array entries are 
inactive. However, you’d like to maintain a lookup time that is approximately 0(1).
Now you suddenly recall that in ECE244 you learned the hash table, which resolves collisions 
with chaining. The hash table would suit your needs perfectly. Even better, you can use an 
existing linked list implementation written by your new colleague.
The following is the class declaration of the linked list. Assume that it works correctly and 
encapsulates all the operations your hash table may need. Read it carefully, as you will need it 
to build your VTubers hash table later. Remember, it will not allocate any list node 
automatically, and only the destructor will deallocate list node memory.
using nam espace std;
class ListNode { 
public:
ListNode(const string& nam e_) { 
nam e = nam e_; 
next = NULL;
};
string nam e; 
ListNode* next;
};
class LinkedList { 
private:
ListNode* head; 
public:
// Default constructor: initialize the head to NULL. 
LinkedListO ;
Page 20 of 29 pages


## Page 21

![Page 21](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_021.png)

// Return true if and only if the list is em pty, 
bool is_em pty();
// Insert the given node to the head of the list. 
// Tim e com plexity: 0(1) 
void insert(ListNode* node);
// Traversing from  the head. Rem ove the first node found with the given 
// nam e from  the list. The rem oved node is NOT deallocated.
// Returns this node (or NULL if the nam e is not found).
// Tim e com plexity: 0(n)
ListNode* rem ove(const strings nam e);
// Return true if there exists at least one node with the given nam e.
// Tim e com plexity: 0(n)
bool find(const strings nam e);
// Rem ove the current head node from  the linked list, 
// and return it.
// M ove the head one node forward.
// Tim e com plexity: 0(1)
ListNode* pop_head();
// Destructor: Properly deallocate all the nodes. 
~LinkedList();
Also, you are given a string hash function, which uses a secret algorithm to turn the given string 
into a non-negative integer value. You can safely assume that given the same string inputs, the 
output value is always the same. However, two different strings may be turned into the same 
number.
int string_hash(const strings name);
And finally, here is how the hash table is declared. It stores all the names of active VTubers at a 
given time, using the name as a unique key. The hash table solves collisions by chaining 
using the linked list.
#define INIT CAPACITY 32
class HashTable { 
private:
// Array of Linked List: resolving collisions by chaining
Page 21 of 29 pages


## Page 22

![Page 22](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_022.png)

LinkedList** table;
// The length of the table array, 
int table_slot_size;
// Keep track of how m any elem ents (nam es) are in the hash table 
int num _elem ents;
int get_hash_index(const strings nam e) { 
return string_hash(nam e) % table_slot_size;
}
public:
// Constructors and destructors.
HashTableO ;
-HashTableO ;
// Hash table m ethod, 
bool exist(const strings nam e); 
bool insert(const strings nam e); 
bool rem ove(const strings nam e);
bool change_nam e(const strings old_nam ej const strings new_nam e);
};
Essentially, the hash table should be similar to what has been discussed during the lecture. The 
following diagram should help you visualize what this hash table looks like:
table
(LinkedList**)
LinkedList
NULL
next
next
head
name
name
0
ListNode
ListNode
1
NULL
Hash 
Index 2
NULL
3
NULL
next
head
name
ListNode
LinkedList
Page 22 of 29 pages


## Page 23

![Page 23](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_023.png)

When a VTuber goes online for streaming, insert() should be called to bring the name into the 
hash table. When the VTuber goes offline, remove() method should be called to remove the 
name from the hash table. The constructor and exist () methods are already implemented as 
shown below. They should help you clarify how the hash table works.
HashTable::HashTable() {
table = new LinkedList*[INIT_CAPACITY]; 
table_slot_size= INIT_CAPACITY; 
num _elem ents = 0;
for (int i = 0; i < table_slot_size; ++i) { 
table[i] = NULL;
}
}
bool HashTable::exist(const strings nam e) { 
int idx = this->get_hash_index(nam e); 
if (table[idx] == NULL) { 
return false;
}
return table[idx]->find(name);
}
a. [12 marks] Implement the insert () method of the hash table. The insert should fulfill the 
following requirements:
1) You should maintain the unique name property. If the name already exists in the hash 
table, you should return false. Otherwise, allocate a list node for the string and insert it 
into the correct list, and return true.
2) To address the collision, your hashtable should dynamically grow at run time. 
Specifically, when you try to insert a new name but the value of num_elements will 
become equal to or larger than table_slot_size/2, you should double 
table_slot_size and allocate a new table with the updated size. Then, you should 
move all the existing names from the old table to the newly allocated table, and 
deallocate the old table.
Notice that the hash index is directly related to the slot_list_size, so the hash index 
of the same name can be changed when moving from one table to another.
3) You can add additional member functions if you need to.
4) Your code should not trigger any segmentation fault, and it should not leak memory.
You can define helper functions if you find them useful. You can make helpers as member 
functions if you think that would be necessary.
Page 23 of 29 pages


## Page 24

![Page 24](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_024.png)

// Im plem ent bool HashTable::insert(const strings nam e), and define 
// any helper functions here.
Page 24 of 29 pages


## Page 25

![Page 25](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_025.png)

Page 25 of 29 pages


## Page 26

![Page 26](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_026.png)

b. [4 marks] Implement the remove method. Return true if the given name exists and is 
successfully removed, otherwise, return false. Your code should not trigger any segmentation 
fault, and it should not leak memory.
bool HashTable::remove(const string& name) {
Page 26 of 29 pages


## Page 27

![Page 27](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_027.png)

c. [4 marks] Implement the change_name method. It removes the old_natne and inserts the 
new_name. Return true if successful. Otherwise, it returns false either when the old_name 
doesn’t exist, or the new_natne is the same as any existing name. Your code should not trigger 
any segmentation fault, and it should not leak memory. Hint: you can use the function you 
implemented in the previous questions.
bool HashTable::change_name(const strings old_name, const strings new_name) {
Page 27 of 29 pages


## Page 28

![Page 28](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_028.png)

d. [4 marks] Implement the destructor of HashTable. It should deallocate the table array and all 
the lists. Your code should not trigger any segmentation fault, and it should not leak memory.
HashTable::~HashTable() {
Page 28 of 29 pages


## Page 29

![Page 29](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_029.png)

This is the end of the exam. This page is intended to be left blank.
Page 29 of 29 pages

