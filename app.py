from flask import Flask, render_template

app = Flask('__name__')

#put site content here
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def notebook():
    return render_template('Scraping_Itch_2.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True)