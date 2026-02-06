def convert_to_km(mile: int):
    return mile * 1.609

print(f"{'Miles':^10}{'Kilometers':^12}")
print('---------------------')
for mile in range(1, 11):
    km = convert_to_km(mile) 
    print(f"{mile:^10}{km:^12.3f}")
#    print(f"{mile:3d}{km:12.3}")
