def l(s):
    mm = cnt = 0;cur = ''
    for c in s:
        if c == cur: cnt += 1
        else: cnt = 1;cur = c
        mm = max(cnt,mm)
    return mm > 2

print(l("abbb"))