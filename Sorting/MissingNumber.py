
def missingNumber(nums):
    i = 0
    while i < len(nums):

        correct = nums[i]
        
        if correct < len(nums)-1 and nums[i] != nums[correct]:  
            nums[i],nums[correct] = nums[correct], nums[i]
        else:
            i+=1
    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)



def main():

    arr = [4,1,2,6,0]
    print(missingNumber(arr))


if __name__ == "__main__":
    main()