def l1(s):
    mm = cnt = 0;cur = ''
    for c in s:
        if c == cur: cnt += 1
        else: cnt = 1;cur = c
        mm = max(cnt,mm)
    return mm

def l2(s):
    b = s[0]
    max_cnt = cnt = 0
    for c in s:
        cnt = cnt+1 if c == b else 1
        b = c
        max_cnt = cnt if max_cnt < cnt else max_cnt
    return max_cnt

print(l1("aaaabbaabbbccbbde"))
print(l2("aaaabbaabbbccbbde"))
input()