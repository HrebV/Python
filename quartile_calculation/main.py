import quartille
import percentile
import print_quartile

def main():
    array = [3, 5, 6, 8, 10, 11, 12, 14, 15, 18, 26]
    # array = [11, 31, 21, 19, 8, 54, 35, 26, 23, 13, 29, 17]
    # array = [2, 3, 5, 7, 8, 10, 11, 13, 15, 16, 19]
    # array = [5, 6, 8, 9, 11, 12, 14, 15, 16, 16, 17, 19, 20, 22, 23, 25]
    array.sort()

    a = quartille.Quartile_estimation.calculate(array)
    b = percentile.Percentile.calc_quartile(percentile.Percentile, array)

    k=0
    for i in range(len(a)):
        if a[i] == b[i]:
            k+=1
    if k==len(a):

        print_quartile.print_result(a)
        print('initial array', array)
        quartille.Quartile_estimation.del_outside_num(array, a[-2], a[-1])
    else:
        print('error!!! Check array')

    q1 = percentile.Percentile.calc(percentile.Percentile, array, 25)
    q2 = percentile.Percentile.calc(percentile.Percentile, array, 50)
    q3 = percentile.Percentile.calc(percentile.Percentile, array, 75)
if __name__ == "__main__":
    main()