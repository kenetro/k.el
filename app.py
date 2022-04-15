from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('IB4Cyhn96xxM601nutP+blYMvW1qiA6l5v8FnYWL8lBwS/XNsZGzp4aEd4lKnfDbXCqgxTxeW4+SVGB/rsNTDI97wjj5T4A56zLKEtoj41zjdxnWSkeU+8rRjPp39FURngRf7XWhy31E1o/prHsPygdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1a81518ba9f29b701da43f62d14d23db')



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    ### 這裡可以自行增加code
    message = TextSendMessage(text= "優秀喔")
    line_bot_api.reply_message(event.reply_token, message)



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)