import datetime
import locale
# Türkçe lokal ayarları yükle
locale.setlocale(locale.LC_TIME, 'tr_TR.UTF-8')
# Bugünün tarihini al
bugun = datetime.date.today()
# Tarihi string olarak yazdır
tarih_str = bugun.strftime("%A, %d %B %Y")