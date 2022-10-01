import OxideMass
class comp_oxide:


    def compare_oxide(readoxidelist):
        new = comp_oxide.search_empty(readoxidelist)

        # # перевірку переробити
        # if oxide1==oxide2:
        #     print('1=2')
        # elif oxide1==oxide3:
        #     print('1=3')
        # elif oxide1==oxide4:
        #     print('1=4')
        # elif oxide2==oxide3:
        #     print('2=3')
        # elif oxide2==oxide4:
        #     print('2=4')
        # elif oxide3==oxide4:
        #     print('3=4')
        # else:
        #     # кількість символів у назві оксиду
        #
        #     oxide_list = []
        #     for i in range(0,len(readoxidelist)):
        #         if len(oxide1)!=0:
        #             oxide_list.append(oxide1)
        #         if len(oxide2)!=0:
        #             oxide_list.append(oxide2)
        #         if len(oxide3)!=0:
        #             oxide_list.append(oxide3)
        #         if len(oxide4)!=0:
        #             oxide_list.append(oxide4)
        #         if len(perov)!=0:
        #             oxide_list.append(perov)
        print('new_list', new)
        return new

    def search_empty(readoxide):
        print('readoxide',readoxide)
        k = len(readoxide)
        empty_index = []
        for i in range(0, k-1):
            if readoxide[i] == '':
                empty_index.append(i)
                print('empty', i)
        for i in range(4, 0, -1):
            print('i', i)
            if i in empty_index:
                readoxide.pop(i)
                print('new_read_oxide', readoxide)

        return readoxide

class calc_oxide:

    def split_on_char(n,ol):
        splited_oxide_list = list(ol[n])
        return splited_oxide_list

    def oxide_content(oxide_composition):
        size = int(len(oxide_composition))
        if size == 5:
            r = oxide_composition[0]+oxide_composition[1]
            ind1 = oxide_composition[2]
            ox = oxide_composition[3]
            ind2 = oxide_composition[4]

        if size == 4:
            r = oxide_composition[0]
            ind1 = oxide_composition[1]
            ox = oxide_composition[2]
            ind2 = oxide_composition[3]

        oxide_for_calculation = []
        oxide_for_calculation.append(r.lower())
        oxide_for_calculation.append(ind1)
        oxide_for_calculation.append(ox.lower())
        oxide_for_calculation.append(ind2)

        return oxide_for_calculation


    def perov_content(perov):
        per = list(perov)
        print('perov', perov)
        per_for_calculation = []
        zeroind = []


        if len(per)==6:
                calper1 = per[0]+per[1]
                calper2 = per[2]+per[3]
                x = 1
                per_for_calculation.append(calper1.lower())
                per_for_calculation.append(x)
                per_for_calculation.append(calper2.lower())
                per_for_calculation.append(x)

        if len(per)==5:
            calper1 = per[0]
            calper2 = per[1]+per[2]
            x = 1
            per_for_calculation.append(calper1.lower())
            per_for_calculation.append(x)
            per_for_calculation.append(calper2.lower())
            per_for_calculation.append(x)
        number = ['0','1','2','3','4','5','6','7','8','9']
        for i in range(len(per)):
            if per[i] == '0':
                if per[i+3] in number:
                    calper = per[i-2]+per[i-1]
                    x = str(per[i])+str(per[i+1])+str(per[i+2])+str(per[i+3])
                else:
                    calper = per[i-2]+per[i-1]
                    x = per[i]+per[i+1]+per[i+2]

                per_for_calculation.append(calper.lower())
                per_for_calculation.append(x)
                zeroind.append(i)
        ite = per[len(per)-4]+per[len(per)-3]
        if ite in per_for_calculation:
            per_for_calculation.append('o')
            per_for_calculation.append('3')
        else:
            per_for_calculation.append(ite.lower())
            per_for_calculation.append('1')
            per_for_calculation.append('o')
            per_for_calculation.append('3')
        print('per_for_calcu', per_for_calculation)
        return per_for_calculation


    def calc_precorsors(oxidelist):
        lengo = int(len(oxidelist))
        mol = []
        index_at_r = []
        for i in range(0, lengo-1):
            char_in_oxide = calc_oxide.split_on_char(i, oxidelist)
            oxidelist_for_calc = calc_oxide.oxide_content(char_in_oxide)
            index_at_r.append(oxidelist_for_calc[1])
            molmass_oxide = OxideMass.Molar_Mass_Calc.mol_mass_oxide(oxidelist_for_calc)
            mol.append(molmass_oxide)

        perovlist_for_calc = calc_oxide.perov_content(oxidelist[lengo-1])
        perov_molmass = OxideMass.Molar_Mass_Calc.mol_mass_perovskite(perovlist_for_calc)

        mol.append(perov_molmass[0])
        index_in_per = perov_molmass[1]
        return mol, index_at_r,index_in_per

    def mass_precursors(molarmass, indexoxide, indexper, mper):
        print('molar mass',molarmass)
        lmmo = len(molarmass)
        Mper = float(molarmass[lmmo-1])
        N = round(float(mper)/Mper, 5)
        mprecursors = []
        suma = float(0)
        for i in range(0,lmmo-1):
            mass = round((float(indexper[i])/float(indexoxide[i])) * float(molarmass[i]) * N, 4)
            suma = suma + mass

            mprecursors.append(mass)
        return mprecursors







