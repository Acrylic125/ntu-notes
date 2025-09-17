from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    
    def merge(l: int, r: int):
        delta = r - l
        if delta == 0:
            return [arr[l]]
        if delta == 1:
            if arr[r] < arr[l]:
                return [arr[r], arr[l]]
            return [arr[l], arr[r]]
        mid = delta // 2 + l
        left = merge(l, mid)
        right = merge(mid + 1, r)

        new_list = []
        while len(left) > 0 or len(right) > 0:
            s_l, s_r = len(left), len(right)

            if s_l > 0 and s_r > 0:
                if left[0] < right[0]:
                    new_list.append(left[0])
                    left = left[1:]
                else:
                    new_list.append(right[0])
                    right = right[1:]
            elif s_l > 0:
                new_list.append(left[0])
                left = left[1:]
            elif s_r > 0:
                new_list.append(right[0])
                right = right[1:]
        return new_list 

    return merge(0, len(arr) - 1)

def merge_sort_in_place(arr: List[int]):
    def merge(l: int, r: int):
        delta = r - l
        if delta <= 0:
            return
        mid = delta // 2 + l
        
        merge(l, mid)
        merge(mid + 1, r)

        left_ptr_start, left_ptr_end = l, mid 
        right_ptr_start, right_ptr_end = mid+1, r

        while True:
            left_head = -1
            right_head = -1
            
            if (left_ptr_end-left_ptr_start) < 0:
                left_head = left_ptr_start
            if (right_ptr_end-right_ptr_start) < 0:
                right_head = right_ptr_start

            if left_head == -1 and right_head == -1:
                break

            if left_head != -1 and right_head != -1:
                # Case 1, we take from left 
                # means we just shift left start ptr by +1
                if arr[left_head] < arr[right_head]:
                    left_ptr_start += 1
                else:
                    # Case 2, we take from right 
                    # means we shift right ptr by +1
                    # AND shift elements of left to the right.
                    pick = arr[right_head]
                    for i in range(left_ptr_end, left_ptr_start, -1):
                        arr[i+1] = arr[i]
                    right_ptr_start += 1
                    arr[left_ptr_start] = pick
                    left_ptr_start += 1
                    left_ptr_end += 1
            # Case 1
            elif left_head != -1:
                left_ptr_start += 1
            else:
                pick = arr[right_head]
                for i in range(left_ptr_end, left_ptr_start, -1):
                    arr[i+1] = arr[i]
                right_ptr_start += 1
                arr[left_ptr_start] = pick
                left_ptr_start += 1
                left_ptr_end += 1


        
arr = [1, 4, 2, 7, 8, 5, 6, 3]
print(merge_sort(arr))
arr = [2, 4, 1, 1, 7, 3]
print(merge_sort(arr))
arr = [1, 4, 2, 7, 8, 5, 6, 3]
merge_sort_in_place(arr)
print(arr)
