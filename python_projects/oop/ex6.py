from string import ascii_letters


class Person:
    S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_old(old)
        self.verify_ps(ps)
        self.verify_weight(weight)

        self.__fio = fio.split()
        self.old = old
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("FIO MUST BE STRING!")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Not correct format!")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("There needs to be >1 symbol in FIO")
            if len(s.strip(letters)) != 0:
                raise TypeError("In FIO must be only letters and defise")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError('Old must be integer from 14 to 120')

    @classmethod
    def verify_weight(cls, w):
        if type(w) != float or w < 20:
            raise TypeError('Weight must be float number from 20kg')

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Passport must be string')

        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Not correct format of passport')

        for p in s:
            if not p.isdigit():
                raise TypeError('Passport number must be numbers')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_ps(passport)
        self.__passport = passport


p = Person('Куно Никита Евгеньевич', 21, '1234 567890', 78.0)
p.old = 21
p.passport = '1234 567890'
p.weight = 78.0
print(p.__dict__)




#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
#
# p = Person('Nikita', 20)
# del p.old
# p.old = 21
# print(p.__dict__ )
