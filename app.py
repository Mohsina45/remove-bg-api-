from flask import Flask, request, send_file
from PIL import Image
from rembg import remove
import io

app = Flask(__name__)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No image uploaded", 400

    img_file = request.files['image']
    img = Image.open(img_file.stream).convert("RGBA")
    output = remove(img)

    img_bytes = io.BytesIO()
    output.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
