
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "is now sitting")

    def roll_over(self):
        print(self.name.title() + "rolled over!")


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on  it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Your can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        pass


class Battery:

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + '-KWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This cat can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     print("this car has a " + str(self.battery_size) + "-KWh battery")

    def fill_gas_tank(self):
        print("This car doesn't needs a gas tank!")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")

# my_dog.sit()
# my_dog.roll_over()


# print("\nYour dog's name is " + your_dog.name.title() + ".")
# print("Your dog is " + str(your_dog.age) + " years old.")
# your_dog.sit()

my_new_car = Car('audi', '4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# 直接修改属性的值
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# 通过方法修改属性的值
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# 通过方法对属性的值进行递增
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_new_car.fill_gas_tank()
# my_tesla.fill_gas_tank()

# 将实例用做属性
my_tesla.battery.describe_battery()

my_tesla.battery.get_range()