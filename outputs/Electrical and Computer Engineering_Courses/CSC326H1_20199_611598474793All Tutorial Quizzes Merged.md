## Page 1

ECE326 Quiz 1, Fall 2019
Student Number:
Write a move assignment operator.
Student Name:
class Foo {
    string* ptr;
public:
    Foo (const string& str) : ptr(new string(str)) {}
    ~Foo () { delete ptr; }
    Foo (Foo&& x) : ptr(x.ptr) { x.ptr=nullptr; }
    // move assignment
    Foo& operator=(Foo&& x) {
    }
    const string& content() const { return *ptr; }       
    Foo operator+(const Foo& rhs) {
return Foo(content()+rhs.content());
    }
};
// in main
Foo foo ("Exam");
Foo bar = Foo("ple");   
foo = foo + bar
  // move construction
// move assignment
/* if this and x are not same object */
if (this != &x) {
    /* delete existing (prevent memory leak) */
    delete ptr;
    /* move over x's resource to this */
    ptr = x.ptr;
    /* set x.ptr to null, otherwise when 
     * x is deleted so will the content 
     * that we moved over! */
    x.ptr = nullptr;
}
/* assignment operator returns itself */
return *this;


## Page 2

ECE326 Quiz 2, Fall 2019 
 
Name:  
 
 
 
 
 
Student Number: 
Consider the line below as input for command line: 
python quiz.py a b c d e f g h i j 
Also, we have a file named "names.txt" at the same path, with 10 full names in 10 lines. The 
goal is to associate the command line arguments with the names in names.txt by their order of 
appearance. Please complete dictionaryBuilder function in a way that we have the output as 
below (Note: don’t let the Trap shown in the code produce an error): 
a       Caden Bradley 
b       Kit Roberts 
c       Rene West 
(so on… up to 10 lines) 
---------------------------------------------------------------------- 
from collections import defaultdict 
import sys 
def dictionaryBuilder(argv): 
    #  ***** Start your code here ***** 
    file = open('names.txt') 
    # Define a dictionary with string as default type 
    myDictionary = defaultdict(str) 
    # Define a counter to use as index for arguments passed to the program 
    counter = 1 
    for line in file: 
        myDictionary[argv[counter]] = line 
        # Add to the counter to use next argument for next name 
        counter += 1 
    file.close() 
 
 
 
 
 
 
    # ***** End of your code ***** 
    return myDictionary 
# If we have more than 1 argument passed to the program: 
if len(sys.argv) >= 2: 
    for key,values in dictionaryBuilder(sys.argv).items(): 
        print(str(key) + "\t" + values) 
    # Trap! printing a non-existed index of dictionary 
    print(namesDictionary['z'])


## Page 3

ECE326 Quiz 3, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
Please complete the Factorial function below using a Top-Down approach. Note: use 
factorialTable dictionary for memoization. 
------------------------------------------------------------------------------- 
Def fact(n):  
 
 
# Start your code here 
 
 
 
 
 
If n in factorialTable:  
    
 
 
Return factorialTable[n]  
   
 
Else:  
    
 
 
Result = n * fact(n-1)  
    
 
 
factorialTable[n] = Result  
    
 
 
Return Result 
 
 
 
# End your code here 
 
factorialTable = { 0: 1 } 
 
Please note that, there is no need to use “global” keyword for facrotialTable 
inside our function because no reassignment of the global variable is being 
done.


## Page 4

ECE326 Quiz 4, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
Please do the following for the code below: 
1. Draw the inheritance graph 
2. Write the resolution order (Just put the name of classes in order of resolution)  
3. Write the expected output 
------------------------------------------------------------------------------- 
class A: 
    def whoAmI(self): 
        print("This is A") 
class B(A): 
    def whoAmI(self): 
        print("This is B") 
class C(A): 
    pass 
class D(B,C): 
    pass 
class E(C): 
    def whoAmI(self): 
        print("This is E") 
class F(D,E): 
    pass 
 
myObj = F() 
myObj.whoAmI() 
 
 
 
 
 
 
 
 
 
Solution: 
1. 
 
 
 
2. Method Resolution Order: FDBECA 
3. Output: 
This is B


## Page 5

ECE326 Quiz 5, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
1. For each piece of code below, first, mention if the code works or not, in case of error, 
write down the reason, in case of working code, write down the output. 
Code 
Works? 
Yes/No 
Reason for error/output 
if(print(2)): 
 
print(333) 
else: 
 
print(555) 
Yes 
555 
 
 
Note: print returns None 
if(print = 2): 
 
print(333) 
No 
 
 
Note: you cannot use assignment as an expression in Python 
pp = print 
print =3 
if(print == 3): 
 
pp(444) 
Yes 
444 
 
2. Please write down the output for each piece of code below: 
Code 
Output 
variable = 0  
 
tmp = variable 
tmp += 1 
print(variable) 
0 
variable = [1,2,3,4] 
tmp = variable 
tmp.append(5) 
print(variable) 
[1,2,3,4,5] 
variable = [1,2,3,4] 
tmp = variable.copy() 
tmp.append(5) 
print(variable) 
[1,2,3,4]


## Page 6

ECE326 Quiz 6, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
1. Please write a template struct including the functions and operator overrides needed for 
the code below to run properly. 
 
// start your code here 
template<typename T> 
struct Tuple { 
 
T a, b; 
 
 
Tuple(T && a, T && b) 
 
 
: a(std::move(a)) 
 
 
, b(std::move(b)) 
 
{} 
 
Tuple<T> operator+(const Tuple<T> & rhs) { 
 
 
a += rhs.a; 
 
 
b += rhs.b; 
 
 
return *this; 
 
} 
}; 
 
 
 
 
 
 
int main() 
{ 
 
Tuple<int> tuple1 = Tuple<int>(2,2); 
 
Tuple<int> tuple2 = Tuple<int>(4, 5); 
 
Tuple<int> summation = tuple1 + tuple2; 
 
std::cout << summation.a << ',' << summation.b;  
     
return 0; 
}


## Page 7

ECE326 Quiz 7, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
1. The goal is to write a debugger decorator. When we use this decorator for a function, it 
prints out the input arguments’ and output’s types and values like below: 
inputs: 
<class 'int'>:123 
<class 'str'>:abc 
<class 'float'>:1.0 
output: 
<class 'float'>:1.0 
Please complete the decorator’s code. 
--------------------------------------------------------------------------------------------------------------- 
def debugger_decorator(fun): 
// start your code here 
 
def debugger(*args): 
 
 
ret = fun(*args) 
 
 
print("inputs:") 
 
 
for arg in args: 
 
 
 
print(str(type(arg)) + ":" + str(arg)) 
 
 
print("output:") 
 
 
print(str(type(ret)) + ":" + str(ret)) 
 
 
return ret 
 
return debugger 
 
 
 
 
 
 
 
@debugger_decorator 
def test(*args): 
 
return 1.0 
 
 
test(123,'abc',1.0)


## Page 8

ECE326 Quiz 9, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
Please write a variadic template function printAll to print all the arguments separated 
by space (See the usage example in main function below).  
// Start your code here 
void printAll() 
{ 
} 
 
template<typename T, typename ... Args> 
void printAll(T first, Args ... args)  
{ 
 std::cout << first << " "; 
 printAll(args ...); 
} 
 
 
 
 
 
 
 
 
 
 
 
 
int main() { 
    //output: Jack Connor 25 1.75 
    printAll("Jack","Connor",25,1.75);  
 
    //output: 1 2 test 
    printAll(1,2,"test");  
    return 0; 
}


## Page 9

ECE326 Quiz 10, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
Complete the match operator for the FizzBuzz code to work properly. 
FizzBuzz instructions: 
• Print each x between 1 to 100. 
• For multiples of 3, print “Fizz” instead of the number 
• For multiples of 5, print “Buzz” instead of the number 
• For multiples of both 3 and 5, print “FizzBuzz” instead of the number 
 
 
fn main() { 
    for x in 1 .. 100 { 
        let res = (x % 3, x % 5, x % 15); 
        match res { 
 
 
 
 
            (0, 0, 0) => println!("FizzBuzz"), 
            (_, 0, _) => println!("Buzz"), 
            (0, _, _) => println!("Fizz"), 
            _ => println!("{}", x), 
 
 
 
 
 
 
 
 
 
 
        } 
    } 
}


## Page 10

ECE326 Quiz 11, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
Given a vector as an input, we want to write a function to build a HashMap from that 
vector. We want to use entries of the vector as keys, and number of occurrence of each 
entry as value of that key (see the example in main function). Please complete the 
buildCounterDictionary() function. 
 
use std::collections::HashMap; 
fn buildCounterDictionary(vec: &Vec<i32>) -> HashMap<&i32,i32> { 
 
 
    let mut counter = HashMap::new(); 
    for i in vec { 
 
 
let count = counter.entry(i).or_insert(0); 
 
 
*count += 1;  
    } 
    Counter 
 
 
 
 
 
 
 
 
 
} 
 
fn main() { 
    let v1 = vec![100, 32, 57, 57, 2, 3, 3, 32]; 
    let counter1 = buildCounterDictionary(&v1); 
    let v2 = vec![10, 10, 10, 20]; 
    let counter2 = buildCounterDictionary(&v2); 
 
    //output: {100: 1, 3: 2, 57: 2, 2: 1, 32: 2} 
    println!("{:?}",counter1);  
    println!("{:?}",counter2); // output: {10: 3, 20: 1} 
}


## Page 11

ECE326 Quiz 12, Fall 2019 
 
 
Name:  
 
 
 
 
 
Student Number: 
 
Given two increasing series generators, generator1() and generator2(), we want to 
merge these two series into another one using a third generator. Please complete 
sortedSeriesGenerator() implementation. Note that you should eliminate duplicates 
(e.g. the number 10 should not come up twice) 
 
def generator1(): 
    i = 1 
    while True: 
        yield i 
        i += 7 
 
def generator2(): 
    i = 2 
    while True: 
        yield i 
        i += 3 
 
  
 
 
 
def sortedSerieGenerator(): 
    gen1, gen2 = generator1(), generator2() 
  
    # complete the implementation 
 
 x = next(gen1) 
 y = next(gen2) 
 while True: 
  
if x > y: 
  
 
yield y 
  
 
y = next(gen2) 
  
elif y > x: 
  
 
yield x 
  
 
x = next(gen1) 
  
else: 
  
 
yield x 
  
 
x = next(gen1) 
  
 
y = next(gen2) 
 
 
seriesGenerator = sortedSerieGenerator() 
for i in range(1,10):  
 
 
 print(next(seriesGenerator))

