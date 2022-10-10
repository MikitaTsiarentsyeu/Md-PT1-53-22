from sympy import isprime


def check_str(string: str):
    lower_case = 0
    upper_case = 0
    for i in string:
        if i.islower():
            lower_case += 1
        elif i.isupper():
            upper_case += 1
    return f'{upper_case} upper case, {lower_case} lower case'


# i used this module because it works much faster with big values above 10^5 than other algorithms
def is_prime(number):
    return isprime(number)


def get_ranges(sequence):
    result = ''
    dash_flag = True
    for i in range(len(sequence) - 1):
        if sequence[i] + 1 == sequence[i + 1]:
            if dash_flag:
                result += f'{sequence[i]}-'
                dash_flag = False
        else:
            result += f'{sequence[i]},'
            dash_flag = True
    result += f'{sequence[(len(sequence) - 1)]}'
    return result
