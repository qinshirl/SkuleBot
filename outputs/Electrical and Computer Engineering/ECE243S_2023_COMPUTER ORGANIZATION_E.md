## Page 1

![Page 1](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_001.png)

974943AB-FBBC-40EE-89CB-BCF237B31FC6
ECE243 - Computer Organization
First name (please write as legibly as possible within the boxes)
Student Number
1. There are 6 questions, worth a total of 67 marks, and 22 pages. Do all questions.
3. The test is Closed book. No calculators are permitted.
4. The duration of the test is 2.5 hours.
Page 1
□
□
□
University of Toronto 
Faculty of Applied Science and Engineering
2. ALL WORK IS TO BE DONE ON THESE SHEETS. You can use the blank pages included on 
Pages 18 to 19 if you need more space for any question. Be sure to indicate clearly if your work 
continues elsewhere. Aid Sheets are included on Pages 20 to 22.
Final Examination
April 18, 2023
ece-243-final-exam-66 762
#409 Page 1 of 22
Last name


## Page 2

![Page 2](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_002.png)

9D8A3A27-5DEE-4FC5-8723-BAE24B9D3CFF
'JJ&E
[12 marks]
1. Short answers (Lab 8):
[5 marks]
001 101 1000010000
r3,
#0x10
mvt
r2,
#10
mv
r2.
[r3]
st
rl.
#1
mv
rO,
#11
mv
[rO]
Id
rO,
add
rO,
#-l
bne
6
#1
sub
r2.
bpl
2
b
10
1000000000000000
. word
0x8000
[4 marks]
rO
rl
r2
r3
[3 marks]
Page 2
□
ece-*243-f inal-exam-66762
#409 Page 2 of 22
(a) An assembly language program for the Lab 8 Processor is shown below. In the space on the 
right, give the machine code (in binary) corresponding to each instruction. See the Aid Sheets 
for instruction encodings and address assignments. The program starts at address 0. The first 
instruction is done for you.
(b) What would be the contents of each register after this program reaches the last instruction? Write 
your answers in hexadecimal.
(c) Describe briefly in the space below what you would observe on a DEl-SoC board if you were 
to execute this program on the Lab 8 processor. As part of your answer, explain the purpose of 
any loops in the program.
Answer:


## Page 3

![Page 3](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_003.png)

55632170-1COB-40AB-8766-5A49781FF21D
I
ece-243-final-exam-66762
#409 Page 3 of 22
[10 marks] 2. Short answers (ARM):
[4 marks]
_start:
END:
FIELD:
Page 3
□
□
□
. word
. word
. word
SP,
RO,
Rl,
R2,
RO,
OxFFOOOOOO
24
31
// load Y
// load Z
// load X
X:
Y:
Z :
.global
LDR
LDR
LDR
LDR
LDR
BL
B
_start
=0x20000
=x
[RO, #4]
[RO, #8]
[RO]
FIELD
END
(a) The ARM code below loads into RO, Rl, and R2 the three numbers at addresses X, Y, and Z, 
respectively. The number X could be any positive integer > 0. Both Y and Z can be any integer 
from 0 to 31, where Y < Z. The FIELD subroutine extracts the bits in X from bit position Y to bit 
position Z and returns the result in the low-order bits of RO. For example, if X = OxFFO 0 0000, 
Y = 24 and Z = 31, then FIELD would return RO = OxFF. Similarly, if X = OxOOOOlFOO, Y = 
8 and Z = 12, then FIELD would return RO = OxlF. Write the FIELD subroutine in the space 
provided below. Your code should obey the ARM Procedure Call Standard (PCS).


## Page 4

![Page 4](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_004.png)

■
FEAB1EB2-B1EC-4062-B317-30E41A5AFAB2
I
[6 marks]
BL
DIV
END:
B
END
// Write the DIV subroutine
Page 4
□
□
(b) The ARM code below loads into RO and R1 the two numbers at addresses X and Y, and then calls 
the subroutine named DIV. The number X can be any positive integer > 0 but Y is restricted to 
be only be a power of 2. The DIV subroutine is supposed to remm in register RO the quotient of 
the integer division XjY, and in register R1 the remainder.
In your Lab Exercises in this course you implemented integer division for ARM by using iter­
ative subtraction. But for this question, you are not allowed to use that approach. Instead, you 
have to perform the division operation by appropriately shifting the dividend X, using the LSR 
instmction. This can be done because the divisor Y is a power of 2.
Write the DIV subroutine in ARM assembly language in the space provided on the next page. 
Your code should obey the ARM Procedure Call Standard (PCS).
// load Y
// load X
ece-243-final-exam-66762
#409 Page 4 of 22
SR,
RO, 
Rl,
RO,
_start
=0x20000 
=X 
[RO, #4] 
[RO]
next page
on the
.global
_start: LDR
LDR
LDR
LDR


## Page 5

![Page 5](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_005.png)

43685F9D-7A85-4351-A394—F542742FB063
ece-243-final-exam-66762
#409 Page 5 of 22
// iVrite your DIV subroutine in the space beloM
DIV;
X:
Y:
Page 5
. word
. word
0x63
16


## Page 6

![Page 6](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_006.png)

17008425-2C45-4BF2-94A0-1E598F8023D2
I'X'
ece-243-f inal-exain-66 762
#409 Page 6 of 22
3. This is a question about ModelSim.
[5 marks]
Consider the ModelSim simulation results for the Lab 8 processor shown below.
(a) What is the instruction? Answer: 
Page 6
I
 
ns
Tooo
KMl
100004
100002
1
* c
2500 ns
340 ns
360 ns
280 ns
300 ns
320 ns
240 ns
260 ns
I------ 1—
(1206
In the ModelSim results, examine the instruction that ends at 350 ns in simulation time. Note that the 
instruction encodings for the Lab 8 processor are provided in the Aid Sheets.
(b) Explain in the space below whether or not this instruction appears to be working correctly. If not, 
what do you think is wrong in the processor circuit? Be specific in your answer; for example, 
refer to what value certain signals should have in a given FSM time step, as opposed to what 
values they show in the simulation. Higher marks will be given for more insightful explanations. 
Answer:
3 
3
10004
10006 
10002
10111
I E
110004
1
J-------- 
J-------- 
- {Mte 
fooSo
10003
10002 
10004
Stl
StO 
0 
0003 
0003 
21ff 
000 
0004 
0006 
0003” 
0111 
0004 
0003 
00007 
0 
0 
0 
StO 
stl
10004
lOOOOe
TQOO3 
lOlll
I 
0002
ZmTZ
1206
Con~~
QOOa 
0000
(msZ
0000 
0000
(^6
17001 
lOlO
100^6 z: 
lOQOl ~ 
I000a~
Now
Coo^
J----
-----proc---------- 
 
 
Clock
IR
A. W 
Done 
pc
O--** ADDR
DIN
D--^ FSM 
p-4 rO 
n 
Biuswres 
Sctect
p--4> A
n-4> G
P--^ Sum
■V Am 
-4' On
Hn
J 
L
I 7001


## Page 7

![Page 7](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_007.png)

656E80B2-C651-44C0-A786-C39EFEB0FCA1
[12 marks] 4. This question involves FSM timing concepts.
[6 marks]
Ti
24
25
znv
Answer;
TO
T1
T2
T3
T4
T5
Page?
□
□
□
(a) For this question you may wish to refer to the diagram of the Lab 8 processor that is provided 
in the Aid Sheets. As you are aware, the mv rX, Op2 instruction has the FSM timing given in 
the table below.
In the space below provide a new version of the FSM timing for the mv instruction such that it 
will properly affect the z and n flags in register F (again, the value of the c flag is not relevant 
here). Assume that you can’t make any changes to the processor datapath, and use as few FSM 
time steps as possible to complete the mv instruction. Note that the ALU has the two control 
inputs AddSub and ALU^znd. If ALU^nd = 1, then the ALU performs a logical AND operation, 
else if AddSub = 1 the ALU performs a subtract, else the ALU perform an addition operation.
ece-243-final-exam-66762
#409 Page 7 of 22
2o 
Select = -PC, 
ADDRin, pc-incr
_________ 23_________
Select = rT or JR8 JR8-0, 
rXin, Done
22
2/?tn
Since it does not use the processor’s ALU, the mv instruction does not have any effect on the 
processor’s flags, z, n, and c. Assume now that you wish to change this behaviour; that is, you 
wish to have the mv instruction affect the flags according to the value of the operand Op 2. For 
example, the instruction mv rl, #0 will result in register rO = 0, but should also set z = 1 
and n = 0. Similarly, the instruction mv rl, #-l will result in register rl = OxFFFF, but 
should also set n = 1 and z = 0. Finally, if Op 2 is a register, then the z and c flags should be 
affected based on the register’s contents. (Note that the carry out is not a meaningful result of 
the mv instruction, so the value of the c flag after a mv instruction does not matter.)


## Page 8

![Page 8](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_008.png)

F767AAD2-0E62-48AC-BE4F-63A226411381
[6 marks]
The sub instruction for the Lab 8 processor has the FSM timing shown in the table below.
Ti
sub
-16
-16
B
A
<
>
Sum
16
16
-16
16
z
This question is continued on the next page ...
Page 8
rr“-'_lhT
□
(b) In the Lab 8 processor one of the ALU inputs is driven by register A, as depicted in the Aid 
Sheets, and the other ALU input comes directly from the BusWires. The ALU output is stored in 
register G.
For this question assume that the ALU architecture is changed, by including a new register B 
and removing register G. This new architecture is illustrated below.
(from Buswires 
Multiplexer)
(to Bus-wires 
Multiplexer)
ece-243-final-exam-66762
#409 Page 8 of 22
Ts
Select =-G, 
rXin, Done
n
Select = rX, 
Ain
To 
Select = _PC, 
ADDRin, pcJncr
_________ ___________
Select - rY or JR8 JR8_0, 
AddSub, Gin, Pin
T2 
IRin
Add/Suh \ 
carry r\
B.
" in
c n
> F
Sum 15
T
Arithmetic Logic / 
Unit (ALU) /


## Page 9

![Page 9](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_009.png)

B755D34E-80B8-4B90-AF23-15C68A3CF1C4
ece-243-final-exam-66762
#409 Page 9 of 22
TO
T1
T2
T3
T4
T5
Page 9
□
fl
In the new architecture the BusWires signal has to be modified, because register G no longer 
exists. Suitable Verilog code is shown below:
In the space below you are to provide a new FSM timing table that will implement the sub 
instruction using the new ALU architecture.
0
// define the internal processor bus 
always @ (*)
case
_R0 :
_R1:
_R2 :
_R3:
_R4:
_R5:
_R6:
_PC:
_SUM:
3^4
(Select)
BusWires = rO;
BusWires = rl;
BusWires = r2;
BusWires = r3;
BusWires = r4;
BusWires = r5;
BusWires = r6;
BusWires = pc;
BusWires = Sum[15:0];
_IR8_IR8_0: BusWires = {{7{IR[8]}}, IR[8:01};
_IR7_0_0: BusWires = {IR[7:0], 8'bO};
_DIN: BusWires = DIN;
default: BusWires = 16'bx;
endcase


## Page 10

![Page 10](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_010.png)

8AB4DA3D-A55F-47A5-A696-18831BC6A45C
ece-243-final-exam-66762
#409 Page 10 of 22
// save regs
SHOW:
R2,
// isolate digit 1
// isolate digit 2
SEG7 :
1110001
(a) Provide equivalent C code for this subroutine in the space provided on the next page.
[5 marks]
Page 10
□
□
STR
POP
MOV
LSR
AND
LDRB
LSL
ORR
LSR
AND
LDRB
LSL
ORR
LSR
LDRB
LSL
ORR
LDR
AND
LDRB
PUSH
LDR
. byte
. byte
-byte
ObOOllllll
ObOOOOOllO
ObOlOllOll
RO, #4 
#0xF 
[Rl, R3] 
#8 
R5
// '0'
// '1'
// '2'
// address of SEG7 array
// isolate digit 0
// get code for HEXO
code
to HEX2 position
// get
// shift
// form the HEX3_0 pattern
HEX3_0 
regs
R3,
R3,
R5,
R5,
R4,
R3,
R3,
R5,
R5,
R4,
R3,
R5,
R5,
R4,
Rl,
R3,
R4,
[14 marks] 5. This question is about ARM assembly code and C code. For this part of ±e question you are given 
an ARM assembly language subroutine called SHOW and are asked to translate it into an equivalent 
C language subroutine. This subroutine shows the contents of register RO, as a 4-digit hexadecimal 
number, on the HEX3-0 displays. (In the next part of this question you will be given a main program 
that calls the SHOW subroutine.) The assembly language subroutine is shown below:
{R4, R5}
=0xFF200020
RO, #12
[Rl, R3]
#24
R5
shown)
// 'F'
=SEG7
RO, #0xF
[Rl, R3]
// isolate digit 3
// get code
// shift to HEX3 position
// for the HEX3_0 pattern
// get code
// shift to HEXl position
// form the HEX3_0 pattern
RO, #8 
#0xF 
[Rl, R3] 
#16 
R5
[R2] 
{R4, R5} 
PC, LR
// write to
// restore
(other patterns not
.byte ObOlllOOOl


## Page 11

![Page 11](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_011.png)

9A46C105-AC8C-4F9D-8498-733C84821CAB
0x07,
void show(int value)
{
Page 11
Question 5 continued ...
Put your C code in the space below. The seg7 array is defined for your convenience.
0x06,
0x7c,
0x5b,
0x39,
0x4f,
0x5e,
ece-243-final-exam-66762
#409 Page 11 of 22
char seg7[] = {0x3f,
0x7f, 0x67, 0x77,
0x66, 0x6d, 0x7d, 
0x79, 0x71};


## Page 12

![Page 12](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_012.png)

77D9D6EB-2CDC-4CAD-9E41-4845B55EF0A3
ece-243-final-exam-66762
#409 Page 12 of 22
Question 5 continued ...
_start:
LDR
SP,
// read SM port
R9,
// shift left ?
LEFT:
// shift right
RIGHT:
#0
// shift
until pattern is
0
END:
You are to translate this assembly code into C code as described on the following page.
Page 12
RO,
RO,
MAIN:
LOOP :
// get shift type
// get shift
// perform the shift 
// keep only 16 bits
// pattern to display
// parameter for SHOW
LDR 
MOV 
BL 
BL
LDR
LDR 
MOV 
LSR 
AND
CMP
BNE
LSL
LDR
AND
LSRNE
CMP
BEQ
B
LDR
SUBS
BNE
MOV
R4, 
MAIN 
LOOP
=0x1010
R4
R5,
R5,
R9,
R9,
R5,
R4,
R6,
R4,
R4,
Consider now the assembly language program shown below. The purpose of this program is 
to show the value of register RO on the HEX3-0 displays, and to shift RO either to the right 
or left; after each shift operation RO is displayed by the SHOW subroutine, and then a DELAY 
subroutine is called. The direction of shifting is controlled by switch SWg and the amount to 
shift is determined by switches SW3:0.
R4, :
RO, :
SHOW
DELAY
=0xFF200040
[R5]
R5
#9
#0xF
#0
RIGHT
R5
=0xFFFF
R6
R5
// Delay loop
DELAY:
DLOOP:
=3500000
#1
DLOOP
PC, LR
(SW[9])
amount (SW[3:0])
.global _start
=0x20000


## Page 13

![Page 13](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_013.png)

A608029D-ACDC-4242-B1DE-418D713F4CF1
[8 marks]
Finally, translate the DELAY subroutine into C code on the following page.
Page 13
int main (void) 
{
Question 5 continued...
(b) In the space below write equivalent C code for the MAIN program.
ece-243-final-exam-66762
#409 Page 13 of 22


## Page 14

![Page 14](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_014.png)

E155CC61-4CD5-403D-93E5-8F4419F58CDC
[1 mark]
void delay(void) {
Page 14
□
□
Question 5 continued ...
(c) In the space below write equivalent C code for the DELAY subroutine. Don’t worry about 
whether the amount of the delay will be exactly the same as in the assembly-language version.
ece-243-final-exam-e6762
#409 Page 14 of 22


## Page 15

![Page 15](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_015.png)

534CB7A2-A75C-4884-A70C-9A60889D2ECF
J
[1 mark]
Answer:
[4 marks]
Put your answers on the next page
Page 15
□
• The total number of words in the memory is 32.
• The memory is word-addressable.
• The cache size is 8 words total
• The cache hne size is 2 words
(b) For this Direct-Mapped Cache, consider the sequence of eight memory reads from the addresses 
in the table on the next page. The Read Access Number in that table is to be used to refer to ±e 
specific hne in the table. Assume the cache is initially empty, meaning that none of its fines are 
valid. Which Read Access Numbers result in a cache hit? Your answer should just fist the Read 
Access Number(s) that cause a hit.
(a) For this and the next two parts of this question, assume that the cache is Direct-Mapped. Deter­
mine which bits of the 5-bit main memory address (A4, A3, A2, 
, Aq ) fines are used for the
Tag, the Line and the Word bits in this cache.
ece-243-final-exam-66762
#409 Page 15 of 22
[14 marks] 6. This question is about processor cache design and behaviour. Consider the following specifications 
for a computer memory system that has a very small main memory and a smaller cache:


## Page 16

![Page 16](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_016.png)

B46A023D-E7E5-42A9-B0F4-0DBABF2B6FD9
I
■X
Part(b), cont’d
Answer:
[2 marks]
Answer:
Page 16
□
□
□
(c) Give an address for Read Access Number 4 that would cause the Direct-Mapped cache to have 
a cache hit. The address you give must be different than the one given for Access Number 4 in 
the above table.
ece-243-final-exam-66762
#409 Page 16 of 22
10000 
10001 
10011 
11000 
00100 
00101
11010 
10010
Read Access Number Read Address (in binary) 
1 
2 
3 
4 
5 
6 
7 
8


## Page 17

![Page 17](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_017.png)

235420A4-DBEC-4A4A-837E-B27A2FBCB922
[1 mark]
Answer:
[4 marks]
Answer:
[2 marks]
Answer:
Page 17
(f) Give an address for Read Access Number 8 that would cause the associative cache to have a 
cache miss. NOTE: this part asks for a miss which is different from Part (c) above. The address 
you give must be different than the one given for Access Number 8 in the above table.
(d) For this and the next two parts of the question, assume instead that the cache is 2-way set asso­
ciative. Determine which bits of the 5-bit main memory address {A4, A3, A2, Ai, Aq) are used 
for the Tag, the Set and the Word bits in this cache.
Read Access Number
1
2
3
4
5
6
7
8
Read Address (in binary)
10000
10001
10011 
11000 
00100 
00101
11010
10010
ece-243-final-exam-66762
#409 Page 17 of 22
(e) For the 2-Way Set Associative Cache, consider the (same as in Part (b)) following sequence of 
eight memory reads from the addresses given below. Assume the cache is initially empty, mean­
ing that none of its hnes are valid. Which Read Access Numbers result in a cache hit? Your 
answer should just hst the Read Access Number(s) that cause a hit.


## Page 18

![Page 18](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_018.png)

33422441-2FC6-4539-B49E-F4BD1CD168D2
ece-243-final-exam-66762
#409 Page 18 of 22
Extra answer space for any question on the test, if needed:
Page 18
□


## Page 19

![Page 19](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_019.png)

671FF949-0E2B-4F70-8003-32345E0ECB3C
ece-243-final-exam-66762
#409 Page 19 of 22
Extra answer space for any question on the test, if needed:
Page 19
□
□
(V9^


## Page 20

![Page 20](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_020.png)

F33D0F43-7381-48B3-A7FC-7FF23DE599C2
ece-243-final-exam-66762
#409 Page 20 of 22
Aid Sheets
ARM Addressing Modes
Assembler syntax Address generation
Name
Offset:
[Rn, #offsetj
Address = Rn + offset
immediate offset
offset in Rm
[Rn, ±Rm, shift]
Address = Rn ± Rm shifted
Pre-indexed:
immediate offset
[Rn, #offset]!
offset in Rm
[Rn, ±Rm, shift]!
Post-indexed:
immediate offset
[Rn], #offset
[Rn], ±Rm, shift
offset in Rm
I/O Ports in the DEl-SoC Computer
Address
0XFF200000
Data register
Unused
31
LEDRo
Page 20
J
Address = Rn;
Rn <— Rn ± Rm shifted
Address — Rn -I- offset;
Rn <— address
Address — Rn ± Rm shifted;
Rn <— address
Address = Rn;
Rn <— Rn ■+■ offset
•J
10 I 9"T
LEDRp


## Page 21

![Page 21](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_021.png)

S’;;
955BB2BF-74DC-41CE-B435-AF0F7D30BFAF
ece-243-final-exam-66762
#409 Page 21 of 22
Address
OXFF200040
Data register
Unused
9
SWg
Address
31
30
4
3
1
1
0
0XFF200050
Unused
Data register
Unused
Unused
0XFF200058
Unused
Mask bits
Intemiptmask register
0XFF20005C
Unused
Edge bits
Edgecapture register
Address
OXFF200020
Data register
24
16
8
HEX36_o
HEX26.0
HEXO^
Segments
0XFF200030
Data register
16
24
23 22
Unused
Page 21
□
□
1 6
T r
7 6
TT
23 22
1 r
15 14
"i r
15 14
TT
8r
HEX5g_o
KEYs^
0
|T|.
3
SWo
I 31 30
HEX16.0
ZJ
I 31 30
I
3
r
HEX4^


## Page 22

![Page 22](https://raw.githubusercontent.com/qinshirl/SkuleBot/shifang/images/Electrical%20and%20Computer%20Engineering/page_022.png)

as
H H ■■ ■
D0828333-D95B-46AB-AD2D-BCB9F68FB596
Lab 8 Processor
16
16
'16
24
16
pcjncr
16
C/ocJt
— A DDR
16
16
16
,4
16
“ DOUT
Select
Buswires
DIN
IR
Control FSM
Done
Instruction Encoding for Lab 8 Processor
101 (st), 110 (and)
001 (eq),
010
(none),
(ne) ,
I/O Ports for the Lab 8 Processor System
Page 22
□
□
A
G
J
ri)
T
Run
Res etn
LED:
HEX:
SW:
address 0x1000
addresses 0x2000 (HEXO), 0x2001 (HEXl), 0x2005 (HEX5)
address 0x3000
E 
L
ece-243-f inal-exani-66752
#409 Page 22 of 22
Sum,5
7^^
F
Counter 
(r7)
o 
o
15 
0
IIIOXXXOOOOOOYYY,
IIIIXXXDDDDDDDDD,
III = 000
0 01IXXXODDDDDDDD,
OOlOCCCDDDDDDDDD, 
oil (cc), 100
c n
DOUT,„
W D
a
§
It
when two registers are involved 
when immediate data is used
(mv), 010 (add). Oil (sub), 100 (Id), 
for mvt 
for b{cond}, where CCC = 000 
(OS), 101 (pl), or 110 (mi)
-- t
AddSub \ 
-------- \ Adder/Subracter
r*
Multiplexers /

