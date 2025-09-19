package Array_and_Hashing;


// Complexity: O(n log n)
import java.util.Arrays;
public class Contain_Duplicate {
    public boolean containsDuplicate(int[] nums) {
       // Method in the array function that is used to sort all arrays in ascending order
       Arrays.sort(nums);

       // Traverse through the array:
       for (int i = 1; i < nums.length; i++) {
            // If index of current element and previous element is duplicate, return true
            if (nums[i] == nums[i - 1]) {
                return true;
            }

            // ^ Avoids index out of bounds error array:
       }

       // Else return false
        return false;
}

// Test Cases:
public boolean testCase1() {
    int[] numTest = {1,2,3,4};
    boolean duplicateTest = containsDuplicate(numTest);

    if (duplicateTest != false) {
        return false;
    }

    return true;

}

public boolean testCase2() {
    int[] numTest = {1,1,1,3,3,4,3,2,4,2};
    boolean duplicateTest = containsDuplicate(numTest);

    if (duplicateTest != true) {
        return false;
    }

    return true;
}

public boolean testCase3() {
    int[] numTest = {1,2,3,1};
    boolean duplicateTest = containsDuplicate(numTest);

    if (duplicateTest != true) {
        return false;
    }

    return true;
}

public static void main(String[] args) {
    Contain_Duplicate caseOne = new Contain_Duplicate();
    System.out.println(caseOne.testCase1());


    Contain_Duplicate caseTwo = new Contain_Duplicate();
    System.out.println(caseTwo.testCase2());

    Contain_Duplicate caseThree = new Contain_Duplicate();
    System.out.println(caseThree.testCase3());
}

}