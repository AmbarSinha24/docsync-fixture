def generate_invoice(order_id, amount, tax=0.0):
    return {"order_id": order_id, "amount": amount, "tax": tax}
