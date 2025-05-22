export interface Prompt {
  id: number;
  title: string;
  content: string;
  category?: string; // 可选
  created_at: string; // 后端返回的是 ISO 字符串
  updated_at: string; // 后端返回的是 ISO 字符串
}
