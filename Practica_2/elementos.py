
import itertools
import random
from timeit import timeit
import time
import math

def crear_lista(num_elementos):
    m = 1 
    lista_aleatoria = []
    while m <= num_elementos:
        n = random.randint(1,100)
        lista_aleatoria.append(n)
        m +=1
    return lista_aleatoria

def permutaciones(lista):
    perm = list(itertools.permutations(lista))
    return perm

def bubble_sort(num):
    aux = True
    while aux:
        aux = False
        for i in range(len(num) - 1):
            if num[i] > num[i + 1]:
                num[i], num[i + 1] = num[i + 1], num[i]
                aux = True

def selection_sort(num):
    for i in range(len(num)):
        valor_index = i
        for j in range(i + 1, len(num)):
            if num[j] < num[valor_index]:
                valor_index = j
        num[i], num[valor_index] = num[valor_index], num[i]

def insertion_sort(num):
    for i in range(1, len(num)):
        insertar = num[i]
        j = i - 1
        while j >= 0 and num[j] > insertar:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = insertar

def heap_prim(num, tam_heap, index_inicio):
    mayor = index_inicio
    hoja_izquierda = (2 * index_inicio) + 1
    hoja_derecha = (2 * index_inicio) + 2
    if hoja_izquierda < tam_heap and num[hoja_izquierda] > num[mayor]:
        mayor = hoja_izquierda

    if hoja_derecha < tam_heap and num[hoja_derecha] > num[mayor]:
        mayor = hoja_derecha

    if mayor != index_inicio:
        num[index_inicio], num[mayor] = num[mayor], num[index_inicio]

        heap_prim(num, tam_heap, mayor)

def heap_sort(num):
    n = len(num)
    for i in range(n, -1, -1):
        heap_prim(num, n, i)

    for i in range(n - 1, 0, -1):
        num[i], num[0] = num[0], num[i]
        heap_prim(num, i, 0)

def merge(lista_izquierda, lista_derecha):
    sorted_list = []
    lista_izquierda_index = lista_derecha_index = 0

    lista_izquierda_tam, lista_derecha_tam = len(lista_izquierda), len(lista_derecha)

    for _ in range(lista_izquierda_tam + lista_derecha_tam):
        if lista_izquierda_index < lista_izquierda_tam and lista_derecha_index < lista_derecha_tam:

            if lista_izquierda[lista_izquierda_index] <= lista_derecha[lista_derecha_index]:
                sorted_list.append(lista_izquierda[lista_izquierda_index])
                lista_izquierda_index += 1

            else:
                sorted_list.append(lista_derecha[lista_derecha_index])
                lista_derecha_index += 1

        elif lista_izquierda_index == lista_izquierda_tam:
            sorted_list.append(lista_derecha[lista_derecha_index])
            lista_derecha_index += 1

        elif lista_derecha_index == lista_derecha_tam:
            sorted_list.append(lista_izquierda[lista_izquierda_index])
            lista_izquierda_index += 1

    return sorted_list

def merge_sort(num):

    if len(num) <= 1:
        return num

    mid = len(num) // 2

    lista_izquierda = merge_sort(num[:mid])
    lista_derecha = merge_sort(num[mid:])

    return merge(lista_izquierda, lista_derecha)
def partition(nums, low, high):

    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]
def quick_sort(nums):

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


#lista_nueva = permutaciones(crear_lista(6))
#for x in lista_nueva:
 #   start_time = time.time()
  #  random_list_of_nums = list(x)
   # selection_sort(random_list_of_nums)
    #print((time.time() - start_time))

m = 1

while m <= 100:

    lista_nueva = permutaciones(crear_lista(9))
    vak=0
    vaj = 10000
    suma = 0       
    for x in lista_nueva:
        start_time = time.time()
        random_list_of_nums = list(x)
        quick_sort(random_list_of_nums)
        if (time.time() - start_time)>= vak:
            vak = (time.time() - start_time)
        if (time.time() - start_time) <= vaj:
            vaj = (time.time() - start_time)
        suma += (time.time() - start_time)
    print(vak, vaj, suma/math.factorial(9))
    m+=1
