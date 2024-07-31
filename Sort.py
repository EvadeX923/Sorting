import random
import copy
import sys

def insertion_sort(arr):
  for k in range(1,len(arr)):
    cur = arr[k]
    j = k
    while j>0 and arr[j-1] > cur:
      arr[j] = arr[j-1]
      j = j-1
    arr[j] = cur

def selection_sort(arr):
    for k in range(0, len(arr)):
        minloc = k
        j = k + 1
        while j < len(arr):
            if arr[j] < arr[minloc]:
                minloc = j
            j = j + 1
        temp = arr[k]
        arr[k] = arr[minloc]
        arr[minloc] = temp