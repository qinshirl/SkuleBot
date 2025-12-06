## Page 1

![Page 1](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_001.png)

ECE410H (Linear Control Systems)
Department of Electrical and Computer Engineering
University of Toronto
Final Examination
Wednesday December 14th, 2022
Instructor: John W. Simpson-Porco 
Exam Begins: 9:30am 
Exam Ends: 12:00pm 
Exam Duration: 2 hour 30 minutes
Exam Type: Final Examination
Materials allowed: Non-programmable calculator, two-sided handwritten aid sheet
Name
Student ID
Signature
Instructions
• This exam is 8.5 inches by 14 inches, and is printed double-sided.
• There are a total of 25 pages, including this page.
• When in doubt, explain your thought process and demonstrate what you know; we can only 
grade what is written.
/ 24
Problem 1
Problem 4
/18
/ 24
Problem 2
/lO
Problem 5
/ 24
Problem 3
1 / 25


## Page 2

![Page 2](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_002.png)

Problem 1 (24 Points)
Your firm has been hired by a client who is very interested in making metal objects levitate using 
magnets. In particular, the client is in possession of a metal ball of mass m, which when placed in 
a magnetic field obeys the differential equation
(1)
mz = mg —
z
Here, 2: > 0 is the vertical position of the ball, 5 > 0 is the gravitational constant, and K > 0 
is a positive constant related to the magnetic field strength. The control input u is an electric 
current which is passed through a metal coil; the current modulates a magnetic field which applies 
a vertical force to the ball.
The control objective is for the ball to levitate at a constant reference position r > 0.
(a) Write the model above in nonlinear state-space form with state vector x = {z,z), input u 
and output y = z.
(b) We want the equilibrium output y to equal a desired reference value r. Determine the unique 
equilibrium input u and equilibrium state x such that this comes true.
2/25


## Page 3

![Page 3](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_003.png)

I
c
(c) Assuming parameters g = 10, r = 10, K = 1, and m = 0.1, linearize the system around the 
equilibrium you just found. Is your linearization stable, asymptotically stable, or unstable?
3/25


## Page 4

![Page 4](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_004.png)

(d) The linearized system from part (c) is controllable. Suppose that your next goal is to design 
a state-feedback controller to asymptotically stabilize the linearized system. You have been 
asked by your client to produce two potential designs, one that is “fast” and one that is 
’’slow”. Explain how you would approach this problem, including how you will define “fast” 
and “slow”, and describe the relative trade-offs between a “fast” design and a “slow” design. 
You do not need to calculate any gain matrices.
Note: If you could not complete (c), assume the system matrices are
0 1
B= 0
A =
C= 1 0
£) = 0.
1 0
-1
although you may or may not use them for this part of the question.
4/25


## Page 5

![Page 5](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_005.png)

\
(e) Your linearized system from part (c) is observable. Similar to part (d), your client has asked 
you to design two potential state observers for use, and you have produced the designs
-2
-200
Li =
L2^
-2 ’
-10001 ■
Describe the relative trade-offs between these two designs, commenting on both speed of the 
state estimation and the effect of measurement noise on the state estimation.
Note: If you could not complete (c), assume the system matrices are
0 1
“ . C =
A =
B =
1 0
D = 0.
1 0
-1
5/25


## Page 6

![Page 6](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_006.png)

(f) Draw a block diagram illustrating how you would combine your state feedback controller and 
observer to control the original nonlinear system (1). Clearly label all blocks, all signals, 
include measurement noise in the diagram, and be careful to distinguish between the original 
variables and deviation variables.
6/25


## Page 7

![Page 7](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_007.png)

I
/
(This page is intentionally left blank)
7/25


## Page 8

![Page 8](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_008.png)

Problem 2 (24 Points)
The LTI control system
-2 0 1 
1 2 -1 
0 0-4
1
0
X +
X =
u
0
y = 1 0 0 a;
is both uncontrollable and unobservable. The eigenvalues of A are a{A) — {—2,2, —4}.
Note: Part (e) of this question is separate from parts (a)-(d), so attempt part (e) even if you get 
stuck on (a)-(d).
(a) Determine the general Kalman decomposition of the system.
Hint: Remember, one or more of the subspaces Vco, Vco, Vas; Vao rnay be the zero subspace, 
in which case the corresponding states will disappear from the GKD.
8/25


## Page 9

![Page 9](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_009.png)

(This page is intentionally left blank)
9/25


## Page 10

![Page 10](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_010.png)

(b) Without computing the transfer function G{s), predict number of pole-zero cancellations that 
will occur in the computation of G{s), and determine whether the system is BIBO stable. 
Justify your answers.
10 / 25


## Page 11

![Page 11](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_011.png)

(c) Now, by any means you wish, compute the transfer function G{s) of the system. Does your 
result agree with your conclusions from part (b)?
11 / 25


## Page 12

![Page 12](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_012.png)

r
(d) Is this system stabilizable? Is it detectable? Justify your answers.
12 / 25


## Page 13

![Page 13](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_013.png)

(e) This part of the question is separate from (a)-(d). Suppose you have a state-space LTI system
X = Ax + Bu 
y = Cx -I- Du
which is not controllable, and not observable, but is both stabilizable and detectable. Provide 
a general procedure that you could follow to design an output feedback controller. Include as 
much detail and explanation as you can in your response.
13 / 25


## Page 14

![Page 14](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_014.png)

Extra space if needed
14 / 25


## Page 15

![Page 15](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_015.png)

Extra space if needed
15 / 25


## Page 16

![Page 16](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_016.png)

Problem 3 (24 Points)
This problem is a set of independent multiple choice questions. 
Complete your answers by circling your desired response.
Each question is worth 2 points. No part marks will be awarded. Rough work can be done on the 
extra blank pages immediately after this question, but will not be graded.
Unless the question explicitly states “Select all correct answers”, there is only one correct response 
for each question.
1. The state-space model
0 1
0
X +
X =
1 “
0 0
y = 1 I x-\- [0]rf
has corresponding transfer function
(A) G{s) = l/s"
(B) G(s) = (s + l)/s2
(C) a(s) = l/s
(D) GW = (» + l)/s
(E) none of the above
2. Which of the following are transfer functions that can be obtained from a LTI state-space model? 
Select all correct answers.
(A) (s + 1)V(3 + 2)2
(B) sin(2s)/(s + 1)
(C) (5 + 1)V(s + 2)
(s + 2)/(s-I-!)■ 
(s -I- l)/(s -I- 2)
(D)
(E) s
3. Linearization of a nonlinear control system at an equilibrium point is done because
(A) linearization leads to a LTI model
(B) linearization leads to a stabilizable LTI model
(C) linearization leads to a controllable LTI model
(D) linearization leads to a controllable and observable LTI model
(E) (a) and (b)
0 1
then ^exp(At) is
4. If A =
0 0
(A) undefined
1 t
(B)
0 1
0 t
(C)
0 0
0 1
(D)
0 0
(E) none of the above
a 1
5. With parameters o, 6 £ M, the matrix A =
0 6
(A) always diagonalizable
(B) never diagonalizable
16 / 25


## Page 17

![Page 17](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_017.png)

(C) diagonalizable if and only ii a — b
(D) diagonalizable if and only if a ^ b
(E) none of the above
6. Which of the following output signals cannot be produced by a LTI system? Select all correct 
answers.
(A) y{t) = e*sin(t)
(B) y{t) = t^e~^ cos(f)
(C) y(t) = e*'t2cos(t)
(D) y{t) = e-^/t
(E) y{t) = ^/ism{t)
7. The LTI control system
0 1 
0 -1
1
X +
X =
0 ^
y= 1 0 a; + [0]n
IS
(A) stable and controllable
(B) stable and BIBO stable
(C) unstable and not BIBO stable
(D) unstable and stabilizable
(E) none of the above
8. Suppose we apply the input u{t) = e Ho a state-space LTI system; we do not know the initial 
condition. If we observe the output y{t) = e*, then
(A) the system is not 120 stable
(B) the system is unstable
(C) the system is not BIBO stable
(D) (a) and (b)
(E) (b) and (c)
9. Which of the following statements is false?
(A) If {A, B) is controllable, then {A, B) is stabilizable
(B) If cr(A) C C“, then {A,B) is stabilizable
(C) If cr{A) C C , then (A, B) is stabilizable
(D) If {A,B) is stabilizable, then {A'^,B'^) is detectable
(E) If a{A) C C~, then the system {A, B, C, D) is BIBO stable
10. If a system is controllable, then we can (select all correct answers)
(A) design a control signal u e PW to bring the system from any initial state a;(0) = x q to any 
desired state x{T) = x at some future time T > 0
(B) design a control signal u G PW to steer the system along any desired path from any initial 
state x(0) = x q to any desired state x(T) = x at some future time T > 0
(C) design a state feedback controller u = Kx to ensure the closed-loop system is unstable
(D) design a state observer to produce a converging estimate x{t) of the true state x{t)
(E) design a state feedback controller u = Kx such that the closed-loop system is asymptotically 
stable
11. Consider an LTI control system with matrices {A,B,C,D). If we have an eigenvalue A e cr(A) 
with Re(A) > —5 and such that rank A — XI B < n, then
17 / 25


## Page 18

![Page 18](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_018.png)

(A) the system is controllable
(B) the system is not controllable
(C) the system is stabilizable
(D) the system is not stabilizable
(E) none of the above are definitively true
12. When computing the transfer function from a state-space model, pole-zero cancellations will 
occur if
(A) the system is not controllable
(B) the system is not stabilizable
(C) the system possesses an A-invariant subspace
(D) the system is not detectable
(E) the optimal control problem is not solvable
18 / 25


## Page 19

![Page 19](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_019.png)

Extra space if needed
19 / 25


## Page 20

![Page 20](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_020.png)

£>
Extra space if needed
:
20 / 25


## Page 21

![Page 21](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_021.png)

Problem 4 (18 Points)
Consider the LTI control system
y = 1 Ox
1
X =
(a) Is the system controllable? Is it stabilizable? Justify your answers.
21 / 25


## Page 22

![Page 22](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_022.png)

(b) Find the reachable set Rt {x ) from the non-zero initial condition x = (0,1) in time T = Is, 
and draw this set.
22 / 25


## Page 23

![Page 23](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_023.png)

(c) Is the system observable? Is it detectable? Justify your answers.
23 / 25


## Page 24

![Page 24](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_024.png)

Problem 5 (10 Points)
Consider the LTI system
X = Ax + Bd 
y = Cx
with state x € M", input d G measured output y € and p x m transfer matrix G{s) — 
C{sl — A)~^B. You can assume that the system is asymptotically stable, i.e., c f {A) C C“.
Rather than being a control input, the input d is a constant but unknown vector of disturbances. 
Using the ideas and techniques from the course, develop an approach for estimating d based on the 
measurements y. Specify under what condition(s) your approach will be successful.
Hint: The disturbance d being constant but unknown is equivalent to saying that d satisfies the 
differential equation d = 0 with unknown initial condition d{0).
24 / 25


## Page 25

![Page 25](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_025.png)

(This page is intentionally left blank)
25 / 25

