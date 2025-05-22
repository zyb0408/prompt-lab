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

- **Python** 3.8+
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

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

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

### 运行测试

```bash
# 后端测试
cd backend
python -m pytest

# 前端测试
cd frontend
npm run test
```

### 代码格式化

```bash
# 前端代码格式化
cd frontend
npm run format
npm run lint
```

### 开发工具推荐

- **VS Code** - 推荐的代码编辑器
- **Vue DevTools** - Vue 开发者工具
- **Postman** - API 测试工具

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
