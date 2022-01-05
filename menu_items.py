items = [('Veg Biryani', 'Biryani'), ('Chicken Biryani', 'Biryani'), ('Egg Roll', 'Rolls'), ('Paneer wrap', 'Rolls'), ('Chicken Manchow Soup', 'Soup'), ('Egg Biryani', 'Biryani')]

new_items = { }

for x in items:
    if new_items.get(x[1],'No')=='No':
        new_items[x[1]] = x[0]
    else:
        new_items[x[1]] = list(new_items.get(x[1])) + list((x[0]))
print(new_items)

for k, v in new_items.items():
    if len(v) == 1:
        new_items[k] = list(v)
print(new_items)

