import plotly.graph_objects as go
from plotly.offline import plot
import mariadb
import sys
import pandas as pd
import numpy as np
import os
try:
    os.mkdir('report')
except:
    pass

def connection(user: str = "root", password: str = "admin",
               host: str = "localhost", port: int = 3306, **kwargs):
    """ Connection function

    Args:
        user (str): Defaults to 'root'
        password (str): Defaults to 'admin'
        host (str): Defaults to 'localhost'
        port (int): Defaults to 3306
        **kwargs (str): database=, if you want to connect to exact database.

    Returns (mariadb.connect()): current connection
    """
    try:
        conn = mariadb.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            **kwargs
        )
        print(f'connected to @{host} on port {port}')

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn

if __name__ == '__main__':

    conn = connection(password='8nqw$NS54Yh7FgWU', database="vet_clinic")
    cur = conn.cursor()

    # pierwszwe pytanie
    cur.execute('''select date(real_date), count(*) from visits where real_date is not null
group by year(real_date), month(real_date), day(real_date);
''')

    records = cur.fetchall()
    dates = []
    novs = []
    for date, nov in records:
        dates.append(date)
        novs.append(nov)

    data = [go.Scatter(x=dates[:100], y=novs[:100])]
    graph1 = os.path.join('report', 'graph1.html')
    plot(data, auto_open=False, filename=graph1)

    # drugie pytanie
    cur.execute('''with t1 as (
    select concat(year(date),'-', month(date)) as month_, sum(amount) as profits
    from cash_flow where amount >= 0 group by year(date), month(date)),
t2 as (
    select concat(year(date),'-', month(date)) as month_, sum(amount) as loses
    from cash_flow where amount < 0 group by year(date), month(date))
select month_, profits, 'profit' from t1
union all
select month_, loses, 'loses' from t2;''')

    records = cur.fetchall()
    months = []
    amount = []
    p_or_l = []
    for date, am, pl in records:
        months.append(date)
        amount.append(am)
        p_or_l.append(pl)

    df = pd.DataFrame(data={'amount': amount, 'profit_or_lose':p_or_l, 'months':months})
    data = [go.Bar(x=group['months'], y=group['amount'], name=porl) for porl, group in df.groupby('profit_or_lose')]

    cur.execute("""select concat(year(date),'-', month(date)) as month_, sum(amount) from cash_flow
                group by year(date), month(date)""")

    records = cur.fetchall()
    months = []
    diff = []
    for date, d in records:
        months.append(date)
        diff.append(d)

    data.append(go.Scatter(x=months, y=diff, name='profit-lose'))
    graph2 = os.path.join('report', 'graph2.html')
    plot(data, auto_open=False, filename=graph2)

    # trzecie pytanie
    cur.execute("""select petID, max(timestampdiff(hour,registration_date, planned_date)) as `max_wait`
                from visits group by petID order by `max_wait` DESC limit 20;""")

    records = cur.fetchall()
    petid = [record[0] for record in records]
    wait_time = [record[1] for record in records]
    df = pd.DataFrame(data={'petID': petid, 'wait_time (hours)':wait_time})
    first_df_html = df.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped">')

    # pytanie czwarte
    cur.execute('''select weight from pets;
''')

    records = cur.fetchall()
    data = [float(record[0]) for record in records]
    n = len(data)
    Cumsum = np.cumsum(np.ones((1,n))/n)
    data=[go.Scatter(x=sorted(data), y=Cumsum)]
    graph3 = os.path.join('report', 'graph3.html')
    plot(data, auto_open=False, filename=graph3)

    html_string = """
    <html>
    <head>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
            <style>body{ margin:0 100; background:whitesmoke; }</style>
        </head>
        <body>
            <h1>Analiza kliniki weterynaryjnej</h1>

            <!-- *** Section 1 *** --->
            <h2>Liczba wizyt w poszczególnych miesiącach</h2>
            <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
    src="""+graph1+"""></iframe>

        <h2>Bilans zysków i strat</h2>
            <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
    src="""+graph2+"""></iframe>
    <h2>Najdłużej czeka </h2>"""+first_df_html+"""
    <h2>Rozkład masy zwierzaków </h2>
    <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
    src="""+graph3+"""></iframe>
        </body>
    </html>"""

    with open('analiza.html', 'w') as f:
        f.write(html_string)