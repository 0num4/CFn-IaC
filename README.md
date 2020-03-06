## docker

https://dev.classmethod.jp/cloud/aws/github-actions-fargate-deploy/

dockerのビルド
docker build -t test-nginx . && docker run -p 8080:80 test-nginx

1. クラスターの作成
手動でクラスターの作成ボタンを押す
ネットワーキングのみ→次のステップ→クラスター名:spot-ecs→作成

2. CIを回す・・・nginxという名前のタスクが定義される(一応手動でもjson読み込んでタスクの作成できる)

3. サービスの作成
spot-ecsクラスターのサービスに新規作成。
起動タイプ: fargate
タスク定義: nginx
サービス名: spot-ecs
タスクの数: 1
=====次へ====
作成
サブネット: サブネット作成時にipv6を割り当てます
ALBなどは無しでオッケー(作成してもいいけど)
その他はデフォルトでオッケー

3. 確認
サービスがrunningになったらクラスターを選択して「タスク」タブのタスク(例: 3XXXXX3-0XXb-4XX1-bXX3-9feXXXXX3685)を選択
ネットワークにパブリックIPがあるからそれでアクセスする。