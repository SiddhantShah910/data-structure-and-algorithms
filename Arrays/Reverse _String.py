def Reverse_str(str):
    backwards_str = []
    for i in range(len(str)-1, -1,-1):
        backwards_str.append(str[i])
        
    return ''.join(backwards_str)

print(Reverse_str('hello'))
