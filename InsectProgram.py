import InsectClass as i

housefly = i.Insect(2,4)
mosquito = i.Insect(4,8)
#This creates 2 separate instances; in this case the housefly and mosquito isntances

housefly.calc_flight()
mosquito.calc_flight()

print("The housefly can fly up to", housefly.get_flight())
print("The mosquito can fly up to", mosquito.get_flight())