import requests
import os

# --- إعدادات التليجرام السرية المربوطة بالسيرفر ---
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")

def send_telegram_message(text_message):
    """إرسال التقرير الفوري للتليجرام"""
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text_message,
        "parse_mode": "Markdown"
    }
    response = requests.post(telegram_url, data=payload)
    return response.status_code == 200

def track_live_market():
    print("🔄 جاري سحب الأسعار الحية من السوق الآن...")
    try:
        # استخدام CoinDesk API - مفتوح تماماً ولا يحظر سيرفرات جيت هاب (قاهر الخطأ 451)
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            raw_price = data['bpi']['USD']['rate_float']
            
            # تنسيق السعر ليظهر بشكل مالي احترافي (مثال: $65,250.00)
            formatted_price = f"${raw_price:,.2f}"
            
            # صياغة الرسالة النهائية
            alert_message = (
                f"📊 **نظام مراقبة الأسعار السحابي (ناجح)** 📊\n\n"
                f"🪙 **الأصل المتداول:** Bitcoin (BTC/USD)\n"
                f"💰 **السعر الحالي في السوق:** `{formatted_price}`\n\n"
                f"⚡ _النظام يعمل سحابياً بنجاح ومستقر 100% بدون أي تدخّل بشري!_"
            )
            
            if send_telegram_message(alert_message):
                print("✅ تم إرسال التنبيه الفوري إلى تليجرام بنجاح باهر!")
            else:
                print("❌ الكود جلب السعر بنجاح، لكن فشل إرسال رسالة التليجرام (تأكد من الـ ID والـ Token في الـ Secrets).")
        else:
            print(f"❌ فشل السيرفر في جلب السعر المباشر. رمز الخطأ: {response.status_code}")
            
    except Exception as e:
        print(f"💥 حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    track_live_market()
