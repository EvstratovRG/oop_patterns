Снимок — это поведенческий паттерн, позволяющий делать снимки внутреннего состояния объектов, а затем восстанавливать их.

При этом Снимок не раскрывает подробностей реализации объектов, и клиент не имеет доступа к защищённой информации объекта.
Применимость: Снимок на Python чаще всего реализуют с помощью сериализации. Но это не единственный, да и не самый эффективный метод сохранения состояния объектов во время выполнения программы.

Концептуальный пример
Этот пример показывает структуру паттерна Снимок, а именно — из каких классов он состоит, какие роли эти классы выполняют и как они взаимодействуют друг с другом.