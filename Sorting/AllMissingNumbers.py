

# Use a counter to keep track of the repeated numbers i.e what happens when the current element's
# Correct position already has the element itself? That means there is a duplicate. If duplicate, we just move i forward
# and increment the counter by 1
def findDisappearedNumbers(nums):
   
    i = 0
    ans = []
    counter = 0

    while i < len(nums):
        
        correct = nums[i] - 1
        print(f"i is at: {i} and correct is at : {correct}")
        if nums[correct] != nums[i]:
            nums[i],nums[correct] = nums[correct], nums[i]
       
        else:
            i+=1
        print(counter)
        print(nums)

    for i in range(len(nums)):
        if nums[i]-1 != i:
            ans.append(i+1)
        
    return ans

def main():

    #arr = [4,3,2,7,8,2,3,1]
    arr = [1,1,2,2]
    print(findDisappearedNumbers(arr))

if __name__ == "__main__":
    main()