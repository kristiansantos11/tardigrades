# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# DICTIONARY
# ======================

# Creating a dictionary
phonebook = dict()

d = {}

capitals = {
    'Singaore': 'Singapore', 
    'Malaysia': 'Kuala Lumpur', 
    'Philippines': 'Manila',
    'Thailand': 'Bangkok',
    'Indonesia': 'Jakarta',
    'Taiwan': 'Taipei',
}

d = {'a': 31, 24:'x', 1.23: [4,5,6]}

# Accessing a value
capitals['Malaysia']    # Kuala Lumpur
d['a']                  # 31
d[24]                   # x

# Adding/Updating key-value pair
capitals['Vietnam'] = 'Hanoi'

# Deleting a dictionary item
d.pop(1.23)

# Membership
'Thailand' in capitals  # True

# Iterating through a dictionary
for k, v in capitals.items():
    print(f'{v} is the capital of {k}.')

# Length
len(capitals)