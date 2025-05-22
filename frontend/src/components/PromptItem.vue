<template>
  <el-card class="prompt-card" shadow="hover">
    <template #header>
      <div class="card-header">
        <span>{{ prompt.title }}</span>
        <div>
          <el-button type="primary" :icon="Edit" circle @click="onEdit" size="small" />
          <el-popconfirm
            title="Are you sure to delete this prompt?"
            confirm-button-text="Yes"
            cancel-button-text="No"
            @confirm="onDelete"
          >
            <template #reference>
              <el-button type="danger" :icon="Delete" circle size="small" />
            </template>
          </el-popconfirm>
        </div>
      </div>
    </template>
    <p class="prompt-content">{{ prompt.content }}</p>
    <div class="prompt-footer">
      <el-tag v-if="prompt.category" type="info" size="small" effect="light">
        {{ prompt.category }}
      </el-tag>
      <span v-else></span> <!-- Placeholder for alignment -->
      <small class="timestamp">
        Created: {{ formatDate(prompt.created_at) }}
      </small>
    </div>
  </el-card>
</template>

<script setup lang="ts">
import type { Prompt } from '@/types/prompt';
import { Edit, Delete } from '@element-plus/icons-vue'; // Import icons

interface Props {
  prompt: Prompt;
}
const props = defineProps<Props>();
const emit = defineEmits(['edit', 'delete']);

const onEdit = () => {
  emit('edit', props.prompt);
};

const onDelete = () => {
  emit('delete', props.prompt.id);
};

const formatDate = (dateString: string) => {
  const date = new Date(dateString);
  return date.toLocaleString(); // Adjust formatting as needed
};
</script>

<style scoped>
.prompt-card {
  margin-bottom: 20px;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.card-header span {
  font-weight: bold;
}
.prompt-content {
  white-space: pre-wrap; /* Preserve line breaks in content */
  margin-bottom: 10px;
}
.prompt-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.8em;
  color: #888;
}
.timestamp {
  color: #aaa;
}
</style>
