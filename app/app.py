from flask import Flask, request, jsonify 
import praw

app = Flask(__name__)
reddit = praw.Reddit('bot1')

@app.route('/get_post_info', methods=['POST'])
def get_post_info():
    data = request.get_json()
    post_id = data.get('post_id')

    if post_id:
        try:
            submission = reddit.submission(id=post_id)
            title = submission.title
            contents = submission.selftext
            return jsonify({'title': title, 'contents': contents})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'Invalid post_id'})
    
if __name__ == '__main__':
    app.run(port=5000)