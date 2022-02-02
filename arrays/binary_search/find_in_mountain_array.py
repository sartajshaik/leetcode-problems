"""
/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray nums) {
        int peak = findPeak(nums);
        int result = orderAgnosticBinarySearch(nums, 0, peak, target, true);
        if(result != -1){
            return result;
        }
        return orderAgnosticBinarySearch(nums, peak+1, nums.length()-1, target, false);
    }
    int findPeak(MountainArray nums){
        int left=0, right = nums.length()-1, mid=0;
        while(left < right){
            mid = left + (right-left)/2;
            if(nums.get(mid) < nums.get(mid+1)){
                left = mid + 1;
            }else{
                right = mid;
            }
        }
        return left;
    }
    int orderAgnosticBinarySearch(MountainArray nums, int start, int end, int target, boolean asc){
        int mid=0;
        while(start <= end){
            mid = start + (end-start)/2;
            if(target > nums.get(mid)){
                if (asc) {
                    start = mid + 1; 
                }else{
                    end = mid - 1;
                }
            }else if(target < nums.get(mid)){
                if (asc) {
                    end = mid - 1; 
                }else {
                    start = mid + 1;
                }
            }else{
                return mid;
            }
        }
        return -1;
    }
}

"""