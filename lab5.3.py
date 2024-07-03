def quantity():
    q = int(input("Goods Quantity: "))
    psum = 0.0
    for i in range(q):
        p = float(input(f"Goods {i + 1} Price: "))
        psum += p
    return psum

psum = quantity()

print("\nPrice: %.2f" % psum)
print("Vat7: %.2f" % (psum * (7/100)))
print("PriceIncludeVat: %.2f" % (psum * 1.07))