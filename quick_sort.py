def QuickSort(arr,start,end):
    if start < end:
       loc = part(arr,start,end)
       QuickSort(arr,start,loc-1)
       QuickSort(arr,loc+1,end)
    
def part(a,start,end):
    pivot = a[start]
    left = start +1
    right = end
    while True:
        while pivot > a[left] and left < len() and left<=right:
            left = left +1
        while pivot < a[right] and left<=right:
            right = right-1
        if  left <= right:
            a[left],a[right]=a[right],a[left]
        else:
            break
            
    a[right] ,a[start] = a[start],a[right]
        
    return right
    
        
        
    
    
arr = [7,6,10,5,9,2,15,7]
QuickSort(arr,0,len(arr)-1)
print(arr)

