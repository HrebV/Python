
class Quartile_estimation():

    def quartile_splitter(idx, data):
        if len(data) % 2 == 0:
            median_is = (data[int(idx)-1]+data[int(idx)])/2
        else:
            median_is = data[int(idx)]
        return median_is

    def index_ident(data):
        if len(data) % 2 == 0:
            median_pos = len(data) / 2
        else:
            median_pos = (len(data)//2)
        return round(median_pos)

    def branch_creation(pos, array):
        left_branch = []
        right_branch =[]
        for i in range(0,pos):
            left_branch.append(array[i])
        if len(array)%2 !=0:
            pos= pos+1
        for i in range(pos, len(array)):
            right_branch.append(array[i])

        return left_branch, right_branch

    def calculate(array):
        res = []
        median_pos_q2 = Quartile_estimation.index_ident(array)
        q2 = Quartile_estimation.quartile_splitter(median_pos_q2, array)

        branches = Quartile_estimation.branch_creation(median_pos_q2, array)

        median_pos_q1 = Quartile_estimation.index_ident(branches[0])
        q1 = Quartile_estimation.quartile_splitter(median_pos_q1, array)

        median_pos_q3 = Quartile_estimation.index_ident(branches[1])
        if len(array)%2 ==0:
            pos_q3 = median_pos_q2+median_pos_q3
        else:
            pos_q3 = median_pos_q2 + median_pos_q3+1
        q3 = Quartile_estimation.quartile_splitter(pos_q3, array)

        IQR = q3 - q1
        left_limit = q1 - 1.5*IQR
        right_limit = q3 + 1.5*IQR
        res.append(q1)
        res.append(q2)
        res.append(q3)
        res.append(IQR)
        res.append(left_limit)
        res.append(right_limit)
        return  q1,q2,q3, IQR, left_limit, right_limit

    def del_outside_num(array, left_limit, right_limit):
        new_array = []
        del_elem = []
        for i in array:
            if float(left_limit) < float(i) and float(i) < float(right_limit):
                new_array.append(i)
            else:
                del_elem.append(i)

        if len(del_elem) == 0:
            print('All numbers correspond to conditions\n')
            print('~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~\n \n')
        else:
            print('new array', new_array)
            print('del elem',  del_elem)
            print('~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~\n \n')
            return new_array, del_elem



