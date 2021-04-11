# CS5, hw2pr1
# Filename: hw2pr1.py
# Name: Ashkon Aghassi
# Problem description: Second Python lab, problem 1!

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example problem (problem 0):  [2, 7, 5, 9]
answer0 = e[0:2] + pi[-2:]  
print(answer0)
print()

#Problem 1
answer1 = e[1:2] + pi[1:2]
print(answer1)
print()

#Problem 2
answer2 = pi[5:6] + e[2:3] + e[2:3]
print(answer2)
print()

#Problem 3
answer3 = pi[1:]
print(answer3)
print()

#Problem 4
answer4 = pi[1:2] + e[0:1] + pi[0:1] + pi[2:3] + pi[4:5]
print(answer4)
print()

# Lab1 string practice

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:  'hey'
answer5 = h[0] + h[4:6]
print(answer5)
print()


#Problem 6
answer6 = c[0:4] + m[1:3] + c[6:7]
print(answer6)
print()

#Problem 7
answer7 = h[1:] + m[1:]
print(answer7)
print()

#Problem 8
answer8 = h[0:3] + m[3:4] + c[6:7] + h[0:3] + h[0:3] + h[0:3]
print(answer8)
print()

#Problem 9 
answer9 = c[3:6] + c[1:2] + m[0:1] + h[5:6] + c[6:7] + c[5:6] + c[1:2]
print(answer9)
print()

#Problem 10
answer10 = c[0:5:2] + h[1:3] + c[0:1] + h[1:2] + c[2:4]
print(answer10)