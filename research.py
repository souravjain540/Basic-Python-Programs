'''读入一组字符串（待操作的），再读入一个int n记录记下来有几条命令，总共有2中命令：1、翻转  从下标为i的字符开始到i+len-1之间的字符串倒序；2、替换  命中如果第一位为1，用命令的第四位开始到最后的字符串替换原读入的字符串下标 i 到 i+len-1的字符串。每次执行一条命令后新的字符串代替旧的字符串（即下一条命令在作用在得到的新字符串上）。
命令格式：第一位0代表翻转，1代表替换；第二位代表待操作的字符串的起始下标int i；第三位表示需要操作的字符串长度int len。'''


while True:
    try:
        s = input()
        n = int(input())
        l = []
        for i in range(n):
            l.append(input())
        for i in range(n):
            l2, l3 = int(l[i][1]), (int(l[i][2]) + int(l[i][1]))
            if l[i][0] == '0':
                sfan = s[l2:l3][::-1]
                if l2 == 0:
                    s = sfan + s[l3:]
                else:
                    s = s[:l2] + s[l2:l3][::-1] + s[l3:]
                print(s)
            elif l[i][0] == '1':
                sti = l[i][3:]
                s = s[:l2] + sti + s[l3:]
                print(s)
    except:
        break