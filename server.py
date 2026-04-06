from flask import Flask, request, jsonify
import api

app = Flask(__name__)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/api/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
         驗證必要字段
        required = ['name', 'gender', 'birthdate', 'birthtime', 'location']
        for field in required:
            if not data.get(field):
                return jsonify({'success': False, 'error': f'缺少字段: {field}'}), 400

         調用分析邏輯
        result = api.analyze_birth_data(data)
        return jsonify(result)

    except Exception as e:
        return jsonify({'success': False, 'error': '系統錯誤'}), 500
      @app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'bazi-analyzer'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
