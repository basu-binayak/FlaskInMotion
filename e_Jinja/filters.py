def reverse_filter(s):
    return s[::-1]

def comment_lessThan_100(s):
    l = len(s)
    if (l<100):
        return 'Yes! The length of the comment is less than 100'
    else:
        return 'OOPS! You have more than 100 words in your comment!'