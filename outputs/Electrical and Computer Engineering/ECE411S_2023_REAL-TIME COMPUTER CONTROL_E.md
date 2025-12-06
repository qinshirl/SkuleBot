## Page 1

![Page 1](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_001.png)

FAMILY NAME 
GIVEN NAME(S) 
STUDENT NUMBER 
Page 1 of 16
Instructions
A double-sided, hand-written aid-sheet and a non-programmable calculator are allowed. The dura­
tion is 2| hours. Write your solutions clearly in the spaces provided below the problem statements. 
You can write in pencil. You can use multiple colors, except red.
UNIVERSITY OF TORONTO 
FACULTY OF APPLIED SCIENCE & ENGINEERING 
FINAL EXAMINATION
ECE411S - Real-Time Computer Control
April 21, 2023, 6:30 PM-9 PM 
Exam Type: C 
Calculator Type: 2 
Instructor: Andrew R. Romano
Problem
I
2
3
4
5
Total
Mark
“715
/15
/20
/20
/20
/90


## Page 2

![Page 2](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_002.png)

1. Consider the following single-input discrete-time LTI system
x(k -I- 1) = Xa;(fc) Bu(k')
where x e R” and u e R. It is known that (A, is controllable.
Page 2 of 16
(a) [10 marks] Is it possible to design a state-feedback controller u(A:) = Kxijz} such that 
for any a;(0) £ R”, x{k} 0 in finite-time no, where no < n7 Justify your answer.


## Page 3

![Page 3](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_003.png)

(b) [5 marks] Let (A, B) be given as follows
A =
B =
Page 3 of 16
Design u{k} — Kx^k) such that x{k} —> 0 in finite-time and check your result from part 
(a).
0
2
0 2
2 -1


## Page 4

![Page 4](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_004.png)

2. [15 marks] A continuous-time control system
Page 4 of 16
= Is
Using state space methods, design a sampled-data (discrete-time) output regulator making the 
output ?/(t) track sinusoidal signals of the form r(t) = a sin(7rt-t-(^). Use a sampling period of 
T = Note: write an expression for the observer gain, but do not numerically compute it.


## Page 5

![Page 5](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_005.png)

Page 5 of 16


## Page 6

![Page 6](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_006.png)

3. Consider the discrete-time LTI system
x{k 1) =
1 ,
M-^ =
M =
for any a, b, c 0.
’ (a)- [5 marks] Is the system internally asymptotically stable? Justify your answer.
Page 6 of 16
I 
c  1 
c_
0
1
0
0
1 
~b 
1 
b
1
ex. 
0
a 
h 
0
0 
1 
a 
0
0
a - 1
0
0 a
b 0
c 0
where a e 5? is a constant parameter. You may use the following matrix inverse pair in your 
answers:
a;(A:)2/(A:) =01


## Page 7

![Page 7](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_007.png)

Page 7 of 16
(b) [5 marks] Determine necessary and sufficient conditions on a such that the system is 
observable.


## Page 8

![Page 8](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_008.png)

Page 8 of 16
(c) [5 marks] Find a numerical value a such that the system is not observable, but is 
detectable. Justify your answer thoroughly.


## Page 9

![Page 9](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_009.png)

Page 9 of 16
(d) [5 marks] Set a = 1. According to part (b) is the system observable for this value of a?
T
in finite-time.
Design an observer such that the state estimate error goes to 0 0 0


## Page 10

![Page 10](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_010.png)

y
p
c
(a) [4 marks] Determine the transfer function of the discretized plant, Paiz').
Page 10 of 16
The controller is to be implemented digitally via a sample and hold operator around the plant. 
Assume that a sampling period T = 1 is to be used. Consider two methods for discretizing 
the continuous-time controller, namely the bilinear transformation and pole-zero matching.
4. Consider the continuous-time closed-loop system below, with plant transfer function P(s) = 
I*' 
shown that this closed-loop system is BIBO stable
and that for constant references, asymptotic tracking is achieved, i.e., if r{t) — rol(t), then 
eft) = r^t) — yit) 0 as t oo.
r


## Page 11

![Page 11](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_011.png)

Page 11 of 16
(b) [8 marks] Discretize C(s) using the bilinear transformation to get Cd^z). Determine 
the closed-loop transfer function corresponding to the discretized system. Is stability of 
the closed-loop system preserved? Does e(A:) = r(A;) — —> 0 as A: —> oo?


## Page 12

![Page 12](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_012.png)

(c) [8 marks] Repeat part (b) using pole-zero matching.
Page 12 of 16


## Page 13

![Page 13](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_013.png)

Page 13 of 16
5. Consider 3 periodic tasks A, B and C with periods 20, 10 and 5 and execution times 10, 3 
and 1, respectively. Each task deadline is equal to its period. All tasks are released at t = 0. 
These tasks are to be scheduled with rate monotonic (RM) scheduling.
(a) [3 marks] Determine the utilization factor. How does it compare to the RM upper 
bound? What conclusions can you draw?


## Page 14

![Page 14](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_014.png)

Page 14 of 16
(b) [7 marks] Sketch the timing diagrams for tasks A, B and C using RM scheduling. Can 
you schedule all 3 tasks under RM scheduling?


## Page 15

![Page 15](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_015.png)

Page 15 of 16
(c) [3 marks] Now consider 3 periodic tasks D, E and F with periods 13, 10 and 5 and 
execution times 6, 3 and 1, respectively. Note that tasks E and F are the same as B and 
C. What is the utilization factor? How does it compare to the RM upper bound and to 
the utilization factor found in part (a)? What conclusions can you draw?


## Page 16

![Page 16](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_016.png)

Page 16 of 16
(d) [7 marks] Sketch the timing diagrams for tasks D, E and F using RM scheduling. Each 
task deadline is equal to its period. All tasks are released at t = 0. Can you schedule all 
3 tasks under RM scheduling?

