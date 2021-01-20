# Useful Tables

| Var |       Interpretation        |    Code Friendly Name |
| :-- | :-------------------------: | --------------------: |
| n   | Element count or input size |          input.length |
| k   |   range of non-neg values   | possibleValues.length |
| w   |   bits to store each word   |            word.nBits |
| d   |  bits to store each digit   |           digit.nBits |

| Algorithm        | Worst Time |  Avg Time  |       Best Time        |    Worst space     |    Kind    | Stable | In Place |
| :--------------- | :--------: | :--------: | :--------------------: | :----------------: | :--------: | :----: | :------: |
| Insertion Sort   |    n^2     |    n^2     |           n            |         n          | Comparison |  True  |   True   |
| Bubble Sort      |    n^2     |    n^2     |           n            |         n          | Comparison |  True  |   True   |
| Merge Sort       |    nlgn    |    nlgn    |  nlgn typical, n nat.  |       n + n        | Comparison |  True  |  False   |
| Heap Sort        |    nlgn    |    nlgn    | nlgn (n for same keys) |         n          | Comparison | False  |   True   |
| Quick Sort       |    n^2     |    nlgn    |          nlgn          | n naive, lgn Hoare | Comparison | False  |   True   |
| Counting Sort    |   n + k    |   n + k    |                        |       n + k        |  Counting  |  True  |  False   |
| Radix Sort (LSD) | w/d(n + k) | w/d(n + k) |                        |       n + k        |  Counting  |  True  |  False   |
| Bucket Sort      |    n^2     |     n      |                        |       n + k        |  Counting  |  True  |  False   |
