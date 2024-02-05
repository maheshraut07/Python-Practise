#variable length argument
def student(roll_no,name,*fav_sub):
    print(roll_no,end=' , ')
    print(name,end=' , ')
    print(fav_sub)
student('FH17','mahesh','pps')
student('FH49','shreyash','m2','pps','BEE')
student('FH29','Pranav')

