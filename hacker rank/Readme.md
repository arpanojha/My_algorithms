My unique solutions to hacker rank problems .  
I verified from discussion if they are indeed unique.  

Problem1(minimum_loss.py) :  in a time series array find the minimum possible "loss" that can be incurred. Problem at : https://www.hackerrank.com/challenges/minimum-loss/problem  
My solution in N log n time.   
Uee quicksort type implementation. As we move through the array we pick first element as pivot and move the future elements in order into left and right arrays and make recursive calls to these sub arrays.  
Here we just check differences between pivot element and left array as we need the loss.  
Advantage: no fancy library needed just knowledge of data structures.   


Problem 2(power_time.py) : find power of a number with constraints as follows   
x^n where x is between -100 and +100 while n changes from -10e31 to 10e32 where the power value is always between -10e4 and 10e4.   
Normal solution is either brute force or recursive solution where we use the fact that n can be represented as n//2 and square the result.   
My solution is to take advantage of the fact that powers are always between 10e4 and 10e-4. This means that we can use a neat formula by always raising to the power e.   
Represent problem in euler space by using e^(n * log(x)) The problem is solved in near linear time as shown in graph below. 
