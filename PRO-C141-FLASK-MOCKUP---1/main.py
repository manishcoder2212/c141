from flask import Flask,jsonify,request
import csv

all_articles=[]

liked_articles=[]
disliked_articles=[]

with open('articles.csv',encoding="utf8") as f:
    csvreader=csv.reader(f)
    data=list(csvreader)
    all_articles=data[1:]
    
app=Flask(__name__)

@app.route('/get-articles')
def get_articles():
    return jsonify(
        {
            "data":all_articles,
            "status":"success"
        }
    )

@app.route('/liked-movie',methods=['POST'])
def liked_movie():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    },201)
    
@app.route('/disliked-movie',methods=['POST'])
def disliked_movie():
    article=all_articles[0]
    all_articles=all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        "status":"success"
    },201)
    
if(__name__=="__main__"):
    app.run()