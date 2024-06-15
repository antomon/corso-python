import marimo

app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    import pandas as pd
    import matplotlib.pyplot as plt

    df_vendite = pd.read_csv('vendite.csv')

    print(df_vendite)

    print(df_vendite.isnull().sum())

    df_vendite_ripulito = df_vendite.dropna()

    print(df_vendite_ripulito)

    vendite_notebook_x200 = df_vendite_ripulito[
        df_vendite_ripulito['prodotto'] == 'Notebook X200']

    print(vendite_notebook_x200)

    vendite_per_venditore = df_vendite_ripulito.groupby('venditore')['quantità'].sum()

    print(vendite_per_venditore)

    pivot_table_data_prodotto = df_vendite_ripulito.pivot_table(
        values='quantità',
        index='data_vendita',
        columns='prodotto',
        aggfunc='sum',
        fill_value=0)

    print(pivot_table_data_prodotto)

    vendite_per_venditore.plot(kind='bar')

    plt.title('Vendite per Venditore')
    plt.xlabel('Venditore')
    plt.ylabel('Quantità Venduta')
    plt.show()

    df_vendite_ripulito['data_vendita'] = pd.to_datetime(df_vendite_ripulito['data_vendita'])

    df_vendite_ripulito.set_index('data_vendita', inplace=True)

    vendite_mensili = df_vendite_ripulito.resample('M')['quantità'].sum()

    vendite_mensili.plot(kind='line')

    plt.title('Vendite Mensili Totali')
    plt.xlabel('Mese')
    plt.ylabel('Quantità Venduta')
    plt.show()

    return





if __name__ == "__main__":
    app.run()