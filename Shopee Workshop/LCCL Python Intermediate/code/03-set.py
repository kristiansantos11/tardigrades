# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# SET
# ======================

# Creating a set
fruits = set()
my_fav_food = {'nasi lemak', 'laksa', 'hokkien mee', 'chicken rice'}
your_fav_food = {'chicken rice', 'pan mee', 'nasi lemak'}

# Adding item
fruits.add('durian')   # no duplicates

# Deleting a set item
fruits.discard('durian')

# Membership
'chicken rice' in your_fav_food  # True

# Iterating through a set
for food in my_fav_food:
    print(food)

# Set intersection
my_fav_food & your_fav_food     # {'nasi lemak', 'chicken rice'}

# Set union
my_fav_food | your_fav_food     # {'chicken rice', 'hokkien mee', 'laksa', 'nasi lemak', 'pan mee'}

# Set difference
my_fav_food - your_fav_food     # {'laksa', 'hokkien mee'}

# Length
len(my_fav_food)