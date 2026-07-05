<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goHome = () => router.push('/home')
const goBack = () => router.back()
</script>

<template>
  <div class="min-h-[80vh] flex flex-col items-center justify-center px-4">
    <!-- 404 视觉主体 -->
    <div class="relative mb-8">
      <span class="text-[10rem] font-black text-base-200 select-none leading-none">404</span>
      <!-- 搜索图标覆盖在文字中间 -->
      <div class="absolute inset-0 flex items-center justify-center">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-24 w-24 text-primary/70"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="1.5"
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
      </div>
    </div>

    <!-- 文字说明 -->
    <h1 class="text-3xl font-bold">页面走丢了</h1>
    <p class="mt-3 text-base-content/50 max-w-md text-center leading-relaxed">
      抱歉，您访问的页面不存在、已被移除或地址输入有误。请检查链接是否正确，或返回首页继续浏览。
    </p>

    <!-- 操作按钮 -->
    <div class="mt-10 flex flex-wrap gap-4 justify-center">
      <button class="btn btn-outline gap-2" @click="goBack">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        返回上一页
      </button>
      <button class="btn btn-primary gap-2" @click="goHome">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
        </svg>
        回到首页
      </button>
    </div>

    <!-- 快捷入口 -->
    <div class="mt-12 text-sm text-base-content/40">
      你也可以访问：
      <router-link class="link link-primary mx-1" :to="{ name: 'external-index' }">社会招聘</router-link>
      <router-link class="link link-primary mx-1" :to="{ name: 'campus-index' }">校园招聘</router-link>
      <router-link class="link link-primary mx-1" :to="{ name: 'intern-index' }">实习生招聘</router-link>
    </div>
  </div>
</template>

<style scoped>
</style>
