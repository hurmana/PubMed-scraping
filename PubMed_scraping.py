from bs4 import BeautifulSoup
import pandas as pd
import datetime, requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def pubmed_scraping():
    #pubmed検索結果：guidewire CTO coronary intervention 5years
    url = 'https://pubmed.ncbi.nlm.nih.gov/?term=guidewire%20CTO%20coronary%20intervention&filter=datesearch.y_5&page={}'

    #出力するファイル名を現在の日付に設定
    current_datetime = datetime.datetime.now()
    outputFileName = current_datetime.strftime('%Y-%m-%d') + '.xlsx'

    #変数d_listに空のリストを作成する
    d_list = []

    #webdriverを起動
    driver = webdriver.Chrome()

    for page in range(1,10):
        target_url = url.format(page)
        print('スクレイピング中：' + str(page) + 'ページ目')

        driver.get(target_url)

        for i in range(10):
            #タイトルをクリックする
            target_title = driver.find_elements(By.CLASS_NAME, "docsum-title")[i]
            driver.execute_script('arguments[0].click();', target_title)
            
            #BeautifulSoupでページの内容を解析する
            res = requests.get(driver.current_url)
            soup = BeautifulSoup(res.text, 'html.parser')
            
            #タイトルを取得
            title = soup.find('h1', class_="heading-title")
            if title != None:
                title = title.text.replace("\n", "")
            else:
                title = 'None'
            
            #authorsを取得
            authors = soup.find('div', class_="authors-list").text
            authors = authors.replace("\n", "")
            authors = authors.replace(" ", "")
            
            #abstractを取得
            abstract = soup.find('div', class_="abstract-content selected")
            if abstract != None:
                abstract = abstract.text.replace("\n", "")
            else:
                abstract = 'None'
            
            #journal infoを取得
            article_source = soup.find('div', class_="article-source")
            #ジャーナル名を取得
            journal_name = article_source.find(class_="journal-actions-trigger trigger").text
            journal_name = journal_name.replace("\n", "")
            #発行日とページを取得
            publich_date_and_page = article_source.find('span', class_="cit").text

            #論文タイプを取得
            #if len(driver.find_elements(By.CLASS_NAME, "publication-type")) > 0:
            publication_type = soup.find('div', class_="publication-type")
            if publication_type is None:
                publication_type = "None"
            else:
                publication_type = publication_type.text

            #citation_doiを取得
            citation_doi = soup.find('span', class_="citation-doi")
            if citation_doi != None:
                citation_doi = citation_doi.text.replace("\n", "")
            else:
                citation_doi = 'None'
            
            #urlを取得
            get_url = driver.current_url

            #変数dに、これまで取得した項目を格納する
            d = {
                'Title': title.lstrip(),
                'Authors': authors,
                'Abstract': abstract.lstrip(),
                'Journal': journal_name.lstrip(),
                'Publish date & page': publich_date_and_page,
                'Type': publication_type,
                'Citation doi': citation_doi.lstrip(),
                'URL': get_url
            }

            d_list.append(d)
            driver.back()

    driver.quit()

    #データをDataFrameに変換
    df = pd.DataFrame(d_list)

    #DataFrameをExcelに出力
    with pd.ExcelWriter(outputFileName, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=current_datetime.strftime('%Y-%m-%d'))

    print('データを出力しました')

def add_new_paper():
    current_datetime = datetime.datetime.now()

    listFile = "論文リスト.xlsx"
    newFile = current_datetime.strftime('%Y-%m-%d') + '.xlsx'

    #Excelファイルを読み込む
    df_list = pd.read_excel(listFile)
    df_new = pd.read_excel(newFile)

    #2つのExcelを結合
    merged_df = pd.merge(df_list, df_new, on='Title', how='outer', indicator=True)

    #新しいファイルにのみ存在するデータを抽出
    new_data = merged_df[merged_df['_merge'] == 'right_only'] 

    #新しく追加されたデータをリスト化
    n_list = []
    for i in range(len(df_new)):
        for j in range(len(new_data)):
            if df_new.iloc[i, 1] == new_data.iloc[j, 1]:
                #df_list = pd.concat([df_list, df_new.iloc[i,:]], ignore_index=True)
                n = {
                    'Title': df_new.iloc[i,1],
                    'Authors': df_new.iloc[i,2],
                    'Abstract': df_new.iloc[i,3],
                    'Journal': df_new.iloc[i,4],
                    'Publish date & page': df_new.iloc[i,5],
                    'Type': df_new.iloc[i,6],
                    'Citation doi': [i,7],
                    'URL': df_new.iloc[i,8]
                    }

                n_list.append(n)

    #新たに追加されたデータのDataFrame作成
    newly_added_df = pd.DataFrame(n_list)

    #既存のリストに新しく追加されたデータを追加
    df_list = pd.merge(df_list, df_new, how='outer')
    df_list = df_list.drop('Unnamed: 0', axis=1)

    #Excelに変換
    with pd.ExcelWriter(listFile, engine='openpyxl') as writer:
        df_list.to_excel(writer, sheet_name='list')
        newly_added_df.to_excel(writer, sheet_name='newly_added')

    if len(newly_added_df)==0:
        print('新たな論文はありません')
    else:
        print('新たに' + str(len(newly_added_df)) + '個の論文を追加しました')


pubmed_scraping()

add_new_paper()
