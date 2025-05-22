import axios from 'axios';
import type { Prompt } from '@/types/prompt';

// 从环境变量读取 API 基础 URL
// Vite 中环境变量以 VITE_ 开头
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// --- Prompt API ---
export const getPrompts = (): Promise<Prompt[]> => {
  return apiClient.get('/prompts').then(response => response.data);
};

export const getPromptById = (id: number): Promise<Prompt> => {
  return apiClient.get(`/prompts/${id}`).then(response => response.data);
};

// Omit<Type, Keys> 用于创建一个新类型，该类型排除了原始 Type 中的某些 Keys
// 这里我们排除了 id, created_at, updated_at，因为这些通常由后端生成或管理
export type PromptCreatePayload = Omit<Prompt, 'id' | 'created_at' | 'updated_at'>;
export const createPrompt = (data: PromptCreatePayload): Promise<Prompt> => {
  return apiClient.post('/prompts', data).then(response => response.data);
};

export type PromptUpdatePayload = Partial<Omit<Prompt, 'id' | 'created_at' | 'updated_at'>>;
export const updatePrompt = (id: number, data: PromptUpdatePayload): Promise<Prompt> => {
  return apiClient.put(`/prompts/${id}`, data).then(response => response.data);
};

export const deletePrompt = (id: number): Promise<{ message: string }> => {
  return apiClient.delete(`/prompts/${id}`).then(response => response.data);
};
