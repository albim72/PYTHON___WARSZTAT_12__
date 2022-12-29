from abc import ABCMeta, abstractmethod

class IPojazd(metaclass=ABCMeta):
    
    @abstractmethod
    def spalanie100(self,odl,litry):raise NotImplementedError
    
    @abstractmethod
    def kosztprzejzadu(self,odl,litry,cena_l):raise NotImplementedError
