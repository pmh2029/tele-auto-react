# tele-auto-react
B1: Vào https://my.telegram.org/apps để lấy app_id và app_hash

B2: Clone prj, chạy các lệnh sau
    python3 -m venv venv && source venv/bin/activate
    pip install -r requirements.txt

B3: Chạy python3 utils.py
  - Chat vs người bất kỳ để lấy user_id của họ để thêm vào env
  - Chat trong nhóm bất kỳ để lấy group_id để thêm vào env
  - user_id và group_id thêm nhiều thì cách nhau bởi dấu "," (ví dụ: user_id=1,2)

B4: Sau khi thêm thì chạy python3 main.py để chạy bot
