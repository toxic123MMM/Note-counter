amount=int(input("please enter the amount of withdrawl "))
#calculate the number of notes of of differnt denomination
note1= amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

#print the number of notes for withdrawl
print("notes of 100 rupees ",note1)
print("notes of 50 rupees ",note2)
print("notes of 10 rupees ",note3)