# Toroidal-Rolling
Fundamental Python code for a certain video game

In a certain video game, the screen is square of a given size,s, measured in pixels. The x- and y-coordinates go from (0,0) to (s-1,s-1). Boulders are rolling across the screen, and the player must avoid being hit by them. When a boulder rolls off one edge of the screen, it appears at the opposite edge of the screen, preserving the other coordinate. For example, if s=100 and a boulder on the middle of the right edge of the screen, at coordinate (99, 50), moves to the right, it would reappear at coordinates (0, 50) (i.e. in the middle on the left edge of the screen). The screen is essentially the surface of a torus (doughnut shape) where you can imagine the right side has been joined to the left side, and the top of the screen to the bottom.

The rolling boulders are simulated by updating their (x, y) coordinates in discrete steps. Each rolling boulder is considered to move along a trajectory defined by a sequence of discrete points: (x_0,y_0),(x_1,y_1),...,(x_i,y_i). It moves along a straight line joining consecutive points in the sequence. The trajectory of a rolling boulder is parameterized by two integers a and b so that (x_i+1,y_i+1) is given by:

x_i+1=ax_i - y_i
y_i+1=x_i+by_i

If either coordinate returned by the calculation is either negative or larger than s
, then it is considered to wrap around to the other side of the screen, and carry on counting. For example, if s=100, then the coordinate (131,257) would correspond to the point at (31,57), and the coordinate (-1,-3) would correspond to the coordinate (99,97).

Given the parameters a, b and s (which govern all of the boulders on the screen at the same time), you are asked to determine the result of each of q queries. Each query is of the form (x,y,n), and is asking for the current position of a boulder that would have started at position (x,y) and taken n update steps.

Input Format
Line 1: a b s
Line 2: q
Each of the following q lines is of the format:
x y n
Constraints
1<=a<=1000
1<=b<=1000
100<=s<=1.5*10^9
1<=q<=10^5
0<=x<=s
0<=y<=s
0<=n<=10^5

Output Format
For each query, output on a separate line, the (x,y) coordinates of the result, separated by a single space.
Sample Input 0
2 3 100
3
1 0 3
0 1 4
1 1 3


Sample Output 0
1 18
45 39
83 37

Explanation 0
We are given that a=2,b=3  and s=100.
The first query asks if a boulder starts from (1,0)
 where will it end up after 3 steps. Following the rules:
(1,0)->(2*1-0,1+3*0)=(2,1)
->(2*2-1,2+3*1)=(3,5)
->(2*3-5,3+3*5)=(1,18)
So we output 1 18 on the first line

Similarly, for the second query, we must find where a boulder that starts from (0,1)
 would be after 4 steps. We get the following trajectory:

(0,1)->(2(0)-1,0+3(1))=(-1,3) is equivalent to(99,3)
->(198-3,99+9)=(195,108) is equivalent to (95,8)
->(2(95)-8,95 + 3(8))=(182,119) is equivalent to (82,19)
->(164-19,82+57)=(145,139) is equivalent to(45,39)


Notice that we converted the negative coordinate to a valid screen coordinate according to the given screen width of 100 (value of s).
We respond to the third query in a similar manner to obtain the sequence:

(1,1)->(2-1,1+3)=(1,4)
->(2-4,1+12)=(-2,13) is equivalent to (98, 13)
->(196-13, 98+39)=(183,137) is equivalent to (83, 37)


