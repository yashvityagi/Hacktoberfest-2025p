def subsets(sub,arr,i,nums,target):
    if (i==len(arr)):
        if sum(sub) == target:
            nums.append(sub[::])
        return
    if (sum(sub) > target):
        return


    # pick
    sub.append(arr[i])
    subsets(sub, arr, i,nums,target)
    sub.pop()

    # not pick
    subsets(sub,arr,i+1,nums,target)


def combinationSum(arr, target):
    nums = []
    subsets([], arr, 0, nums, target)
    return nums