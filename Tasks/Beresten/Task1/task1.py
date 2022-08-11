


Initial_Amount_On_Accoutn = int(input('Enter the amount you want to put on the account:'))
P = Initial_Amount_On_Accoutn
Annual_Deposit_Rate = int(2)
I = Annual_Deposit_Rate
Deposit_Period = int(input('Enter the number of years:'))
t = Deposit_Period
Amount_Of_The_Days = int(t * 365)
D = Amount_Of_The_Days
Number_Of_Periods_Per_Year = 12
K = Number_Of_Periods_Per_Year

Choice = int(input('If you want to activate capitalization press "1", if you do not want - "0":'))
if Choice == 0:
    Accrued_Profit = int(((P * I * D) / 365) / 100)
    S = Accrued_Profit
    Final_Amount =  S + P
    G = Final_Amount
    print(G)

else: 
    Accrued_Profit = int((P * (1 + (I / 100) / K) ** (t * K)))
    S = Accrued_Profit
    Final_Amount =  S + P
    G = Final_Amount
    print(G)
