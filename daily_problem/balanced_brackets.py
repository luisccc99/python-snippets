"""
A bracket is considered to be any one of
the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair 
if the an opening bracket (i.e., (, [, or {) occurs to the left of 
a closing bracket (i.e., ), ], or }) of the exact same type. 
There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets
it encloses are not matched. For example, {[(])} is not balanced 
because the contents in between { and } are not balanced. 
The pair of square brackets encloses a single, 
unbalanced opening bracket, (, and the pair of parentheses encloses a single, 
unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:
  1. It contains no unmatched brackets.
  2. The subset of brackets enclosed within the confines 
  of a matched pair of brackets is also a matched pair of brackets.
Given strings of brackets, determine whether each sequence 
of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO. 
"""


def isBalanced(sequence):
    brackets = []
    closing_brackets = ')]}'
    # there are equal number of brackets
    if (len(sequence)%2 != 0):
        return 'NO'

    # if it starts with a closing bracket return NO
    if (sequence[0] in closing_brackets):
        return 'NO'

    for i in range(1, len(sequence)):
        # don't add closing brackets to stack
        if (sequence[i - 1] not in closing_brackets):
            brackets.append(sequence[i - 1])

        char = sequence[i]
        if (char == ')'):
            if (not_equals('(', brackets)):
                return 'NO'
        elif (char == ']'):
            if (not_equals('[', brackets)):
                return 'NO'
        elif (char == '}'):
            if (not_equals('{', brackets)):
                return 'NO'
    return 'YES'

def not_equals(this, stack):
    return this != stack.pop() if len(stack) > 0 else ''

if __name__=='__main__':
    t = int(input().strip())
    for _ in range(t):
        sequence = input()
        print(isBalanced(sequence))
