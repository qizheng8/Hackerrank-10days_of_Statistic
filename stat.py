def median(numbers):
    if len(numbers) % 2 == 1:
        return numbers[len(numbers)//2]
    else:
        return (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1])//2
                       
n = int(input())
numbers = sorted([int(numbers) for numbers in input().split()])
Q1 = median(numbers[:len(numbers)//2])
Q2 = median(numbers)
if n%2 == 1:
    Q3 = median(numbers[(len(numbers)//2 + 1):])
else:
    Q3 = median(numbers[(len(numbers)//2):])
    
print(Q1, Q2, Q3, sep = "\n")
