# PubMed論文検索結果スクレイピング
PubMedで「guidewire CTO coronary intervention 5years」での検索結果の10ページ分をスクレイピングし、エクセルに論文リストとして出力するPythonコード。 
スクレイピング学習のために作成。

## 概要
### スクレイピング
- 取得情報：各論文のTitle、Authors、Abstract、Journal、Publish date & page、Publication type、Citation doi、URL 
- 出力形式：エクセル（ファイル名：年-月.xlsx）

### 論文リストの更新
- 新しく追加された論文がある場合： 
  「新たに〇個の論文を追加しました」というコメントを出力。 
  論文リストに新しく追加された論文を追加。 
  別シートに新しく追加された論文のみを記載。 
- 新しく追加された論文がない場合： 
  「新たな論文はありません」というコメントを出力。 
