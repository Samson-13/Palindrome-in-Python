def palin(A):
    if A == A[::-1]:
        return 'Is A Palindrome'
    return 'Not A Palindrome'

A = input('Enter something: ')
print(palin(A))