# https://leetcode.com/problems/poor-pigs/

'''
Explanation:

Given, 
#buckets = n
die & test minutes are provided

First, let see how many total experiments we can conduct
i.e #experiments = test // die

Now let say #experiments = m, we can perform (to check when pig dies)

Consider if we use 1 pig in each experiment for 1 bucket then it will take
m pigs to verify m+1 buckets  (ie after verifyin m buckets, we can deduce the last bucket easlily)

(considering 1 pig per experiment)
Now So total number of buckets we can verify is n // m -> 
Hence,
Inorder to verify all buckets we need to consider multiple pigs in single experiment

Approach :

So now it would be kinda Tensor (or k-dimensional Matrix) based approach
where k is #pigs we will consider in each experiment
|
So from the start k pigs will move in k-diff direction/axis of Tensor
& will move till they found poisionous cell in resp direction

NOTE:
max-length of each direction vector can be m + 1 (ie maximum experiments that can be conducted + Infered)
(If we conduct m experiments then we can confer 1 extra experiment without conducting it so m+1)

Thus this way we can deduce the intersecting cell by all k pigs at the end of all experiments as a poisionous cell

'''

from math import ceil, log10

def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    n = buckets
    m =  minutesToTest // minutesToDie # Experiments
    # As natural log is not accurate, so using base10
    # return math.ceil(math.log(n, m+1))  # m+1 -> As 1 experiment can be confer/deduced if all {m} fails  
    return ceil(log10(n) / log10(m+1))