import time
import random



def bubble_sort(arr):
    startTime = time.process_time()
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Main Program:




startTime = 0
endTime = 0
startTime2 = 0
endTime2 = 0

n = int(input("Enter amount of numbers you wish to check: "))
listOfNumbers = []
for x in range (0, n):
    listOfNumbers.append(random.randint(0, 100))


print(listOfNumbers)

bubble_sort(listOfNumbers)
endTime = time.process_time()

print(listOfNumbers)

print("Bubble Time taken: ", endTime)

