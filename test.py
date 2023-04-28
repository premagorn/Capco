def flaoting_num(arr1, tar):
    ans = 0
    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if arr1[i] + arr1[j] == tar:
                ans = int(i + j)
    return ans

def main():
    tar = int(input("Enter Target: "))
    nums = [2.5, 7.5, 11.2, 15.1]
    ans = flaoting_num(nums, tar)
    print(f'Answer: {ans}')

if __name__ == "__main__":
    main()