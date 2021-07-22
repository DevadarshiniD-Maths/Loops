Start_no = 0
Sec_no = 1
Number = 1
End_no = int(input("Enter a number till where you want the series to stop : "))
while Sec_no <= End_no:
    Number = Start_no + Sec_no
    Start_no = Sec_no
    Sec_no = Number
    print(Start_no)
