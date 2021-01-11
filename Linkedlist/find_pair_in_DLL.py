class Node:
   def __init__(self,x):
      self.data=x
      self.next=None
      self.prev=None
def insert(head,data):
   temp=Node(data)
   if head==None:
      head=temp
   else:
      temp.next=head
      head.prev=temp
      head=temp
   return head
   

def printl(head):
   temptr=head
   while(temptr!=None):
      print(temptr.data)
      temptr=temptr.next


def pairfunctn(head,x):
   count=0
   first=head
   last=head
   while(last.next!=None):
      last=last.next
   while(first!=None and last!=None and first!=last and last.next!=first):
      if first.data+last.data==x:
         count+=1
         print(first.data,last.data)
         first=first.next
         last=last.prev
      if first.data+last.data<x:
         first=first.next
      else:
         last=last.prev
         
   return count   
"""def counttriplet(head,x):
   if head==None:
      return 0
   #print(head.data)
   current, first, last = head, None, None
   count = 0
   last=head
   while(last.next!=None):
      last=last.next
   while current!=None and last!=None:
      first=current.next
      if current.data +first.data+last.data==x:
         count+=1
         current=current.next
         #first=first.next
         last=last.prev
      elif current.data+first.data+last.data<x:
         current=current.next
      else:
         last=last.prev
   return count"""
      

if __name__ == '__main__':
   head=None
   head=insert(head,9)
   head=insert(head,8)
   head=insert(head,6)
   head=insert(head,5)
   head=insert(head,4)
   head=insert(head,3)
   head=insert(head,2)
   head=insert(head,1)
   #printl(head)
   x=7
   #print(counttriplet(head,x))
   print(pairfunctn(head,x))
   