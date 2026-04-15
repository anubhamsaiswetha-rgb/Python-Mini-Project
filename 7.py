from abc import ABC, abstractmethod
class order(ABC):
    @abstractmethod
    def  choose(self):
        pass
class AmazonOrder(order):
    def choose(self):
        print("order through amazon")
class FlipkartOrder(order):
    def choose(self):
        print("order by flipkart")
a=AmazonOrder()
f=FlipkartOrder()
a.choose()
f.choose()