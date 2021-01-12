# Node of a doubly linked list 
class Node: 
	def __init__(self, next = None, 
					prev = None, data = None): 
		self.next = next # reference to next node in DLL 
		self.prev = prev # reference to previous node in DLL 
		self.data = data 

def push(head, new_data): 

	new_node = Node(data = new_data) 

	new_node.next = head 
	new_node.prev = None

	if head is not None: 
		head.prev = new_node 

	head = new_node 
	return head 

def printList(head): 

	node = head 

	print("Given linked list") 
	while(node is not None): 
		print(node.data, end = " "), 
		last = node 
		node = node.next
	
def rotate(head, N): 
	if N == 0: 
		return
	curr=head;
	l=1
	while curr.next!=None:
	   l+=1
	   curr=curr.next
	if N>l:
	   return
	curr.next=head
	head.prev=curr
	#N=N%l
	#N=l-N
	while N:
	   curr=curr.next
	   N-=1
	head=curr.next
	curr.next=None
	head.prev=None
	return head
	
	   
	


if __name__ == "__main__": 
	head = None

	head = push(head, 'e') 
	head = push(head, 'd') 
	head = push(head, 'c') 
	head = push(head, 'b') 
	head = push(head, 'a') 

	printList(head) 
	print("\n") 
	
	N = 6
	head = rotate(head, N) 

	printList(head) 

