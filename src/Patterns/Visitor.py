from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def accept(self, current_visiting):
        pass

class Visitable:
    def visit(self, visitor: Visitor):
        visitor.accept(self)
