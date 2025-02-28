# pypresentation
Библиотека для создания красивых презентаций.

Поддерживает изображения, автоматическую перемотку, создание своих шаблонов, поэтапное отображение слайдов и многое другое. 
`pypresentation` построена на основе rich и работает с `python>=3.12`.
Примеры готовых презентаций вы сможете найти ниже, код для них находится в папке `examples`.

## Установка

Чтобы установить библиотеку, введите команду:

```sh
pip install pypresentation
```

Чтобы проверить библиотеку, выполните следующую команду:

```sh
python -m pypresentation
```

## Простой пример

![example.png](docs/images/simple_example.png)

```python
from pypresentation import Presentation
from pypresentation.slide import TitleSlide
from rich.table import Table, Column


def generate_subtitle() -> Table:
	table = Table(Column(justify="center"), box=None)

	table.add_row("[#aac7ff]Привет, новичок! 👋")
	table.add_row("[grey66]https://github.com/klimvill/pypresentation")

	return table


presentation = Presentation()
title_slide = TitleSlide(
	"[#aac7ff]pypresentation[/] - библиотека для создания презентаций",
	generate_subtitle(),
	border_style="#74777f"
)

presentation.add(title_slide)
presentation.start()
```

## Документация

Пользовательскую документацию можно получить по [этой ссылке](./docs/index.md).
