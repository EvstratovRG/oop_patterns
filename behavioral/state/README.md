Состояние — это поведенческий паттерн, позволяющий динамически изменять поведение объекта при смене его состояния.

Поведения, зависящие от состояния, переезжают в отдельные классы. Первоначальный класс хранит ссылку на один из таких объектов-состояний и делегирует ему работу.
Применимость: Паттерн Состояние часто используют в Python для превращения в объекты громоздких стейт-машин, построенных на операторах switch.

Признаки применения паттерна: Методы класса делегируют работу одному вложенному объекту.

Концептуальный пример
Этот пример показывает структуру паттерна Состояние, а именно — из каких классов он состоит, какие роли эти классы выполняют и как они взаимодействуют друг с другом.