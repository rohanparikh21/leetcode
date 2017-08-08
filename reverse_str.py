def reverse(s):
    s = list(s)
    n = len(s)
    if n==0 or n==1:
        return s
    else:
        i=0
        j=n-1
        while(i<j):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i=i+1
            j=j-1
        return ''.join(s)

if __name__ == '__main__':
    print reverse('shilen')
