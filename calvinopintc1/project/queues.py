# ======================
# Queue implementation
# ======================

from verbose import verbose_log


class ArrayQueue:
    """
    Array-based circular queue.

    Attributes:
        underlying_storage_list: internal list storing items
        front_index: index of the front element
        current_length: number of elements in the queue
        maximum_length: maximum allowed length, or -1 for unbounded
    """

    def __init__(self, maximum_length=-1):
        """
        Initialize queue.

        optional, maximum_length: integer
          If maximum_length < 0: unbounded queue
          If maximum_length >= 0: bounded queue
        """
        self.underlying_storage_list = [None]  # start with a size-1 array
        self.front_index = 0  # front starts at index 0 because the queue is empty
        self.current_length = 0  # length starts at 0 because we have no items yet
        self.maximum_length = maximum_length  # store max capacity; -1 would mean "unbounded"
        verbose_log("Initialized an empty ArrayQueue.")

    def enqueue(self, item):
        """
        Add item to back of queue.

        item: any object
        returns: True if added, False if queue is full (bounded case)
        """
        if self.maximum_length >= 0 and self.current_length == self.maximum_length:  # bounded case; if length == max_length, we cannot add
            verbose_log("Queue is at maximum capacity; enqueue() failed.")
            return False  # indicate failure to add item

        if self.current_length == len(self.underlying_storage_list):  # if the internal array is full, we need to grow it before inserting
            verbose_log("ArrayQueue is full; resizing underlying storage.")
            self._resize_underlying_storage()  # double the array size (or cap at maximum_length) and copy items in queue order

        item_index = (self.front_index + self.current_length) % len(self.underlying_storage_list)  # compute the "back" position using circular wraparound (front_index + length) % size
        self.underlying_storage_list[item_index] = item  # store the item at the computed position (this is the enqueue write)
        self.current_length += 1  # increase length because we successfully added one element
        verbose_log("Enqueued item; new queue length = " + str(self.current_length))
        return True  # indicate success

    def dequeue(self):
        """
        Remove and return front item.

        returns: item or None if queue is empty
        """
        if self.current_length == 0:  # if there are no elements, we cannot dequeue
            verbose_log("Attempted dequeue() from empty queue.")
            return None  #return None for empty queue

        item = self.underlying_storage_list[self.front_index]  # read the item at the front of the queue (front_index points to the front)
        self.current_length -= 1  # we are removing one item, so decrease length
        self.front_index = (self.front_index + 1) % len(self.underlying_storage_list)  # move front forward by 1 with wraparound (circular buffer)
        verbose_log("Dequeued item; new queue length = " + str(self.current_length))
        return item  # return the removed item

    def peek(self):
        """
        Return front item without removing it.

        returns: item or None
        """
        if self.current_length == 0:  # if empty, there is nothing to peek at (same empty rule as dequeue)
            return None  # None indicates no front item
        return self.underlying_storage_list[self.front_index]  # otherwise, return the front item without changing indices/length

    def is_empty(self):
        """
        returns: True if queue is empty, False otherwise
        """
        return self.current_length == 0  # queue is empty exactly when length is 0

    def get_length(self):
        """
        returns: current number of elements in the queue
        """
        return self.current_length

    def _resize_underlying_storage(self):
        """
        Double the array size, respecting the maximum_length if it is set.
        """
        new_size = len(self.underlying_storage_list) * 2  # standard strategy, double the underlying array size when full
        if self.maximum_length >= 0 and new_size > self.maximum_length:  # if bounded, we cannot grow beyond maximum_length
            new_size = self.maximum_length  # cap the new array size to the maximum allowed size

        new_storage_list = [None] * new_size  # allocate a new list to copy items into

        for offset in range(self.current_length):  # copy items in queue order, starting from front_index
            old_index = (self.front_index + offset) % len(self.underlying_storage_list)  # compute each old index with wraparound so we copy the logical queue order
            new_storage_list[offset] = self.underlying_storage_list[old_index]  # place item into the new list starting at index 0

        self.underlying_storage_list = new_storage_list  # swap in the new list as the underlying storage (queue items are preserved in order)
        self.front_index = 0  # reset front_index to 0 because we copied the front item into index 0
        verbose_log("Resized queue internal array to size " + str(new_size) + ".")
