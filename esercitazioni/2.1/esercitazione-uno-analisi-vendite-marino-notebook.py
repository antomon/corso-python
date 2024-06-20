import marimo

__generated_with = "0.6.19"
app = marimo.App(width="medium", app_title="Esercitazione 1 - Analisi vendite")


@app.cell
def __():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def __(mo):
    files = mo.ui.file_browser(
        multiple=False, 
        label="Seleziona un file csv di vendite"
    )

    mo.vstack([files])
    return files,


@app.cell
def __(files, mo, pd):
    df_vendite = pd.read_csv(files.path(0))

    tabella_vendite = mo.ui.table(
        data=df_vendite,
        pagination=True,
        label="Vendite",
    )
    return df_vendite, tabella_vendite


@app.cell
def __(mo, tabella_vendite):
    mo.vstack([tabella_vendite, tabella_vendite.value])
    return


@app.cell
def __(df_vendite, mo):
    mo.vstack(["Numero valori nulli per colonna:", df_vendite.isnull().sum()])
    return


@app.cell
def __(df_vendite, mo):
    df_vendite_ripulito = df_vendite.dropna()

    tabella_vendite_ripulito = mo.ui.table(
        data=df_vendite_ripulito,
        pagination=True,
        label="Vendite",
    )
    return df_vendite_ripulito, tabella_vendite_ripulito


@app.cell
def __(mo, tabella_vendite_ripulito):
    mo.vstack([tabella_vendite_ripulito, tabella_vendite_ripulito.value])
    return


@app.cell
def __(df_vendite_ripulito, mo):
    mo.ui.data_explorer(df_vendite_ripulito)
    return


@app.cell
def __(df_vendite_ripulito, mo):
    mo.ui.dataframe(df_vendite_ripulito)
    return


@app.cell
def __(df_vendite_ripulito, mo):
    vendite_per_venditore = df_vendite_ripulito.groupby('venditore')['prezzo'].sum()

    vendite_per_venditore.plot(kind='bar')

    import matplotlib.pyplot as plt

    plt.title('Vendite per Venditore')
    plt.xlabel('Venditore')
    plt.ylabel('Quantità Venduta')

    mo.mpl.interactive(plt.gcf())
    return plt, vendite_per_venditore


@app.cell
def __(df_vendite_ripulito, mo, pd, plt):
    df_vendite_ripulito['data_vendita'] = pd.to_datetime(df_vendite_ripulito['data_vendita'])

    df_vendite_ripulito.set_index('data_vendita', inplace=True)

    vendite_mensili = df_vendite_ripulito.resample('ME')['quantità'].sum()

    vendite_mensili.plot(kind='line')

    plt.title('Vendite Mensili Totali')
    plt.xlabel('Mese')
    plt.ylabel('Quantità Venduta')

    mo.mpl.interactive(plt.gcf())
    return vendite_mensili,


if __name__ == "__main__":
    app.run()
