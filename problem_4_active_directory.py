"""
a function that provides an efficient look up of whether the user is in a group.
"""

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
        

###################################
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    
    # check sub-groups
    for g_sub in group.get_groups():
        if is_user_in_group(user, g_sub):
            return True

    return False

###################################
if __name__=="__main__":
    # test set - 1: default
    print('---------- test set - 1: default case')
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")
    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)
    child.add_group(sub_child)
    parent.add_group(child)

    print("Pass" if (is_user_in_group(sub_child_user, parent) == True) else "FAIL")
    print("Pass" if (is_user_in_group(sub_child_user, child) == True) else "FAIL")

    # test set - 2: edge cases
    print('---------- test set - 2: some edge cases')
    print("Pass" if (is_user_in_group('vm', parent) == False) else "FAIL")
    print("Pass" if (is_user_in_group(None, parent) == False) else "FAIL")
    print("Pass" if (is_user_in_group(1, parent) == False) else "FAIL")
    print("Pass" if (is_user_in_group('data', parent) == False) else "FAIL")

    # test set - 3: mode cases
    print('---------- test set - 3: more cases')
    g1 = Group("g1")
    g2 = Group("g2")
    g3 = Group("g3")
    g4 = Group("g4")
    g0 = Group("g0")
    g1.add_group(g2)
    g2.add_group(g3)
    g3.add_group(g4)
    g1.add_group(g0)
    g0.add_user("u0->Tree 1-0")
    g2.add_user("u2->Tree 1-2")
    g4.add_user("u4->Tree 1-2-3-4")

    print("Pass" if (is_user_in_group("u0->Tree 1-0", g0) == True) else "FAIL")
    print("Pass" if (is_user_in_group("u0->Tree 1-0", g1) == True) else "FAIL")
    print("Pass" if (is_user_in_group("u0->Tree 1-0", g2) == False) else "FAIL")
    print("Pass" if (is_user_in_group("u2->Tree 1-2", g0) == False) else "FAIL")
    print("Pass" if (is_user_in_group("u2->Tree 1-2", g1) == True) else "FAIL")
    print("Pass" if (is_user_in_group("u2->Tree 1-2", g2) == True) else "FAIL")
    print("Pass" if (is_user_in_group("u4->Tree 1-2-3-4", g2) == True) else "FAIL")
    print("Pass" if (is_user_in_group("u4->Tree 1-2-3-4", g4) == True) else "FAIL")
    print("Pass" if (is_user_in_group("u4->Tree 1-2-3-4", g0) == False) else "FAIL")
    
    

