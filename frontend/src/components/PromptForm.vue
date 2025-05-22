<template>
  <el-form :model="form" ref="promptFormRef" :rules="rules" label-width="120px">
    <el-form-item label="Title" prop="title">
      <el-input v-model="form.title" placeholder="Enter prompt title" />
    </el-form-item>
    <el-form-item label="Content" prop="content">
      <el-input v-model="form.content" type="textarea" :rows="5" placeholder="Enter prompt content" />
    </el-form-item>
    <el-form-item label="Category" prop="category">
      <el-input v-model="form.category" placeholder="Enter category (optional)" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm">
        {{ mode === 'create' ? 'Create' : 'Update' }}
      </el-button>
      <el-button @click="resetForm">Reset</el-button>
      <el-button v-if="mode === 'edit'" @click="cancelEdit" type="info" plain>Cancel Edit</el-button>
    </el-form-item>
  </el-form>
</template>

<script setup lang="ts">
import { ref, reactive, watch, onMounted } from 'vue';
import type { FormInstance, FormRules } from 'element-plus';
import { ElMessage } from 'element-plus';
import type { Prompt, PromptCreatePayload, PromptUpdatePayload } from '@/types/prompt';

interface Props {
  mode: 'create' | 'edit';
  promptToEdit?: Prompt | null; // For edit mode
}

const props = withDefaults(defineProps<Props>(), {
  mode: 'create',
  promptToEdit: null,
});

const emit = defineEmits(['promptCreated', 'promptUpdated', 'cancelEdit']);

const promptFormRef = ref<FormInstance>();

const initialFormState = (): PromptCreatePayload => ({
  title: '',
  content: '',
  category: '',
});

const form = reactive<PromptCreatePayload | PromptUpdatePayload>(initialFormState());

const rules = reactive<FormRules>({
  title: [{ required: true, message: 'Please input title', trigger: 'blur' }],
  content: [{ required: true, message: 'Please input content', trigger: 'blur' }],
});

watch(() => props.promptToEdit, (newVal) => {
  if (props.mode === 'edit' && newVal) {
    form.title = newVal.title;
    form.content = newVal.content;
    form.category = newVal.category || '';
  } else {
    resetFormFields();
  }
}, { immediate: true });


const resetFormFields = () => {
  const initial = initialFormState();
  form.title = initial.title;
  form.content = initial.content;
  form.category = initial.category;
  promptFormRef.value?.clearValidate();
};

const submitForm = async () => {
  if (!promptFormRef.value) return;
  await promptFormRef.value.validate((valid) => {
    if (valid) {
      if (props.mode === 'create') {
        emit('promptCreated', { ...form });
      } else if (props.mode === 'edit' && props.promptToEdit) {
        // Only send changed fields for update if desired, or send all
        const payload: PromptUpdatePayload = {};
        if (form.title !== props.promptToEdit.title) payload.title = form.title;
        if (form.content !== props.promptToEdit.content) payload.content = form.content;
        if (form.category !== (props.promptToEdit.category || '')) payload.category = form.category;

        // If no changes, perhaps don't emit or emit with a flag
        // For simplicity, we'll emit even if no changes if they hit update.
        // Or, we can check if Object.keys(payload).length > 0
        emit('promptUpdated', { ...form }); // Send the whole form for simplicity now
      }
      resetFormFields();
    } else {
      ElMessage.error('Please correct the errors in the form.');
      return false;
    }
  });
};

const resetForm = () => {
  resetFormFields();
  promptFormRef.value?.clearValidate();
};

const cancelEdit = () => {
  emit('cancelEdit');
  resetForm();
}

onMounted(() => {
  if (props.mode === 'edit' && props.promptToEdit) {
    form.title = props.promptToEdit.title;
    form.content = props.promptToEdit.content;
    form.category = props.promptToEdit.category || '';
  }
})

</script>

<style scoped>
.el-form {
  max-width: 600px;
  margin: 20px auto;
}
</style>
