
class MergeSort:

    @classmethod
    def merge(cls, array):
        n: int = len(array)
        if n == 1:
            return array
        
        mid = n//2
        left_arr = array[:mid]
        right_arr = array[mid:]

        left_arr = MergeSort.merge(left_arr)
        right_arr = MergeSort.merge(right_arr)

        return MergeSort.merge_sort(left_arr, right_arr)
    
    @classmethod
    def merge_sort(cls, left_arr, right_arr):
        
        i_left: int = 0
        i_right: int = 0
        sorted_array = []
        while i_left < len(left_arr) and i_right < len(right_arr):
            if left_arr[i_left] <= right_arr[i_right]:
                sorted_array.append(left_arr[i_left])
                i_left += 1
            else:
                sorted_array.append(right_arr[i_right])
                i_right += 1
        
        sorted_array += left_arr[i_left:] + right_arr[i_right:]
        return sorted_array
