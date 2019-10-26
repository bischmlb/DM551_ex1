
### Problem 1

First we find n to make the explanation easier.
We know that 17 = (n^2)+1. Hence n = 4.
In other words 17 = (4^2)+1 distinct integers.
We need to show that, there exists atleast one increasing or decreasing subsequence of length at least n+1 (4+1) = 5.

We suppose that if there is not an increasing subsequence of length 5, then there must be a decreasing.

If we suppose that mk is the length of the longest sequence of increasing price from left to right, then 1 <= mk <= 4, because we assume that there is no increasing subsequence of length 5 or more. Hence, we have a list  of 17 integers m1, m2, m3 .., m17(m(n^2+1)) in the range 1 .. n.
The generalized pigeonhole principle tells us that at least n+1 (5) of these integers are equal, however this tells us that there actually exists a subsequence of length 5 that is decreasing in price.
Consider the worst case {1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1}, which gives us 5 (n+1) 1's. This shows that it is actually possible to find subsequences of length 5, that is decreasing. This would not change if the last entry was not a 1, but instead in range [2..4].

***

### Problem 2

a)

Possible pairs to make:

We have 9 men, and 6 women, hence:

```
9*6
=
54
```


b)

How many pairs can one make?
6 Possible pairs, with 3 leftovers. How many can one make?
The answer is P(9,6)
```
n*(n-1)*(n-2)....(n-r+1)
```
9 ways to select first pair
8 ways to select second pair
.....
4 ways to select last pair

```
9*8*7*6*5*4
=
9!/3!
=
60480
```
Consider: pairs (9,6), (8,5) (7,4) .. (4,1).
No more women are left.
This means we have 9!/3! possible ways of combining pairs between men and women.

c)

Two arrangements are only identical when the sequence of arrangements are reversed. Hence,
Ways to arrange the 6 women around the table = (N-1!) = 5! = 120 ways.

d)

Consider the sequence from the exercise with gaps of men inbetween:
``` {wi1,mi1,wi2,mi2,wi3,mi3,wi4,mi4,wi5,mi5,wi6,mi6,wi1} ```  
As we can see, there are 6! ways to arrange the men into the gaps between the women, so that no two women stand next to each other.
Because the women are already arranged in the cycle, we will only have to arrange the men.
Therefore

10C5 ??

((6+6-1)!)/(6!(6-1)!)

```
6!
=
720
```
720 ways.

***


### Problem 3

a)
Suppose we have 2 dice mapped as:

```
DIE 1:  
1:R  
2:E  
3:C  
4:U  
5:N  

DIE 2:  
1:R  
2:E  
3:L  
4:A  
5:T  
6:I  
7:O  
8:N  
```
Die 1 only has 5 values, but higher chances of rolling R, E and C because of more occurences.
However we will check for events where x = y:  
P1(E1 1 and 1(R and R)) = 3/10 * 1/8 = 3/80  
P2(E2 2 and 2(E and E)) = 3/10 * 1/8 = 3/80  
P3(E3 5 and 8(N and N)) = 1/5 * 1/8 = 1/80  
```P(x=y) = P1 + P2 + P3 = 7/80 ~ 8.75% ```


b)
Letters: RRR, EEE, CC , U, N  
We have 10 letters, and we have 3 repetitions of R, 3 repepetitions of E, 2 repetitions of C.

Solution:
```
10! / (3!3!2!)
=
50400

in python:
>>> math.factorial(10)/(math.factorial(3)*math.factorial(3)*math.factorial(2))
50400.0
```

***

### Problem 4

For n = 0
1 = 1

BASE CASE
For n = 1
3 + 7 = 5 + 5

We assume that for all n = i it holds true.

Now for n = i + 1




***


### Problem 5  
a)
Possible values X can take:
We have 2 dice, which means we have 6 unique items 1,2,3,4,5,6.

The range of X is:

```
X = {1,2,3,4,5,6}
```

b)

First we find all the possible maximum values, when throwing a pair of dice. The possible outcomes are:
```
X((1,1)) = 1  
X((1,2)) = X((2,1)) = X((2,2) = 2  
X((1,3)) = X((3,1)) = X((3,2)) = X((2,3)) = X((3,3)) = 3  
X((1,4)) = X((4,1)) = X((2,4)) = X((4,2)) = X((3,4)) = X((4,3)) = X((4,4)) = 4  
X((1,5)) = X((5,1)) = X((2,5)) = X((5,2)) = X((5,3)) = X((3,5)) = X((4,5)) = X((5,4)) = X((5,5)) = 5  
X((1,6)) = X((6,1)) = X((2,6)) = X((6,2)) = X((3,6)) = X((6,3)) = X((4,6)) = X((6,4)) = X((5,6)) = X((6,5)) = X((6,6)) = 6  
```
```
P(X = 1) = 1/36 = 0.0276 = 2.76%
P(X = 2) = 3/36 = 0.083 = 8.3%
P(X = 3) = 5/36 = 0.1389 = 13.89%
P(X = 4) = 7/36 = 0.1945 = 19.45%
P(X = 5) = 9/36 = 0.25 = 25%
P(X = 6) = 11/36 = 0.3056 = 30.56%
```

c)

For values in range X, we have:

1 possible outcome where X = 1  
3 possible outcomes where X = 2  
5 possible outcomes where X = 3  
7 possible outcomes where X = 4  
9 possible outcomes where X = 5  
11 possible outcomes where X = 6  

We can now find the expected value E(X):
```
E(X)
=
1 * 1/36 + 2 * 3/36 + 3 * 5/36 + 4 * 7/36 + 5 * 9/36 + 6 * 11/36
=
4.47222222222
```

***

### Problem 6
a)  
We have 3 variables x1, x2, x3. In order to find the answer we take:

```
(n + r - 1)!/r!(n - 1)!
```
```py
>>> math.factorial((3+15-1))/(math.factorial(15)*math.factorial(3-1))
136.0
```
Total amount:
```
C(17,15)
=
136 solutions
```

b)

We apply the principle of inclusion-exclusion. Consider:  
P1 if x1 <= 3, P2 if x3 <= 4.
The number of solutions satisfying this is:  
N(P1'P2') = N - N(P1) - N(P2) + N(P1P2)  
We need everything that is not in the set P1 and not in the set P2, also we need to add P1P2, since it is already included in the two sets.


N = total solutions = C(3+15-1,15) = C(17,15) = 136  
N(P1) = (Number of solutions with x1 <= 3) = C(3+12-1, 12) = C(14,12) = 91  
N(P2) = (Number of solutions with x3 <= 4) = C(3+11-1, 11) = C(13,11) = 78  
N(P1P2) = (Number of solutions with x1 <= 3 and x3 <= 4) = C(3 + 8-1, 8) = C(10,8) = 45  

```
N(P1'P2') = 136 - 91 - 78 + 45 = 12
```

12 Solutions.


c)  
In this exercise we use inclusion-exclusion.  
We can interpret the exercise, and find the number of solutions to:  

x1 + x2 + x3 = 15 where x1 <= 5, x2 <= 8, x3 <= 9.

Now we can solve this in similar fashion to previous exercises.  
So, we have 3 conditions: ```P1: x1 <= 5, P2: x2 <= 8, P3: x3 <= 9.```

First, the number of solutions satisfying this equation is by inclusion-exclusion principle:  
```N(P1'P2'P3') = N - N(P1) - N(P2) - N(P3) + N(P1P2) + N(P1P3) + N(P2P3) - N(P1P2P3).```  
This is because we want everything that is outside condition P1, P2, P3. We have to remember that the intersections between these sets are already included, and we will also have the small "center" of the intersection of all the conditions which will be included in the other intersections.


Again we will have 136 total solutions to this equation, as it is identical to the ones before. Hence,

```py
>>> math.factorial(3 + 15 - 1)/(math.factorial(15)*math.factorial(3 - 1))
136.0
----
C(17,15)
```

N = total solutions = C(3+15-1,15) = C(17,15) = 136  
N(P1) = (Number of solutions with x1 >= 6) = C(3+(15-6)-1, (15-6)) = C(11,9) = 55  
N(P2) = (Number of solutions with x2 >= 9) = C(3+(15-9)-1, (15-9)) = C(8,6) = 28  
N(P3) = (Number of solutions with x3 >= 10) = C(3+(15-10)-1), (15-10)) = C(7,5) = 21  
N(P1P2) = (Number of solutions with x1 >= 6, x2 >= 9) = C(3+(15-6-9) -1, (15-6-9)) = C(2,0) = 1  
*From here everything is 0 ..*  
N(P1P3) = (Number of solutions with x1 >= 6, x3 >= 10) = C(3+(15-6-10)-1, (15-6-10)) = C(1,-1) = 0  
N(P2P3) = (Number of solutions with x2 >= 9, x3 >= 10) = C(3+(15-9-10)-1, (15-9-10)) = C(-2,-4) = 0  
N(P1P2P3) = (Number of solutions with x1 >= 6, x2 >= 9, x3 >= 10) = C(3+(15-6-9-10)-1, (15-6-9-10)) = C(-8,-10) = 0  

Now we can plug our results in:  
```N(P1'P2'P3') = N - N(P1) - N(P2) - N(P3) + N(P1P2) + N(P1P3) + N(P2P3) - N(P1P2P3).```  
N(P1'P2'P3') = 136 - 55 - 28 - 21 + 1 + 0 + 0 - 0 = **33** solutions.


d)

***

### Problem 7

a)

b)
***
### Problem 8

a)

b)

c)

d)

e)

f)

***


exercises for help

test

x1 + x2 + x3 = 11  
x1 ≤ 3, x2 ≤ 4, and x3 ≤ 6

solve for P1: x1 >= 4, P2: x2 >= 5, P3: x3 >= 7

N = C(3+11-1,11) = C(13,11) = 78  
N(P1) = C(9, 7) = 36  
N(P2) = C(8, 6) = 28  
N(P3) = C(6, 4) = 15  
N(P1P2) = C(4,2) = 6  
N(P1P3) = C(2,0) = 1  
N(P2P3) = C(1, -1) = 0  
N(P1P2P3) = C(-3, -5) = 0  

78 - 36 - 28 - 15 + 6 + 1 + 0 - 0  
