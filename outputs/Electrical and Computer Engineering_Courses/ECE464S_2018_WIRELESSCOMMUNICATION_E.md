## Page 1

UNIVERSITY OF TORONTO 
DEPARTMENT OF ELECTRICAL & COMPUTER ENGINEERING 
ECE 464S 
Wireless Communication 
Final Exam 
April 26, 2018 
Time: 6:3OPM-9:OOPM 
Examiner: Prof. Elvino S. Sousa 
Instructions: 
Type D exam: All distributed notes and materials except textbooks are allowed. All 
calculators are allowed. 
Answer any 4 of the 5 questions. All questions have equal value. 
If you feel that a question is not clear or there is information missing, clearly state the 
assumptions made in answering the question. 
For each question clearly write the answer in the space provided following the question, 
clearly label the parts, and put a box around the final answer for each part, if applicable. 
Each question must be answered in the pages dedicated for the question. If additional 
space is required, please use the back of the previous page. 
Marks: 
1. 
2. 
3. 
4. 
5. 
Page 1 of 11 pages


## Page 2

1. A wireless communication system utilizes OFDM modulation. The channel is modelled 
as a multi-path channel with multi-path delays, relative to the main path, i.e. excess delays, 
ranging from 0 to 10 js. The system utilizes an RF band in the range 1.9 GHz to 1.91 GHz. 
The modulation scheme utilizes a sub-carrier frequency spacing equal to 12 KHz. In order 
to minimize interference to other systems we impose a guard-band of 140 KHz at each end 
of the RF band. 
a) Determine the OFDM symbol period in the ideal case of no multi-path propagation. 
b) Determine the number of sub-carriers in the OFDM modulation scheme. 
c) Determine the sampling period if we are to synthesize the signal using an FFT with length 
equal to a power of 2. What is the length of the FFT? 
Page 2 of 11 pages


## Page 3

d) Determine a suitable cyclic prefix (CP) in order to combat multi-path propagation as 
described above. What is the number of symbols in the CP? 
e) Determine the OFDM transmission symbol rate under the assumption of the transmission 
of the CP as in d). 
Determine the bit rate for the system assuming the use of 64 QAM in the sub-carriers. 
Page 3 of 11 pages


## Page 4

Q 
a) In a wireless link the received signal arrives at the receiver as a plane wave. A dipole 
antenna oriented horizontally produces the maximum signal strength of -60 dBm. What is 
the signal strength if the antenna is oriented at an angle of 30 degrees with respect to the 
horizontal? Give the answer in dBm. 
In a wireless system the received power is given by P-. = 
, where P0  is a constant, R 
is the link distance, and L is a shadow fading random variable. Assume that L has a 
probability density function given by fL(X) = 1 - Ix - ii 
for 0 <x < 2 and 0 
elsewhere. Now assume that without shadow fading the received power is given by P = 
P0/R2  , and that beyond the distance R0  the link is in outage (i.e. R0  is the critical 
distance for signal reception). With shadow fading what is the probability of outage if the 
link distance is equal to R0? 
Assuming a two-path ground wave propagation model what is the change in signal 
strength (in dB), assuming the same transmitted signal, if we double the link distance? 
Page 4 of 11 pages


## Page 5

d) In a wireless link with a certain propagation environment we consider two modulation 
schemes, a scheme A with a channel bandwidth of 50 KHz, and a scheme B with a channel 
bandwidth of 100 KHz. Is the degree of frequency selective fading equal for both systems, 
or is it different? If it is different, which scheme has a higher degree of frequency selective 
fading? 
e) A wireless channel, with center frequency equal to 1 GHz and for which the receiver is 
traveling at a speed of 50 Km/H relative to the transmitter has a coherence time equal to I 
ms. What would be the coherence time for the channel if instead the center frequency was 
1.8 GHz and the speed was 60 Km/H? 
1) A wireless channel with an rms delay spread of 1 is has a coherence bandwidth equal to 
200 KHz. What would be the coherence bandwidth for the channel if the delay spread has 
the same distribution but the rms value is equal to 0.2 jis? 
Page 5 of 11 pages


## Page 6

3) A GSM cellular system utilizes two blocks of spectrum each of 19.8 MHz bandwidth. The 
frequency separation for the FDD RF channels is 100 MHz. The first block of spectrum 
starts at 1.9 GHz. Assume that RF guard bands of 1/2 of an RF channel are used in each 
spectrum block. 
a) Specify (accurately) the carrier frequencies for the RF channels. 
b) What is the number of information bits transmitted per TDMA slot? 
c) Suppose we transmit bits in the GSM system (for a user) without error protection bits in 
some data communications service, i.e. the usual FEC bits are allocated to information bits. 
What would be the average bit rate achieved for the service? 
Page 6 of 11 pages


## Page 7

d) Assume that instead of GMSK the modulation is changed to 16QAM with a = 0.3. The 
time for transmission of equalizer training sequence remains the same and the FEC code 
rate is 3/4,  Determine the achievable data transmission rate in a whole RF carrier. 
e) What is the time available per TDMA frame for a terminal to search for signals in 
neighbouring cells (e.g. to determine hand-off)? 
I) If the system uses a frequency re-use cluster size of 4 cells and omnidirectional antennas. 
What is the number of users supported per cell assuming that one RF channel per cell is 
used for control functions and not speech signals. 
Page 7 of 11 pages


## Page 8

4) A cellular operator has frequency spectrum of 15 + 15 MIHz in the PCS band. This is an 
FDD system, which means 15 MIHz in the downlink and 15 MHz in the uplink. The 
operator wishes to deploy LTE using RF carriers with as large as possible bandwidth. We 
will focus on the downlink. 
What is the number of subcarriers in the modulation scheme? 
Determine the maximum bit rate achieved in the downlink if all the resource elements are 
used for the payload and if the signal to noise ratio is large (e.g. terminal is close to the 
base station). 
c) Determine the maximum bit rate as in b) but under low SNR conditions, that is the terminal 
is far from the base station. 
Page 8 of 11 pages


## Page 9

d) Determine the percentage overhead incurred by the use of channel equalization symbols. 
e) Assume that the minimum allocation of a transmission resource, in time, is one sub-frame 
(i.e. 2 slots). What is the largest number of users that can be supported in the system 
simultaneously and what is the bit rate for each user in such a case assuming no FEC. 
f) Assume that the above LTE system is implemented with a 2 x 2 MIMO configuration, i.e. 
2 transmitter antennas and 2 receiver antennas. Determine the maximum bit rate assuming 
that all the resource elements are allocated to one user. 
Page 9 of 11 pages


## Page 10

5) A wireless communication system utilizes an array antenna with a beam pattern (amplitude gain) 
given by A(çb) = (1 + cos(4))2  cos(6) u(9), where is the azimuth angle (0 to 2m), 8 is the 
elevation angle (- to 
and u(.) Is the step function, (i.e. no radiation in the lower half 
Ir 
 
sphere). For parts a) to e) assume zero elevation, i.e. 8 = 0, or ground links. 
a) Plot the beam pattern for the array in terms of the power gain. 
b) Specify the directions (angles of arrival) where the antenna gain is maximum. 
c) Specify the directions (angles of arrival) where the antenna gain is minimum. 
Page 10 of 11 pages


## Page 11

d) Can this antenna be used in a sectorized cellular system? If so, what is the angle for the cell 
sector assuming that we use a 3 dB power level to define antenna beam-width? 
e) 
In a wireless system a signal is being received in the presence of three interferers. The signal 
7r 
27r 
is in the direction 
= --, and the interferers are in the directions 
, 
, and 
. If the antenna 
pattern was contant with unity amplitude gain, then the signal and interferers would have 
received powers equal to -60 dBm, -70 dBm, -73 dBm, and -73 dBm respectively. Find the 
signal to interference ratio in the case that the antenna is as specified in the above. 
Page 11 of 11 pages

