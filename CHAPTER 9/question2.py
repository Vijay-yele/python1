#  Create a class laptop with attributes : Brand , RAM , price, color.
# create two objects with different values.

class Laptop:
    Brand = "default"
    RAM = "default"
    Price= 450000
    
laptop1 = Laptop()
laptop1.Brand = "Dell"
laptop1.RAM = "16GB"
laptop1.Price = 80000

laptop2 = Laptop()
laptop2.Brand = "Asus"
laptop2.RAM = "8GB"
laptop2.Price = 120000

print("Laptop 1 details:")
print("Brand:", laptop1.Brand)
print("RAM:", laptop1.RAM)
print("Price:", laptop1.Price)


print("\nLaptop 2 details:")
print("Brand:", laptop2.Brand)
print("RAM:", laptop2.RAM)
print("Price:", laptop2.Price)