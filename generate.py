from faker import Faker
import random
import string
import datetime
import csv

fakeSweden = Faker(['sv_SE'])
fakeNorway = Faker(['no_NO'])
fakeFinland = Faker(['fi_FI'])
fakeDenmark = Faker(['dk_DK'])

def getFaker():
    n = random.randint(0,80)
    if n < 40:
        return  fakeSweden, 'sv_SE'
    if n < 60:
        return fakeNorway,'no_NO'
    if n < 75:
        return  fakeDenmark,'dk_DK'
    if n <= 80:
        return fakeFinland,'fi_FI'
    


def getRandomCountry():
    n = random.randint(0,80)
    if n < 20:
        return  "Sverige"
    if n < 40:
        return "Norge"
    if n < 60:
        return "Finland"
    if n <= 80:
        return "Danmark"


def getRandomCallingCode():
    n = random.randint(0,80)
    if n < 20:
        return  "+46"
    if n < 40:
        return "+47"
    if n < 60:
        return "+358"
    if n <= 80:
        return "+45"

def getCountry(currentCountry):
    correct = ""
    if currentCountry == "sv_SE":
        correct = "Sverige"
    if currentCountry == "no_NO":
        correct = "Norge"
    if currentCountry == "fi_FI":
        correct = "Finland"
    if currentCountry == "dk_DK":
        correct = "Danmark"

    if random.randint(0,100) == 1:
        correct = getRandomCountry()


    if random.randint(0,200) == 1:
        characters = string.ascii_lowercase
        newLetter = random.sample(characters,1)[0]
        replaceIndex = random.randint(0,len(correct))
        correct =  correct[:replaceIndex] + newLetter + correct[replaceIndex + 1:]
        return correct
    return correct



def getCountryCode(currentCountry):
    correct = ""
    if currentCountry == "sv_SE":
        correct = "SE"
    if currentCountry == "no_NO":
        correct = "NO"
    if currentCountry == "fi_FI":
        correct = "FI"
    if currentCountry == "dk_DK":
        correct = "DK"
    return correct    



def getConsentToContact():
    if random.randint(0,100) == 1:
        return False
    return True




def getCallingCode(currentCountry):
    correct = ""
    if currentCountry == "sv_SE":
        correct = "+46"
    if currentCountry == "no_NO":
        correct = "+47"
    if currentCountry == "fi_FI":
        correct = "+358"
    if currentCountry == "dk_DK":
        correct = "+45"

    if random.randint(0,100) == 1:
        correct = getRandomCallingCode()


    if random.randint(0,100) == 1:
        return correct.replace("+","")
    return correct


# f = fake.first_name(), 'no_NO', 'fi_FI','dk_DK'])

antal = 0

with open('profiles1.csv', 'w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    field = ["Givenname", "Surname", "Streetaddress", "City", "Zipcode","Country", "CountryCode","NationalId","TelephoneCountryCode","Telephone","Birthday", "ConsentToContact"]
    writer.writerow(field)

    while antal < 1000:
        fake, current = getFaker()
        f = fake.first_name()
        f2 = fake.last_name()
        adr = fake.street_name()
        bn = fake.building_number()
        z = fake.postcode()
        city = fake.city()
        phone = fake.phone_number()
        telephoneCountryCode = getCallingCode(current)
        countryCode = getCountryCode(current)
        country = getCountry(current)
        birthDay = fake.date_between_dates(datetime.date(1940,1,1),datetime.date(2001,1,1))

        natId =  birthDay.strftime("%Y%m%d-") + fake.ssn()[-4:]
        consentToContact = getConsentToContact()

        print (birthDay,natId)

        field = [f, f2, adr + " " + bn, city, z,country, countryCode,natId,telephoneCountryCode,phone,birthDay, consentToContact]
        writer.writerow(field)

        antal = antal + 1


