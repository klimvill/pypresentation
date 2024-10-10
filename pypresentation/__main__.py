from rich.table import Table, Column

from pypresentation import Presentation
from pypresentation.slide import TitleSlide


def generate_subtitle() -> Table:
	table = Table(Column(justify="center"), box=None)

	table.add_row("[blue]Привет, новичок! 👋")
	table.add_row("[grey66]https://github.com/klimvill/pypresentation")

	return table


presentation = Presentation()
title_slide = TitleSlide(
	"[red]p[/][blue]y[/][green]p[/][yellow]r[/][orange1]e[/][red]s[/][green]e[/][blue]n[/][yellow]t[/][red]a[/][blue]t[/][green]i[/][yellow]o[/][orange1]n[/] - библиотека для создания презентаций",
	generate_subtitle(),
	border_style="grey37"
)

presentation.add(title_slide)

if __name__ == "__main__":
	presentation.start()
