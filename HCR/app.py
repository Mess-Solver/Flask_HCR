import os

from flask import Flask, render_template, request,redirect

from ocr_core import ocr_core


UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/proceed', methods=["GET","POST"])
def proceed():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
       return redirect("upload.html")

@app.route('/preview', methods=['GET', 'POST'])
def preview_page():
    if request.method == 'POST':
        file = request.files['file']
        lang=request.form['lang']
        if file and allowed_file(file.filename):
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))


            extracted_text = ocr_core(file,lang)
            #extracted_text=extracted_text,
            # extract the text and display it
            return render_template('preview.html', msg='Successfully Uploaded',img_src=UPLOAD_FOLDER + file.filename,extracted_text=extracted_text)
    elif request.method == 'GET':
        return render_template('upload.html')


@app.route('/loading', methods=['GET', 'POST'])

def loading():
    file = request.files['file']
    return render_template('loading.html',file=file)

@app.route('/success', methods=['GET', 'POST'])
def success():
    file = request.files['file']
    extracted_text = ocr_core(file)
    return render_template('success.html',msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)

if __name__ == '__main__':
    app.run()

