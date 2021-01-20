# Radix Sort

### Takes $ \Theta \big( \frac{word.nBits}{digit.nBits} (n + 2^{digit.nBits} )\big) $ time

### Optimal to divide words into lg(n) bit digits

Radix-Sort(Array, digits):  
-- for i = 1 to d:  
-- -- Stable-Sort(Array thru i digits)  
-- end for  
end
