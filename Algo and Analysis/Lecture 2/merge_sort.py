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


arr = [1, 4, 2, 7, 8, 5, 6, 3]
print(merge_sort(arr))
arr = [2, 4, 1, 1, 7, 3]
print(merge_sort(arr))
