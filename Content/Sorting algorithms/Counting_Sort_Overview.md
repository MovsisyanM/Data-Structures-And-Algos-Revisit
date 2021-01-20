# Counting Sort

Assumes input is integers 0 thru k

### Stable

### Theta(n + k) or Theta(n) if k = O(n)

Storage: array of 0-k + maybe output  
Outputs: Sorted Array

Counting-Sort(Array, MaxVal):  
-- counts = new array of size k filled with zeros  
-- output = new array of size Array.length  
-- for item in Array:  
-- -- increment counts\[ item \]  
-- end for  
-- for i = 1 to counts.length:  
-- -- counts\[ i \] = itself + counts\[ i - 1 \]  
-- end for  
-- for j = Array.length down to 1:  
-- -- output\[ counts[ Array[ j ] ] \] = Array\[ j \]  
-- -- decrement counts\[ Array[ j ] \]  
-- end for  
end
