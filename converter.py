from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])

def home():
    if request.method=="POST":
        deg=eval(request.form['degrees'])
        temp=request.form["temp"]
        if temp=="cf":
            ans = (deg * 1.8) + 32

        if temp=="fc":
            ans = (deg - 32) / 1.8

        return render_template("converter_result.html",**{'ans':ans})
    return render_template("converter.html")


if __name__=="__main__":
    app.run(debug=True)