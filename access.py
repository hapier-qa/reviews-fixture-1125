def may_read(user_id, owner_id):
    """Only the owner may read a private document."""
    return user_id == owner_id
