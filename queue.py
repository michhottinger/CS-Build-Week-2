#create a queue

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []              #create an empty array to work with

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.array.append(x)          #append x onto the array

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.array) >= 0:  #create a while loop
            x = self.array[0]        #save the value in x
            self.array.remove(x)      #remove the value
            return x             #return the value

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.array) > 0:       #check to make sure there is something to remove
            return self.array[0]       #reutrn the [0] element which is the first

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.array) > 0:          #if our array is less than 0, we know its empty
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
