from datetime import timedelta
import pytz

def convert_duration_to_time(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}"

def convert_time_to_duration(time):
    total_seconds = time.total_seconds()
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return timedelta(hours=minutes, minutes=seconds)
