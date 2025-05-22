<template>
  <el-container class="app-container">
    <el-header class="app-header">
      <h1>Prompt Lab</h1>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink> <!-- Example, if you have an About page -->
      </nav>
    </el-header>
    <el-main>
      <RouterView />
    </el-main>
    <el-footer class="app-footer">
      <p>© {{ new Date().getFullYear() }} Prompt Lab. All rights reserved.</p>
    </el-footer>
  </el-container>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background-color: #409EFF; /* Element Plus primary color */
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  line-height: 60px; /* Default header height */
}

.app-header h1 {
  margin: 0;
  font-size: 1.5em;
}

.app-header nav a {
  color: white;
  text-decoration: none;
  margin-left: 15px;
}

.app-header nav a.router-link-exact-active {
  font-weight: bold;
  border-bottom: 2px solid white;
}

.el-main {
  flex-grow: 1; /* Make main content area take up available space */
  padding: 20px;
  background-color: #f4f6f8;
}

.app-footer {
  background-color: #f0f2f5;
  color: #606266;
  text-align: center;
  padding: 10px 0;
  font-size: 0.9em;
  border-top: 1px solid #e0e0e0;
}
</style>
