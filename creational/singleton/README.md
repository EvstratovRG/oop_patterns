Одиночка — это порождающий паттерн, который гарантирует существование только одного объекта определённого класса, а также позволяет достучаться до этого объекта из любого места программы.

Одиночка имеет такие же преимущества и недостатки, что и глобальные переменные. Его невероятно удобно использовать, но он нарушает модульность вашего кода.

Вы не сможете просто взять и использовать класс, зависящий от одиночки в другой программе. Для этого придётся эмулировать присутствие одиночки и там. Чаще всего эта проблема проявляется при написании юнит-тестов.
Применимость: Многие программисты считают Одиночку антипаттерном, поэтому его всё реже и реже можно встретить в Python-коде.

Признаки применения паттерна: Одиночку можно определить по статическому создающему методу, который возвращает один и тот же объект.

Наивный Одиночка (небезопасный в многопоточной среде)
Топорно реализовать Одиночку очень просто — достаточно скрыть конструктор и предоставить статический создающий метод.

Тот же класс ведёт себя неправильно в многопоточной среде. Несколько потоков могут одновременно вызвать метод получения Одиночки и создать сразу несколько экземпляров объекта.