class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


def segregateEvenOdd(head):
    curr=head
    evenstart=None
    evenend=None
    oddstart=None
    oddend=None
    
    while curr:
        if curr.data%2==0:
            if evenstart==None:
                evenstart=curr
                evenend=curr
            else:
                evenend.next=curr
                evenend=evenend.next
        else:
            if oddstart==None:
                oddstart=curr
                oddend=curr
            else:
                oddend.next=curr
                oddend=oddend.next
        curr=curr.next
    if evenstart==None or oddstart==None:
        return head
    evenend.next=oddstart
    oddend.next=None
    head=evenstart
    return head



def push(head,data):
    newNode=Node(data)
    #inserting the node in front O(n)
    newNode.next=head
    head=newNode
    return head

#print(linklist)
def printlinklist(head):
    #due to global head
    node=head
    while node:
        print(node.data,end=" ")
        node=node.next
    print()


if __name__=='__main__':
    #Test case 
    
    T=int(input())
    while T:
        head=None
        T-=1
        #No. of Nodes
        n=int(input())
        #node data given
        arr=list(map(int,input().split()))
        for i in range(n-1,-1,-1):
            #funct call to create linklis
            head=push(head,arr[i])
        head=segregateEvenOdd(head)
        printlinklist(head)