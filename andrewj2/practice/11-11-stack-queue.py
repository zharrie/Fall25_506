# Simple Python Implementation
class Stack:
    """Simple unbounded stack using Python list"""
    
    def __init__(self):
        self.stack_list = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.stack_list.append(item)
    
    def pop(self):
        """Remove and return top item"""
        return self.stack_list.pop()
    
    def peek(self):
        """Return top item without removing"""
        return self.stack_list[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.stack_list) == 0
    
    def get_length(self):
        """Return number of items"""
        return len(self.stack_list)

# Python Implementation
# Node class for the linked list
class QueueNode:
    def __init__(self, data_value, next_node=None):
        self.data = data_value
        self.next = next_node

# Queue class using linked list
class Queue:
    def __init__(self):
        self.front = None
        self.end = None
    
    def enqueue(self, new_data):
        """Add an item to the back of the queue"""
        # Create a new node
        new_node = QueueNode(new_data)
        
        # If queue is empty, front and end are the same
        if self.front == None:
            self.front = new_node
            self.end = new_node
        else:
            # Link current end to new node
            self.end.next = new_node
            # Update end pointer
            self.end = new_node
    
    def dequeue(self):
        """Remove and return the front item"""
        # Save the front node's data
        dequeued_item = self.front.data
        
        # Move front pointer to next node
        self.front = self.front.next
        
        # If queue is now empty, also update end
        if self.front == None:
            self.end = None
        
        return dequeued_item
    
    def peek(self):
        """Return the front item without removing it"""
        return self.front.data
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front == None
    
    def print(self, separator=", ", suffix=""):
        """Print queue from front to back"""
        node = self.front
        if node != None:
            print(node.data, end="")
            node = node.next
            while node != None:
                print(f"{separator}{node.data}", end="")
                node = node.next
            print(suffix, end="")

# Exercises
# 1.Write a function that removes all items from a stack.
def clear_stack(stack):
    while not stack.is_empty():
        stack.pop()

# Test
s = Stack()
s.push(1)
s.push(2)
s.push(3)
clear_stack(s)
print(f"Stack is empty? {s.is_empty()}")  # Should print: True

# 2.Write a function to count items in a queue without destroying it.
def count_queue_items(queue):
    new_q = Queue()
    n = 0
    while not queue.is_empty():
        new_q.enqueue(queue.dequeue())
        n += 1
    while not new_q.is_empty():
        queue.enqueue(new_q.dequeue())

    return n


# Test
q = Queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print(f"Queue count: {count_queue_items(q)}")  # Should print: 3
print(f"Queue content: {q.dequeue()} {q.dequeue()} {q.dequeue()}") # Should print: 5 10 15

# 3. Check if a string has balanced parentheses (only one type: ( and )).
def is_balanced_simple(text):
    """
    Input: "(()())"  → True
    Input: "(()"     → False
    Input: "())"     → False
    """
    pstack = Stack()
    for c in text:
        if c == '(': pstack.push(1)
        if c == ')':
            if pstack.is_empty(): return False
            else: pstack.pop()
    return pstack.is_empty()

def print_is_balanced(text):
    print(f"Is '{text}' balanced? {is_balanced_simple(text)}")

print_is_balanced("(()())")
print_is_balanced("(()")
print_is_balanced("())")
print_is_balanced(")()(")
print_is_balanced("(()()(()(()(((()()()()(()()(()()()()()()((((((()()()(()(()(()(()))))))))))))))))))")