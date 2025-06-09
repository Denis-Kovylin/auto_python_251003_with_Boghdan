from datetime import datetime
from checker.logger import logger


def analyze_heartbeat(log_path: str, target_key: str = "Key TSTFEED0300|7E3E|0400") -> None:
    """
    Анализирует лог heartbeat по заданному ключу и логирует отклонения:
    - WARNING, если разница между метками > 31 и < 33 сек
    - ERROR, если разница >= 33 сек
    """
    with open(log_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    filtered = [line.strip() for line in lines if target_key in line]

    timestamps = []
    for line in filtered:
        index = line.find("Timestamp ")
        if index != -1:
            time_str = line[index + 10: index + 18]
            try:
                time_obj = datetime.strptime(time_str, "%H:%M:%S")
                timestamps.append((time_obj, line.strip()))
            except ValueError:
                logger.warning(f"⛔ Невалидный формат времени: {line.strip()}")

    for i in range(len(timestamps) - 1):
        current_time, _ = timestamps[i]
        next_time, next_line = timestamps[i + 1]

        delta = (current_time - next_time).total_seconds()

        if 31 < delta < 33:
            logger.warning(f"⚠️ Heartbeat delay: {delta} сек — строка: {next_line}")
        elif delta >= 33:
            logger.error(f"❌ Превышен heartbeat: {delta} сек — строка: {next_line}")
