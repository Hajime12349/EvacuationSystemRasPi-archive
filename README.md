## システム説明
　本システムは町役員がアプリケーションに地区・立地ごとに必要な災害情報のテキストを入力し、各世帯にある防災ラジオに付属したシステムに送信して、ディスプレイに情報を表示することで、ラジオが聞き取りづらい高齢者の早期避難を促します。
 
![タイトルなし](https://github.com/Hajime12349/EvacuationSystemRasPi-archive/assets/51946324/c5145781-8b33-4906-be8f-fcae313e7af6)
![2](https://github.com/Hajime12349/EvacuationSystemRasPi-archive/assets/51946324/9805fceb-06f5-4e64-84c7-1b6aa71c357f)

## log
### 2023/01/31
+ 最終版

### 2023/01/23
+ ラズパイでの動作確認完了
+ WindowをFullScreen化

### 2023/01/20
+ テキスト送信プログラム記述など

### 2023/01/17
+ 履歴画面への画面遷移とUIを追加
+ 一通りのUIが一応完成
+ シリアル通信クラスを持つファイルserial_com.pyを追加（serial_test.pyの複製）
+ str -> binary　の関数を追加
+ コメント更新（カラーコード等）

### 2023/01/16
+ 通報入力送信確認画面作成
+ 通報完了画面作成

### 2023/01/09
+ 入力画面のドロップダウンリストUIを作成
+ ラベルの追加

### 2023/01/06
+ 通報ボタン画面遷移の実装
+ 入力画面作成中

### 2023/01/05
+ ファイル名変更(eva_system.py, .kv -> eva_system_admin.py, .kv)
+ Home画面作成

### 2022/12/20
+ Mainとなるpythonとkivyファイルを追加(eva_system)
+ requirements.txt更新

### 2022/12/06
+ Devフォルダ内にシリアル通信のテストコードを置いてます

## Requirement
- Python 3.9.x
- requirements.txt
