# Документация pypresentation

## Введение
Прежде чем приступить к изучению этой библиотеки, ознакомьтесь с `rich`. 
Особенное внимание рекомендую уделить: [Panels](https://rich.readthedocs.io/en/stable/panel.html), 
[Tables](https://rich.readthedocs.io/en/stable/tables.html), [Tree](https://rich.readthedocs.io/en/stable/tree.html), 
[Layout](https://rich.readthedocs.io/en/stable/layout.html), [Group](https://rich.readthedocs.io/en/stable/group.html), 
[Box](https://rich.readthedocs.io/en/stable/appendix/box.html), [Standard Colors](https://rich.readthedocs.io/en/stable/appendix/colors.html).

## Основы

Первом делом в создании презентации является импорт класса `Presentation` и создание экземпляра. Вот пример кода:

```python
from pypresentation import Presentation

presentation = Presentation()
```

Для того чтобы запустить презентацию, необходимо вызвать метод `start`.

```python
from pypresentation import Presentation

presentation = Presentation()

if __name__ == "__main__":
	presentation.start()
```

Данный код выдаст ошибку, поскольку мы пытаемся запустить презентацию, в которой нет слайдов. Давайте это исправим!

## Слайды
