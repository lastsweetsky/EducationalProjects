from dec import catchErrorInFunction


@catchErrorInFunction
def catchErrorEx_one(numA:float,numB:float):
  return numA / numB

catchErrorEx_one(9,0)


@catchErrorInFunction
def greet(name):
  print("Hello, " + name + ". Good morning!")

greet(032e4)



@catchErrorInFunction
def absolute_value(num):
  if num >= 0:
    return num
  else:
    return -num

absolute_value()


@catchErrorInFunction
def calculate_route_service_fees(
        service_charge_on_root_for_100_km: float,
        l_i: float,
        max_take_off_weight: float
):
  return service_charge_on_root_for_100_km * l_i * (max_take_off_weight / 5) ** (1 / 2)

calculate_route_service_fees(0,39)