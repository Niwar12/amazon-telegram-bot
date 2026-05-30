import requests
from bs4 import BeautifulSoup
import os

# --- إعدادات التليجرام ---
# ملاحظة احترافية: نستخدم os.environ لجلب المفاتيح بأمان عند رفع الكود على سيرفر Render
BOT_TOKEN = os.environ.get("BOT_TOKEN", "ضع_هنا_توكن_البوت_الذي_نسخته")
CHAT_ID = os.environ.get("CHAT_ID", "ضع_هنا_رقم_الشات_ايدي_الذي_نسخته")

# الرابط المراد مراقبته (مثال لهاتف آيفون على أمازون)
URL = "https://www.amazon.com/dp/B0CHX68YCH"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

def send_telegram_message(text_message):
    """دالة مخصصة لإرسال الرسائل عبر تليجرام API"""
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text_message,
        "parse_mode": "Markdown" # تتيح تنسيق الخط ليكون غامقاً أو مائلاً
    }
    response = requests.post(telegram_url, data=payload)
    return response.status_code == 200

def check_price_and_notify():
    print("🔄 جاري فحص الأسعار الآن وإرسالها للتليجرام...")
    try:
        response = requests.get(URL, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # البحث عن السعر داخل صفحة أمازون
            price_element = soup.find("span", class_="a-price-whole")
            
            if price_element:
                current_price = price_element.get_text().strip().replace(".", "")
                
                # صياغة رسالة احترافية تظهر بشكل رائع في الهاتف
                alert_message = (
                    f"🔔 **تحديث الأسعار الفوري** 🔔\n\n"
                    f"📱 **المنتج:** iPhone 15 Pro Max\n"
                    f"💰 **السعر الحالي:** ${current_price}\n\n"
                    f"🔗 **رابط الشراء المباشر:**\n{URL}"
                )
                
                # إرسال الرسالة
                if send_telegram_message(alert_message):
                    print("✅ تم إرسال التنبيه إلى تليجرام بنجاح!")
                else:
                    print("❌ فشل السكربت في إرسال رسالة التليجرام.")
            else:
                print("❌ تعذر العثور على عنصر السعر في الصفحة (قد يكون المنتج غير متوفر).")
        else:
            print(f"❌ فشل الاتصال بالموقع. رمز الخطأ: {response.status_code}")
    except Exception as e:
        print(f"💥 حدث خطأ غير متوقع: {e}")

if __name__ == "__main__":
    check_price_and_notify()