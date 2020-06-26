# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

# TUPLE
# ======================

# Creating a tuple
scores = tuple()
scores = ()
scores = (1,2,3,1,1) 

# Accessing a value
scores[2]    # 3

# Adding item
scores += (0,0,2,3,3)   # scores = scores + (0,0,2,3,3) 
scores += (1,)

# Membership
10 in scores    # False

# Iterating through a tuple
for s in scores:
    print(s)

# Length
len(scores)