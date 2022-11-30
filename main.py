class LinkedList:
    # The __Node class is used internally by the LinkedList class. It is
    # invisible from outside this class due to the two underscores
    # that precede the class name. Python mangles names so that they
    # are not recognizable outside the class when two underscores
    # precede a name but aren't followed by two underscores at the
    # end of the name (i.e. an operator name).
    def getitematindex(self, index):
      Prior = None
      cursor = self.first.getNext()
      for i in range(index):
        Prior = cursor
        cursor = cursor.getNext()
      return cursor, Prior

    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1

    def isSorted(self):
      cursor = self.first.getNext()
      prioritem = cursor.getItem()
      while cursor is not None:
        if cursor.getItem() < prioritem:
          return False
        prioritem = cursor.getItem()
        cursor = cursor.getNext()
      return True
    
    def swap(self, index1, index2):
      node1, n = self.getitematindex(index1)
      node2, n = self.getitematindex(index2)
      item1saved = node1.getItem()
      node1.setItem(node2.getItem())
      node2.setItem(item1saved)

    def bubblesort(self):
      length = len(self)
      while length > 0:
        for x in range(0, length - 1):
          if self[x] > self[x + 1]:
            self.swap(x, x+1)
        length -= 1
    
    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next

        def getItem(self):
            return self.item

        def getNext(self):
            return self.next

        def setItem(self, item):
            self.item = item

        def setNext(self, next):
            self.next = next

    def __init__(self, contents=[]):
        # Here we keep a reference to the first node in the linked list
        # and the last item in the linked list. The both point to a
        # dummy node to begin with. This dummy node will always be in
        # the first position in the list and will never contain an item.
        # Its purpose is to eliminate special cases in the code below.
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.numItems = 0

        for e in contents:
            self.append(e)

    def __getitem__(self, index):
        if 0 <= index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()

        raise IndexError("LinkedList index out of range")

    def __setitem__(self, index, val):
        if 0 <= index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            cursor.setItem(val)
            return

        raise IndexError("LinkedList assignment index out of range")

    def insert(self, index, item):
      if index == 0:
        newnode = LinkedList.__Node(item, self.first.getNext())
        self.first.setNext(newnode)
        self.numItems += 1
        return
      
      if 1 <= index:
        cursor = self.first.getNext()
        
        # get the item and at index
        for x in range(1, index, 1):
          cursor = cursor.getNext()
          if cursor == None:
            cursor = self.first.getNext()

        #set next of cursor to newnode
        #set next of newnode to next of cursor old
        newnode = LinkedList.__Node(item, cursor.getNext())
        cursor.setNext(newnode)
        self.numItems += 1
        
        return
      raise IndexError("LinkedList assignment index out of range")

    def __contains__(self, item):
      cursor = self.first.getNext()
      while cursor is not None:
        if cursor.getItem() == item:
          return True
        cursor = cursor.getNext()
      return False
    
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + \
                            str(type(self)) + " + " + str(type(other)))

        result = LinkedList()
        cursorself = self.first.getNext()
        while cursorself is not None:
          result.append(cursorself.getItem())
          cursorself = cursorself.getNext()

        cursorother = other.first.getNext()
        while cursorother is not None:
          result.append(cursorother.getItem())
          cursorother = cursorother.getNext()

        return result

    

    def __delitem__(self, index):
        item, prior = self.getitematindex(index)
        next = item.getNext()
        prior.setNext(next)
        self.numItems -= 1

    def __eq__(self, other):
      if len(self) != len(other) or type(self) != type(other):
        return False

      curself = self.first.getNext()
      curother = other.first.getNext()

      while curself is not None:
        if curself.getItem() != curother.getItem():
          return False

        curself = curself.getNext()
        curother = curother.getNext()
      return True
      

    def __len__(self):
      return self.numItems

    

    def __str__(self):
      cursor = self.first.getNext()
      outString = "["

      while cursor is not None:
        outString += str(cursor.getItem()) + ","
        cursor = cursor.getNext()

      outString = outString.rstrip(",")
      outString += "]"
      return outString


def main():
    lst = LinkedList()

    for i in range(100):
        lst.append(i)
    lst2 = LinkedList(lst)

    if lst == lst2:
        print("Test 1 Passed")
    else:
        print("Test 1 Failed")

    lst3 = lst + lst2

    if len(lst3) == len(lst) + len(lst2):
        print("Test 2 Passed")
    else:
        print("Test 2 Failed")

    if 1 in lst3:
        print("Test 3 Passed")
    else:
        print("Test 3 Failed")

    if 2 in lst3:
        print("Test 4 Passed")
    else:
        print("Test 4 Failed")

    del lst[1]

    if 1 in lst:
        print("Test 5 Failed")
    else:
        print("Test 5 Passed")

    if len(lst) == 99:
        print("Test 6 Passed")
    else:
        print("Test 6 Failed")

    if lst == lst2:
        print("Test 7 Failed")
    else:
        print("Test 7 Passed")

    del lst2[2]

    if lst == lst2:
        print("Test 8 Failed")
    else:
        print("Test 8 Passed")

    lst4 = LinkedList(lst)
    lst.insert(0, 100)
    lst4 = LinkedList([100]) + lst4

    print(lst)
    print(lst4)

    if lst == lst4:
        print("Test 9 Passed")
    else:
        print("Test 9 Failed")

    lst.insert(1000, 333)
    lst4.append(333)


    if lst == lst4:
        print("Test 10 Passed")
    else:
        print("Test 10 Failed")

    
def main2():
  lst = LinkedList([2, 3, 8, 1, 21, 23, 21, 5, 5, 5, 233, 932, 902838289392, 0, 8, 10, 243, 213])
  lst.bubblesort()
  print(lst)

if __name__ == "__main__":
    main2()