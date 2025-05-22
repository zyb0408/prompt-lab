# Prompt Lab

一个现代化的 AI 提示词管理平台，帮助您组织、管理和优化您的 AI 提示词库。

## 📋 项目简介

Prompt Lab 是一个全栈 Web 应用，专为 AI 从业者、研究人员和爱好者设计，用于高效管理和组织各种 AI 提示词。通过直观的界面，您可以轻松创建、编辑、分类和搜索您的提示词集合。

### ✨ 主要特性

- 🎯 **提示词管理**: 创建、编辑、删除和组织您的 AI 提示词
- 🔍 **智能搜索**: 支持按标题、内容和分类进行实时搜索
- 📂 **分类管理**: 为提示词添加分类标签，便于组织
- 📱 **响应式设计**: 完美适配桌面端和移动端设备
- ⚡ **实时更新**: 即时保存和同步您的更改
- 🎨 **现代化 UI**: 基于 Element Plus 的美观界面

## 🛠 技术栈

### 后端

- **Flask** - 轻量级 Python Web 框架
- **SQLAlchemy** - Python SQL 工具包和 ORM
- **MySQL** - 关系型数据库
- **Flask-CORS** - 跨域资源共享支持
- **python-dotenv** - 环境变量管理

### 前端

- **Vue 3** - 渐进式 JavaScript 框架
- **TypeScript** - 类型安全的 JavaScript 超集
- **Element Plus** - Vue 3 组件库
- **Vite** - 现代化前端构建工具
- **Pinia** - Vue 状态管理
- **Vue Router** - Vue 官方路由管理器
- **Axios** - HTTP 客户端

## 📁 项目结构

```
prompt-lab/
├── backend/                 # Flask后端应用
│   ├── app.py              # 主应用文件
│   ├── models.py           # 数据模型
│   ├── config.py           # 配置文件
│   ├── requirements.txt    # Python依赖
│   └── .env               # 环境变量
├── frontend/               # Vue前端应用
│   ├── src/
│   │   ├── components/     # Vue组件
│   │   ├── views/         # 页面视图
│   │   ├── services/      # API服务
│   │   ├── types/         # TypeScript类型定义
│   │   └── router/        # 路由配置
│   ├── package.json       # Node.js依赖
│   ├── .env.development   # 开发环境配置
│   └── .env.production    # 生产环境配置
└── README.md              # 项目文档
```

## 🚀 快速开始

### 环境要求

- **Python** 3.10+ (推荐使用 3.10)
- **uv** - 现代 Python 包管理器 (推荐) 或 **pip**
- **Node.js** 16+
- **MySQL** 5.7+ 或 8.0+
- **npm** 或 **yarn**

### 1. 克隆项目

```bash
git clone <repository-url>
cd prompt-lab
```

### 2. 数据库设置

#### 创建 MySQL 数据库和用户

```sql
-- 连接到MySQL
mysql -u root -p

-- 创建数据库
CREATE DATABASE prompt_lab_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 创建用户并授权
CREATE USER 'prompt_lab_user'@'localhost' IDENTIFIED BY 'your_strong_password';
GRANT ALL PRIVILEGES ON prompt_lab_db.* TO 'prompt_lab_user'@'localhost';
FLUSH PRIVILEGES;
```

### 3. 后端设置

```bash
# 进入后端目录
cd backend

# 安装uv（如果尚未安装）
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows: 下载安装程序或使用 pip install uv

# 使用uv创建Python 3.10虚拟环境
uv venv --python 3.10 venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 使用uv安装依赖
uv pip install -r requirements.txt

# 配置环境变量
cp .env.example .env  # 如果有示例文件
# 或直接编辑 .env 文件，设置数据库连接信息

# 初始化数据库
flask init-db

# 启动后端服务
python app.py
```

后端服务将在 `http://localhost:5000` 启动

### 4. 前端设置

```bash
# 打开新终端，进入前端目录
cd frontend

# 安装依赖
npm install
# 或使用 yarn
yarn install

# 启动开发服务器
npm run dev
# 或使用 yarn
yarn dev
```

前端应用将在 `http://localhost:5173` 启动

### 5. 访问应用

打开浏览器访问 `http://localhost:5173`，开始使用 Prompt Lab！

## ⚙️ 配置说明

### 后端配置 (backend/.env)

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
SQLALCHEMY_DATABASE_URI=mysql+pymysql://prompt_lab_user:your_strong_password@localhost/prompt_lab_db
```

### 前端配置

#### 开发环境 (frontend/.env.development)

```env
VITE_API_BASE_URL=http://127.0.0.1:5000/api
```

#### 生产环境 (frontend/.env.production)

```env
VITE_API_BASE_URL=/api
```

## 📖 API 文档

### 提示词相关接口

| 方法   | 端点                | 描述           |
| ------ | ------------------- | -------------- |
| GET    | `/api/prompts`      | 获取所有提示词 |
| POST   | `/api/prompts`      | 创建新提示词   |
| GET    | `/api/prompts/{id}` | 获取指定提示词 |
| PUT    | `/api/prompts/{id}` | 更新指定提示词 |
| DELETE | `/api/prompts/{id}` | 删除指定提示词 |

### 数据模型

```typescript
interface Prompt {
  id: number;
  title: string;
  content: string;
  category?: string;
  created_at: string;
  updated_at: string;
}
```

## 🏗 生产部署

### 使用 Docker 部署

1. **创建 Dockerfile (后端)**

```dockerfile
# backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

2. **创建 Dockerfile (前端)**

```dockerfile
# frontend/Dockerfile
FROM node:16-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

3. **创建 docker-compose.yml**

```yaml
version: "3.8"

services:
  mysql:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: prompt_lab_db
      MYSQL_USER: prompt_lab_user
      MYSQL_PASSWORD: your_strong_password
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"

  backend:
    build: ./backend
    environment:
      SQLALCHEMY_DATABASE_URI: mysql+pymysql://prompt_lab_user:your_strong_password@mysql/prompt_lab_db
      FLASK_ENV: production
    depends_on:
      - mysql
    ports:
      - "5000:5000"

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  mysql_data:
```

### 传统部署

1. **后端部署**

   - 使用 Gunicorn 作为 WSGI 服务器
   - 配置 Nginx 作为反向代理
   - 设置 SSL 证书

2. **前端部署**
   - 构建生产版本：`npm run build`
   - 将 dist 目录部署到 Web 服务器
   - 配置路由重定向

## 🧪 开发指南

### 本地开发环境运行

#### 后端开发运行

```bash
# 1. 进入后端目录
cd backend

# 2. 安装uv（如果尚未安装）
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# 或使用pip安装:
pip install uv

# Windows:
# 下载并运行安装程序: https://github.com/astral-sh/uv/releases
# 或使用pip安装:
pip install uv

# 3. 使用uv创建Python 3.10虚拟环境（首次运行）
uv venv --python 3.10 venv

# 4. 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 5. 使用uv安装依赖
uv pip install -r requirements.txt

# 6. 设置环境变量（开发模式）
export FLASK_APP=app.py
export FLASK_ENV=development
# Windows CMD:
# set FLASK_APP=app.py
# set FLASK_ENV=development

# 7. 初始化数据库（首次运行）
flask init-db

# 8. 启动开发服务器
# 方式1: 使用Flask命令
flask run --host=0.0.0.0 --port=5000

# 方式2: 直接运行Python文件
python app.py

# 9. 查看服务状态
# 访问健康检查接口: http://localhost:5000/health
```

#### 前端开发运行

```bash
# 1. 进入前端目录
cd frontend

# 2. 安装依赖（首次运行或package.json更新后）
npm install
# 或使用yarn
yarn install

# 3. 启动开发服务器
npm run dev
# 或使用yarn
yarn dev

# 4. 构建生产版本（可选）
npm run build
# 或使用yarn
yarn build

# 5. 预览生产构建（可选）
npm run preview
# 或使用yarn
yarn preview
```

#### 同时运行前后端

**推荐方式：使用两个终端窗口**

```bash
# 终端1 - 启动后端
cd backend
source venv/bin/activate  # macOS/Linux
# 或 venv\Scripts\activate  # Windows
python app.py

# 终端2 - 启动前端
cd frontend
npm run dev
```

**使用并发运行工具（可选）**

```bash
# 安装并发运行工具
npm install -g concurrently

# 在项目根目录创建启动脚本
# package.json 中添加:
{
  "scripts": {
    "dev": "concurrently \"cd backend && python app.py\" \"cd frontend && npm run dev\""
  }
}

# 然后运行
npm run dev
```

### 开发环境配置

#### 后端环境变量 (backend/.env)

```env
# 开发环境配置
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=dev-secret-key-change-in-production

# 数据库配置
SQLALCHEMY_DATABASE_URI=mysql+pymysql://prompt_lab_user:your_password@localhost/prompt_lab_db

# 可选：启用SQL查询日志
SQLALCHEMY_ECHO=True
```

#### 前端环境变量 (frontend/.env.local)

```env
# 本地开发覆盖配置（优先级最高）
VITE_API_BASE_URL=http://127.0.0.1:5000/api
VITE_APP_TITLE=Prompt Lab (Dev)
```

### 开发调试技巧

#### 后端调试

```bash
# 1. 启用Flask调试模式
export FLASK_DEBUG=1
flask run

# 2. 使用Python调试器
python -m pdb app.py

# 3. 查看数据库内容
flask shell
>>> from models import db, Prompt
>>> Prompt.query.all()

# 4. 重置数据库
flask init-db
```

#### 前端调试

```bash
# 1. 启用详细日志
npm run dev -- --debug

# 2. 类型检查
npm run type-check

# 3. 代码检查
npm run lint

# 4. 查看构建分析
npm run build -- --analyze
```

### 热重载说明

- **后端**: Flask 开发服务器支持热重载，修改 Python 文件后自动重启
- **前端**: Vite 提供快速热重载，修改 Vue 文件后即时更新浏览器

### 常用开发命令

#### 后端常用命令

```bash
# 查看所有Flask命令
flask --help

# 查看路由
flask routes

# 进入Flask Shell
flask shell

# 数据库迁移（如果使用Flask-Migrate）
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

#### 前端常用命令

```bash
# 查看所有可用脚本
npm run

# 安装新依赖
npm install package-name
npm install -D package-name  # 开发依赖

# 更新依赖
npm update

# 检查依赖安全性
npm audit
npm audit fix
```

### 运行测试

```bash
# 后端测试
cd backend
python -m pytest
python -m pytest -v  # 详细输出
python -m pytest tests/test_api.py  # 运行特定测试文件

# 前端测试
cd frontend
npm run test
npm run test:unit  # 单元测试
npm run test:e2e   # 端到端测试（如果配置了）
```

### 代码格式化

```bash
# 前端代码格式化
cd frontend
npm run format      # 格式化代码
npm run lint        # 检查代码规范
npm run lint:fix    # 自动修复代码规范问题

# 后端代码格式化（推荐安装black和flake8）
cd backend
pip install black flake8
black .             # 格式化Python代码
flake8 .           # 检查代码规范
```

### 开发工具推荐

- **VS Code** - 推荐的代码编辑器
  - 推荐插件：Python, Vue Language Features (Volar), TypeScript Vue Plugin
- **Vue DevTools** - Vue 开发者工具
- **Postman** - API 测试工具
- **MySQL Workbench** - 数据库管理工具
- **Git** - 版本控制工具

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 🆘 故障排除

### 常见问题

1. **数据库连接失败**

   - 检查 MySQL 服务是否启动
   - 验证数据库连接信息
   - 确认用户权限设置

2. **前端无法连接后端**

   - 检查后端服务是否运行在正确端口
   - 验证 CORS 配置
   - 检查防火墙设置

3. **依赖安装失败**
   - 更新 npm/pip 到最新版本
   - 清除缓存：`npm cache clean --force`
   - 使用国内镜像源

### 获取帮助

- 查看 [Issues](../../issues) 页面
- 提交新的问题报告
- 联系项目维护者

## 📊 项目状态

- ✅ 基础 CRUD 功能
- ✅ 搜索和过滤
- ✅ 响应式设计
- 🔄 用户认证系统 (开发中)
- 🔄 批量操作功能 (计划中)
- 🔄 导入/导出功能 (计划中)

---

**Prompt Lab** - 让 AI 提示词管理变得简单高效！ 🚀
