def validatePassword(pw):
    def l(s):
        mm = cnt = 0;cur = ''
        for c in s:
            if c == cur: cnt += 1
            else: cnt = 1;cur = c
            mm = max(cnt,mm)
        return mm <= 2
    c1 = len(pw)>=6 and len(pw)<=24
    c2 = any(x.isupper() for x in pw)
    c3 = any(x.islower() for x in pw)
    c4 = any(x.isdigit() for x in pw)
    c5 = l(pw)
    valid  = '''0123456789!@#$%^&*()+=_-{}[]:;"'?<>,.'''
    valid += '''abcdefghijklmnopqrstuvwxyz'''
    valid += '''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    c6 = any(x in valid for x in pw)
    print(c1,c2,c3,c4,c5,c6)
    return all([c1,c2,c3,c4,c5,c6])


print(validatePassword("iMiissyou"))

