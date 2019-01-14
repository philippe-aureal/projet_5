class Table:

def __init__(self, fillables):
#

def insert(self):
request = "Insert INTO " + self.table + " ("
for key, val in self.fillables:
request += key + ", "
request += ") "
request += "VALUES ("
for key, val in self.fillables:
request += val + ", "
request += ")"


return db_connect.execute_sql(request)


# Tester toutes les valeurs
def fill(self, fillables):
for key, val in self.fillable:
# Attention, tu DOIS tester toutes tes valeurs !!!
if fillables[key] != None:
self.fillable[key] = fillables[key]


##################################################################################################


class Product(Table):

def __init__(self, fillables=None):
self.table = "product"
self.fillable = {
'name_product': None,
'brand_product': None,
'nutritional_note': None,
'url': None,
'category_id': None
}
self.fill(fillables)



class Category(Table):



if _name_ == "__main__":
print(p.fillables.url)
