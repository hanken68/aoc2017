import time
import json

class executionTime:
    def __init__(self) -> None:
        self.start = time.time()
        self.last = self.start
    def __repr__(self) -> str:
        now = time.time()
        sinceLast = now - self.last
        self.last = now
        return f"Time passed: {time.time()-self.start:.3f}, Since Last {sinceLast:.3f} "
    def elapsed(self) -> float:
        return time.time()-self.start

def getSettingFromFile(filename="./secrets/vars.json"):
    return json.load(open(filename, "r", encoding="utf8"))

def splitByEval(inputList, splitBy):
    returnlist = []
    index_pos = 0
    listPart = []
    for listItem in inputList:
        if listItem != splitBy:
            listPart.append(eval(listItem))
        else:
            returnlist.append(listPart)
            listPart = []
    if len(listPart) > 0:
        returnlist.append(listPart)
    return returnlist

def splitBy(inputList, splitBy):
    returnlist = []
    index_pos = 0
    listPart = []
    for listItem in inputList:
        if listItem != splitBy:
            listPart.append(listItem)
        else:
            returnlist.append(listPart)
            listPart = []
    if len(listPart) > 0:
        returnlist.append(listPart)
    return returnlist

class DblLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def add_first(self, node):
        node.next = self.head
        self.head = node
        self.len += 1
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        self.len += 1
    def insert_after(self, node, newNode):
        newNode.next = node.next
        newNode.prev = node
        node.next.prev = newNode
        node.next = newNode
        self.len += 1
    def pop(self): # pop last
        pass
    def popleft(self): # pop first
        pass
    def popat(self): # pop node num
        pass
    def pop_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.len -= 1

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    def __repr__(self):
        return self.data

        self.next.prev = node
        self.next = node
        
class NodeCost:
    def __init__(self, weight, distance):
        self.visited = False
        self.weight = int(weight)
        self.distance = int(distance)
    
    def __repr__(self):

        return f"{self.visited} {self.weight} {self.distance}"

class NodeCostLetter:
    def __init__(self, weight, distance):
        self.visited = False
        self.weight = int(weight)
        self.distance = int(distance)
    
    def __repr__(self):

        return f"{self.visited} {self.weight} {self.distance}"

def ArrSubtract(arr1, arr2):  # subtracts elements in array 2 from elements in array 1
    arrLen = min(len(arr1), len(arr2))
    returnArr = []
    for elCount in range(0,arrLen):
        returnArr.append(arr1[elCount] - arr2[elCount])
    return returnArr

def ArrAdd(arr1, arr2):
    arrLen = min(len(arr1), len(arr2))
    returnArr = []
    for elCount in range(0,arrLen):
        returnArr.append(arr1[elCount] + arr2[elCount])
    return returnArr

def spiltby(s, num):
    t = []
    x = 0
    while (x) < len(s):
        t.append((s[x:x+num]).strip())
        x=x+num
    return t