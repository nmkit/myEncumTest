import dash
from dash import dcc, html
from dash.dependencies import Output, Input, State
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime

eng_incum_list=['AGREEMENT FOR SALE AND PURCHASE',
 'AGREEMENT FOR SALE AND PURCHASE WITH PLAN',
 'AGREEMENT FOR SUBSALE AND PURCHASE',
 'AGREEMENT FOR SUBSALE AND SUBPURCHASE',
 'APPROVAL LETTER',
 'ASSENT',
 'ASSIGNMENT',
 'ASSIGNMENT OF RENTAL',
 'ASSIGNMENT WITH PLAN',
 'CANCELLATION AGREEMENT',
 'CARBON COPY OF PRELIMINARY SALE AND PURCHASE AGREEMENT',
 'CARBON COPY OF PROVISIONAL AGREEMENT FOR SALE AND PURCHASE',
 'CERTIFICATE OF COMPLIANCE',
 'CERTIFICATE OF EXEMPTION FROM ESTATE DUTY',
 'CERTIFICATE OF REGISTRATION OF DEATH',
 'CERTIFICATE UNDER S.33(1) OF THE BUILDINGS ORDINANCE',
 'CERTIFIED COPY OF AN ENTRY IN A REGISTER OF DEATH',
 'CERTIFIED COPY OF CERTIFICATE OF DEATH',
 'CERTIFIED COPY OF DEATH CERTIFICATE',
 'CERTIFIED COPY OF LETTER OF DETERMINATION',
 'CERTIFIED TRUE COPY OF DEATH CERTIFICATE',
 'CHINESE PROVISIONAL AGREEMENT FOR SALE AND PURCHASE',
 'CONFIRMATORY RELEASE',
 'CONSENT LETTER',
 'CONSENT TO ASSIGN',
 'DEATH CERTIFICATE',
 'DEED OF ASSENT',
 'DEED OF ASSIGNMENT',
 'DEED OF ASSIGNMENT OF RENTAL INCOME',
 'DEED OF FAMILY ARRANGEMENT',
 'DEED OF GIFT',
 'DEED OF LOAN',
 'DEED OF MUTUAL COVENANT AND MANAGEMENT AGREEMENT WITH PLAN',
 'DEED OF MUTUAL COVENANT INCORPORATING MANAGEMENT AGREEMENT WITH PLAN',
 'DEED OF RECTIFICATION',
 'DEED OF RELEASE',
 'DEED OF SEVERANCE',
 'DEED POLL',
 'DUPLICATE OF UNDERTAKING LETTER',
 'EQUITABLE MORTGAGE',
 'FINAL RELEASE',
 'FINANCE UNDERTAKING',
 'FIRE SAFETY COMPLIANCE ORDER UNDER S.6(1) OF FIRE SAFETY (BUILDINGS) ORDINANCE (CHAPTER 572)',
 'FIRST CHARGE',
 'FIRST EQUITABLE MORTGAGE',
 'FIRST LEGAL CHARGE',
 'FIRST LEGAL CHARGE/MORTGAGE',
 'FOURTH MORTGAGE',
 'FURTHER CHARGE',
 'GOVERNMENT NOTICE',
 'IRREVOCABLE POWER OF ATTORNEY',
 'LEGAL CHARGE',
 'LEGAL CHARGE/MORTGAGE',
 'LETTER FOR REMOVAL OF ALIENATION RESTRICTIONS',
 'LETTER OF COMPLIANCE',
 'LETTER OF NOMINATION',
 'LETTER OF REMOVAL OF ALIENATION RESTRICTIONS',
 'LETTER OF WITHDRAWAL',
 'LETTERS OF ADMINISTRATION',
 'LETTERS OF ADMINISTRATION DE BONIS NON',
 'LOAN AGREEMENT',
 'MEMORANDUM FOR SALE AND PURCHASE',
 'MEMORANDUM OF AGREEMENT FOR SALE AND PURCHASE',
 'MEMORANDUM OF CHARGE',
 'MEMORANDUM OF DETERMINATION',
 'MEMORANDUM OF DISCHARGE',
 'MEMORANDUM OF RELEASE',
 'MEMORANDUM OF SALE',
 'MEMORANDUM OF SALE AND PURCHASE',
 'MEMORANDUM OF SATISFACTION',
 'MEMORIAL OF SATISFACTION UNDER S.33(10) OF THE BUILDINGS ORDINANCE',
 'MORTGAGE',
 'MORTGAGE DEED',
 'MORTGAGE TO SECURE GENERAL BANKING FACILITIES',
 'MORTGAGE/LEGAL CHARGE',
 'NO OBJECTION LETTER',
 'NOMINATION',
 'NOTICE OF SEVERANCE',
 'NOTICE OF SEVERANCE OF JOINT TENANCY',
 'NOTICE UNDER S.24C(1) OF THE BUILDINGS ORDINANCE',
 'NOTICE UNDER S.30B(3) OF THE BUILDINGS ORDINANCE',
 'NOTICE UNDER S.30C(3) OF THE BUILDINGS ORDINANCE',
 'NOTIFICATION LETTER OF COMPLETION OF WORKS',
 'NOTIFICATION LETTER OF COMPLETION OF WORKS RELATING TO ORDER',
 'OCCUPATION PERMIT',
 'ORDER',
 'ORDER UNDER S.24(1) OF THE BUILDINGS ORDINANCE',
 'ORDER UNDER S.24(1) OF THE BUILDINGS ORDINANCE WITH PLAN',
 'ORDER UNDER S.26 OF THE BUILDINGS ORDINANCE',
 'ORDER UNDER S.26 OF THE BUILDINGS ORDINANCE WITH PLAN',
 'ORDER UNDER S.26A(1) OF THE BUILDINGS ORDINANCE',
 'ORDER UNDER S.26A(1) OF THE BUILDINGS ORDINANCE WITH PLAN',
 'ORDER UNDER S.27A OF THE BUILDINGS ORDINANCE WITH PLAN',
 'ORDER UNDER S.28(3) OF THE BUILDINGS ORDINANCE',
 'ORDER UNDER S.28(3) OF THE BUILDINGS ORDINANCE WITH PLAN',
 'PARTIAL RELEASE',
 'POWER OF ATTORNEY',
 'PRELIMINARY AGREEMENT FOR SALE AND PURCHASE',
 'PRELIMINARY SALE AND PURCHASE AGREEMENT',
 'PROBATE',
 'PROVISIONAL AGREEMENT FOR SALE AND PURCHASE',
 'RECEIPT ON DISCHARGE',
 'RECEIPT ON DISCHARGE OF A CHARGE',
 'RELEASE',
 'RENT ASSIGNMENT',
 'RENTAL ASSIGNMENT',
 'REREGISTRATION OF AGREEMENT FOR SALE AND PURCHASE MEMORIAL',
 'REREGISTRATION OF ASSIGNMENT MEMORIAL',
 'REVERSE MORTGAGE',
 'SALE AND PURCHASE AGREEMENT',
 'SATISFACTION LETTER',
 "SEALED COPY OF BANKRUPTCY ORDER ON DEBTOR'S PETITION",
 'SEALED COPY OF CHARGING ORDER ABSOLUTE',
 'SEALED COPY OF CHARGING ORDER: NOTICE TO SHOW CAUSE',
 'SEALED COPY OF ORDER',
 'SEALED COPY OF WRIT OF SUMMONS',
 'SECOND EQUITABLE MORTGAGE',
 'SECOND LEGAL CHARGE',
 'SECOND LEGAL CHARGE/MORTGAGE',
 'SECOND MORTGAGE',
 'SECOND SUPPLEMENTAL STATUTORY DECLARATION',
 'STATUTORY DECLARATION',
 'SUBCHARGE/SUBMORTGAGE',
 'SUBDEED OF MUTUAL COVENANT AND MANAGEMENT AGREEMENT WITH PLAN',
 'SUBDEED OF MUTUAL COVENANT WITH PLAN',
 'SUBMORTGAGE',
 'SUPERSEDING NOTICE UNDER S.30B(3) OF THE BUILDINGS ORDINANCE',
 'SUPERSEDING NOTICE UNDER S.30C(3) OF THE BUILDINGS ORDINANCE',
 'SUPERSEDING ORDER UNDER S.24(1) OF THE BUILDINGS ORDINANCE',
 'SUPERSEDING ORDER UNDER S.24(1) OF THE BUILDINGS ORDINANCE WITH PLAN',
 'SUPERSEDING ORDER UNDER S.26 OF THE BUILDINGS ORDINANCE',
 'SUPPLEMENTAL AGREEMENT',
 'SUPPLEMENTAL STATUTORY DECLARATION',
 'TENANCY AGREEMENT',
 'THIRD LEGAL CHARGE',
 'THIRD MORTGAGE',
 'THREE-PARTY MORTGAGE DEED',
 'TRANSFER OF MORTGAGE',
 'TRIPARTITE EQUITABLE MORTGAGE',
 'TRIPARTITE LEGAL CHARGE/MORTGAGE',
 'TRIPARTITE MORTGAGE/LEGAL CHARGE',
 'TRIPARTITE SECOND LEGAL CHARGE/MORTGAGE',
 'TWO-PARTY MORTGAGE DEED',
 'UNDERTAKING',
 'UNDERTAKING LETTER',
 'WAIVER LETTER']



# https://stooq.com/
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime(2020, 12, 3)
df = web.DataReader(['AMZN', 'GOOGL', 'FB', 'PFE', 'MRNA', 'BNTX'],
                    'stooq', start=start, end=end)
# df=df.melt(ignore_index=False, value_name="price").reset_index()
df = df.stack().reset_index()
df.rename(columns={'level_0': 'Date'}, inplace=True)
print(df[:15])

# df.to_csv("mystocks.csv", index=False)
# df = pd.read_csv("mystocks.csv")
# print(df[:15])

w120_meaning_en_dict= np.load(r'C:\Users\Terry\Desktop\temp_data_store\Incumbrance Project/w120_meaning_en_dict.npy', allow_pickle=True).item()
w120_meaning_zh_dict= np.load(r'C:\Users\Terry\Desktop\temp_data_store\Incumbrance Project/w120_meaning_zh_dict.npy', allow_pickle=True).item()
sim_meaning_en_dict= np.load(r'C:\Users\Terry\Desktop\temp_data_store\Incumbrance Project/sim_meaning_en_dict.npy', allow_pickle=True).item()
sim_meaning_zh_dict= np.load(r'C:\Users\Terry\Desktop\temp_data_store\Incumbrance Project/sim_meaning_zh_dict.npy', allow_pickle=True).item()

simple_text = dcc.Markdown('{}'.format('a')
)
full_text = dcc.Markdown('{}'.format('b')
)

# https://www.bootstrapcdn.com/bootswatch/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.COSMO],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server

# Layout section: Bootstrap (https://hackerthemes.com/bootstrap-cheatsheet/)
# ************************************************************************
app.layout = dbc.Container([

    dbc.Row(
        dbc.Col(html.H2("Encumbrance Dictionary",
                        className='text-center text-primary mb-4'),
                width=12)
    ),

    dbc.Row([

        dbc.Col([
            dcc.Markdown('Enter Encumbrance:'),
            dcc.Dropdown(id='my-dpdn', multi=False,
                         options=[{'label': x, 'value': x}
                                  for x in eng_incum_list],
                         ),
            #dcc.Graph(id='line-fig', figure={})
            dcc.Markdown(id='simple_text', children= '{}'.format(''), style={"margin-top": "25px"} ),
            # dbc.Collapse(
            #         dbc.CardBody("Because it's a lot better than a hotdog."),
            #         id="collapse-question-1", is_open=True
            # ),

            html.Div(#html.H6("Product: a beautiful Pizza reheated after a day in the fridge, for $99"),
                     style={"text-align":"center"}),
                html.Hr(),
                dbc.CardHeader(
                        dbc.Button(
                            "More Details on this Encumbrance",
                            color="link",
                            id="button-question-1",
                        )
                ),
                dbc.Collapse(
                    dbc.CardBody(children="Please enter an Encumbrance first.",),
                    id="collapse-question-1", is_open=False
                ),






        ],  # width={'size':5, 'offset':1, 'order':1},
            xs=12, sm=12, md=12, lg=5, xl=5
        ),



    ], #className='p-1 bg-light border',
        justify='center'),  # Horizontal:start,center,end,between,around

    # dbc.Row([
    #     dbc.Col([
    #         html.P("Select Company Stock:",
    #                style={"textDecoration": "underline"}),
    #         dcc.Checklist(id='my-checklist', value=['FB', 'GOOGL', 'AMZN'],
    #                       options=[{'label': x, 'value': x}
    #                                for x in eng_incum_list],
    #                       labelClassName="mr-3"),
    #         dcc.Graph(id='my-hist', figure={}),
    #     ],  # width={'size':5, 'offset':1},
    #         xs=12, sm=12, md=12, lg=5, xl=5
    #     ),
    #
    #     dbc.Col([
    #         dbc.Card(
    #             [
    #                 dbc.CardBody(
    #                     html.P(
    #                         "We're better together. Help each other out!",
    #                         className="card-text")
    #                 ),
    #                 dbc.CardImg(
    #                     src="https://media.giphy.com/media/Ll0jnPa6IS8eI/giphy.gif",
    #                     bottom=True),
    #             ],
    #             style={"width": "24rem"},
    #         )
    #     ],  # width={'size':5, 'offset':1},
    #         xs=12, sm=12, md=12, lg=5, xl=5
    #     )
    # ], align="center")  # Vertical: start, center, end

], fluid=True)


# Callback section: connecting the components
# ************************************************************************
# Line chart - Single
@app.callback(
    [Output(component_id='simple_text', component_property='children'), Output(component_id='collapse-question-1', component_property='children') ],
    Input('my-dpdn', 'value'),
    prevent_initial_call=True
)
def update_text(selected_incum):
    print(w120_meaning_en_dict[selected_incum])
    w120_list= w120_meaning_en_dict[selected_incum].split('\n')

    return "Explanation: "+ sim_meaning_en_dict[selected_incum] , html.Ul(id='my-list', children=[html.Li(i) for i in w120_list])

@app.callback(
    Output("collapse-question-1", "is_open"),
    [Input("button-question-1", "n_clicks")],
    [State("collapse-question-1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# # Line chart - multiple
# @app.callback(
#     Output('line-fig2', 'figure'),
#     Input('my-dpdn2', 'value')
# )
# def update_graph(stock_slctd):
#     dff = df[df['Symbols'].isin(stock_slctd)]
#     figln2 = px.line(dff, x='Date', y='Open', color='Symbols')
#     return figln2
#
#
# # Histogram
# @app.callback(
#     Output('my-hist', 'figure'),
#     Input('my-checklist', 'value')
# )
# def update_graph(stock_slctd):
#     dff = df[df['Symbols'].isin(stock_slctd)]
#     dff = dff[dff['Date'] == '2020-12-03']
#     fighist = px.histogram(dff, x='Symbols', y='Close')
#     return fighist




if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

# https://youtu.be/0mfIK8zxUds