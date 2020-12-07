import random
import time
import statistics


def selection_sort(list):
    '''returns the number of comparisons made and sorts the list'''
    
    comparison = []
    index = 1
    return selection_sort_helper(list, comparison, index)


def selection_sort_helper(list, comparison, index):
    while index < len(list):
        min = list[index - 1]
        min_index = index - 1
        for i in range(len(list) - index):  # this line throws error
            comparison.append(0)
            if list[i + index] <= min:
                min = list[i + index]
                min_index = i + index
        list[index - 1], list[min_index] = min, list[index - 1]
        index += 1
    return len(comparison)

#print(selection_sort([7, 8, 5, 3, 1]))


def insertion_sort(list):
    '''returns the number of comparisons made and sorts the list'''
    
    index = 1
    comparison = []
    return insertion_sort_helper(list, comparison, index)


def insertion_sort_helper(list, comparison, index):
    while index < len(list):
        for i in range(index):  # this line throws error
            comparison.append(0)
            if list[index - i] < list[index - i - 1]:
                list[index - i], list[index - i - 1] = list[index - i - 1], list[index - i]
            else:
                break
        index += 1
    return len(comparison)

#print(insertion_sort([7, 8, 5, 3, 1]))


def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time()
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()


##SELECTION SORT ANALYSIS##
comps = [499500, 1999000, 7998000, 31996000, 127992000, 511984000]
time = [0.09744405746459961, 0.4201488494873047, 1.5905959606170654, 6.2845611572265625, 26.428600072860718, 116.63792896270752]
ratio = []
cum_sum = 0
for i in range(len(comps)):
    ratio.append(comps[i] / time[i])
    cum_sum += (comps[i] / time[i])
print(ratio)
print(cum_sum / len(comps))
# AVG = 4872636.20152994


##INSERTION SORT ANALYSIS##
comps = [247986, 1018717, 3995264, 16112194, 64667449, 257507119]
time = [0.1898, 0.8072, 3.27, 12.71, 55.05, 210.77262115478516]
ratio = []
cum_sum = 0
for i in range(len(comps)):
    ratio.append(comps[i] / time[i])
    cum_sum += (comps[i] / time[i])
print(ratio)
print(cum_sum / len(comps))
# AVG = 1242417.9744265238
