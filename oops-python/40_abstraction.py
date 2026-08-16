# ============================================================
# ABSTRACTION AND INTERFACES
# ============================================================
# Abstraction means exposing only the essential behavior while
# hiding implementation details.
#
# Example:
#     ATM -> withdraw()
#
# The user knows WHAT operation is available, but does not need
# to know HOW the operation is internally implemented.
#
# In Python, abstraction is commonly implemented using the abc
# module and Abstract Base Classes (ABCs).
# ============================================================


# ============================================================
# 1. ABSTRACT BASE CLASS
# ============================================================
# ABC is the base class used for creating abstract classes.
#
# @abstractmethod declares a method that subclasses are required
# to implement.
#
# An abstract class cannot be instantiated while it contains
# unimplemented abstract methods.

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


# car = Car()  # TypeError


# ============================================================
# 2. CONCRETE CHILD CLASSES
# ============================================================
# A concrete class implements all abstract methods inherited
# from the abstract base class.

class MarutiSuzuki(Car):
    def mileage(self):
        print("Mileage is 30 km/l")


class Tata(Car):
    def mileage(self):
        print("Mileage is 40 km/l")


maruti = MarutiSuzuki()
tata = Tata()

maruti.mileage()
tata.mileage()


# ============================================================
# 3. ABSTRACTION AS A CONTRACT
# ============================================================
# The parent defines WHAT every Car must provide.
#
# Each child decides HOW that behavior is implemented.
#
# Car:
#     mileage() -> required behavior
#
# MarutiSuzuki:
#     mileage() -> its implementation
#
# Tata:
#     mileage() -> its implementation


# ============================================================
# 4. ABSTRACT CLASS WITH MULTIPLE ABSTRACT METHODS
# ============================================================
# A class can contain multiple abstract methods.
#
# A concrete subclass must implement ALL of them before it can
# be instantiated.

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using credit card")

    def refund(self, amount):
        print(f"Refunded ₹{amount} to credit card")


payment = CreditCardPayment()

payment.pay(1000)
payment.refund(500)


# ============================================================
# 5. INCOMPLETE SUBCLASS
# ============================================================
# If a subclass does not implement every abstract method, it
# remains abstract and cannot be instantiated.

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# upi = UPI()
# TypeError: Can't instantiate abstract class UPI


# ============================================================
# 6. ABSTRACT CLASS CAN ALSO CONTAIN CONCRETE METHODS
# ============================================================
# An abstract class does NOT have to contain only abstract
# methods.
#
# It can provide common implementation that subclasses inherit.

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Vehicle stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")


bike = Bike()

bike.start()
bike.stop()


# ============================================================
# 7. ABSTRACT METHOD WITH COMMON IMPLEMENTATION
# ============================================================
# An abstract method can technically contain implementation.
#
# A subclass still has to override it to become concrete.
#
# super() can be used when the subclass wants to reuse the common
# implementation.

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        print(f"LOG: {message}")


class FileLogger(Logger):
    def log(self, message):
        super().log(message)
        print(f"Writing '{message}' to file")


logger = FileLogger()

logger.log("Application started")


# ============================================================
# 8. INTERFACE-STYLE DESIGN
# ============================================================
# Python does not have a separate interface keyword like Java.
#
# An interface-like design can be created using an ABC containing
# only abstract methods.
#
# The interface specifies WHAT operations must exist.
# Implementing classes decide HOW they work.

class CommandInterface(ABC):
    @abstractmethod
    def execute(self):
        pass


class SaveCommand(CommandInterface):
    def execute(self):
        print("Saving data")


class DeleteCommand(CommandInterface):
    def execute(self):
        print("Deleting data")


SaveCommand().execute()
DeleteCommand().execute()


# ============================================================
# 9. POLYMORPHISM + ABSTRACTION
# ============================================================
# A major benefit of abstraction is that code can depend on the
# abstract interface instead of specific implementations.
#
# Any object implementing the required interface can be passed
# to the function.

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class Card(PaymentMethod):
    def pay(self, amount):
        print(f"Card payment: ₹{amount}")


class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"UPI payment: ₹{amount}")


def checkout(payment_method, amount):
    payment_method.pay(amount)


checkout(Card(), 1000)
checkout(UPI(), 2000)


# ============================================================
# 10. ADVANCED: DEPENDENCY INVERSION WITH ABSTRACTION
# ============================================================
# Instead of making a service depend directly on a concrete
# implementation, make it depend on an abstraction.
#
# This makes the system easier to extend and test.

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(NotificationService):
    def send(self, message):
        print(f"Email: {message}")


class SMSNotification(NotificationService):
    def send(self, message):
        print(f"SMS: {message}")


class AlertManager:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def alert(self, message):
        self.notification_service.send(message)


email_alert = AlertManager(EmailNotification())
sms_alert = AlertManager(SMSNotification())

email_alert.alert("Server is down")
sms_alert.alert("OTP sent")


# ============================================================
# 11. ABSTRACT CLASS + CLASSMETHOD
# ============================================================
# Abstract methods can also be combined with classmethod when
# subclasses must provide class-level behavior.

class Serializer(ABC):
    @classmethod
    @abstractmethod
    def format_name(cls):
        pass


class JSONSerializer(Serializer):
    @classmethod
    def format_name(cls):
        return "JSON"


class XMLSerializer(Serializer):
    @classmethod
    def format_name(cls):
        return "XML"


print(JSONSerializer.format_name())
print(XMLSerializer.format_name())


# ============================================================
# 12. ABSTRACT CLASS + STATICMETHOD
# ============================================================
# Abstract static methods can define required utility behavior
# that does not depend on self or cls.

class Validator(ABC):
    @staticmethod
    @abstractmethod
    def validate(value):
        pass


class AgeValidator(Validator):
    @staticmethod
    def validate(value):
        return isinstance(value, int) and value >= 18


print(AgeValidator.validate(20))
print(AgeValidator.validate(15))


# ============================================================
# 13. CHECKING ABSTRACT STATUS
# ============================================================
# Python internally tracks abstract methods using
# __abstractmethods__.

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass


print(Database.__abstractmethods__)


class MySQL(Database):
    def connect(self):
        print("Connected")

    def close(self):
        print("Closed")


print(MySQL.__abstractmethods__)


# ============================================================
# 14. ABSTRACT PROPERTY
# ============================================================
# Properties can also be abstract.
#
# This is useful when every subclass must expose a particular
# attribute-like interface.

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass


class Developer(Employee):
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary


developer = Developer(80000)

print(developer.salary)


# ============================================================
# 15. ABSTRACT FACTORY-STYLE EXAMPLE
# ============================================================
# Abstraction becomes especially useful in larger systems where
# the calling code should not care about the concrete object.

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def fetch(self):
        pass


class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB")

    def fetch(self):
        return ["User1", "User2"]


class PostgreSQL(Database):
    def connect(self):
        print("Connected to PostgreSQL")

    def fetch(self):
        return ["User3", "User4"]


def load_users(database: Database):
    database.connect()
    return database.fetch()


print(load_users(MongoDB()))
print(load_users(PostgreSQL()))


# ============================================================
# ABSTRACT CLASS vs INTERFACE-STYLE ABC
# ============================================================
# ABSTRACT CLASS:
#     Can contain:
#         - abstract methods
#         - concrete methods
#         - attributes
#         - properties
#         - constructors
#
# INTERFACE-STYLE ABC:
#     Usually contains only abstract methods/properties.
#     Its purpose is to define a contract.
#
# Python does not enforce a separate "interface" language
# construct like Java.
# ============================================================


# ============================================================
# ABSTRACTION vs ENCAPSULATION
# ============================================================
# ABSTRACTION:
#     Focuses on WHAT an object exposes.
#     Hides unnecessary implementation complexity.
#
# ENCAPSULATION:
#     Focuses on bundling and controlling access to internal state.
#
# Example:
#
#     BankAccount.withdraw()
#
# Abstraction:
#     User only needs to know that withdraw() exists.
#
# Encapsulation:
#     Balance is controlled internally and cannot be modified
#     arbitrarily.
# ============================================================


# ============================================================
# KEY IDEA
# ============================================================
# Abstraction:
#     Hide implementation details.
#
# ABC:
#     from abc import ABC, abstractmethod
#
# Abstract method:
#     Defines required behavior.
#
# Concrete class:
#     Implements all required abstract methods.
#
# Interface-style ABC:
#     Defines a strict contract with abstract methods.
#
# Polymorphism:
#     Different implementations can be used through the same
#     abstract interface.
#
# Most important idea:
#
#     Abstract class -> WHAT must be done
#     Concrete class -> HOW it is done
#
# This makes large systems easier to extend, maintain, test,
# and replace without changing the code that depends on them.
# ============================================================