name=input("enter name:")
python=int(input("marks of py:"))
java=int(input("marks of java:"))
maths=int(input("marks of maths:"))

total=python+java+maths
avg=total/3

if python<30 or maths<30 or java<30:
    result="fail"
    grade="f"
elif avg>=90:
        result="ppass"
        grade="a"
elif avg>=75:
        result="ppass"
        grade="b"

elif avg>=50:
        result="ppass"
        grade="c"
else:
        result="ppass"
        grade="d"

print("ENTER stUDENT DETAILS ____")
print("name:", name)
print("pyt ma:", python)
print("jva ma:", java)

print("math:", maths)
print("result:", result)
print("grade",grade)

    

    
