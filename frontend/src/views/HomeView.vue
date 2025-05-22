<template>
  <div class="home-view">
    <el-row :gutter="20">
      <el-col :md="formVisible ? 10 : 24" :sm="24">
         <div class="controls-header">
            <h2>{{ currentEditingPrompt ? 'Edit Prompt' : 'Create New Prompt' }}</h2>
            <el-button v-if="!formVisible && !currentEditingPrompt" @click="showCreateForm" type="primary" :icon="Plus">
                Add New Prompt
            </el-button>
         </div>

        <PromptForm
          v-if="formVisible || currentEditingPrompt"
          :mode="currentEditingPrompt ? 'edit' : 'create'"
          :prompt-to-edit="currentEditingPrompt"
          @prompt-created="handlePromptCreated"
          @prompt-updated="handlePromptUpdated"
          @cancel-edit="handleCancelEdit"
        />
      </el-col>
      <el-col :md="formVisible ? 14 : 24" :sm="24">
        <h2>Prompt List</h2>
        <el-input
          v-model="searchTerm"
          placeholder="Search prompts by title or content..."
          clearable
          class="search-input"
          :prefix-icon="Search"
        />
        <el-skeleton :rows="5" animated v-if="loading" />
        <PromptList
          v-else
          :prompts="filteredPrompts"
          @edit-prompt="startEditPrompt"
          @delete-prompt="handleDeletePrompt"
        />
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { Plus, Search } from '@element-plus/icons-vue';
import PromptForm from '@/components/PromptForm.vue';
import PromptList from '@/components/PromptList.vue';
import * as api from '@/services/api';
import type { Prompt, PromptCreatePayload, PromptUpdatePayload } from '@/types/prompt';

const prompts = ref<Prompt[]>([]);
const loading = ref(true);
const currentEditingPrompt = ref<Prompt | null>(null);
const formVisible = ref(false); // To control create form visibility
const searchTerm = ref('');

const fetchPrompts = async () => {
  loading.value = true;
  try {
    prompts.value = await api.getPrompts();
  } catch (error) {
    console.error('Failed to fetch prompts:', error);
    ElMessage.error('Failed to load prompts.');
  } finally {
    loading.value = false;
  }
};

const handlePromptCreated = async (payload: PromptCreatePayload) => {
  try {
    await api.createPrompt(payload);
    ElMessage.success('Prompt created successfully!');
    fetchPrompts(); // Refresh list
    formVisible.value = false; // Hide create form
  } catch (error) {
    console.error('Failed to create prompt:', error);
    ElMessage.error('Failed to create prompt.');
  }
};

const handlePromptUpdated = async (payload: PromptUpdatePayload) => {
  if (!currentEditingPrompt.value) return;
  try {
    await api.updatePrompt(currentEditingPrompt.value.id, payload);
    ElMessage.success('Prompt updated successfully!');
    currentEditingPrompt.value = null; // Exit edit mode
    fetchPrompts(); // Refresh list
  } catch (error) {
    console.error('Failed to update prompt:', error);
    ElMessage.error('Failed to update prompt.');
  }
};

const startEditPrompt = (prompt: Prompt) => {
  currentEditingPrompt.value = { ...prompt }; // Create a copy to edit
  formVisible.value = false; // Ensure create form is hidden if it was open
  window.scrollTo({ top: 0, behavior: 'smooth' }); // Scroll to top
};

const handleCancelEdit = () => {
    currentEditingPrompt.value = null;
}

const showCreateForm = () => {
    currentEditingPrompt.value = null; // Ensure not in edit mode
    formVisible.value = true;
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

const handleDeletePrompt = async (promptId: number) => {
  ElMessageBox.confirm(
    'This will permanently delete the prompt. Continue?',
    'Warning',
    {
      confirmButtonText: 'OK',
      cancelButtonText: 'Cancel',
      type: 'warning',
    }
  )
    .then(async () => {
      try {
        await api.deletePrompt(promptId);
        ElMessage.success('Prompt deleted successfully!');
        fetchPrompts(); // Refresh list
        if (currentEditingPrompt.value && currentEditingPrompt.value.id === promptId) {
          currentEditingPrompt.value = null; // Clear edit form if deleting the item being edited
        }
      } catch (error) {
        console.error('Failed to delete prompt:', error);
        ElMessage.error('Failed to delete prompt.');
      }
    })
    .catch(() => {
      // User cancelled
    });
};

const filteredPrompts = computed(() => {
  if (!searchTerm.value) {
    return prompts.value;
  }
  const lowerSearchTerm = searchTerm.value.toLowerCase();
  return prompts.value.filter(prompt =>
    prompt.title.toLowerCase().includes(lowerSearchTerm) ||
    prompt.content.toLowerCase().includes(lowerSearchTerm) ||
    (prompt.category && prompt.category.toLowerCase().includes(lowerSearchTerm))
  );
});

onMounted(() => {
  fetchPrompts();
});
</script>

<style scoped>
.home-view {
  padding: 20px;
}
.controls-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}
.search-input {
  margin-bottom: 20px;
}
</style>
