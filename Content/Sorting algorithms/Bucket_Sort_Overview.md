# Bucket Sort

Assumes 0 <= input values < 1  
Relies on good distribution so that each linked list has on avarage 1 element

Divide \[0, 1\] into nBuckets equal-sized buckets.  
Distribute values into buckets.  
Sort the buckets with some sorting algo.  
List every element in every bucket.

Bucket-Sort(Array):  
-- buckets = new array of length Array.length filled with empty linked lists  
-- for i = 0 to Array.length - 1:  
-- -- buckets\[ Array.length \* Array[ i ] \].insert( Array\[ i \] )  
-- end for  
-- for i = 0 to Array.length - 1:  
-- -- Sort(buckets\[ i \])  
-- end for  
-- result = new array of length 0
-- for list in buckets:  
-- -- result.concat( list )  
-- end for  
end  

