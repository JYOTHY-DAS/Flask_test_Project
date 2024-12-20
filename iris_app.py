from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def iris_app():
    return render_template('iris.html')
@app.route('/result', methods=['POST'])
def result_page():
    sl=request.form['sl']
    sw=request.form['sw']
    pl=request.form['pl']
    pw=request.form['pw'] 
    
    file_name= 'iris_model.pkl'
    with open(path.join("static", file_name), 'rb') as f:
        iris_model = pickle.load(f)

    pred=iris_model.predict(np.array([[sl,sw,pl,pw]]))[0] 
    return render_template('result.html',prediction=pred)
if __name__ == '__main__':
    app.run(debug = True)