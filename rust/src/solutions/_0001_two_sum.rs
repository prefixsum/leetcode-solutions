struct Solution;

use std::collections::HashMap;

impl Solution {
    fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // Initialise dictionary of seen element
        let mut seen: HashMap<i32, i32> = HashMap::new();
        // Pass over inputs
        for (i, &n) in nums.iter().enumerate() {
            // Get complement
            let complement: i32 = target - n;
            if let Some(&j) = seen.get(&complement) {
                return vec![j, i as i32];
            } else {
                seen.insert(n, i as i32);
            }
        }
        vec![]
    }
}

#[test]
fn test() {
    let case = vec![2, 7, 11, 15];
    let target = 9;
    let expected = vec![0, 1];
    assert_eq!(Solution::two_sum(case, target), expected);
}
