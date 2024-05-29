# PubMed論文検索結果スクレイピング
プログラミング言語「Python」を使用して、医学論文検索サイトPubMedでの検索結果を  
Excelに自動抽出するサンプルコード。  
Python/スクレイピング学習のために作成。

## 概要
### スクレイピング
- 検索条件：guidewire CTO coronary intervention 5years
- 取得情報：各論文のTitle、Authors、Abstract、Journal、Publish date & page、Publication type、Citation doi、URL 
- 出力形式：エクセル（ファイル名：年-月-日.xlsx）

### 論文リストの更新
- 新しく追加された論文がある場合：  
  「新たに〇個の論文を追加しました」というコメントを出力  
  論文リストに新しく追加された論文を追加  
  別シートに新しく追加された論文のみを記載   
- 新しく追加された論文がない場合：  
  「新たな論文はありません」というコメントを出力  

## 機能
- PubMedの検索結果をスクレイピング
- 各論文のTitle、Authors、Abstract、Journal、Publish date & page、Publication type、Citation doi、URLを取得
- xlsx形式で取得結果をファイル出力
- 過去にスクレイピングした結果との比較し、論文リストを更新

## version
- conda 24.1.2
- python 3.11.7
- BeautifulSoup4 4.12.2 
- pandas 2.2.1
- selenium 4.19.0

## 画面サンプル
### 出力結果例
- スクレイピング結果（ファイル名の例：2024-05-23.xlsx）
  <img width="627" alt="image" src="https://github.com/hurmana/PubMed-scraping/assets/170585900/3f5d4944-9278-4b8b-8d4e-c01be87e8e18">

- 論文リスト：新たな論文をlistタブに追加するとともに、新たな論文を別タブに表示
  <img width="620" alt="image" src="https://github.com/hurmana/PubMed-scraping/assets/170585900/16ecdbc9-29c5-4c15-9e44-045ad908ad6b">


### スクレイピング中
- ブラウザ自動操作画面：https://gyazo.com/4bb2251846518720003da739c39f6273
- ターミナル  
  ![image](https://github.com/hurmana/PubMed-scraping/assets/170585900/d5452379-d145-4f64-bd2b-3e22504b841c)

## 備考
Java及びPython初学者で、スクレイピング等について本やネットで調べながら作製したため、約1ヵ月かかりました。

