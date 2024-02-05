BP=int(input("basic pay:"))
HRA=BP*(10/1000)
TA=BP*(5/100)
Tot_sal=BP+HRA+TA
PT=Tot_sal*(2/100)
pay_sal=Tot_sal-PT
print("salary payable after deductions=",pay_sal)
