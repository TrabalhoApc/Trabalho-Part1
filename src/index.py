import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('C:\Users\matro\Desktop\Trabalho APC\social-media-stocks-2012-2022-_1_.csv')
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
total12,total13,total14,total15,total16,total17,total18,total19,total20,total21,total22,totalface = ([] for i in range(12))

for i in range(len(Data)):
  a = list(df[i])
  b = list(Data[i])

  if b[2]=='1' and b[3]=='2' and a[1]== 'FB':
    total12.append(a[2]) 

  if b[2]=='1' and b[3]=='3' and a[1]== 'FB':
    total13.append(a[2])
  
  if b[2]=='1' and b[3]=='4' and a[1]== 'FB':
    total14.append(a[2]) 
  
  if b[2]=='1' and b[3]=='5' and a[1]== 'FB':
    total15.append(a[2])
  
  if b[2]=='1' and b[3]=='6' and a[1]== 'FB':
    total16.append(a[2])
  
  if b[2]=='1' and b[3]=='7' and a[1]== 'FB':
    total17.append(a[2])
  
  if b[2]=='1' and b[3]=='8' and a[1]== 'FB':
    total18.append(a[2])
  
  if b[2]=='1' and b[3]=='9' and a[1]== 'FB':
    total19.append(a[2])
  
  if b[2]=='2' and b[3]=='0' and a[1]== 'FB':
    total20.append(a[2])
  
  if b[2]=='2' and b[3]=='1' and a[1]== 'FB':
    total21.append(a[2])
  
  if b[2]=='2' and b[3]=='2' and a[1]== 'FB':
    total22.append(a[2])

total12 = sum(total12)/len(total12);totalface.append(total12) 
total13 = sum(total13)/len(total13);totalface.append(total13) 
total14 = sum(total14)/len(total14);totalface.append(total14) 
total15 = sum(total15)/len(total15);totalface.append(total15)
total16 = sum(total16)/len(total16);totalface.append(total16) 
total17 = sum(total17)/len(total17);totalface.append(total17)
total18 = sum(total18)/len(total18);totalface.append(total18) 
total19 = sum(total19)/len(total19);totalface.append(total19)
total20 = sum(total20)/len(total20);totalface.append(total20) 
total21 = sum(total21)/len(total21);totalface.append(total21)
total22 = sum(total22)/len(total22);totalface.append(total22) 

total12,total13,total14,total15,total16,total17,total18,total19,total20,total21,total22,totaltwitter = ([] for i in range(12))

for i in range(len(Data)):
  a = list(df[i])
  b = list(Data[i])

  if b[2]=='1' and b[3]=='2' and a[1]== 'TWTR':
    total12.append(a[2]) 

  if b[2]=='1' and b[3]=='3' and a[1]== 'TWTR':
    total13.append(a[2])
  
  if b[2]=='1' and b[3]=='4' and a[1]== 'TWTR':
    total14.append(a[2]) 
  
  if b[2]=='1' and b[3]=='5' and a[1]== 'TWTR':
    total15.append(a[2])
  
  if b[2]=='1' and b[3]=='6' and a[1]== 'TWTR':
    total16.append(a[2])
  
  if b[2]=='1' and b[3]=='7' and a[1]== 'TWTR':
    total17.append(a[2])
  
  if b[2]=='1' and b[3]=='8' and a[1]== 'TWTR':
    total18.append(a[2])
  
  if b[2]=='1' and b[3]=='9' and a[1]== 'TWTR':
    total19.append(a[2])
  
  if b[2]=='2' and b[3]=='0' and a[1]== 'TWTR':
    total20.append(a[2])
  
  if b[2]=='2' and b[3]=='1' and a[1]== 'TWTR':
    total21.append(a[2])
  
  if b[2]=='2' and b[3]=='2' and a[1]== 'TWTR':
    total22.append(a[2])

if len(total12)>=1:
  total12 = sum(total12)/len(total12);totaltwitter.append(total12) 
else:
  totaltwitter.append(0)  
if len(total13)>=1:
  total13 = sum(total13)/len(total13);totaltwitter.append(total13)  
else:
  totaltwitter.append(0)  
if len(total14)>=1:
  total14 = sum(total14)/len(total14);totaltwitter.append(total14) 
else:
  totaltwitter.append(0)  
if len(total15)>=1:
  total15 = sum(total15)/len(total15);totaltwitter.append(total15) 
else:
  totaltwitter.append(0)  
if len(total16)>=1:
  total16 = sum(total16)/len(total16);totaltwitter.append(total16) 
else:
  totaltwitter.append(0)  
if len(total17)>=1:
  total17 = sum(total17)/len(total17);totaltwitter.append(total17) 
else:
  totaltwitter.append(0)  
if len(total18)>=1:
  total18 = sum(total18)/len(total18);totaltwitter.append(total18) 
else:
  totaltwitter.append(0)  
if len(total19)>=1:
  total19 = sum(total19)/len(total19);totaltwitter.append(total19) 
else:
  totaltwitter.append(0)  
if len(total20)>=1:
  total20 = sum(total20)/len(total20);totaltwitter.append(total20) 
else:
  totaltwitter.append(0)  
if len(total21)>=1:
  total21 = sum(total21)/len(total21);totaltwitter.append(total21) 
else:
  totaltwitter.append(0)  
if len(total22)>=1:
  total22 = sum(total22)/len(total22);totaltwitter.append(total22) 
else:
  totaltwitter.append(0)  

total12,total13,total14,total15,total16,total17,total18,total19,total20,total21,total22,totaletsy = ([] for i in range(12))

for i in range(len(Data)):
  a = list(df[i])
  b = list(Data[i])

  if b[2]=='1' and b[3]=='2' and a[1]== 'ETSY':
    total12.append(a[2]) 

  if b[2]=='1' and b[3]=='3' and a[1]== 'ETSY':
    total13.append(a[2])
  
  if b[2]=='1' and b[3]=='4' and a[1]== 'ETSY':
    total14.append(a[2]) 
  
  if b[2]=='1' and b[3]=='5' and a[1]== 'ETSY':
    total15.append(a[2])
  
  if b[2]=='1' and b[3]=='6' and a[1]== 'ETSY':
    total16.append(a[2])
  
  if b[2]=='1' and b[3]=='7' and a[1]== 'ETSY':
    total17.append(a[2])
  
  if b[2]=='1' and b[3]=='8' and a[1]== 'ETSY':
    total18.append(a[2])
  
  if b[2]=='1' and b[3]=='9' and a[1]== 'ETSY':
    total19.append(a[2])
  
  if b[2]=='2' and b[3]=='0' and a[1]== 'ETSY':
    total20.append(a[2])
  
  if b[2]=='2' and b[3]=='1' and a[1]== 'ETSY':
    total21.append(a[2])
  
  if b[2]=='2' and b[3]=='2' and a[1]== 'ETSY':
    total22.append(a[2])

if len(total12)>=1:
  total12 = sum(total12)/len(total12);totaletsy.append(total12) 
else:
  totaletsy.append(0)  
if len(total13)>=1:
  total13 = sum(total13)/len(total13);totaletsy.append(total13)  
else:
  totaletsy.append(0)  
if len(total14)>=1:
  total14 = sum(total14)/len(total14);totaletsy.append(total14) 
else:
  totaletsy.append(0)  
if len(total15)>=1:
  total15 = sum(total15)/len(total15);totaletsy.append(total15) 
else:
  totaletsy.append(0)  
if len(total16)>=1:
  total16 = sum(total16)/len(total16);totaletsy.append(total16) 
else:
  totaletsy.append(0)  
if len(total17)>=1:
  total17 = sum(total17)/len(total17);totaletsy.append(total17) 
else:
  totaletsy.append(0)  
if len(total18)>=1:
  total18 = sum(total18)/len(total18);totaletsy.append(total18) 
else:
  totaletsy.append(0)  
if len(total19)>=1:
  total19 = sum(total19)/len(total19);totaletsy.append(total19) 
else:
  totaletsy.append(0)  
if len(total20)>=1:
  total20 = sum(total20)/len(total20);totaletsy.append(total20) 
else:
  totaletsy.append(0)  
if len(total21)>=1:
  total21 = sum(total21)/len(total21);totaletsy.append(total21) 
else:
  totaletsy.append(0)  
if len(total22)>=1:
  total22 = sum(total22)/len(total22);totaletsy.append(total22) 
else:
  totaletsy.append(0)  

total12,total13,total14,total15,total16,total17,total18,total19,total20,total21,total22,totalsnap = ([] for i in range(12))

for i in range(len(Data)):
  a = list(df[i])
  b = list(Data[i])

  if b[2]=='1' and b[3]=='2' and a[1]== 'SNAP':
    total12.append(a[2]) 

  if b[2]=='1' and b[3]=='3' and a[1]== 'SNAP':
    total13.append(a[2])
  
  if b[2]=='1' and b[3]=='4' and a[1]== 'SNAP':
    total14.append(a[2]) 
  
  if b[2]=='1' and b[3]=='5' and a[1]== 'SNAP':
    total15.append(a[2])
  
  if b[2]=='1' and b[3]=='6' and a[1]== 'SNAP':
    total16.append(a[2])
  
  if b[2]=='1' and b[3]=='7' and a[1]== 'SNAP':
    total17.append(a[2])
  
  if b[2]=='1' and b[3]=='8' and a[1]== 'SNAP':
    total18.append(a[2])
  
  if b[2]=='1' and b[3]=='9' and a[1]== 'SNAP':
    total19.append(a[2])
  
  if b[2]=='2' and b[3]=='0' and a[1]== 'SNAP':
    total20.append(a[2])
  
  if b[2]=='2' and b[3]=='1' and a[1]== 'SNAP':
    total21.append(a[2])
  
  if b[2]=='2' and b[3]=='2' and a[1]== 'SNAP':
    total22.append(a[2])

if len(total12)>=1:
  total12 = sum(total12)/len(total12);totalsnap.append(total12) 
else:
  totalsnap.append(0)  
if len(total13)>=1:
  total13 = sum(total13)/len(total13);totalsnap.append(total13)  
else:
  totalsnap.append(0)  
if len(total14)>=1:
  total14 = sum(total14)/len(total14);totalsnap.append(total14) 
else:
  totalsnap.append(0)  
if len(total15)>=1:
  total15 = sum(total15)/len(total15);totalsnap.append(total15) 
else:
  totalsnap.append(0)  
if len(total16)>=1:
  total16 = sum(total16)/len(total16);totalsnap.append(total16) 
else:
  totalsnap.append(0)  
if len(total17)>=1:
  total17 = sum(total17)/len(total17);totalsnap.append(total17) 
else:
  totalsnap.append(0)  
if len(total18)>=1:
  total18 = sum(total18)/len(total18);totalsnap.append(total18) 
else:
  totalsnap.append(0)  
if len(total19)>=1:
  total19 = sum(total19)/len(total19);totalsnap.append(total19) 
else:
  totalsnap.append(0)  
if len(total20)>=1:
  total20 = sum(total20)/len(total20);totalsnap.append(total20) 
else:
  totalsnap.append(0)  
if len(total21)>=1:
  total21 = sum(total21)/len(total21);totalsnap.append(total21) 
else:
  totalsnap.append(0)  
if len(total22)>=1:
  total22 = sum(total22)/len(total22);totalsnap.append(total22) 
else:
  totalsnap.append(0)

total12,total13,total14,total15,total16,total17,total18,total19,total20,total21,total22,totalpinterest = ([] for i in range(12))

for i in range(len(Data)):
  a = list(df[i])
  b = list(Data[i])

  if b[2]=='1' and b[3]=='2' and a[1]== 'PINS':
    total12.append(a[2]) 

  if b[2]=='1' and b[3]=='3' and a[1]== 'PINS':
    total13.append(a[2])
  
  if b[2]=='1' and b[3]=='4' and a[1]== 'PINS':
    total14.append(a[2]) 
  
  if b[2]=='1' and b[3]=='5' and a[1]== 'PINS':
    total15.append(a[2])
  
  if b[2]=='1' and b[3]=='6' and a[1]== 'PINS':
    total16.append(a[2])
  
  if b[2]=='1' and b[3]=='7' and a[1]== 'PINS':
    total17.append(a[2])
  
  if b[2]=='1' and b[3]=='8' and a[1]== 'PINS':
    total18.append(a[2])
  
  if b[2]=='1' and b[3]=='9' and a[1]== 'PINS':
    total19.append(a[2])
  
  if b[2]=='2' and b[3]=='0' and a[1]== 'PINS':
    total20.append(a[2])
  
  if b[2]=='2' and b[3]=='1' and a[1]== 'PINS':
    total21.append(a[2])
  
  if b[2]=='2' and b[3]=='2' and a[1]== 'PINS':
    total22.append(a[2])

if len(total12)>=1:
  total12 = sum(total12)/len(total12);totalpinterest.append(total12) 
else:
  totalpinterest.append(0)  
if len(total13)>=1:
  total13 = sum(total13)/len(total13);totalpinterest.append(total13)  
else:
  totalpinterest.append(0)  
if len(total14)>=1:
  total14 = sum(total14)/len(total14);totalpinterest.append(total14) 
else:
  totalpinterest.append(0)  
if len(total15)>=1:
  total15 = sum(total15)/len(total15);totalpinterest.append(total15) 
else:
  totalpinterest.append(0)  
if len(total16)>=1:
  total16 = sum(total16)/len(total16);totalpinterest.append(total16) 
else:
  totalpinterest.append(0)  
if len(total17)>=1:
  total17 = sum(total17)/len(total17);totalpinterest.append(total17) 
else:
  totalpinterest.append(0)  
if len(total18)>=1:
  total18 = sum(total18)/len(total18);totalpinterest.append(total18) 
else:
  totalpinterest.append(0)  
if len(total19)>=1:
  total19 = sum(total19)/len(total19);totalpinterest.append(total19) 
else:
  totalpinterest.append(0)  
if len(total20)>=1:
  total20 = sum(total20)/len(total20);totalpinterest.append(total20) 
else:
  totalpinterest.append(0)  
if len(total21)>=1:
  total21 = sum(total21)/len(total21);totalpinterest.append(total21) 
else:
  totalpinterest.append(0)  
if len(total22)>=1:
  total22 = sum(total22)/len(total22);totalpinterest.append(total22) 
else:
  totalpinterest.append(0)  

#ABAIXO SOMENTE GRAFICOS

#Gráfico de linha Quantidade e Data 2020 a 2021
fig = px.line(x = datasParsed['2020']+datasParsed['2021'],color_discrete_sequence=['#3b5998','#00acee','#E60023','#FFFC00','#F56400'],y = Maior_Valor[len(Empresa)-505:len(Empresa)],title = 'Maior valor das ações nos anos de 2021 e 2022', color = Empresa[len(Empresa)-505:len(Empresa)])
fig.update_xaxes(title_text='Data')                                             
fig.update_yaxes(title_text='Valor de venda')
fig.update_layout(legend_title='Empresa')
fig.show()

#Grafico de torta Quant de Vendas relação á empresas
cores = ['#3b5998','#00acee','#FFFC00','#E60023','#F56400']
fig2 = px.pie(values= Quantidade_de_Vendas, names= Empresa,hole = 0.5,title='Quantidade total de vendas nos anos de 2012 e 2022',color_discrete_sequence=cores)
fig2.update_layout(legend_title='Empresa')
fig2.show()

#Exemplo de Gráfico de analise de mercado que mostra quase todas as variáveis
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
    go.Bar(name = 'Facebook', x = ['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'],y = totalface,marker_color='#3b5998'),
    go.Bar(name = 'Twitter', x=['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'], y=totaltwitter,marker_color='#00acee'),
    go.Bar(name = 'Etsy', x=['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'], y=totaletsy,marker_color='#F56400'),
    go.Bar(name = 'Snap', x=['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'], y=totalsnap,marker_color='#FFFC00'),
    go.Bar(name = 'Pinterest', x=['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'], y=totalpinterest,marker_color='#E60023')]

fig4 = go.Figure(Dados)
fig4.update_layout(barmode='group',title='Valor médio de abertura de cada empresa em cada ano')
fig4.update_yaxes(title = 'Valor de abertura')
fig4.update_xaxes(title = 'Anos')
fig4.update_layout(legend_title='Empresa')
fig4.show()

#Valor das ações ao decorrer dos anos 

Empresas = ["Facebook", "Pinterest", "Snapchat", "Twitter", "Etsy"]
fig6 = go.Figure()
fig6.add_trace(go.Scatter(
    y=[max(totalface), max(totalpinterest), max(totalsnap), max(totaltwitter), max(totaletsy)],
    x=Empresas,
    marker=dict(color="#006400", size=20),
    mode="markers",
    name="Maior Valor das Ações"))

fig6.add_trace(go.Scatter(
    y=[min(x for x in totalface if x != 0), min(x for x in totalpinterest if x != 0), min(x for x in totalsnap if x != 0), min(x for x in totaltwitter if x != 0), min(x for x in totaletsy if x != 0)],
    x=Empresas,
    marker=dict(color="red", size=20),
    mode="markers",
    name="Menor Valor das Ações"))

fig6.update_layout(title="Maiores e menores valores das ações ao decorrer dos anos",
                  xaxis_title="Empresa",
                  yaxis_title="Valor das ações")
fig6.update_layout(legend_title='Legenda')

fig6.show()
