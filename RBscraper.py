import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwings as xw

rbplayers_list = []
rbplayers_list1= []
rbplayers_list2= []
rbplayers_list3= []
rbplayers_list4= []
rbplayers_list5= []
rbplayers_list6= []
rbplayers_list7= []
rbplayers_list8= []
rbplayers_list9= []


for week in range(9,19):
    RBurl = 'https://www.fantasypros.com/nfl/stats/rb.php?year=2023&week={}&range=week'.format(week)

    RBresponse = requests.get(RBurl)
    RBsoup = BeautifulSoup(RBresponse.text, 'html.parser')

    RBrows = RBsoup.find('table').find('tbody').find_all('tr')

    

        
    for row in RBrows:
            if week == 9:
                RBdic = {}
                
                RBdic['Player'] = row.find('a').text
                RBdic['rYds'] = row.find_all('td')[3].text
                RBdic['rTds'] = row.find_all('td')[7].text
                RBdic['recs'] = row.find_all('td')[8].text
                RBdic['recYds'] = row.find_all('td')[10].text
                RBdic['recTds'] = row.find_all('td')[12].text
                RBdic['fumbs'] = row.find_all('td')[13].text
                RBdic['games'] = row.find_all('td')[14].text
                rbplayers_list.append(RBdic)
                
            if week == 10:
                RBdic1 = {}

                RBdic1['Player'] = row.find('a').text
                RBdic1['rYds'] = row.find_all('td')[3].text
                RBdic1['rTds'] = row.find_all('td')[7].text
                RBdic1['recs'] = row.find_all('td')[8].text
                RBdic1['recYds'] = row.find_all('td')[10].text
                RBdic1['recTds'] = row.find_all('td')[12].text
                RBdic1['fumbs'] = row.find_all('td')[13].text
                RBdic1['games'] = row.find_all('td')[14].text
                rbplayers_list1.append(RBdic1)
                
            if week == 11:
                RBdic2 = {}

                RBdic2['Player'] = row.find('a').text
                RBdic2['rYds'] = row.find_all('td')[3].text
                RBdic2['rTds'] = row.find_all('td')[7].text
                RBdic2['recs'] = row.find_all('td')[8].text
                RBdic2['recYds'] = row.find_all('td')[10].text
                RBdic2['recTds'] = row.find_all('td')[12].text
                RBdic2['fumbs'] = row.find_all('td')[13].text
                RBdic2['games'] = row.find_all('td')[14].text
                rbplayers_list2.append(RBdic2)
                
            if week == 12:
                RBdic3 = {}

                RBdic3['Player'] = row.find('a').text
                RBdic3['rYds'] = row.find_all('td')[3].text
                RBdic3['rTds'] = row.find_all('td')[7].text
                RBdic3['recs'] = row.find_all('td')[8].text
                RBdic3['recYds'] = row.find_all('td')[10].text
                RBdic3['recTds'] = row.find_all('td')[12].text
                RBdic3['fumbs'] = row.find_all('td')[13].text
                RBdic3['games'] = row.find_all('td')[14].text
                rbplayers_list3.append(RBdic3)
                
            if week == 13:
                RBdic4 = {}

                RBdic4['Player'] = row.find('a').text
                RBdic4['rYds'] = row.find_all('td')[3].text
                RBdic4['rTds'] = row.find_all('td')[7].text
                RBdic4['recs'] = row.find_all('td')[8].text
                RBdic4['recYds'] = row.find_all('td')[10].text
                RBdic4['recTds'] = row.find_all('td')[12].text
                RBdic4['fumbs'] = row.find_all('td')[13].text
                RBdic4['games'] = row.find_all('td')[14].text
                rbplayers_list4.append(RBdic4)
                
            if week == 14:
                RBdic5 = {}

                RBdic5['Player'] = row.find('a').text
                RBdic5['rYds'] = row.find_all('td')[3].text
                RBdic5['rTds'] = row.find_all('td')[7].text
                RBdic5['recs'] = row.find_all('td')[8].text
                RBdic5['recYds'] = row.find_all('td')[10].text
                RBdic5['recTds'] = row.find_all('td')[12].text
                RBdic5['fumbs'] = row.find_all('td')[13].text
                RBdic5['games'] = row.find_all('td')[14].text
                rbplayers_list5.append(RBdic5)
                
            if week == 15:
                RBdic6 = {}

                RBdic6['Player'] = row.find('a').text
                RBdic6['rYds'] = row.find_all('td')[3].text
                RBdic6['rTds'] = row.find_all('td')[7].text
                RBdic6['recs'] = row.find_all('td')[8].text
                RBdic6['recYds'] = row.find_all('td')[10].text
                RBdic6['recTds'] = row.find_all('td')[12].text
                RBdic6['fumbs'] = row.find_all('td')[13].text
                RBdic6['games'] = row.find_all('td')[14].text
                rbplayers_list6.append(RBdic6)
                
            if week == 16:
                RBdic7 = {}

                RBdic7['Player'] = row.find('a').text
                RBdic7['rYds'] = row.find_all('td')[3].text
                RBdic7['rTds'] = row.find_all('td')[7].text
                RBdic7['recs'] = row.find_all('td')[8].text
                RBdic7['recYds'] = row.find_all('td')[10].text
                RBdic7['recTds'] = row.find_all('td')[12].text
                RBdic7['fumbs'] = row.find_all('td')[13].text
                RBdic7['games'] = row.find_all('td')[14].text
                rbplayers_list7.append(RBdic7)
                
            if week == 17:
                RBdic8 = {}

                RBdic8['Player'] = row.find('a').text
                RBdic8['rYds'] = row.find_all('td')[3].text
                RBdic8['rTds'] = row.find_all('td')[7].text
                RBdic8['recs'] = row.find_all('td')[8].text
                RBdic8['recYds'] = row.find_all('td')[10].text
                RBdic8['recTds'] = row.find_all('td')[12].text
                RBdic8['fumbs'] = row.find_all('td')[13].text
                RBdic8['games'] = row.find_all('td')[14].text
                rbplayers_list8.append(RBdic8)
                
            if week == 18:
                RBdic9 = {}

                RBdic9['Player'] = row.find('a').text
                RBdic9['rYds'] = row.find_all('td')[3].text
                RBdic9['rTds'] = row.find_all('td')[7].text
                RBdic9['recs'] = row.find_all('td')[8].text
                RBdic9['recYds'] = row.find_all('td')[10].text
                RBdic9['recTds'] = row.find_all('td')[12].text
                RBdic9['fumbs'] = row.find_all('td')[13].text
                RBdic9['games'] = row.find_all('td')[14].text
                rbplayers_list9.append(RBdic9)


RBdf = pd.DataFrame(rbplayers_list)
RBdf1 = pd.DataFrame(rbplayers_list1)
RBdf2 = pd.DataFrame(rbplayers_list2)
RBdf3 = pd.DataFrame(rbplayers_list3)
RBdf4 = pd.DataFrame(rbplayers_list4)
RBdf5 = pd.DataFrame(rbplayers_list5)
RBdf6 = pd.DataFrame(rbplayers_list6)
RBdf7 = pd.DataFrame(rbplayers_list7)
RBdf8 = pd.DataFrame(rbplayers_list8)
RBdf9 = pd.DataFrame(rbplayers_list9)


wb_name = "bigboy.xlsx"
sheet_name = "RB"
df_mapping = {"A1": RBdf, "A275": RBdf1, "A550": RBdf2, "A825":RBdf3, "A1100":RBdf4, "A1375":RBdf5, "A1650":RBdf6, "A1925":RBdf7, "A2200":RBdf8, "A2475":RBdf9}

#open excel in background
# with xw.App(visible=False) as app:
#     wb = app.books.open(wb_name)


#     # add sheet if it doesnt exist
#     current_sheets = [sheet.name for sheet in wb.sheets]
#     if sheet_name not in current_sheets:
#         wb.sheets.add(sheet_name)
    
#     #write dataframe to cell range
#     for cell_target, df in df_mapping.items():
#         wb.sheets(sheet_name).range(cell_target).options(pd.DataFrame, index = False).value = df
    
#     wb.save()



RBdf.to_csv("playerData.csv")    
            
#RBdf1.to_csv("bigboy.csv")


    
print("Done.")