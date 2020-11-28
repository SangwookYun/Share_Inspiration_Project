import re

import pandas as pd
from flask import (Flask, abort, request)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

article = pd.read_json('final.json')
article.head(2)


@app.route("/")
def hello():
    return "Share & Inspire Lab3 Homework!"


@app.route('/article/<int:article_id>', methods=['GET'])
def get_article_by_id(article_id):
    result = article[article.id == article_id]
    print(result)

    return result.to_json(orient='records')


@app.route('/articles', methods=["POST"])
def search_articles():
    try:
        if request.method == "POST":
            content = request.json
            keyword = content['keyword'].lower()

            df = pd.DataFrame(article)
            df.columns = article.keys()

            df['text'] = df[['title', 'summary']].apply(lambda x: ''.join(x.fillna('')), axis=1)
            df['frequency'] = df['text'].str.count(keyword, re.I)
            df = df.drop(columns=['text', 'summary'])
            df = df[df.frequency > 0]
            return df.to_json(orient='records')
        else:
            abort([501, "input text required"])
    except IndexError:
        abort(404)


def format_date(x):
    return str(x.left.strftime('%Y-%m'))


@app.route('/statistics', methods=["GET"])
def get_statistics():
    df = pd.DataFrame(article)
    sorted_df = df.sort_values('date')
    sorted_df = sorted_df[sorted_df['date'].notna()]

    bins_dt = pd.date_range(start=sorted_df.iloc[0]['date'], end="now", freq='MS')
    monthly_bins = pd.cut(sorted_df.date, bins=bins_dt)
    monthly_stats = sorted_df.groupby(monthly_bins).size().reset_index(name='count')
    monthly_stats = monthly_stats.query("count>0")
    monthly_stats['date'] = monthly_stats['date'].apply(format_date)
    return monthly_stats.to_json(orient='records')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
