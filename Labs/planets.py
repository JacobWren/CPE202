def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    print("\n" + "On Mars you would weigh {0} pounds.".format(weight * .38) +
          "\n" + "On Jupiter you would weigh {0} pounds.".format(weight * 2.34))
if __name__ == '__main__':
    weight_on_planets()