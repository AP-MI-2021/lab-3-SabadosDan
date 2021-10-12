def citire_lista():
    '''
    Citeste elementele unei liste separate printr-un singur spatiu
    '''
    lst=[]
    given_string = input("Introdu elementele listei fiind separate printr-un singur spatiu: ")
    list_as_string = given_string.split(" ")
    for i in list_as_string:
        lst.append(int(i))
    return lst


def is_prime(number: int) -> bool:
    '''
    Verifica daca un numar este prim.
    :param number: intreg
    :return: True sau False
    '''
    if number < 2:
        return False
    for i in range (2, number//2+1):
        if number % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(1) == False
    assert is_prime(15) == False
    assert is_prime(23) == True


def sum_of_list(lst: list[int]) -> int:
    '''
    Calculeaza suma elementelor unei liste
    :param lst: lista de numere intregi
    :return: suma: nr intreg
    '''
    suma = 0
    for i in lst:
        suma = suma + i
    return suma


def get_longest_sum_is_prime(lst: list[int]) -> list[int]:
    '''
    Returneaza cea mai lunga subsecventa cu proprietatea sa aiba suma elementelor prima, cu ajutorul a 2 for-uri
    :param lst: lista de numere intregi
    :return: subsecventa_maxima: lista de numere intregi
    '''
    subsecventa_maxima = []
    for i in range(len(lst)):
        for j in range (i, len(lst)):
            if is_prime(sum_of_list(lst[i:j+1])) == True and len(lst[i:j+1]) > len(subsecventa_maxima):
                subsecventa_maxima = lst[i:j+1]
    return subsecventa_maxima


def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([15, 3, 7, 2, 4]) == [15,3,7,2,4]
    assert get_longest_sum_is_prime([15, 3, 7, 2, 5]) == [3,7,2,5]
    assert get_longest_sum_is_prime(([4, 4, 4, 4, 4, 4, 4])) == []
    assert get_longest_sum_is_prime([2, 2, 2, 2, 2]) == [2]


def bit_1_counter_in_base_2(x: int) -> int:
    '''
    Returneaza numarul de cate ori apare 1 in scrierea binara
    :param x: numar intreg
    :return: counter: numar intreg
    '''
    counter = 0
    while x:
        counter = counter + x % 2
        x = x//2
    return counter




def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    '''
    Returneaza subsecventa maxima cu proprietea ca toate elementele sa aiba acelasi numar de cifra 1 in scrierea binara
    Functia afla subsecventa maxima prin verificarea continua a doi termeni consecutivi
    :param lst: lista de numere intregi
    :return: subsecventa_maxima: lista de numere intregi
    '''
    i = 1
    pozitia_initiala = 0
    pozitia_finala = 0
    subsecventa_maxima = [lst[0]]
    while i < len(lst):
        if bit_1_counter_in_base_2(lst[i-1]) == bit_1_counter_in_base_2(lst[i]):
            pozitia_finala = i
        else:
            pozitia_initiala = i
        if len(lst[pozitia_initiala:pozitia_finala+1]) > len(subsecventa_maxima):
            subsecventa_maxima = lst[pozitia_initiala:pozitia_finala+1]
        i=i+1
    return subsecventa_maxima


def test_get_longest_same_bit_counts():
    assert get_longest_same_bit_counts([16, 454, 7, 6, 10, 7, 10, 6, 5, 16, 454]) == [10,6,5]
    assert get_longest_same_bit_counts([10, 454, 6]) == [10]


def print_Menu():
    print("  1. Citire lista.")
    print("  2. Determinare cea mai lungă subsecvență cu proprietatea ca suma numerelor sa fie prima")
    print("  3. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sa aiba același număr de biți de 1 în reprezentarea binară.")
    print("  4. Iesire")


def main():
    test_get_longest_same_bit_counts()
    test_is_prime()
    test_get_longest_sum_is_prime()
    print_Menu()
    lst=[]
    should_run = True
    while should_run == True:
        optiune = input("Alege o optiune din cele prezentate mai sus: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            print(get_longest_sum_is_prime(lst))
        elif optiune == "3":
            print(get_longest_same_bit_counts(lst))
        elif optiune == "4":
            should_run = False
        else:
            print("Ai introdus o optiune gresita! Mai incearca! ")


if __name__ == '__main__':
    main()
