# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    def reverseKGroup(self, head, k):
        fakeNode = ListNode(0, head) #set it to be the head of the linked 
        groupPrevious = fakeNode # need to save one node before the group, as that node need to point to the first node of the newly swapped group

        while True:
            kNode = self.getKNode(groupPrevious, k)
            if not kNode: #as if kNode is equal to null, that means the end of the group has been reached, and no swap can be reached
                break;
            groupNext = kNode.next

            #reversing the group
            prev, curr = kNode.next, groupPrevious.next #as we have a fake node at the start, the kNode will be the first node of the [null , first] group, and as we are aimming to flip the group next to null, so prev = kNode.next, and current node should be the first node, so it is = groupPrevious.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            #swapping the groupPrevious to be the last node of the group
            temp = groupPrevious.next 
            groupPrevious.next = kNode
            groupPrevious = temp

        return fakeNode.next
    def getKNode(self, curr, k):
        while curr and k > 0: #when current node is not at the end, and it is still not at the end node of the group
            curr = curr.next #update current node to the node next to it
            k -= 1 #updat the k to count towards the next node
        return curr
    
    