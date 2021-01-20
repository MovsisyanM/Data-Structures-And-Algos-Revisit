# Find i-th smallest/greatest element

We take i, Array as input  
Pick a random point between start and end  
Use the Partition method from quicksort to partition Array around that random point  
if indexof(random point) == i return random point  
if indexof(random point) < i return recurse(\[random point to end\])  
else return recurse(0 to random point)

#### Worst Case Theta(n^2)

#### Expected Theta(n)
