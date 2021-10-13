from multiprocessing import Pool


def eh_primo(n):
    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
            print(n, 'não é primo!')
            return False
    print(n, 'é primo!')
    return True


numeros = [0,1, 2, 3, 4,5,6]*10 
pool = Pool()
pool.map(eh_primo, numeros)

