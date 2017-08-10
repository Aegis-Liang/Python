"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: 
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 




123456789                      n             	r=1	c=1

1 3 5 7 9  11  13  15          2n + 1		r=2	c=2	
 2 4 6 8 10  12  14  16        2n

1   5   9      13              4n + 1		r=3	c=4
 2 4 6 8 10  12  14  16        4n + 2, 4n    
  3   7    11      15          4n + 3

1     7        13              6n + 1   	r=4	c=6
 2   6 8     12  14            6n + 2, 6n
  3 5   9  11      15          6n + 3, 6n + 5
   4     10          16        6n + 4

1       9              	       8n + 1,          r=5     c=8
 2     8 10          16        8n + 2, 8n
  3   7    11      15          8n + 3, 8n + 7
   4 6       12  14            8n + 4, 8n + 6
    5          13              8n + 5
"""







class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
    
    # input: modNumber(r), output: [1, [2,0], [3,7], [4,6], 5]
    def modNumberList(r):
        
        
    
        
        