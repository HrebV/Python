from molar_constant import MOLAR_MASS


class Molar_Mass_Calc:

    def __init__(self):
        pass

    def mol_mass_oxide(ox):
        r = float(MOLAR_MASS.get(ox[0]))
        nr = float(ox[1])
        o = float(MOLAR_MASS.get(ox[2]))
        no = float(ox[3])
        massox = round(nr*r+no*o, 4)
        return(massox)

    def mol_mass_perovskite(per):
        print('per', per)
        molar_mass_elem = []
        index_at_elem = []
        number_unit = len(per)
        for i in range(0, int(number_unit)):
            if i==0 or i%2==0:
                rr = float(MOLAR_MASS.get(per[i]))
                molar_mass_elem.append(rr)
            if i%2!=0:
                ind_elem = float(per[i])
                index_at_elem.append(ind_elem)

        number_rr = len(molar_mass_elem)
        sum = float(0.0)
        for i in range(0, int(number_rr)):
            mm = float(molar_mass_elem[i])*float(index_at_elem[i])
            sum = sum + round(mm, 4)

        return(round(sum,4), index_at_elem)

    def mol_mass_garnet(gar):

        a1 = float(MOLAR_MASS.get(gar[0]))
        na1 = float(gar[1])
        a2 = float(MOLAR_MASS.get(gar[2]))
        na2 = float(gar[3])
        b1 = float(MOLAR_MASS.get(gar[4]))
        nb1 = float(gar[5])
        b2 = float(MOLAR_MASS.get(gar[6]))
        nb2 = float(gar[7])
        o = float(MOLAR_MASS.get(gar[8]))
        no = float(gar[9])
        massgar = a1*na1+a2*na2+b1*nb1+b2*nb2+no*o
        return(massgar)

    def mol_mass_van_phos(van_phos):

        a1 = float(MOLAR_MASS.get(van_phos[0]))
        na1 = float(van_phos[1])
        a2 = float(MOLAR_MASS.get(van_phos[2]))
        na2 = float(van_phos[3])
        b1 = float(MOLAR_MASS.get(van_phos[4]))
        nb1 = float(van_phos[5])
        b2 = float(MOLAR_MASS.get(van_phos[6]))
        nb2 = float(van_phos[7])
        o = float(MOLAR_MASS.get(van_phos[8]))
        no = float(van_phos[9])
        van_phos = a1*na1+a2*na2+b1*nb1+b2*nb2+no*o
        return(van_phos)
