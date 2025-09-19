package Array_and_Hashing;


// Complexity: O(n^2)

public class Two_sum {
    public int[] twoSum(int[] nums, int target) {        
        
        // Iterate through the array (TWICE)
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                // Return [i,j] if sum of index i and i + 1 is the target
                if (nums[i] + nums[j] == target) { 
                    return new int[]{i, j};
                }
            }
        }

        // Just return the default array values
        return nums;
    }


    // Test Cases:
    public boolean testCase() {
        int nums[] = {2,7,11,15};
        int target = 9;
        int[] sum = twoSum(nums, target);

        System.out.println(sum);
        return true;
    }

    public static void main(String[] args) {
        Two_sum sum = new Two_sum();
        System.out.println(sum.testCase());


    }
}
