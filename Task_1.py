def convert_time(duration: int) -> str:
    d = (duration // 86400)
    h = (duration - d * 86400) // 3600
    m = ((duration - d * 86400)- (h * 3600)) // 60
    s = ((duration - d * 86400)- (h * 3600) - (m * 60)) // 1

    if duration >= 86400:
        t = f'{d} дн {h} час {m} мин {s} сек'
    elif duration >= 3600:
        t = f'{h} час {m} мин {s} сек'
    elif duration >= 60:
        t = f'час {m} мин {s} сек'
    elif duration < 60:
        t = f'{s} сек'

    return t



duration = 400153
result = convert_time(duration)
print(result)