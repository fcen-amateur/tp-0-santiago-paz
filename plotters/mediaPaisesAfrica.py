import seaborn.objects as so
from gapminder import gapminder

esperanza_vida = gapminder.groupby([ 'year','continent'])['lifeExp'].mean().unstack()

def plot():
    figura = (
        so.Plot(
            esperanza_vida,
            "year",
            esperanza_vida["Africa"],
        )
        .add(so.Dot())
        .add(so.Line(), so.PolyFit())
        .label(
            title="Expectativa de vida en África",
            x="Año",
            y="Expectativa de vida",
        )
    )
    return dict(
        descripcion="Media de vida en países de África a lo largo del tiempo",
        autor="Santiago Paz",
        figura=figura,
    )
