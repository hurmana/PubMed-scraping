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
- xlsx形式でファイル出力
- 過去にスクレイピングした結果との比較、差分を表示

## version
- conda 24.1.2
- python 3.11.7
- BeautifulSoup4 4.12.2 
- pandas 2.2.1
- selenium 4.19.0

## 画面サンプル
### スクレイピング中
- ブラウザ自動操作画面：https://gyazo.com/4bb2251846518720003da739c39f6273
- 

### スクレイピング完了

### 新しく追加された論文がある場合

### 新しく追加された論文がない場合
