def MergeSort(a,lb,ub):
    if lb<ub:
        mid=(lb+ub)//2
        MergeSort(a,lb,mid)
        MergeSort(a,mid+1,ub)
        merge(a,lb,mid,ub)
        
    
def merge(a,lb,mid,ub):
     i= lb
     j= mid+1
     b=[]
     while i<=mid and j<=ub:
         if a[i]<=a[j]:
             b.append(a[i])
             i=i+1
         else:
             b.append(a[j])
             j=j+1
             
     if i > mid:
        while(j<=ub):
            b.append(a[j])
            j=j+1
     else:
        while(i<=mid):
            b.append(a[i])
            i=i+1
     for idx in range(len(b)):
        a[lb + idx] = b[idx]
    
a = [7,6,10,5,9,2,15,7]
MergeSort(a,0,len(a)-1)
print(a)

