from heapq import heappop, heappush, heapify
def sort_k(arr,n,k):
   heap=arr[:k+1]
   heapify(heap)
   tar_ind=0
   for rem_elmnts_index in range(k+1,n):
      arr[tar_ind]=heappop(heap)
      heappush(heap, arr[rem_elmnts_index])
      tar_ind+=1
   while heap:
      arr[tar_ind]=heappop(heap)
      tar_ind+=1
k=3
arr=[2,6,3,12,56,8]
n=len(arr)
sort_k(arr,n,k)
print(arr)

#time complexity [nlogk]