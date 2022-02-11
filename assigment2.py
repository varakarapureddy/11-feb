sno=input()
name=input()
s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
s5=int(input())
s6=int(input())
total=s1+s2+s3+s4+s5+s6
avg=total/6
if avg<35:
    print("fail")
elif avg>91:
        print("o grade")
elif avg>81:
        print("a grade")
elif avg>71:
        print("b grade")
elif avg>61:
        print("c grade")
elif avg>51:
        print("d grade")
elif avg>40:
    print("pass")
