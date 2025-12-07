## Page 1

UNIVERSITY OF TORONTO 
FACULTY OF APPLIED SCIENCE & ENGINEERING 
FINAL EXAMINATION, December, 2019 
ECE41OF - LINEAR CONTROL SYSTEMS 
Calculator Type: 4 
Exam Type: C 
Examiner: Prof. M. Maggiore 
FAMILY NAME 
GIVEN NAME(S) 
STUDENT NUMBER 
Instructions: • Write your answers in the boxes provided, when available. 
A non-programmable calculator is allowed. 
A one-page aid sheet (both sides) is allowed. 
Duration of exam is 21 hr. 
There are five problems in this exam. 
Problem I 
Mark 
1 
/8 
2 
/7 
3 
/10 
4 
/8 
5 
/7 
Total: 
/40 
41 
Page 1 of 14


## Page 2

1. Two unit point mass robots have dynamics 
r11  
0 1 
Xi 
0 
= 
+ 
U 
X2 
0 0 
x2  
1 
01 x3  
0 
'61 
 
= 
+ 
U. 
X4  
0 0 
x4  
—1 
The two robots are subjected to the same control force u, but in opposite directions. The state of the 
two robots is x = (x1, x2, x3, x4) E R, where x1, x3  are the positions of the two robots on the real line, 
and X2, X4 are their speeds. 
We wish to design a controller such that, asymptotically, the states of the two robots are synchronized, 
i.e., the robot positions coincide, and their speeds coincide. 
(a) Find a basis for the subspace V c R corresponding to the robots being synchronized, and prove 
that V is A-invariant, where A e 1R4>< 4  is the system matrix of the two robots. Be careful: A 
mistake in this part will invalidate the rest of the problem. 
Page 2 of 14


## Page 3

(b) Using the representation theorem, design a feedback controller synchronizing the two robots, and 
making their states converge to each other at a rate of exp ( - 2t). You may express the controller 
gain K in the form K = kp1, without computing P 
Page 3 of 14


## Page 4

2. Consider a unit point mass moving on a straight line in the presence of viscous friction and a control 
force u. Denoting by y the displacement of the mass along the real line, the equation of motion is 
= —l; + U. 
Letting x = [y 
T denote the state of the point mass, we want to design a state feedback controller 
minimizing the cost function 
J(x°,u) = 
fo  00 
Y 2 (-r) +u2(r)dr, 
subject to 
= - + u, {y(0) 
(0)]T = x°. 
This problem has two parts. 
(a) Checking suitable conditions, verify whether or not there is guaranteed to exist a solution to the 
optimal control problem. Be clear on what are the conditions you check. 
Page 4 of 14


## Page 5

(b) If the check of part (a) gives a positive answer, find the optimal feedback controller. 
Page 5 of 14


## Page 6

3. The control system 
o 
o 
—2 
—1 
x= —2-1 
4x+ 
1  
0 
0-2 
0 
0 1]x 
is neither controllable nor observable. This problem has four parts. 
(a) Is the system stabilizable? Is it detectable? Justify your answer. 
Page 6 of 14


## Page 7

(b) Find the general Kalman decomposition of the system, and highlight the co, co, E5, cô components 
of various matrices. 
Page 7 of 14


## Page 8

(This page intentionally left blank) 
Page 8 of 14


## Page 9

(c) Without computing the system transfer function, predict the number of pole-zero cancellations. 
Justify your answer. 
(d) Without computing the system transfer function, determine whether or not the system is B I BO 
stable, and whether or not it is 120 stable. Justify your answer. 
Page 9 of 14


## Page 10

4. In this problem you will design a cruise controller for a unit point mass robot on the real line subject 
to a disturbance force. The equation of motion of the robot is 
where v E R is the speed of the robot, u E R is its control input, and d(t) = csin(t + ) is a 
sinusoidal disturbance force, with c, q  arbitrary real numbers. The control specification is to design a 
full information controller making the speed v(t) converge to a desired constant (cruise control). This 
problem has three parts. 
(a) Formulate the appropriate full information output regulation problem corresponding to the control 
specification described above. 
Page 10 of 14


## Page 11

(b) By checking appropriate assumptions, determine whether or not the full information output reg-
ulation problem is solvable. 
Page 11 of 14


## Page 12

(c) If the problem is solvable, find a full information output regulator solving the output regulation 
problem. 
Page 12 of 14


## Page 13

5. Consider the control system 
—1 0 —1 
1 
x 00 2x+lu 
00 
0 
-0- 
Y [1 0 1]x. 
This problem has two parts. 
(a) Let T > 0 be arbitrary. Does there exist a piecewise continuous control signal u(t) steering the 
1 
1 
state from x(0) = 0 to x(T) = 
- 1 ? Repeat for x(T) = 0 , and justify your answers. 
0 
-1 - 
Page 13 of 14


## Page 14

1 
(b) Denote by (t) the output signal produced by the system when x(0) = 0 and u(t) 
1. Find 
0 
the set of all initial conditions producing the output signal (t) when u(t) 
1. 
Page 14 of 14

