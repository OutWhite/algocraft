#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        seen.reserve(nums.size());

        for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
            const int need = target - nums[i];
            const auto it = seen.find(need);
            if (it != seen.end()) {
                return {it->second, i};
            }
            seen.emplace(nums[i], i);
        }

        return {};
    }
};
