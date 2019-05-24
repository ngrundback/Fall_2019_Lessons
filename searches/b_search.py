# What does this function do
# Fill in the comments to describe the process
# Is this recursive or iterative?
# Make suggestions to better this code
def mystery (arr, l, r, x):

    #
    if r >= l:

        mid = l + (r - l)/2

        #
        if arr[mid] == x:
            return mid

        #
        #
        elif arr[mid] > x:
            return mystery(arr, l, mid-1, x)

        #
        #
        else:
            return mystery(arr, mid + 1, r, x)

    else:
        #
        return -1
