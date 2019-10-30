
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

Using the binomial theorem with x = 7 and y = 3,  we see that

```
10n = (7+3)n = ... exercise
```

This shows to us that, a set of n elements has a total of 10^n different subsets. Each subset will have 0, 1, ... n-1 or n elements in it. Corresponding there are ```C(n,0)*5^n with 0 elements, C(n,1)*5^n with 1 element ... C(n,n-1)*5^n with n-1 elements and C(n,n)*5^n with n elements.```

```SUM(n,k=0( C(nk)*5^n ))``` gives us the total number of subsets of a set with n elements, hence
```
SUM(n,k=0( C(nk)*5^n )) = 10n
```


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

First we find all the possible scenarios of maximum values, when throwing a pair of dice. The possibilities are:
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

For this we recognize that a solution to this will correspond to a choice of 4 items of type 1, and 5 items of type 3, with a choice of 6 additional items of any type. We still have 3 variables defined, so still 3 different kinds of types, but no condition for type 2 x2. So:
C(3+6-1,6) = C(8,6) = C(8,2) = 28 solutions.


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
Ways to distribute 7 balls into 3 boxes, with k = 7, n = 3:  
C((7+3-1),3-1) = C(9,2) = 36 ways.

***

### Problem 7

a)
m committees with k persons
each committe k different skills from set S with n skills
one person per skill
exactly n different persons covering the skills

example: 4 skills = 4 people
3 committees with 3 skills each, each skill = one person.

n skills = n different persons (distinct)

We know that, if we have n skills, each skills will be covered by n distinct persons. We do not know how many of them are men, and how many are women, and this is not important, because we dont care whether the skills are being covered by a man or a woman, we are just interested in making pairs between persons p1, p2 ..pn.  
Ways to assign persons to n skills is therefore the number of skills n, and the number of persons pn, multiplied:
n * n = n^2

s1 p1 p2 p3 p4
s2 p1 p2 p3 p4
s3 p1 p2 p3 p4
s4 p1 p2 p3 p4



b)
***
### Problem 8

**Monte Carlo algorithms and majority element**

When looking for the majority element in a set of integers, we know that an element is a majority element if the element occurs more than n/2 times, for a set with n elements. When dealing with Monte Carlo algorithms, there is always a probability that the algorithm can return the wrong answer, but it is possible to reduce this probability by having a significant number of test cases, or iterations.  
The Monte Carlo algorithm for the majority element will iterate through a loop m times, and pick a random element s from a given set S, and check if s is a majority element of S. If it is, it will return true and stop the algorithm, and if no majority element is found for m iterations, it will break the loop and return false.  
In order to find the number of repetitions we need, in order to reduce the probability that the algorithm will return the wrong answer, we can make the assumption that there exists a majority element in the given set. If we assume this, then we know that the majority element will occur for more than n/2 times, hence, the probability of not stumbling upon the majority element is less than 1/2. This means that the probability that all of the chosen elements are not equal to the majority element is at most (1/2)^m, because all of our chosen elements, are chosen independently, meaning we do not base our choices on any previous computations. Hence, the more iterations m of the main loop, the lower the probability that all of the elements will be different from the majority element.  

a)

Pseudocode for *A*:
```
S'
firstFound = False
Found = False

For i in range 0 to m, do
  if firstFound is False, then
    xr = random(S)
    count = 0
    For j in S, do
      if j is equal to xr, then
        count++
        if count is at least K, then
          For k in range 0 to size(S), do
            if S[k] is not equal to xr, then
              Append S[k] to S'
              if k is equal to size(S)-1, then
                firstFound = True
  if size(S') is not 0, then
    xt = random(S')
    count = 0
      For j in S', do
        if j is equal to xt, then
          count++
      if count is at least K, then
        Found = True
return Found


```
in python (for self):

```py
def majorityPair(set, m):
    newSet = []
    found = False
    firstFound = False
    K = math.floor(len(set)/3)+1
    for i in range(0,m):
        if firstFound == False:
            xr = random.choice(set)
            print("CHOSEN xr:", xr)
            count = 0
            for j in set:
                if j == xr:
                    count = count + 1
                    if count == K:
                        print("count == K")
                        for k in range(0,len(set)):
                            print("POPPING ELEMENT ...")
                            if set[k] != xr:
                                newSet.append(set[k])
                                print("Element popped, newSet:")
                                print(newSet)
                                if k == len(set)-1:
                                    firstFound = True
        if len(newSet) != 0:
            xt = random.choice(newSet)
            print("CHOSEN xt:", xt)
            count = 0
            for j in newSet:
                if j == xt:
                    count = count + 1
            if count == K:
                print(xt, "HAS K(", count, ") occurences in ", newSet, ", and so does ", xr)
                found = True
    return found
```

b)

The reason why ```A``` is always correct if it returns ```true```, is because it only returns ```true``` if it finds a second element ```xt```, which appears in the resulting set ```S'```  
Should step 2 successfully find a case where x_r occurs K times in S, and pass the resulting set S' to step3, but for every x_t there won't be K occurences, then we will return ```false```, and move to the next iteration(round). The algorithm will simply skip step 3 and 4, if it does not find an element ```xr``` that occurs at least K times, and move to the next iteration ```m+1```.

c)

The reason why S can have at most one majority pair, is because, assuming that there is a majority pair in S, we will have ```2 * (n/3+1)``` occurences of x_i, x_j in the set, which means that we will have ```n - (2*K)``` elements left in the set.      
Because we add 1 to n/3 in K, the majority pair will occur for ```more than``` 2/3 occurences, and the remaining n - (2*K) elements will not be able to fulfill the requirement of being at least K, even if they were all the same.

d)

When assuming that we have a majority pair in a given set, we can define event E1 for representing the probability of choosing the first element xr, and E2 for choosing the second element xt, making it a majority pair.

The chance of picking the first majority pair element xr from the intial set S is equal to 2*K, which is at least 2/3. This is given that our choices are of course independent.
```
E1 = 2*(n/3+1) >= 2/3 = 0.66 = 66%
```
The chance of picking the second majority pair element xt from the leftover set, after deleting the elements which are copies of xr, is the chance K of picking an element from S'. We have to remember, that when we receive S', n/3+1 elements in the set will be gone. This means that the probability of selecting xr, will not be the same as the probability of selecting xt, because there will be less occurences, and thereby possibilites of picking a majority number. But, we also have to remember that the new set will be smaller than the initial thus, this will also increase the chance of finding xt.
The total amount of elements we will have left to choose from in S' is therefore:  
```n - (n * 1/3 + 1)```  
The amount of numbers that will be a part of the majority pair does however not change, and will still be our initial number of elements ```n/3+1```. This means that the probability of choosing the second majority pair element xt will be at least  1/2:  
```
E2 = (n/3+1)/(n-(n*1/3+1)) >= 1/2 = 0.50 = 50%
```

Now we can find the lower bound for  
```
p(E1 ∩ E2) = (2*(n/3+1)/n)*(n/3+1)/(n-(n*1/3+1))
```
Because the events are already represented as their lower bounds, being E1 >= 66%, E2 >= 50%, we can find the lower bound by multiplying ```E1 * E2```:  
```
2/3 * 1/2 = 2/6 = 1/3 = 0.33 = 33%
```
This proves that, we will have atleast 1/3 or 33% chance to find the majority pair in any of the loops.

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
