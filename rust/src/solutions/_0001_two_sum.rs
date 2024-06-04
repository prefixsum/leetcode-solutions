struct Solution;

use std::collections::HashMap;

impl Solution {
    fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // Initialise map of seen elements
        let mut seen: HashMap<i32, i32> = HashMap::new();
        // Pass over inputs
        for (i, &n) in nums.iter().enumerate() {
            // Get complement
            let complement: i32 = target - n;
            // Check if current element's complement has been seen
            if let Some(&complement_index) = seen.get(&complement) {
                // Return current index and the complement's index
                return vec![complement_index, i as i32];
            }
            // Add current input to map
            seen.insert(n, i as i32);
        }
        // Return empty vector if no pair found
        vec![]
    }
}

#[test]
fn test() {
    /// Given test case from Leetcode.
    let case = vec![2, 7, 11, 15];
    let target = 9;
    let expected = vec![0, 1];
    assert_eq!(Solution::two_sum(case, target), expected);
}

#[test]
fn test_last() {
    /// Given test case from Leetcode, with one index being the final index.
    let case = vec![3, 2, 4];
    let target = 6;
    let expected = vec![1, 2];
    assert_eq!(Solution::two_sum(case, target), expected);
}

#[test]
fn test_repeated() {
    /// Given test case from Leetcode, with repeated values.
    let case = vec![3, 3];
    let target = 6;
    let expected = vec![0, 1];
    assert_eq!(Solution::two_sum(case, target), expected);
}
