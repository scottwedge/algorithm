"""
Decode Variations
A letter can be encoded to a number in the following way:

'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
A message is a string of uppercase letters, and it is encoded first using this scheme.

For example, 'AZB' -> '1262'

Given a string of digits S from 0-9 representing an encoded message,
return the number of ways to decode it.

Examples:
input:  S = '1262'
output: 3

explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB', and 'LFB'.
"""


def decodeVariations(S):
    result = []
    charMap = {}
    for i in range(65, 65 + 26):
        asciiChr = chr(i)
        charMap[str(i - 64)] = asciiChr

    def helper(s, acc):
        if s == "" and acc:
            result.append(acc)
            return
        curr = ""
        for i, num in enumerate(s):
            curr += num
            if curr in charMap:
                if i < len(s):
                    helper(s[i + 1:], acc + charMap[curr])

    helper(S, "")
    return len(result)


"""
	@param S: str
	@return: int


  '1262' => 1 26 2 => 12 6 2 => 1 2 6 2 

  1 -> (262) ->2 -> (62)
                     62 -> "" F
                     6  -> (2) T
             ->26 -> (2)     T

  12 -> (62) -> 6 ->(2)   T
               (62)       F



'1262' => [1], "262",              [12], "62") => 
       => [2], "62" [26], "2"      [6], "2"
       => [6], "2", [2], ""        [2], ""
       => [2], "" ,  

=======> [1, 2, 6, 2], [1, 26, 2], [12, 6, 2]


    candidates = []

    helper(S, acc):
      if S == "":
        candidates.append(acc)
      curr = ""
      for i, v in enumerate(S):
        if (curr + v) in dictionary:
          curr = curr + v
          helper(S[:i+1], acc + [(curr)])
        else:
          break

   helper(S, [])
"""
import string


# Time: (n^2) <= no this is not just n^2 because recursion is conducted inner function call and that makes exponential time complexity by accumulating the functions call.
# Space: O(26 + n) => O(n) number of number is one case
def decodeVariations(S):
    upper = string.ascii_uppercase
    result = []
    num_upper = {}
    for i in range(len(upper)):
        num_upper[str(i + 1)] = upper[i]

    def helper(s, path):
        if not s:
            result.append(path)
            return
        curr = ""
        for i, char in enumerate(s):
            curr += char
            if curr in num_upper:
                helper(s[i + 1:], path + num_upper[curr])

    helper(S, "")
    return len(result)


import string


def decodeVariations(S):
    result = []
    charMap = {}
    for i in range(65, 65 + 26):
        asciiChr = chr(i)
        charMap[str(i - 64)] = asciiChr

    def helper(s, acc):
        if s == "" and acc:
            result.append(acc)
            return
        curr = ""
        for i, num in enumerate(s):
            curr += num
            if curr in charMap:
                if i < len(s):
                    helper(s[i + 1:], acc + charMap[curr])

    helper(S, "")
    return len(result)


"""
	@param S: str
	@return: int


  '1262' => 1 26 2 => 12 6 2 => 1 2 6 2 

  1 -> (262) ->2 -> (62)
                     62 -> "" F
                     6  -> (2) T
             ->26 -> (2)     T

  12 -> (62) -> 6 ->(2)   T
               (62)       F



'1262' => [1], "262",              [12], "62") => 
       => [2], "62" [26], "2"      [6], "2"
       => [6], "2", [2], ""        [2], ""
       => [2], "" ,  

=======> [1, 2, 6, 2], [1, 26, 2], [12, 6, 2]


    candidates = []

    helper(S, acc):
      if S == "":
        candidates.append(acc)
      curr = ""
      for i, v in enumerate(S):
        if (curr + v) in dictionary:
          curr = curr + v
          helper(S[:i+1], acc + [(curr)])
        else:
          break

   helper(S, [])
"""
import string


# Time: (n^2)
# Space: O(26 + n) => O(n) number of number is one case
def decodeVariations(S):
    upper = string.ascii_uppercase
    result = []
    num_upper = {}
    for i in range(len(upper)):
        num_upper[str(i + 1)] = upper[i]

    def helper(s, path):
        if not s:
            result.append(path)
            return
        curr = ""
        for i, char in enumerate(s):
            curr += char
            if curr in num_upper:
                helper(s[i + 1:], path + num_upper[curr])

    helper(S, "")
    return len(result)


import string


# queue
# Time complexity: O(n*m) n is number of possible candidats for queue, m is number of branchs for each queue candidate
# <= Yes I think we need to count inner for loop m calcuolation as well.
# Space complexity: O(26+n) 26 for alpha_map, n for length of result,
# and when we don't know what is the bigger one we can just write down whole thing like this O(26+n).
def decodeVariations(S):
    alphas = string.ascii_uppercase
    alpha_map = {}
    result = []
    for i in range(1, len(alphas) + 1):
        alpha_map[str(i)] = alphas[i - 1]

    queue = [(S, "")]
    while queue:
        rest, path = queue.pop(0)
        if not rest:
            result.append(path)

        acc = ""
        for i in range(len(rest)):
            acc += rest[i]
            if acc in alpha_map:
                queue.append((rest[i + 1:], path + alpha_map[acc]))

    return len(result)


# Time complexity: O(n), n is the number of all possible queue's element
# Space complexity: O(26+n)
# just need to check the number of finishing thing
def decodeVariations(S):
    map1 = {}
    for i in range(65, 91):
        map1[str(i - 64)] = chr(i)

    count = 0
    queue = [S]
    while queue:
        res = queue.pop(0)
        if res == "":
            count += 1
        acc = ""
        for i in range(len(res)):
            acc += res[i]
            if acc in map1:
                queue.append(res[i + 1:])
    return count
