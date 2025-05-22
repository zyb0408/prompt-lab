<template>
  <div class="prompt-list">
    <PromptItem
      v-for="prompt in prompts"
      :key="prompt.id"
      :prompt="prompt"
      @edit="handleEdit"
      @delete="handleDelete"
    />
    <el-empty v-if="prompts.length === 0" description="No prompts yet. Create one!"></el-empty>
  </div>
</template>

<script setup lang="ts">
import type { Prompt } from '@/types/prompt';
import PromptItem from './PromptItem.vue';

interface Props {
  prompts: Prompt[];
}
defineProps<Props>();

const emit = defineEmits(['editPrompt', 'deletePrompt']);

const handleEdit = (prompt: Prompt) => {
  emit('editPrompt', prompt);
};

const handleDelete = (promptId: number) => {
  emit('deletePrompt', promptId);
};
</script>

<style scoped>
.prompt-list {
  margin-top: 20px;
}
</style>
