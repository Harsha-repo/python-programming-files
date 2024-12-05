# this algo works based on the divide and conquer technique
# in this algo we select the pivot elements and then fix them into their crt position
#and we partion the array where we fixed the element '
# another pivot another fixing... recursively we fix all the elements in their sorted positions

def swap(start,end,elements):
    temp=elements[start]
    elements[start]=elements[end]
    elements[end]=temp

def partition(element,start,end):
    pivot_index=start
    pivot = elements[pivot_index]

    start = pivot_index+1
    end = len(elements)-1
    
    while(start<end):
        while  start<len(elements) and elements[start]<pivot:
            start+=1
        while elements[end]>pivot:
            end-=1
        
        if start < end:
            swap(start,end,elements)
    swap(end,pivot_index,elements)

    return end

def quick_sort(elements,start,end):
    if start<end:
        part_index=partition(elements,start,end)
        quick_sort(elements,start,part_index-1)
        quick_sort(elements,part_index+1,end)

if __name__== '__main__':
    elements = [11,9,29,7,2,15,28]
    quick_sort(elements,0,len(elements)-1)
    print(elements)