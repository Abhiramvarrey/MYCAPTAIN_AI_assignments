# To generate the first n Fibonacci numbers
def generate_fibonacci_series(n):
    series = []
    if n<=0:
        return "Input should be a positive number"
    else:
        a,b=0,1
        for i in range(1, n+1):
            if i==1:
                series.append(0)
            elif i==2:
                series.append(1)
            else:
                a, b = b, a + b
                series.append(b)
    return series


n = int(input('enter nuber to generate series'))  # Number of Fibonacci numbers to generate
print(f"The first {n} Fibonacci numbers are: {generate_fibonacci_series(n)}")
