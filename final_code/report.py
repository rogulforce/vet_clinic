import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
import numpy as np
import os
from schema_creation import connection


def make_report():

    try:
        os.mkdir('report')
    except OSError:
        print('report already exists')

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

    df = pd.DataFrame(data={'amount': amount, 'profit_or_lose': p_or_l, 'months': months})
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
    df = pd.DataFrame(data={'petID': petid, 'wait_time (hours)': wait_time})
    first_df_html = df.to_html().replace('<table border="1" class="dataframe">', '<table class="table table-striped">')

    # pytanie czwarte
    cur.execute('''select weight from pets;
''')

    records = cur.fetchall()
    data = [float(record[0]) for record in records]
    n = len(data)
    Cumsum = np.cumsum(np.ones((1, n)) / n)
    data = [go.Scatter(x=sorted(data), y=Cumsum)]
    graph3 = os.path.join('report', 'graph3.html')
    plot(data, auto_open=False, filename=graph3)

    # pytanie piąte
    cur.execute('''select salary, employeeID from employees where position = 'Weterynarz';
    ''')

    records1 = cur.fetchall()

    cur.execute('''select employeeID, sum(cost) from visits where real_date is not null
    group by employeeID, year(real_date), month(real_date) ;
    ''')
    records2 = cur.fetchall()
    records2 = [(item[0], int(item[1])) for item in records2]
    df = pd.DataFrame(data={'vet': [item[0] for item in records2], 'sum': [item[1] for item in records2]})
    df = df.groupby('vet').agg(np.mean).reset_index()
    df['sum'] = df['sum'] / [int(it[0]) for it in records1]
    data = [go.Bar(x=df['vet'], y=df['sum'])]
    graph4 = os.path.join('report', 'graph4.html')
    plot(data, auto_open=False, filename=graph4)

    # pytanie 6
    cur.execute('''select drugID, sum(amount), name from meds_prescribed left join meds using (drugID)
    group by drugID order by sum(amount) desc limit 20 ;
    ''')
    records = cur.fetchall()

    df = pd.DataFrame(data={'id': [it[0] for it in records], 'name': [it[2] for it in records],
                            'total quantity': [it[1] for it in records]})

    second_df_html = df.to_html().replace('<table border="1" class="dataframe">', '<table class="table table-striped">')

    # pytanie 7
    cur.execute('''select avg(x), type from (select sum(amount) as 'x', type from cash_flow where amount < 0 group by type, year(date), month(date)) as zzz group by type;
    ''')

    records = cur.fetchall()
    labels = [it[1] for it in records]
    values = [round(int(-1 * it[0]), 2) for it in records]
    data = [go.Pie(labels=labels, values=values)]
    graph5 = os.path.join('report', 'graph5.html')
    plot(data, auto_open=False, filename=graph5)
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
    src=""" + graph1 + """></iframe>

        <h2>Bilans zysków i strat</h2>
            <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
    src=""" + graph2 + """></iframe>
    <h2>Najdłużej czeka </h2>""" + first_df_html + """
    <h2>Rozkład masy zwierzaków </h2>
    <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
    src=""" + graph3 + """></iframe>
    <h2>zarobki lekarzy w stosunku do przychodów z wizyt </h2>
    <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
    src=""" + graph4 + """></iframe>
    <h2>Najdłużej czeka </h2>""" + second_df_html + """
    <h2>Procentowy podział strat </h2>
    <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
    src=""" + graph5 + """></iframe>
        </body>
    </html>"""

    with open('analiza.html', 'w') as f:
        f.write(html_string)
