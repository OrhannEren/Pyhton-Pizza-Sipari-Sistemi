import csv
import datetime

class Pizza:
    def get_description(self):
        return self.__class__.__name__
    
    def get_cost(self):
        return self.__class__.cost
    

class Klasik(Pizza):
    cost = 60
    
    #alt sınıf özellikleri
    def __init__(self):
       
        self.description = "Malzemeler: Sucuk, Kaşar, Mantar"
        print(self.description + "\n")

class Margarita(Pizza):
    cost = 70
    
    def __init__(self):
       
        self.description = "Malzemeler: Mozerella, Fesleğen, Domates"
        print(self.description + "\n")

class TurkPizza(Pizza):
    cost = 100
    
    def __init__(self):
       
        self.description = "Malzemeler: Et, Biber, Salam, Sarımsak"
        print(self.description + "\n")


class SadePizza(Pizza):
    cost = 100
    
    def __init__(self):
       
        self.description = "Malzemeler: Zeytin, Sosis, Kaşar"
        print(self.description + "\n")



#Decorator üst sınıfı
class Decorator(Pizza):
    def __init__(self, sauce ):
        self.ingredients = sauce

    def get_cost(self):
        return self.ingredients.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.ingredients.get_description() + Pizza.get_description(self)
    


#Decorator Alt Sınıfı
class Zeytin(Decorator):
    cost = 1.0

    def __init__(self, sauce):
            Decorator.__init__(self, sauce)


class Mantar(Decorator):
    cost = 3.0

    def __init__(self, sauce):
            Decorator.__init__(self, sauce)

class Peynir(Decorator):
    cost = 4.0

    def __init__(self, sauce):
            Decorator.__init__(self, sauce)

class Et(Decorator):
    cost = 10.0

    def __init__(self, sauce):
            Decorator.__init__(self, sauce)


class Sogan(Decorator):
    cost = 2.0

    def __init__(self, sauce):
            Decorator.__init__(self, sauce)


class Misir(Decorator):
    cost = 4.0

    def __init__(self, sauce):
            Decorator.__init__(self, sauce)


#Menüyü ekrana yazmak
def main():
    with open("menu.txt") as menu:
        for i in menu:
            print(i, end="")

    class_dict = {
        1: Klasik,
        2: TurkPizza,
        3: TurkPizza,
        4: SadePizza,
        5: Zeytin,
        6: Mantar,
        7: Peynir,
        8: Et, 
        9: Sogan,
        10: Misir
    }
    
    command = input("Pizzanızı seçiniz:")
    
    #Yanlış girdi olursa kontrol ediyoruz
    while command not in ["1", "2", "3", "4"]:
        command = input("Yanlış tuşlama yaptınız:")

    order = class_dict[int(command)]()

    while command != "*":
        command = input("Ek malzeme seçin, Seçmek istemiyorsanız '*' tuşuna basınız: ")
        if command in ["5","6","7","8","9","10"]:
            order = class_dict[int(command)](order)


    print("\n" + order.get_description().strip() + ", ₺" + str(order.get_cost()))

#Sipariş Bilgileri

    print("***************Sipariş Bilgileri***************")
    name = input("İsminiz:")
    Kimlik_no = input("TC kimlik numaranız:")
    Kredi_kartı = input("Kredi kartı numaranızı giriniz:")
    Kredi_kartı_sifre = input("Kredi kartı şifrenizi giriniz:")
    Siparis_zamanı = datetime.datetime.now()

    with open("Orders_Database.csv", "a") as siparisler:
        siparisler = csv.writer(siparisler)
        siparisler.writerow([name, Kimlik_no, Kredi_kartı, Kredi_kartı_sifre, order.get_description(), Siparis_zamanı])

        print("Siparişiniz onaylandı...")


main()