'''
Author: Nicole Torres
CS2303: Lab 5A
Objective: To implement a min heap
Last Modification: 11/27/18
'''

import time


class Heap:

    def __init__(self):
        self.heap_array = [0]  # choosing to not use first element to make child/parent math easier
        self.isMin = True

    def insert(self, k):

        self.heap_array.append(k)  # k is integer

        currentIndex = len(self.heap_array)-1

        if self.isMin:
            minMaxCondition = self.heap_array[int(currentIndex / 2)] > k

            while(currentIndex !=1 and minMaxCondition):
                parentIndex = int(currentIndex / 2)
                temp = self.heap_array[parentIndex]
                self.heap_array[parentIndex] = k
                self.heap_array[currentIndex] = temp

                currentIndex = parentIndex
                if self.isMin:
                    minMaxCondition = self.heap_array[int(currentIndex / 2)] > k

    def extract_min(self):

        if len(self.heap_array) < 2:
            raise ValueError("Heap is empty!")
        elif len(self.heap_array) == 2:
            return self.heap_array.pop()
        else:

            returnValue = self.heap_array[1]
            self.heap_array[1] = self.heap_array.pop()  # put last inserted node of heap as root
            currentIndex = 1
            leftchildindex = currentIndex * 2  # left child index

            while leftchildindex < len(self.heap_array):
                # current node has left child!
                rightchildindex = 2 * currentIndex + 1
                if rightchildindex < len(self.heap_array):
                    # current node has two children!
                    leftIsSmaller = self.heap_array[leftchildindex] < self.heap_array[rightchildindex]

                    if self.isMin:
                        if leftIsSmaller:
                            swapIndex = leftchildindex
                        else:
                            swapIndex = rightchildindex
                    else:
                        if leftIsSmaller:
                            swapIndex = rightchildindex
                        else:
                            swapIndex = leftchildindex

                    if self.isMin:
                        minMaxCond = self.heap_array[currentIndex] > self.heap_array[swapIndex]
                    else:
                        minMaxCond = self.heap_array[currentIndex] < self.heap_array[swapIndex]

                    if minMaxCond:
                        temp = self.heap_array[currentIndex]
                        self.heap_array[currentIndex] = self.heap_array[swapIndex]
                        self.heap_array[swapIndex] = temp
                        currentIndex = swapIndex
                        leftchildindex = swapIndex * 2
                    else:
                        break

                else:
                    # does not have right child, only need to worry about left
                    if self.isMin:
                        minMaxCond = self.heap_array[currentIndex] > self.heap_array[leftchildindex]
                    else:
                        minMaxCond = self.heap_array[currentIndex] < self.heap_array[leftchildindex]

                    if minMaxCond:
                        tmp = self.heap_array[currentIndex]
                        self.heap_array[currentIndex] = self.heap_array[leftchildindex]
                        self.heap_array[leftchildindex] = tmp
                        currentIndex = leftchildindex
                        leftchildindex = leftchildindex * 2
                    else:
                        break

            return returnValue

    def print(self):
        print(self.heap_array[1:-1])

    def print_heap(self):
        if self.isMin:
            print("MIN HEAP:")
        # else:
        #     print("MAX HEAP")
        #
        # for i in range(1, len(self.heap_array)):
        #     print("%d:%d" % (i, self.heap_array[i]))

        for i in range(1, len(self.heap_array)):
            print(self.heap_array[i])

    def is_empty(self):
        return len(self.heap_array) == 0


def heap_sort(nums):

    heap = Heap()

    for num in nums:
        heap.insert(num)

    sorted = [0] * len(nums)  # create a new container so we don't modify the original list
    for i in range(len(sorted)):
        sorted[i] = heap.extract_min()  # extract min/max of heap and place in ith position in array

    return sorted


# read file
start_time = (time.time())
f = open("test.txt", "r")
line = f.readline()  # at this point reading the line from the file and it's stored as a string: '1, 2, 3' etc
line = line.split(', ')

#print(line)
#print(type(line)) # the type() function returns a string denoting the "type" of a variable

nums = []
for thing in line:
    nums.append(int(thing))

#nums = [int(thing) for thing in line] #this doesthe exact same thing as the above three lines

print()
print("UNSORTED: ", nums)
print("SORTED: ", heap_sort(nums))
end_time = (time.time())
print('\n' "<<< %s RUNNING TIME IN SECONDS >>>" '\n' % (end_time - start_time))
exit(0)


