## Approach 1: Recursive Dynamic Programming
### Intuition
If you are new to Dynamic Programming, please see our Leetcode Explore Card for more information on it!

An intutive approach to solve this problem is to generate all the subsequences of the given string and find the longest palindromic string among all the generated strings. There are a total of `2^n` strings possible, where `n` denotes the length of the given string.

We can use recursion to generate all possible strings.

If the first and last characters are the same, both characters are guaranteed to be considered in the final palindrome. As a result, we add `2` to our answer variable and recursively remove the first and last characters from the remaining substring.

If the first and last characters aren’t the same, they cannot both occur in the final palindrome. As a result, we recurse over the substring removing the first and also recurse over the substring removing the last character. As we want the longest palindromic subsequence, we pick the maximum out of both of these.

To perform this recursion, we use two pointers, `i` and `j`, where `i` is the index of the first character and `j` is the index of the last character, to form a substring of `s` that is being considered. As a result, the recursive relation can be written as follows:

If `s[i] == s[j]`, perform `answer = 2 + LPS(i + 1, j - 1)`.
Else, perform `answer = max(LPS(i, j - 1), LPS(i + 1, j))`.
where `LPS(int i, int j)` is a recursive method that returns the longest palindromic subsequence of the substring formed from index `i` to index `j` in `s`. The solution is `LPS(0, n - 1)`, where `n` is the length of `s`

The recursion tree of the above relation would look something like this:

![image info](./longest_palindromic_subsequence_1.png)

Several subproblems, such as `LPS(2, n - 2)`, `LPS(1, n - 3)`, etc., are solved twice in the partial recursion tree shown above. If we draw the entire recursion tree, we can see that there are many subproblems that are solved repeatedly.

To avoid this issue, we store the solution of the subproblem in a 2D array when it is solved. When we encounter the same subproblem again, we simply refer to the array. This is called memoization.

### Algorithm
1. Create an integer variable `n` and initialize it to the size of `s`.
1. Create a 2D-array called `memo` having `n` rows and `n` columns where `memo[i][j]` contains the length of the longest palindromic subsequence of the substring formed from index `i` to `j` in `s`.
1. Return `lps(s, 0, n - 1, memo)` where `lps` is a recursive method with four parameters: `s`, the starting index of the substring under consideration as `i`, the ending index of the substring as `j` and `memo`. We perform the following in this method:
    - If `memo[i][j] != 0`, it indicates that we have already solved this subproblem, so we return `memo[i][j]`.
    - If `i > j`, the string is empty. We return 0.
    - If `i == j`, it is a substring having one character. As a result, we return `1`.
    - If the first and the last characters are the same, i.e., `s[i] == s[j]`, we include these two characters in the palindromic subsequence and add it to the longest palindromic subsequence formed using the substring from index `i + 1` to `j - 1` (inclusive). We perform `memo[i][j] = lps(s, i + 1, j - 1, memo) + 2`.
    - Otherwise, if the first and the last characters do not match, we recursively search for the longest palindromic subsequence in both the substrings formed after ignoring the first and last characters. We pick the maximum of these two. We perform `memo[i][j] = max(lps(s, i + 1, j, memo), lps(s, i, j - 1, memo))`.
    - Return `memo[i][j]`.

## Approach 2: Iterative Dynamic Programming
### Intuition
We used memoization in the preceding approach to store the answers to subproblems in order to solve a larger problem. We can also use a bottom-up approach to solve such problems without using recursion. We build answers to subproblems iteratively first, then use them to build answers to larger problems.

Using the same method as before, we create a 2D-array dp, where `dp[i][j]` contains the answer of the longest palindromic subsequence of the substring formed from index i to j in s. Our answer would be `dp[0][n - 1]`, where n is the size of s. The state transition would be as follows:

If `s[i] == s[j]`, perform `dp[i][j] = 2 + dp[i + 1][j - 1]`.
Otherwise, perform `dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])`.
The dp array can be filled in a variety of ways. A few of them are briefly discussed below:

Building from smaller to larger strings: We can begin by selecting all possible substrings of length '1', then find the largest palindromic subsequence in all substrings of length '2', then in length '3', and so on to obtain the answer for the entire string.
Using two pointers: We can use two pointers, i and j, where i points to the first character of the substring under consideration and j points to the last character. Using dp entries corresponding to all the substrings formed by selecting indices within the range from i to j (inclusive), we form answers for all the substrings that start index i - 1. The pointer j moves from j = i - 1 to j = n - 1 to cover all possible substrings that start at index i - 1. (we can also choose to move from i to j + 1, i.e., from left to right). From the end of the string, we move from right to left, decrementing i by 1 until we reach the index 0. This is the approach we take here.
Algorithm
Create an integer variable n and initialize it to the size of s.
Create a 2D-array called dp having n rows and n columns where dp[i][j] contains the length of the longest palindromic subsequence of the substring formed from index i to j in s.
We iterate using two loops. The outer loop iterates from i = n - 1 to i = 0 decrementing i by 1 after each iteration. At the end of each iteration, we will have the length of longest palindromic subsequence in all the substrings that start from index i in s. For each i, we first mark dp[i][i] = 1 because it denotes just one character and then we iterate over j = i + 1 to j = n - 1 and perform the following:
If the first and the last characters are the same, i.e., s[i] == s[j], we include these two characters in the palindromic subsequence and add it to the longest palindromic subsequence formed using the substring from index i + 1 to j - 1 (inclusive). We perform dp[i][j] = dp[i + 1][j - 1] + 2. We already have the answer for dp[i + 1][j - 1] because we computed it for substrings starting at index i + 1 in the previous iteration of outer loop.
Otherwise, if the first and the last characters do not match, we look for the longest palindromic subsequence in both the substrings formed after ignoring the first and last characters. We pick the maximum of these two. We perform dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]).
Return dp[0][n - 1].