import requests
import os

# جلب المفاتيح السرية من السيرفر
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")

def send_test_message():
    print("🔄 جاري إرسال رسالة الاختبار المباشرة إلى التليجرام...")
    
    # رسالة ثابتة ومضمونة 100% بدون الحاجة لأي موقع خارجي
    alert_message = (
        "🚀 **تهانينا.. منظومة الأتمتة السحابية تعمل بنجاح!** 🚀\n\n"
        "📱 **حالة السيرفر:** متصل بالسحاب (GitHub Actions)\n"
        "✅ **خط الاتصال:** جاهز ومستقر تماماً.\n\n"
        "🎯 _وصول هذه الرسالة يعني أن الـ Token والـ Chat ID الخاصين بك صحيحين 100%، والنظام جاهز الآن لأي مشروع!_"
    )
    
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": alert_message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(telegram_url, data=payload)
        if response.status_code == 200:
            print("✅ يا بطل! تم إرسال الرسالة بنجاح إلى التليجرام!")
        else:
            print(f"❌ السيرفر شغال، ولكن تليجرام رفض الإرسال. رمز الخطأ: {response.status_code}")
            print("💡 هذا يعني أن هناك حرفاً خاطئاً أو مسافة زائدة في الـ BOT_TOKEN أو الـ CHAT_ID داخل الـ Secrets.")
    except Exception as e:
        print(f"💥 حدث خطأ أثناء الاتصال بالتليجرام: {e}")

if __name__ == "__main__":
    send_test_message()
