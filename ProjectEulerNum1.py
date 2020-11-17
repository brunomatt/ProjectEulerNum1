#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

multiples_of_three = []
multiples_of_five = []
shared_multiples = []
upper_limit = 1000

def three_multiples(max):
    for k in range(max):
        if k % 3 == 0:
            multiples_of_three.append(k)

def five_multiples(max):
    for k in range(max):
        if k % 5 == 0:
            multiples_of_five.append(k)

def common_multiples(max):
    for k in range(max):
        if k % 15 == 0:
            shared_multiples.append(k)

three_multiples(upper_limit)
five_multiples(upper_limit)
common_multiples(upper_limit)

sums_of_threes = 0
sums_of_fives = 0
sums_of_shared = 0

for i in multiples_of_three:
    sums_of_threes = sums_of_threes + i
for k in multiples_of_five:
    sums_of_fives = sums_of_fives + k
for j in shared_multiples:
    sums_of_shared = sums_of_shared + j

answer = sums_of_threes + sums_of_fives - sums_of_shared

print(answer)