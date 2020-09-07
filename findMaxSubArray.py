def findMaxSubArray(A):
    left = 0
    l_ans = 0
    r_ans = 0
    sum_cur = 0
    sum_max = -9223372036854775808
    for r in range(len(A)):
        sum_cur += A[r]
        if sum_cur > sum_max:
            sum_max = sum_cur
            l_ans, r_ans = left, r
        if sum_cur < 0:
            left = r + 1
            sum_cur = 0
    return A[l_ans: r_ans + 1]


if __name__ == "__main__":
    arg_list = [1, -54, 0]
    print(findMaxSubArray(arg_list))
