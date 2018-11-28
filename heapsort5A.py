# from lab_5A import Heap
'''
Author: Nicole Torres
CS2303: Lab 5A
Objective: To implement a min heap
Last Modification: 11/27/18
'''
import time

start_time = (time.time())


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

    sorted = [0] * len(nums)
    for i in range(len(sorted)):
        sorted[i] = heap.extract_min()  # extract min/max of heap and place in ith position in array

    return sorted


if __name__ == '__main__':
    # hard coding for heap sort method
    data1 = [0, 2, 1, 3]
    data2 = [9, 6, 8, 54]
    data3 = [70, 90, 88, 65, 3]

    end_time = (time.time())

    print()
    print("This is data 1 sorted: ", heap_sort(data1))
    print()
    print("This is data 2 sorted: ", heap_sort(data2))
    print()
    print("This is data 3 sorted: ", heap_sort(data3))
    print()

    print('\n' "<<< %s seconds >>>" '\n' % (end_time - start_time))
