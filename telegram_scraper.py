import requests
import os

# جلب المفاتيح السرية من السيرفر السحابي
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")

def send_telegram_message(text_message):
    """إرسال التقرير المالي الفوري للتليجرام"""
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text_message,
        "parse_mode": "Markdown"
    }
    response = requests.post(telegram_url, data=payload)
    return response.status_code == 200

def track_gold_market():
    print("🔄 جاري سحب أسعار الذهب الحية من البورصة العالمية...")
    try:
        # استخدام رابط ياهو فاينانس لأسعار الذهب (XAU/USD) - مستقر وضد الحظر
        url = "https://query1.finance.yahoo.com/v8/finance/chart/GC=F"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            gold_price = data['chart']['result'][0]['meta']['regularMarketPrice']
            
            # تنسيق السعر ليظهر بشكل مالي (مثال: $2,350.50)
            formatted_price = f"${gold_price:,.2f}"
            
            # صياغة التقرير المالي الاحترافي للعميل
            alert_message = (
                f"📈 **نظام المراقبة المالية السحابي** 📈\n\n"
                f"🏆 **الأصل المراقب:** الذهب العالمي (XAU/USD)\n"
                f"💰 **السعر الحالي للأونصة:** `{formatted_price}`\n\n"
                f"⚡ _تحديث فوري تلقائي - النظام يعمل بالكامل في السحاب بدون أي تدخل بشري._"
            )
            
            if send_telegram_message(alert_message):
                print("✅ تم إرسال تقرير الذهب بنجاح!")
            else:
                print("❌ فشل إرسال الرسالة.")
        else:
            print(f"❌ خطأ في جلب البيانات من البورصة: {response.status_code}")
            
    except Exception as e:
        print(f"💥 حدث خطأ: {e}")

if __name__ == "__main__":
    track_gold_market()
