from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

@app.route('/', methods=['GET', 'POST'])
def home():

    caption = ""

    if request.method == 'POST':

        product = request.form['product']
        tone = request.form['tone']

        prompt = f"""
        Generate an Instagram caption for a jewellery business.

        Product: {product}
        Tone: {tone}

        Make it elegant, engaging and luxury themed.
        Add emojis.
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        caption = response.choices[0].message.content

    return render_template(
        'index1.html',
        caption=caption
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)