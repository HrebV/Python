from molar_constant import MOLAR_MASS as MM
from molar_constant import OXIDE_PRECURSORS as OP

class Split_By_Char:

    def split_by_char(self, im_data):
        splited_oxide_list = im_data.splitlines()

        return splited_oxide_list

    def search_elem(self, book):
        elem_list = []
        for i in range(0, len(book)):
            ls = list(book[i])
            elem = []
            for j in range(0, len(ls)):
                if str(ls[j]).isalpha():
                    if str(ls[j]).isupper():
                        if str(ls[j+1]).isalpha() and str(ls[j+1]).islower():
                            temp = ls[j]+ls[j+1]
                            elem.append(temp)
                        elif str(ls[j]).isupper() and str(ls[j+1]).isdigit():
                            elem.append(ls[j])
                        elif str(ls[j]).isupper() and str(ls[j + 1]).isupper():
                            elem.append(ls[j])
            elem_list.append(elem)

        return elem_list

    def search_content(self, book):
        cont_list = []
        for i in range(0, len(book)):
            ls = list(book[i])
            cont = []
            k = 0
            while k < len(ls):
                temp = ''
                while (str(ls[k]).isdigit() or str(ls[k]) == '.'):
                    temp += ls[k]
                    if k >= len(ls) - 1:
                        break
                    else:
                        k += 1
                if temp:
                    cont.append(temp)
                if str(ls[k]).isupper() and str(ls[k + 1]).isupper():
                    cont.append('1')
                if str(ls[k]).islower() and str(ls[k + 1]).isupper():
                    cont.append('1')
                k += 1
            cont_list.append(cont)

        return cont_list

class Calc_Molar_Mass:

    def calc_molar_mass(self, formula):
        self.formula_list_sample = Split_By_Char.split_by_char(Split_By_Char, formula)
        self.elem_list_sample = Split_By_Char.search_elem(Split_By_Char, self.formula_list_sample)
        self.cont_list_sample = Split_By_Char.search_content(Split_By_Char, self.formula_list_sample)
        self.molar_mass_list_sample = Calc_Molar_Mass.calculate_mass(Calc_Molar_Mass, self.elem_list_sample, self.cont_list_sample)
        sample_dict = dict(zip(self.formula_list_sample, self.molar_mass_list_sample))
        print('\n Список зразків для синтезу: ', self.formula_list_sample)
        print('Eлементи в зразках: ', self.elem_list_sample)
        print('Склад зразків: ', self.cont_list_sample)
        print('Молярна маса вихідних сполук: ', self.molar_mass_list_sample)
        print('\n \n')

        self.prec_molar_mass, self.key_for_dict_prec, self.prec_list_symb, \
        self.prec_list_cont = Calc_Molar_Mass.calc_precursors(Calc_Molar_Mass, self.elem_list_sample)
        prec_dict = dict(zip(self.key_for_dict_prec, self.prec_molar_mass))
        print('Список прекурсорів: ', self.key_for_dict_prec)
        print('Eлементи прекурсорів: ', self.prec_list_symb)
        print('Склад прекурсорів: ', self.prec_list_cont)
        print('Молярна маса прекурсорів: ', self.prec_molar_mass)
        print('dict ', prec_dict.keys())

        Weight_Mass_precursors.find_coef_and_mass(Weight_Mass_precursors, sample_dict,  self.elem_list_sample, self.cont_list_sample,
                                                  prec_dict,  self.elem_list_sample, self.cont_list_sample)

    def calculate_mass(self, elem_list, cont_list):
        molar_mass_list = []
        for i in range(0, len(elem_list)):
            molar_mass = 0
            for j in range(0, len(elem_list[i])):
                mass = MM.get(elem_list[i][j])
                coef = cont_list[i][j]
                molar_mass = molar_mass + float(mass)*float(coef)
            molar_mass_list.append(str(round(molar_mass, 4)))

        return molar_mass_list

    def calc_precursors(self, elem_list):
        precursors = []
        for i in range(0, len(elem_list)):
            for j in range(0, len(elem_list[i])):
                if elem_list[i][j]!='O':
                    if not elem_list[i][j] in precursors:
                        precursors.append(elem_list[i][j])

        prec_list_symb = Split_By_Char.search_elem(Split_By_Char, OP)
        prec_list_cont = Split_By_Char.search_content(Split_By_Char, OP)
        new_prec_list_cont = []
        new_prec_list_symb = []
        key_for_dict_prec = []
        for i in range(0, len(precursors)):
            for j in range(0, len(prec_list_symb)):
                if precursors[i] in prec_list_symb[j]:
                    new_prec_list_symb.append(prec_list_symb[j])
                    new_prec_list_cont.append(prec_list_cont[j])
                    sum = ''
                    for k in range(0, len(prec_list_symb[j])):
                        sum = sum + prec_list_symb[j][k]+prec_list_cont[j][k]
                    key_for_dict_prec.append(sum)

        return Calc_Molar_Mass.calculate_mass(Calc_Molar_Mass, new_prec_list_symb, new_prec_list_cont), \
               key_for_dict_prec, new_prec_list_symb, new_prec_list_cont

class Weight_Mass_precursors():
    def find_coef_and_mass(self, sample_dict, sample_elem, sample_count, prec_dict, prec_elem, prec_cont):
        sample_dict_key = sample_dict.keys()
        sample_molar_mass = sample_dict.values()
        prec_dict_key = list(prec_dict.keys())
        prec_molar_mass = list(prec_dict.values())
        sample_mass = 1
        nev = []
        for smm in sample_molar_mass:
            nev_one = round(float(sample_mass)/float(smm), 5)
            nev.append(nev_one)
        print('nev', nev)

        for item in sample_elem:
            for it in item:
                for i in range(0, len(prec_dict_key)):
                    if it in prec_dict_key[i] and it != 'O':
                        print('it', it)

