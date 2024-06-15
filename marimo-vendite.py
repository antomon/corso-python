import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    vendite = mo.ui.text(placeholder="Inserisci dati in CSV", label="Dati di vendita")
    return vendite,


@app.cell
def __(vendite):
    import pandas as pd
    from io import StringIO

    vendite_ = StringIO(vendite.text)

    df_vendite = pd.read_csv(vendite_)

    print(df_vendite)
    return StringIO, df_vendite, pd, vendite_


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
