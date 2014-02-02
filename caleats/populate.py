from bs4 import BeautifulSoup, Comment
import urllib2
from caleats.models import Entree, MenuItem

def get_entree_if_exists(itemname):
    try:
        entree = Entree.objects.get(name = itemname)
    except: #DoesNotExist
        entree = Entree(name = itemname)
        entree.save()
        print("Create Entree: " + itemname)
    return entree

def populate_day(url='http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp'):
    print("Starting population")
    MenuItem.objects.all().delete()
    print("Deleted old MenuItems")

    response = urllib2.urlopen(url)
    html = response.read()
    print("Read HTML")

    #trash.py - go for <!-- -->
    content = BeautifulSoup(html, 'html5lib').find_all(id = 'content')[2].tbody.find_all(
        'tr', {"valign":"top"})

    LOCATIONS = {0: "crossroads", 1: "cafe_3", 2: "foothill", 3: "clark_kerr"}
    #FOODTYPE = {u'#800040': 'Vegan', u'#008000': 'Vegetarian', u'#000000': 'Regular'}
    #more than one vegetarian color o__O
    print("Strained content")

    for time in content: #b/l/d
        for l, loc in enumerate(time.find_all('td')): #cr/c3/fh/ck
            meal = unicode(loc.find('b').string) #meals bolded
            #TRASH.PY
            if meal == u"Lunch/Brunch":
                meal = u"Lunch"
            entrees = loc.find_all('a')      #all meals linked to nutrition
            for entree in entrees:
                name = unicode(entree.string)
                #ftype = FOODTYPE[unicode(entree.font['color'])]
                dininghall = LOCATIONS[l]
                ent = get_entree_if_exists(name)
                newitem = MenuItem(entree = ent, hall = dininghall, meal = meal)
                newitem.save()
                print("Create MenuItem: " + name)
    print("Finished")

def populate_day_test():
    populate_day('http://web.archive.org/web/20140129140004/http://services.housing.berkeley.edu/FoodPro/dining/static/todaysentrees.asp')