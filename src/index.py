import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/OGatoCapitalista/trabalhinho/main/social-media-stocks-2012-2022-_1_.csv')
df = df.values.tolist()

Quantidade_de_Vendas, Menor_Valor,  Maior_Valor, Fechamento, Abertura, Empresa, Data = ([] for i in range(7))
ANOS_BRUTOS = ['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']

for i in range(len(df)):
  dataFrame = list(df[i])
  Data.append(dataFrame[0])
  Empresa.append(dataFrame[1])
  Abertura.append(dataFrame[2])
  Fechamento.append(dataFrame[3])
  Maior_Valor.append(dataFrame[4])
  Menor_Valor.append(dataFrame[5])
  Quantidade_de_Vendas.append(dataFrame[6])

datasParsed = { ano : list() for ano in ANOS_BRUTOS }

x = 0
while x < len(ANOS_BRUTOS):
    i = 0
    while i < len(Data):
        ano = list(Data[i])
        if (ano[2]==ANOS_BRUTOS[x][2] and ano[3]==ANOS_BRUTOS[x][3]) and (Data[i] not in datasParsed[ANOS_BRUTOS[x]]):
            datasParsed[ANOS_BRUTOS[x]].append(Data[i])
        i += 1
    x += 1

#Esse código separa as empresas
Facebook , Twitter, Pinterest, Snapchat, Etsy = ([] for i in range(5))
for i in range(len(Empresa)):
  if Empresa[i] == 'FB':
    Facebook.append(Empresa[i])
  elif Empresa[i] == 'TWTR':
    Twitter.append(Empresa[i])   
  elif Empresa[i] == 'PINS':
    Pinterest.append(Empresa[i])
  elif Empresa[i] == 'SNAP':
    Snapchat.append(Empresa[i])
  else:
    Etsy.append(Empresa[i])    

#Calcula a média de abertura de cada ano de cada empresa
def mediasAnuais(d):
  total = []
  totais = ['total12','total13','total14','total15','total16','total17','total18','total19','total20','total21','total22']
  totalParsed = { total : list() for total in totais }
  for x in range(len(totais)):
    for i in range(len(Data)):
      ano = list(Data[i])
      Ano_igual = (ano[2]==ANOS_BRUTOS[x][2] and ano[3]==ANOS_BRUTOS[x][3])
      a = list(df[i])
      if Ano_igual and a[1]== d:
        totalParsed[totais[x]].append(a[2])
    if len(totalParsed[totais[x]])>=1:
      totalParsed[totais[x]] = sum(totalParsed[totais[x]])/len(totalParsed[totais[x]]);total.append(totalParsed[totais[x]])
    else:
      total.append(0)
  return total  

#ABAIXO SOMENTE GRAFICOS

#Gráfico de linha Quantidade e Data 2021 a 2022
fig = px.line(x = datasParsed['2021']+datasParsed['2022'],color_discrete_sequence=['#E60023','#FFFC00','#F56400','#3b5998','#00acee'],y = Maior_Valor[len(Empresa)-318:len(Empresa)],title = 'Maior valor das ações nos anos de 2021 e 2022', color = Empresa[len(Empresa)-318:len(Empresa)])
fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Valor de venda')
fig.update_layout(legend_title='Empresa')
fig.show()

#Grafico de torta Quant de Vendas relação á empresas
cores = ['#3b5998','#00acee','#FFFC00','#E60023','#F56400']
fig2 = px.pie(values= Quantidade_de_Vendas, names= Empresa,hole = 0.5,title='Quantidade total de vendas nos anos de 2012 a 2022',color_discrete_sequence=cores)
fig2.update_layout(legend_title='Empresa')
fig2.show()

#Exemplo de Gráfico de analise de mercado que acompanha o valor das ações do Facebook, em seus picos e queda na bolsa
fig3 = go.Figure(go.Candlestick(x = datasParsed['2012'],
                open=Abertura[0:252],
                high=Maior_Valor[0:252],
                low=Menor_Valor[0:252],
                close=Fechamento[0:252]))
fig3.update_layout(
    title='Análise de mercado do Facebook no ano de 2012',
    yaxis_title='Valores máximos de venda',
    xaxis_title='Linha temporal')
fig3.show()

#grafico das medias de abertura de cada ano
Dados = [
    go.Bar(name = 'Facebook', x = ANOS_BRUTOS,y = mediasAnuais('FB'),marker_color='#3b5998'),
    go.Bar(name = 'Twitter', x= ANOS_BRUTOS, y=mediasAnuais('TWTR'),marker_color='#00acee'),
    go.Bar(name = 'Etsy', x= ANOS_BRUTOS, y=mediasAnuais('ETSY'),marker_color='#F56400'),
    go.Bar(name = 'Snap', x= ANOS_BRUTOS, y=mediasAnuais('SNAP'),marker_color='#FFFC00'),
    go.Bar(name = 'Pinterest', x= ANOS_BRUTOS, y=mediasAnuais('PINS'),marker_color='#E60023')]

fig4 = go.Figure(Dados)
fig4.update_layout(barmode='group',title='Valor médio de abertura de cada empresa em cada ano')
fig4.update_yaxes(title = 'Valor de abertura')
fig4.update_xaxes(title = 'Anos')
fig4.update_layout(legend_title='Empresa')
fig4.show()

#Valor das ações ao decorrer dos anos 

Empresas = ["Facebook", "Pinterest", "Snapchat", "Twitter", "Etsy"]
fig5 = go.Figure()
fig5.add_trace(go.Scatter(
    y=[max(mediasAnuais('FB')), max(mediasAnuais('PINS')), max(mediasAnuais('SNAP')), max(mediasAnuais('TWTR')), max(mediasAnuais('ETSY'))],
    x=Empresas,
    marker=dict(color="#006400", size=20),
    mode="markers",
    name="Maior Valor das Ações"))

fig5.add_trace(go.Scatter(
    y=[min(x for x in mediasAnuais('FB') if x != 0), min(x for x in mediasAnuais('PINS') if x != 0), min(x for x in mediasAnuais('SNAP') if x != 0), min(x for x in mediasAnuais('TWTR') if x != 0), min(x for x in mediasAnuais('ETSY') if x != 0)],
    x=Empresas,
    marker=dict(color="red", size=20),
    mode="markers",
    name="Menor Valor das Ações"))

fig5.update_layout(title="Maior e menor valor de abertura (em média) das ações por empresa",
                  xaxis_title="Empresa",
                  yaxis_title="Valor de abertura")
fig5.update_layout(legend_title='Legenda')

fig5.show()
