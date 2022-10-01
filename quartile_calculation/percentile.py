import quartille

class Percentile():

    def percentile_location(self, data, per):
        loc = (per/100)*(len(data) + 1)
        return int(loc)

    def percentile_calc(self, data, loc):
        if len(data)%2==0:
            return (data[loc-1]+data[loc])/2
        else:
            return data[int(loc-1)]

    def calc_quartile(self, data):
        percent = [25, 50, 75]
        q = []
        for i in percent:
            q_loc = Percentile.percentile_location(self, data, i)
            q.append(Percentile.percentile_calc(self, data, q_loc))

        IQR = q[2] - q[0]
        q.append(IQR)
        left_limit = q[0] - 1.5 * IQR
        q.append(left_limit)
        right_limit = q[2] + 1.5 * IQR
        q.append(right_limit)
        return q

    def calc(self, data, per):
        persentile_loc = Percentile.percentile_location(self,data, per)
        persentile = Percentile.percentile_calc(self,data, persentile_loc)
        print('P('+str(per) + ') =', persentile)
        return persentile