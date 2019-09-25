def square_sort(arr):
    def merge_sort(arr):
        if len(arr) > 1:
            n = len(arr)
            mid = n//2
            l_half = arr[:mid]
            r_half = arr[mid:]
            
            merge_sort(l_half)
            merge_sort(r_half)
            
            li,rj,k = 0,0,0
            
            while li < len(l_half) and rj < len(r_half):
                if l_half[li] > r_half[rj]:
                    arr[k] = r_half[rj]
                    rj += 1
                else:
                    arr[k] = l_half[li]
                    li += 1
                k += 1
            
            while li < len(l_half):
                arr[k] = l_half[li]
                li+=1
                k += 1
            
            while rj < len(r_half):
                arr[k] = r_half[rj]
                rj += 1
                k += 1
        
        return arr
    arr = [x*2 for x in arr]
    return merge_sort(arr)

if __name__ == "__main__":    
    arr = [14,3,2,8,34,6,345,32,24,97,45,42,1]
    print(square_sort(arr))