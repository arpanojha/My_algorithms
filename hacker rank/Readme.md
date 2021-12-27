My unique solutions to hacker rank problems .  
I verified from discussion if they are indeed unique.  

Problem1(minimum_loss.py) :  in a time series array find the minimum possible "loss" that can be incurred. Problem at : https://www.hackerrank.com/challenges/minimum-loss/problem  
My solution in N log n time.   
Uee quicksort type implementation. As we move through the array we pick first element as pivot and move the future elements in order into left and right arrays and make recursive calls to these sub arrays.  
Here we just check differences between pivot element and left array as we need the loss.  
Advantage: no fancy library needed just knowledge of data structures.   
