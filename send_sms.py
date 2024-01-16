import requests
import argparse

def send_sms(number, message, sender_name, regional_code):
    number_format = regional_code + "+" + number
    url = "https://globfone.com/send-text-online/"
    params = {
        'number': number_format,
        'message': message,
        'sender-name': sender_name,
        'action': "SendSms",
        'g-recaptcha-response': "03AFcWeA7Fui0S1CEqC0jzvjJPJljtDTbKXMPJgG9uMnW2qeZc3Y90MhmZ9WLLaIqAkLyTrNc0F84tDZLMC_MkW2tk-Gai9Bxp214RSWqXvYrpoJt-zF30gnqmPp0oqVRhLxLokFk3OjwBNC45VfVfJWzf00LKpG7G0oq58ul18s447VERS5pv4jdXQmPTrejSkNKuT3xW6nyB3HJMKORrIPguWjltO7MYOtIb-88Ru3I2ju1gMCf0kUmBgMIDuWQ6_QNoH3TBsHRaBo7lIVZErSOU8_EOTuft4z859QZTbUnTQAsofY29LCHTwqf99xfIY-WBAKcgIGUS6VWO4z-69juGO_Ckc_7H8cU2D3DTlHgyntkHgWUBWJkTVwcOxbUl-KELR1Uaxl9j944YUkFjR5fYDBgASQIThq5CrZ15tuEi_8GYnj_Wos_m0T0I9rYx-YxhSkXhy5o9IQn002tqyFsOHCGXA6Brq3GaWmLG8GhW3HFmYf2VTS7NAzUQ1M5ZBfnAVtFpaUVTaYUE9A6xil8uNb1HGcVqa_veNmiSpeDrI5KBnuQBCuw",
    }
    try:
        response = requests.post(url, data=params)
        
        if response.status_code == 200:
            print("SMS sent successfully to", number_format, "with message:", message)
        else:
            print("Failed to send SMS. Status code:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

def main():
    parser = argparse.ArgumentParser(description="Send SMS using globfone.com")
    parser.add_argument("-n", "--number", help="Phone number without regional code (e.g., 0612345619)", required=True)
    parser.add_argument("-r", "--regional-code", help="Regional code (e.g., +33 for France)", required=True)
    parser.add_argument("-m", "--message", help="SMS message", required=True)
    parser.add_argument("-s", "--sender", help="Sender name", required=True)
    
    args = parser.parse_args()
    send_sms(args.number, args.message, args.sender)

if __name__ == "__main__":
    main()
