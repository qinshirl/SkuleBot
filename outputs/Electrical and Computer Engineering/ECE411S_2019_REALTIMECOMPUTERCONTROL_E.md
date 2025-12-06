## Page 1

![Page 1](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_001.png)

UNIVERSITY OF TORONTO 
FACULTY OF APPLIED SCIENCE AND ENGINEERING 
FINAL EXAMINATION - APRIL 15, 2019 
ECE411S - REAL-TIME COMPUTER CONTROL 
III-AECPEBASC, III-AEELEBASC, IV-AEESCBASEB, IV-AEESCBASER 
III-AECPEBASC, III-AEELEBASC, IV-AEESCBASEB, IV-AEESCBASER 
EXAMINER - Prof. L. Pavel 
SURNAME 
GIVEN NAME 
STUDENT NUMBER 
DATE OF EXAMINATION 
PLACE OF EXAMINATION' 
INSTRUCTIONS: 
Students may use one 8.5" x 11" aid sheet in preparing their answers. The aid sheet 
can be either the type supplied by the Faculty Office, or it can be any other sheet with 
the above specified dimensions. A non-programmable calculator is allowed. 
Write your solutions in the blank space provided between questions. 
TOTAL MARKS: 55 
There are 5 questions. The value for each question or part of a question is shown in 
parentheses next to the question number. 
MARKER'S REPORT 
1 
2 
3 
4 
5 
TOTAL 
Page 1 of 14 pages


## Page 2

![Page 2](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_002.png)

1. [10 marks] Consider the system with input u and output y: 
0 
11 
11x1(k) + ['11 u(
k 
1-1/ 
 
y2(k)+y2(k-1)=u(k)—u(k-1) 
y(k)= [1 0]xi(k)+y2(k) 
Is the system linear time-invariant? Justify your answer. 
Is the system BIBO stable? Justify your answer. 
Find a state-space model of the system with three states. The input is u and the output 
is Y. 
Is the state-space model controllable? Justify your answer. 
Page 2 of 14 pages


## Page 3

![Page 3](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_003.png)

(Extra space for work) 
Page 3 of 14 pages


## Page 4

![Page 4](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_004.png)

2. [10 marks] Consider the continuous-time linear time-invariant system 
=Ax+Bu 
where 
A=[g 
], B=[] 
Design a sampled-data controller with sampling period T = in 2, where In is the natural 
logarithm, such that for all initial conditions the two components of x(kT) have the form 
c1  sin(2kT + c2), where c1, c2  are constant scalars depending on the initial conditions. 
Note: Give an expression for your controller, without performing all the matrix multiplications 
in the expression. 
Page 4 of 14 pages


## Page 5

![Page 5](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_005.png)

(Extra space for work) 
Page 5 of 14 pages


## Page 6

![Page 6](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_006.png)

3.(i) [10 marks] Consider the discrete-time system x(k + 1) = A x(k)  + Bu(k) with 
A = [1 11] 
B = [1)hl 
[1 a 
Lb2i 
where a e R is a constant, unknown parameter and b1, b2  are unspecified yet. 
Consider that the following experiment is performed. When u(k) = 0 and the initial condition 
is x(0) 
= [ 
], 
the state x(k) is given as 
1 [ 
i 
x(k) =
1  - 21 
Is the system internally asymptotically stable? Fully justify your answer. 
If the answer in part (a) is Yes, determine necessary and sufficient conditions on B such 
that with control u(k) the state x(k) can be brought to [0 0]T  in two steps. 
If the answer in part (a) is No, determine necessary and sufficient conditions on B such 
that the system is stabilizable. 
Page 6 of 14 pages


## Page 7

![Page 7](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_007.png)

(Extra space for work) 
Page 7 of 14 pages


## Page 8

![Page 8](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_008.png)

3. (ii) [5 marks] 
A discrete-time system has transfer function 
Y(Z)_ 
z2 +1 
U(z) - (z-3)(z-4) 
An output feedback controller is to be designed such that the output y(k) tracks the discrete-time 
reference signal r(k) = A0  cos (k + ), obtained as discretization of r(t) = A0  cos (t + ) for 
sampling period T = , where amplitude A0  and phase 0 are unknown. 
Starting from r(t) and the exo-system model that generates it, determine the discrete-time exo-
system model that generates the discrete-time reference signal r(k) and write it as 
w(k + 1) = A w(k), 
r(k) = C w(k) 
Is the tracking control design problem feasible? 
If Yes, sketch the steps that would need to be followed by using the state-space methodology. 
If No, justify your answer. 
Page 8 of 14 pages


## Page 9

![Page 9](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_009.png)

(Extra space for work) 
Page 9 of 14 pages


## Page 10

![Page 10](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_010.png)

4. [10 marks] 
Consider the continuous-time linear system described by 
1 
P(s) = s+ 
 
s(s— 1)• 
 
An output feedback sampled-data controller is to be designed based on the discretized system 
so that the states of the system are driven to 0 in finite time. 
Obtain the state-space model for the discretized system for T = 1n2, where in is the natural 
logarithm, and write it in the form 
x(k + 1) 
Ax(k) + Bu(k) 
y(k) = Cx(k) 
Design a state feedback law u = Kx so that the eigenvalues of A + BK are at 0, 0. 
Find a numerical value for K. 
Determine the gain L so that the observer given by 
(k + 1) = AI(k) + Bu(k) + L[Cc(k) - y(k)] 
has poles at 0, 0. Write an expression for computing L but do not find a numerical value. 
State the separation principle and the properties that it guarantees. 
Set u = Kui. Determine the controller transfer function C(z) from y to u. 
Write C(z) as an expression in terms of A, B, C, K, L (no numerical values). 
Page 10 of 14 pages


## Page 11

![Page 11](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_011.png)

(Extra space for work) 
Page 11 of 14 pages


## Page 12

![Page 12](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_012.png)

(Extra space for work) 
Page 12 of 14 pages


## Page 13

![Page 13](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_013.png)

5. [10 marks] 
Consider 3 periodic tasks A, B, and C with periods 40, 20, and 10 and execution times 20, 
5, and 2, respectively. Each task deadline is equal to its period. All tasks are released at 0. 
These tasks need to be scheduled with Rate monotonic (RM) scheduling or earliest deadline 
first (EDF) scheduling. In the case of EDF, if earliest deadlines are the same, the priorities are 
ordered according to A highest, B second, C lowest. 
Determine the utilization. How is it compared to the rate monotonic (RM) upper bound? 
What conclusion can you draw? 
Sketch the timing diagrams for these tasks using RM scheduling. Can you schedule all 
3 tasks using RM? Does this agree with your conclusion in part (a)? If not, use EDF 
scheduling and sketch the timing diagrams. 
Page 13 of 14 pages


## Page 14

![Page 14](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_014.png)

(Extra space for work) 
Page 14 of 14 pages

