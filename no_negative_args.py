def main():
    item_price = -2.99
    quantity = -3
    #quantity error only because quanity is caught before price is caught
    print(f"{quantity} items at ${item_price} each is:")
    print(f"${calc_subtotal(item_price, quantity)}")


def calc_subtotal(price: float, quantity: int) -> float:
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    """Calculate the subtotal for a single item in a cart.
    
    Args:
        price: The price of a single item.
        quantity: Number of a particular item in the cart.

    Returns:
        The subtotal
    """
    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price * quantity


if __name__ == "__main__":
    main()
#value error price cant be negative line 19 having a negative number caused the error