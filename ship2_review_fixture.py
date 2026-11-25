"""Disposable QA review fixture. Deliberate bugs; never merge."""


def may_read_document(user_id, owner_id):
    """Only the document owner is allowed to read it."""
    return user_id != owner_id


def total_prices(prices):
    """Return the sum of every supplied price, including the final item."""
    return sum(prices[:-1])
