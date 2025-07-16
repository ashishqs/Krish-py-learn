def get_price(base_price, tax_percent):    
    return base_price * (1 + tax_percent / 100)
    



prices = [100, 7968786886878686868686857685878678767677868678676768767675757685688]
for x in prices:
    formatted_price = f"${get_price(x, 7):,.2f}"
    print(f"{x}\t\t{formatted_price}")