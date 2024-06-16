class Solution:
    # Function to merge two sorted doubly linked lists
    def merge(self, first, second):
        if first is None:
            return second 
        if second is None:
            return first

        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second

    # Function to do merge sort on a doubly linked list
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head

        # Find the middle node of the list
        middle = self.findMiddle(head)

        # Split the list into two halves
        next_to_middle = middle.next
        middle.next = None
        next_to_middle.prev = None

        # Recursively sort the two halves
        left_sorted = self.mergeSort(head)
        right_sorted = self.mergeSort(next_to_middle)

        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    # Function to find the middle node of a doubly linked list
    def findMiddle(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # Function to sort the given doubly linked list using Merge Sort
    def sortDoubly(self, head):
        return self.mergeSort(head)
