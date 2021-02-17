
class Person:
    def print_info(self,n):
        for i in range (n):
            print( f' Name: {self.name}, Surname: {self. sername}, Place of birth: {self. place_of_birth}')

    def get_age (self, current_year):
        print(f'Age: {current_year - self.year_of_birth}')


p1= Person ()
p1.name = 'Elon'
p1. sername = 'Musk'
p1.place_of_birth = 'ЮАР'
p1.year_of_birth = 1971


p2 = Person()
p2.name = 'Sergei'
p2. sername = 'Korolev'
p2.place_of_birth = 'Россия'
p2.year_of_birth = 1907

p1.print_info(1)
p1.get_age(2021)

p2.print_info(1)
p2.get_age(2021)




