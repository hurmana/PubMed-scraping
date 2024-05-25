# PubMed論文検索結果スクレイピング
PubMedで「guidewire CTO coronary intervention 5years」での検索結果の10ページ分をスクレイピングし、  
エクセルに論文リストとして出力するPythonサンプルコード  
スクレイピング学習のために作成  

## 概要
### スクレイピング
- 取得情報：各論文のTitle、Authors、Abstract、Journal、Publish date & page、Publication type、Citation doi、URL 
- 出力形式：エクセル（ファイル名：年-月.xlsx）

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
![image](https://github.com/hurmana/PubMed-scraping/assets/170585900/01d95297-46c5-4d02-9699-f592da0c1b62)

- 論文リスト：新たな論文をlistタブに追加するとともに、新たな論文を別タブに表示
  ![image](https://github.com/hurmana/PubMed-scraping/assets/170585900/a71bb0e6-ece1-4c69-b89d-7b07cd31ec70)

### スクレイピング中
- ブラウザ自動操作画面：https://gyazo.com/4bb2251846518720003da739c39f6273
- ターミナル  
  ![image](https://github.com/hurmana/PubMed-scraping/assets/170585900/d5452379-d145-4f64-bd2b-3e22504b841c)

