from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from models import db, Prompt
import os

app = Flask(__name__)
app.config.from_object(Config)

# 初始化 SQLAlchemy
db.init_app(app)

# 启用 CORS
# CORS(app, resources={r"/api/*": {"origins": "*"}}) # 允许所有来源访问 /api/* 路径
CORS(app, origins=["http://localhost:5173"])
# --- API 路由 ---
@app.route('/api/prompts', methods=['POST'])
def create_prompt():
    data = request.get_json()
    if not data or not 'title' in data or not 'content' in data:
        return jsonify({'message': 'Title and content are required'}), 400

    new_prompt = Prompt(
        title=data['title'],
        content=data['content'],
        category=data.get('category') # .get() 允许 category 为空
    )
    db.session.add(new_prompt)
    db.session.commit()
    return jsonify(new_prompt.to_dict()), 201

@app.route('/api/prompts', methods=['GET'])
def get_prompts():
    prompts = Prompt.query.order_by(Prompt.created_at.desc()).all()
    return jsonify([prompt.to_dict() for prompt in prompts]), 200

@app.route('/api/prompts/<int:prompt_id>', methods=['GET'])
def get_prompt(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    return jsonify(prompt.to_dict()), 200

@app.route('/api/prompts/<int:prompt_id>', methods=['PUT'])
def update_prompt(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    data = request.get_json()

    prompt.title = data.get('title', prompt.title)
    prompt.content = data.get('content', prompt.content)
    prompt.category = data.get('category', prompt.category)

    db.session.commit()
    return jsonify(prompt.to_dict()), 200

@app.route('/api/prompts/<int:prompt_id>', methods=['DELETE'])
def delete_prompt(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    db.session.delete(prompt)
    db.session.commit()
    return jsonify({'message': 'Prompt deleted successfully'}), 200

# 一个简单的健康检查路由
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# --- 数据库初始化命令 ---
@app.cli.command("init-db")
def init_db_command():
    """Creates the database tables."""
    with app.app_context(): # 确保在应用上下文中操作
        db.create_all()
    print("Initialized the database.")

if __name__ == '__main__':
    # 从 .env 文件加载 FLASK_APP 和 FLASK_ENV (如果还没有被外部设置)
    # 这主要用于直接 python app.py 运行，但 flask run 会自动处理
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true': # 避免在 Werkzeug reloader 中重复加载
        from dotenv import load_dotenv
        load_dotenv() # 加载 .env

    app.run(debug=os.environ.get('FLASK_ENV') == 'development', host='0.0.0.0', port=5000)
