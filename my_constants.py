from flask import Flask


DOWNLOAD_FOLDER = "C:\\Users\\nisha\\Safe-Master\\client-server\\downloads"
UPLOAD_FOLDER = "C:\\Users\\nisha\\Safe-Master\\client-server\\uploads"

app = Flask(__name__)
app.secret_key = "f1006dcd31a6ec5023b9b964cd4556da"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'docx', 'mov', 'mp4', 'mp3', 'pdf', 'png', 'jpg', 'csv', 'xlsx', 'svg', 'zip', 'exe', 'bat', 'bin', 'html', 'jpeg', 'gif'])
app.config['SERVER_IP'] = '127.0.0.1:5111'
app.config['NODE_ADDR'] = {'Host' : '127.0.0.2', 'Port' : 5113}
app.config['NODE_ADDR'] = {'Host': '127.0.0.1', 'Port': 5113}
app.config['BUFFER_SIZE'] = 64 * 1024
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
