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

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Recursively searches through the given group and all its subgroups. 
    If the user is found in any of these groups, returns True. 
    If the user is not found after all groups are checked, returns False.

    Args:
      user(str): user name/id to be searched for in the group.
      group(class:Group): the group (and its subgroups) to check for the user's membership.

    Returns:
      bool: True if the user is found in the group or its subgroups, False otherwise.
    """
    # Check if the user is in the current group's users list
    if user in group.get_users():
        return True

    # Recursively check each subgroup
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True

    # If the user is not found in the current group or any of its subgroups, return False
    return False


# Group structure setup
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

# Adding a user to sub_child
sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

# Constructing the hierarchy
child.add_group(sub_child)
parent.add_group(child)

# Test Case 1: User in Nested Subgroup
print("Test Case 1: User in Nested Subgroup")
result = is_user_in_group("sub_child_user", parent)
print("Expected: True, Got:", result)
print("\n")

# Test Case 2: Null User
print("Test Case 2: Null User")
result = is_user_in_group(None, parent)
print("Expected: False, Got:", result)
print("\n")

# Test Case 3: Empty Subgroup
# Adding an empty subgroup to parent
empty_group = Group("empty")
parent.add_group(empty_group)

print("Test Case 3: Empty Subgroup")
# Testing with a user that exists in a different subgroup
result = is_user_in_group("sub_child_user", empty_group)
# The expected result is False since "sub_child_user" is not in "empty_group"
print("Expected: False, Got:", result)

