from typing import Dict
import abc

class GenAIParent(abc.ABC):
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        
        if not hasattr(cls, 'service_name'):
            raise ValueError(f"Subclasses of {cls.__name__} must define a 'service_name' attribute.")
        
        if cls.service_name in cls._registry:
            raise ValueError(f"Service name {cls.service_name} is already registered.")
        
        cls._registry[cls.service_name] = cls
        print(f"Registered service: {cls.service_name}") 

    @property
    def service_name(self): 
        return self.__class__.service_name

    @classmethod
    def get_service_class(cls, service_name: str):
        if service_name not in cls._registry:
            raise ValueError(f"Service {service_name} not found in registry.")
        return cls._registry[service_name]

    @abc.abstractmethod
    async def getAnalytics(self, transcript: str, prompt: str) -> Dict:
        pass