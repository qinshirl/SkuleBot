## Page 1

B4E11C95-984C-4556-86AA-55A6B060F38C
UNIVERSITY OF TORONTO
FACULTY OF APPLIED SCIENCE & ENGINEERING
Fourth Year - Electrical and Computer
ECE421H1 S - Introduction to Machine Learning
First name (please write as legibly as possible within the boxes)
Last name
Student Number
Calculator Type: 3
Exam Type: C
Examiners - A. Khisti, C. Lucasius
Score
FINAL EXAMINATION, April 21.2023 
DURATION: 2 and Ya hours
final-exam-25c47
#2 Page 1 of 18
01
02
03
04
05 
Total
Max 
16 
20 
20 
18 
26 
100
• 
There are 17 pages in this exam, including this one.
• 
One 8.5 x 11 aid-sheet is permitted.


## Page 2

AB1BF7DC-768A-46F8-ADF8-EFA7F3809B3D
QUESTION 1 [16 marks]
Answer the following short answer questions and justify briefly.
1.
2.
3.
4.
final-exam-25c47
#2 Page 2 of 18
[2 marks] Suppose the hypothesis sets Jfi and Jfz satisfy the relationship 
<^^2- What do we know about the relationship between the VC 
dimensions dvc(^i) and
[2 marks] Using two concepts in the course, explain why a linear hard- 
margin SVM generalizes better than a perceptron model for a d - 
dimensional input space.
[2 marks] Suppose a soft-margin SVM is used to solve a binary 
classification problem. If one of the non-margin support vectors is removed, 
would re-running the soft-margin SVM algorithm yield a different solution?
[2 marks] If it is known that the VC dimension for a particular hypothesis set 
is dye, what are all the possible break points of Jf?


## Page 3

U ■ ■ I L
E08253C7-CB8B-49E9-A527-D14AB05360E1
■rss:
5.
6.
7.
8.
□
[2 marks] Consider the soft E-M algorithm. What constraints would you add 
to the Ynj to convert it to the hard E-M algorithm?
final-exam-25c47
#2 Page 3 of 18
[2 marks] In the soft E-M algorithm, suppose the are initialized to 
where k is the number of Gaussian components. How would this affect the 
algorithm?
[2 marks] Consider a convolutional neural network with convolutional layers 
of stride 1 that classifies 224 x 224 images. What would be the receptive 
field of a stack of three layers consisting of a 3 x 3, a 5 x 5, and a 7 x 7 filter, 
respectively?
[2 marks] Consider a 2-layer MLP and a 2-layer neural network where the 
former only uses the sign function for its activation functions and the latter 
only uses the tanh function. Which one do you expect to have a higher VC 
dimension and why?


## Page 4

Sb"-
3426315E-1A23-490E-9182-4339C19DFB8A
QUESTION 2 [20 marks]
subject to; f'^'a > c
Provide the values of Q, p, f, and c.
□
□
□I-___
1. [4 marks] Formulate the Lagrange dual of the quadratic programming 
problem corresponding to this SVM:
final-exam-25c47
#2 Page 4 of 18
Xi = [0 0f,yi = +l 
X2 = [11]'^, 72 = +1 
X3 = [0 1]\ 73 = -1 
X4 = [1 0]\ 74 = -1
\Ne are going to apply a hard-margin SVM with a radial basis function kernel 
K(x,x') = 
to approximate the XOR function. Consider the training
dataset with TV = 4 given as follows:


## Page 5

5DD3A8B9-945E-4267-9AC6-CD38EB0D2DD0
final-exam-25c47
#2 Page 5 of 18
2. [4 marks] Suppose the solution to the QP problem from the previous 
question is given by a* = [2.5027 2.5027 2.5027 2.5027]"^. Which data 
points correspond to the support vectors?
3. [6 marks] Suppose we have an arbitrary data point x = [xj Xz]^. Write the 
optimal hypothesis function given by the hard-margin SVM, ^(xi,X2). 
explicitly as a function of Xj and X2.


## Page 6

857D1DBA-95DE-4A2D-A9BB-7020911667EA
final-exam-25c47
#2 Page 6 of 18
4. [6 marks] Show that g = 9 corresponds to the decision 
boundary of the final hypothesis found in the previous part. Then use this 
information to sketch the decision boundary, including the labelled training 
dataset.


## Page 7

07402D77-6531-42C6-B82F-9617D32DBC27
QUESTION 3 [20 marks]
Xi = [0.0 O.O]"^, X2 = [2.0 1.5]'^, X3 = [0.0 0.5]’^
X4 = [1.0 l.Ol’T, xg = [0.5 0.0]T
final-exam-25c47
#2 Page 7 of 18
We would like to use unsupervised learning for outlier detection. We are given 
the following unlabelled dataset as follows:
1. [8 marks] Use Lloyd’s Algorithm to solve the k-means clustering problem 
with k = 2. Assume an initial partition of {xi,X2,X3} and {x4,X5}. Assuming 
the cluster with the minority of the points contains the outliers, identify 
which of the 5 points are outliers.


## Page 8

s
7BA7BFC1-A9ED-4349-85D6-DC9EEA1F1BBA
Hint: If A =
final-exam-25c47
#2 Page 8 of 18
2. [8 marks] We will now try to solve the problem of outlier detection with a 
single component GMM. Compute the probability density values of each of 
the five points. Identify the outliers by setting a threshold of 0.3 (any data 
point with a density less than 0.3 is considered an outlier).
a 
c
fol 
d.
-i,]
a J
lAI l-c
■ri


## Page 9

FF8F423F-052B-476D-9983-814B4B78CBAA
final-exam-25c47
#2 Page 9 of 18
3. [4 marks] Suppose you want to solve the outlier detection problem by 
using a GMM with two components instead of only one. Outline clearly 
what steps you would take, including key concepts in the course.


## Page 10

63D4BFEB-8531-4424-95EA-80BD01239C7E
QUESTION 4 [18 marks]
Consider a binary classification problem in one dimension. Let be the 
hypothesis class of all Q-th order polynomial classifiers where any h 6 Hq can be 
expressed as:
1. [4 marks] Show that there exists a dataset containing Q + 1 points that can 
be shattered by Construct the hypothesis class associated with each 
possible label sequence.
final-exam-25c47
#2 Page 10 of 18
/ Q \ 
h(x) = sign^c,x‘ 
)


## Page 11

22CD7953-FD9C-4080-A8C0-834057F57B13
I
E
□
□
□
2. [4 marks] Show that it is impossible to find a dataset containing Q + 2 
points that can be shattered by Xq . Construct a label sequence that 
cannot be realized by any hypothesis class. Use the result of this question 
and the previous one to conclude that dvc(^Q) = Q + 1.
final-exam-25c47
#2 Page 11 of 18


## Page 12

57EB8271-E90E-4D8A-B74D-F10E31E6D7B9
9
Hint: Start by incrementing your guesses for by 10,000.
□
final-exam-25c47
#2 Page 12 of 18
3. [4 marks] Suppose we want to find the minimum number of points Nj^in 
that guarantees the following:
With a probability of at least 90%, the generalization error of IC2 (i.e., the 
set of all 2"^ order polynomial classifiers) is at most 0.1.
[■0
What is the value of


## Page 13

2A9C6DAC—207C-44A4-84FD—18FE59E31EA7
4. [6 marks] Consider a modified version of where we constrain the 
constant term to be 0. It is given as:
Find the growth functions 
and by drawing all
possible dichotomies on three separate graphs. Then determine dye(^2) 
and relate it to dvc(^2)-
final-exam-25c47
#2 Page 13 of 18
X2 =


## Page 14

s?
6D0D1769-D7B7-4529-8A42-174828177EE6
0
±1
QUESTION 5 [26 marks]
□
1. [5 marks] Explain how you would choose an appropriate value for the 
regularization constant using validation techniques.
final-exam-25c47
#2 Page 14 of 18
We would like to use linear regression with regularization to approximate a target 
function y = /(x) where x g is an augmented vector. Assume you are 
provided a dataset matrix X g iRWx(d+i) and a target vector y G IR".


## Page 15

1608353C-5070-48EC-A706-EBE84315D377
final-exam-25c47
#2 Page 15 of 18
n
2. [5 marks] Find the final hypothesis function, by minimizing the in- 
sample error function Ei^ = ||Xw - yll^ -i- A||w||2 with respect to w, where 
w E denotes the parameters of the model and A > 0 is the 
regularization constant.


## Page 16

4F6B5D50-A007-43F4-B750-FC5FAC6A11BF
Hints:
,A
final-exam-25c47
#2 Page 16 of 18
3. [8 marks] We will now simplify the above problem. Assume the input 
dimension is one and the input variable is uniformly distributed in [-1,1], 
We are given a training dataset with two points D = (xj, Xz), and the target 
function we are trying to approximate is /(x) = x^.
Assuming no regularization, use your answer from the previous question 
to compute the average final hypothesis function ^(x).
lI 
fl 
L' 
J
-1 = j_r d 
|A| L-c
a J
a^-b^ = Qa-bXa^ + ab + b^y, 
If A = a b 
c d


## Page 17

D2F6A8DB-A88E-4128-AD27-E4FC1DDC0ECE □
□
4. [8 marks] Assuming the same simplified problem from the previous 
question, compute the bias bias, variance var, and expected out-of-sample 
error lED[£out(5^°^)]-
final-exam-25c47
#2 Page 17 of 18
V


## Page 18

BB644A18-1A61-455A-890C-A33F88886D92
final-exam-25c47
#2 Page 18 of 18

