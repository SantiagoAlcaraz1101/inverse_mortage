from math import ceil

def CalcInterestRate(Amount: int, InterestRate:float,  MonthsTime: int) -> any:

    if InterestRate == 0: return Amount/MonthsTime
    if MonthsTime == 1: return Amount
    
    
        
    I = (Amount * InterestRate * (1 + InterestRate)**MonthsTime) /((1 + InterestRate)**MonthsTime - 1)
    return ceil(I)


def ErrorHandler(Amount: int, InterestRate:float,  MonthsTime: int) -> int | float:
    if MonthsTime > 60:
        print("Maximo de cuotas excedidas, vuelva a intentar")
        return 0
    if InterestRate < 0:
        print("No se pueden tener intereses negativos")
        return 0
    if InterestRate > 0.065:
        print("La tasa de interes super el maximo permitido")
        return 0
    return CalcInterestRate(Amount, InterestRate,MonthsTime)

def main(): 
    Amount = int(input("Ingrese cuanto sera su prestamo: "))
    MonthsTime = int(input("Ingrese el tiempo en meses: "))
    InterestRate = float(input("Ingrese la cuota de interes mensual: "))

    print("El pago mensual debe de ser: ", ErrorHandler(Amount, InterestRate,MonthsTime) )




main()