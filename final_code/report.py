import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
import numpy as np
import os
from final_code.schema_creation import connection


def make_report(cur):

    try:
        os.mkdir('report')
    except OSError:
        print('direction report already exists')

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
    layout = go.Layout(xaxis=dict(title='Data'), yaxis=dict(title='Liczba wizyt'))
    graph1 = os.path.join('report', 'graph1.html')
    fig = go.Figure(data, layout)
    plot(fig, auto_open=False, filename=graph1)

    # drugie pytanie
    cur.execute('''with t1 as (
    select concat(year(date),'-', month(date)) as month_, sum(amount) as profits
    from cash_flow where amount >= 0 group by year(date), month(date)),
t2 as (
    select concat(year(date),'-', month(date)) as month_, sum(amount) as loses
    from cash_flow where amount < 0 group by year(date), month(date))
select month_, profits, 'zysk' from t1
union all
select month_, loses, 'strata' from t2;''')

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

    data.append(go.Scatter(x=months, y=diff, name='zysk-strata'))
    graph2 = os.path.join('report', 'graph2.html')
    layout = go.Layout(xaxis=dict(title='Data'), yaxis=dict(title='Zysk/Strata'))
    fig = go.Figure(data, layout)
    plot(fig, auto_open=False, filename=graph2)

    # trzecie pytanie
    cur.execute("""select petID, max(timestampdiff(hour,registration_date, planned_date)) as `max_wait`
                from visits group by petID order by `max_wait` DESC limit 10;""")

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
    layout = go.Layout(xaxis=dict(title='Waga'), yaxis=dict(title='Dystrybuanta'))
    fig = go.Figure(data, layout)
    plot(fig, auto_open=False, filename=graph3)

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
    layout = go.Layout(xaxis=dict(title='ID pracownika'),
                       yaxis=dict(title='zarobki lekarzy w stosunku\n do przychodów z wizyt'))
    fig = go.Figure(data, layout)
    fig.update_xaxes(tickvals=[5, 6, 7])
    plot(fig, auto_open=False, filename=graph4)

    # pytanie 6
    cur.execute('''select drugID, sum(amount), name from meds_prescribed left join meds using (drugID)
    group by drugID order by sum(amount) desc limit 10 ;
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
    html_string = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Raport kliniki weterynatyjnej</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
    <style>
    body{
        margin:0;
        background:whitesmoke;
    }
    iframe{
      border: hidden;
    }
    .content{
        background-color: white;
        margin: auto;
        margin-top: 20px;
        margin-bottom: 20px;
        padding: 10px;
        width: 1020px;
    }</style>
</head>
<body>
    <div class="content">
        <h1>Analiza kliniki weterynaryjnej</h1>
        
        <!-- *** Section 1 *** --->
        <h2>Liczba wizyt w poszczególnych miesiącach</h2>
        <iframe width="1000" height="550" seamless="seamless" scrolling="no" src=""" + graph1 + """></iframe>
        
        <!-- *** Section 2 *** --->
        <h2>Bilans zysków i strat</h2>
        <iframe width="1000" height="550" seamless="seamless" scrolling="no" src=""" + graph2 + """></iframe>
        
        <!-- *** Section 3 *** --->
        <h2>Najdłużej czekający pacięci</h2>""" + first_df_html + """
        
        <!-- *** Section 3 *** --->
        <h2>Rozkład masy zwierzaków </h2>
        <iframe width="1000" height="550" seamless="seamless" scrolling="no" src=""" + graph3 + """></iframe>
        
        <!-- *** Section 4 *** --->
        <h2>zarobki lekarzy w stosunku do przychodów z wizyt </h2>
        <iframe width="1000" height="550" seamless="seamless" scrolling="no" src=""" + graph4 + """></iframe>
        
        <!-- *** Section 5 *** --->
        <h2>Najczęściej przepisywane leki </h2>""" + second_df_html + """
        
        <!-- *** Section 6 *** --->
        <h2>Procentowy podział kosztów</h2>
        <iframe width="1000" height="550" seamless="seamless" scrolling="no" src=""" + graph5 + """></iframe>
    </div>
</body>
</html>"""

    with open('analiza.html', 'w', encoding="utf-8") as f:
        f.write(html_string)
