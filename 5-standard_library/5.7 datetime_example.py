from datetime import datetime, timedelta

now = datetime.now()
print("当前时间:", now)

tomorrow = now + timedelta(days=1)
print("明天此时:", tomorrow)