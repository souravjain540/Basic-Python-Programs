"""
LC 118
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.
        1
      1   1
    1  2   1
  1  3   3   1
 1  4  6   4   1
etc
 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

below is my solution
"""

class Solution:
  def generate(self, numRows: int) -> List[List[int]]
  r = 0
  rows = []
  while r<= numRows:
    #first two rows always the same
    if r == 1:
      rows.append([1])
    if r == 2:
      rows.append([1,1])
    if r > 2:
      #row that we're on
      latestRow = rows[len(rows)-1]
      #newRow blank
      newRow = []
      newRow.append(1)
      #so it's fairly simple: add the two items from row 3+ and append it to newRow, which will turn into rows.
      for i in range(len(latestRow)-1):
          newRow.append(latestRow[i]+latestRow[i+1])
        newRow.append(1)
        rows.append(newRow)
      r+=1
  return rows