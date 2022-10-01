import math

class Calculation():

    def average_cation_cation(mas):
        sum = 0
        count = 0
        for i in range(len(mas)):
            sum = sum + float(mas[i])
            count = count + 1
        z = sum/count
        ave = round(z, 5)

        return ave

    def average_BB(mas):
        sum = float(mas[0])+2*float(mas[1])
        z = sum/3
        ave = round(z, 5)

        return ave

    def average_BB_rh(mas):

        return float(mas[0])

    def maxmin_RB(mas):
        a = mas[0]
        b = mas[3]
        c = float(b)/float(a)
        maxmin = round(c, 5)

        return maxmin

    def maxmin_RB_rh(mas):
        a = mas[0]
        b = mas[1]
        c = float(b)/float(a)
        maxmin = round(c, 5)

        return maxmin


    def deformation(mas, ave, n):
        sum = 0
        for i in range(len(mas)):
            a = 2*((float(mas[i]) - float(ave))/float(ave))**2
            sum = sum + round(a, 6)
        deform = round((1000 * sum)/n, 5)

        return deform

    def deformation_RB_rh(mas, ave, n):
        for i in range(len(mas)):
            a = 2*((float(mas[0]) - float(ave))/float(ave))**2
            b = 6*((float(mas[1]) - float(ave))/float(ave))**2
            sum = a + b
        deform = round((1000 * sum)/n, 5)

        return deform

    def deformation_BB(mas, ave):
        a = 2*((float(mas[0]) - float(ave))/float(ave))**2
        b = 4*((float(mas[1]) - float(ave))/float(ave))**2
        deform = (1000 * (a+b))/6

        return deform

    def average_RO(mas):
        ave_RO = []
        ro8 = (float(mas[0]) + 2*float(mas[1]) + float(mas[2]) + 2*float(mas[3]) + 2*float(mas[4]))/8
        ro9 = (float(mas[0]) + 2*float(mas[1]) + float(mas[2]) + 2*float(mas[3]) + 2*float(mas[4]) + float(mas[5]))/9
        ro10 = (float(mas[0]) + 2*float(mas[1]) + float(mas[2]) + 2*float(mas[3]) + 2*float(mas[4])
                + float(mas[5]) + float(mas[6]))/10
        ro12 = (float(mas[0]) + 2*float(mas[1]) + float(mas[2]) + 2*float(mas[3]) + 2*float(mas[4])
                + float(mas[5]) + float(mas[6]) + 2*float(mas[7]))/12
        ave_RO.append(round(ro8, 5))
        ave_RO.append(round(ro9, 5))
        ave_RO.append(round(ro10, 5))
        ave_RO.append(round(ro12, 5))

        return ave_RO

    def average_RO_rh(mas):
        ave_RO = []
        ro9 = (3*float(mas[0]) + 6*float(mas[1]))/9
        ro12 = (3*float(mas[0]) + 6*float(mas[1]) + 3*float(mas[2]))/12
        ave_RO.append(round(ro9, 5))
        ave_RO.append(round(ro12, 5))

        return ave_RO

    def average_BO(mas):
        sum = 0
        for i in range(len(mas)):
            sum = sum + float(mas[i])
        z = sum/3.0
        ave = round(z, 5)

        return ave

    def average_BO_rh(mas):

        return mas[0]

    def tolerance_calc(ro, bo):
        tolerance_factor = []

        for i in range(len(ro)):
            toleran = (float(ro[i])/float(bo))/(2 ** 0.5)
            tolerance_factor.append(round(toleran, 5))

        return tolerance_factor

    def average_OO(mas):
        ave_OO = []
        O2O2_ave = round((float(mas[0]) + float(mas[-1]))/2, 5)
        O2O1_ave = round((float(mas[1]) + float(mas[2]) + float(mas[3]) + float(mas[4]))/4, 5)
        OO_ave = round((O2O2_ave + O2O1_ave)/2, 5)
        ave_OO.append(O2O2_ave)
        ave_OO.append(O2O1_ave)
        ave_OO.append(OO_ave)

        return ave_OO

    def average_OO_rh(mas):
        ave_OO = round((float(mas[0]) + float(mas[1]))/2, 5)

        return ave_OO

    def deformation_RO(mas, ave):
        deform = []
        print('ave', ave)
        a0 = ((float(mas[0]) - float(ave[0]))/float(ave[0]))**2
        a1 = 2*((float(mas[1]) - float(ave[0]))/float(ave[0]))**2
        a2 = ((float(mas[2]) - float(ave[0]))/float(ave[0]))**2
        a3 = 2*((float(mas[3]) - float(ave[0]))/float(ave[0]))**2
        a4 = 2*((float(mas[4]) - float(ave[0]))/float(ave[0]))**2
        sum8 = a0 + a1 + a2 + a3 + a4
        def_RO_8 = round((1000 * sum8) / 8, 5)

        a0 = ((float(mas[0]) - float(ave[1])) / float(ave[1])) ** 2
        a1 = 2 * ((float(mas[1]) - float(ave[1])) / float(ave[1])) ** 2
        a2 = ((float(mas[2]) - float(ave[1])) / float(ave[1])) ** 2
        a3 = 2 * ((float(mas[3]) - float(ave[1])) / float(ave[1])) ** 2
        a4 = 2 * ((float(mas[4]) - float(ave[1])) / float(ave[1])) ** 2
        a5 = ((float(mas[5]) - float(ave[1])) / float(ave[1])) ** 2
        sum9 = a0 + a1 + a2 + a3 + a4 + a5
        def_RO_9 = round((1000 * sum9) / 9, 5)

        a0 = ((float(mas[0]) - float(ave[2])) / float(ave[2])) ** 2
        a1 = 2 * ((float(mas[1]) - float(ave[2])) / float(ave[2])) ** 2
        a2 = ((float(mas[2]) - float(ave[2])) / float(ave[2])) ** 2
        a3 = 2 * ((float(mas[3]) - float(ave[2])) / float(ave[2])) ** 2
        a4 = 2 * ((float(mas[4]) - float(ave[2])) / float(ave[2])) ** 2
        a5 = ((float(mas[5]) - float(ave[2])) / float(ave[2])) ** 2
        a6 = ((float(mas[6]) - float(ave[2])) / float(ave[2])) ** 2
        sum10 = a0 + a1 + a2 + a3 + a4 + a5 + a6
        def_RO_10 = round((1000 * sum10) / 10, 5)

        a0 = ((float(mas[0]) - float(ave[3])) / float(ave[3])) ** 2
        a1 = 2 * ((float(mas[1]) - float(ave[3])) / float(ave[3])) ** 2
        a2 = ((float(mas[2]) - float(ave[3])) / float(ave[3])) ** 2
        a3 = 2 * ((float(mas[3]) - float(ave[3])) / float(ave[3])) ** 2
        a4 = 2 * ((float(mas[4]) - float(ave[3])) / float(ave[3])) ** 2
        a5 = ((float(mas[5]) - float(ave[3])) / float(ave[3])) ** 2
        a6 = ((float(mas[6]) - float(ave[3])) / float(ave[3])) ** 2
        a7 = 2 * ((float(mas[7]) - float(ave[3])) / float(ave[3])) ** 2
        sum12 = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7
        def_RO_12 = round((1000*sum12) / 12, 5)

        deform.append(def_RO_8)
        deform.append(def_RO_9)
        deform.append(def_RO_10)
        deform.append(def_RO_12)

        return deform

    def deformation_RO_rh(mas, ave):
        deform = []
        a0 = 3 * ((float(mas[0]) - float(ave[0])) / float(ave[0])) ** 2
        a1 = 6 * ((float(mas[1]) - float(ave[0])) / float(ave[0])) ** 2
        sum9 = a0 + a1
        def_RO_9 = round((1000 * sum9) / 9, 5)

        a0 = 3 * ((float(mas[0]) - float(ave[1])) / float(ave[1])) ** 2
        a1 = 6 * ((float(mas[1]) - float(ave[1])) / float(ave[1])) ** 2
        a2 = 3 * ((float(mas[2]) - float(ave[1])) / float(ave[1])) ** 2
        sum12 = a0 + a1 + a2
        def_RO_12 = round((1000*sum12) / 12, 5)

        deform.append(def_RO_9)
        deform.append(def_RO_12)

        return deform

    def average_Theta(mas):
        ave = []
        ThetaZ = round((180 - float(mas[0]))/2.0, 4)
        ThetaY = round((180 - float(mas[1]))/2.0, 4)
        Theta_ave = round((ThetaZ + ThetaY)/2, 4)
        ave.append(ThetaZ)
        ave.append(ThetaY)
        ave.append(Theta_ave)

        return ave

    def average_Theta_rh(mas):

        Theta = round((180 - float(mas[0]))/2.0, 4)
        return Theta

    def calculate_banthwidth(BO, BOB):

        val = round(math.cos(float(BOB[-1]) * (math.pi/180))/(float(BO)**3.5), 5)

        return val

    def calculate_banthwidth_rh(BO, BOB):

        val = round(math.cos(float(BOB) * (math.pi/180))/(float(BO)**3.5), 5)

        return val

