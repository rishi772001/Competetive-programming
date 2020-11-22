print("please enter the grades as follows, O=10,A+=9,A=8,B+=7,B=6,RA=0")
eng=int(input("enter the english grade"))
mat=int(input("enter the maths grade"))
python=int(input("enter the python grade"))
eg=int(input("enter the eg grade"))
phy=int(input("enter the physics grade"))
che=int(input("enter the chemistry grade"))
python_lab=int(input("enter the python lab grade"))
phyche_lab=int(input("enter the physics chemistry lab grade"))

gpa1=(4*mat)+(4*eg)+(3*eng)+(3*python)+(3*phy)+(3*che)+(2*python_lab)+(2*phyche_lab)
gpa2=gpa1/24
print("your current gpa is",gpa2)
