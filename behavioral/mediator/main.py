from __future__ import annotations

from abc import ABC


class Mediator(ABC):
    """
    Интерфейс Посредника предоставляет метод, используемый компонентами для
    уведомления посредника о различных событиях. Посредник может реагировать на
    эти события и передавать исполнение другим компонентам.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component1, component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()
