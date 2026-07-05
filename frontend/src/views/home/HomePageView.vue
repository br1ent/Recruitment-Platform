<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const jobCategories = [
  {
    title: '社会招聘',
    description: '面向有工作经验的专业人士，寻找更广阔的职业发展平台。',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>`,
    route: 'external-index',
    color: 'bg-primary/10 text-primary',
  },
  {
    title: '校园招聘',
    description: '面向应届毕业生，开启职业生涯的第一步，与企业共同成长。',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path d="M12 14l9-5-9-5-9 5 9 5z" /><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14zm-4 6v-7.5l4-2.222" /></svg>`,
    route: 'campus-index',
    color: 'bg-secondary/10 text-secondary',
  },
  {
    title: '实习生招聘',
    description: '面向在校学生，提供实践机会，积累宝贵的工作经验。',
    icon: `<svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" /></svg>`,
    route: 'intern-index',
    color: 'bg-accent/10 text-accent',
  },
]

const stats = [
  { label: '在招职位', value: '120+' },
  { label: '已录用人数', value: '3000+' },
  { label: '合作院校', value: '50+' },
  { label: '员工满意度', value: '95%' },
]

const advantages = [
  { title: '有竞争力的薪酬', desc: '提供行业领先的薪资待遇和绩效奖金。' },
  { title: '完善的福利体系', desc: '五险一金、带薪年假、节日福利、健康体检。' },
  { title: '广阔的成长空间', desc: '完善的培训体系和清晰的晋升通道。' },
  { title: '开放的团队氛围', desc: '扁平化管理，鼓励创新和自我表达。' },
]
</script>

<template>
  <div class="min-h-screen">
    <!-- Hero -->
    <section class="hero min-h-[70vh] bg-gradient-to-br from-primary/5 via-base-100 to-secondary/5">
      <div class="hero-content text-center">
        <div class="max-w-2xl">
          <h1 class="text-5xl font-bold">加入我们，共创未来</h1>
          <p class="py-6 text-lg text-base-content/70">
            我们正在寻找充满激情和创造力的人才。无论你是经验丰富的专业人士还是刚刚步入职场的新人，这里都有属于你的舞台。
          </p>
          <div class="flex gap-4 justify-center">
            <router-link :to="{ name: 'external-index' }" class="btn btn-primary btn-lg">
              浏览职位
            </router-link>
            <router-link :to="{ name: 'register-index' }" class="btn btn-outline btn-lg">
              立即注册
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- 招聘分类 -->
    <section class="py-20 px-4 max-w-6xl mx-auto">
      <h2 class="text-3xl font-bold text-center mb-4">招聘通道</h2>
      <p class="text-center text-base-content/60 mb-12">选择适合你的招聘通道，开启职业新篇章</p>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div
          v-for="cat in jobCategories"
          :key="cat.route"
          class="card bg-base-100 shadow-md hover:shadow-xl transition-shadow cursor-pointer border border-base-200"
          @click="router.push({ name: cat.route })"
        >
          <div class="card-body items-center text-center">
            <div :class="['rounded-2xl p-4 mb-4', cat.color]" v-html="cat.icon"></div>
            <h3 class="card-title text-xl">{{ cat.title }}</h3>
            <p class="text-base-content/60 text-sm">{{ cat.description }}</p>
            <div class="card-actions mt-4">
              <span class="link link-primary text-sm font-medium">了解更多 →</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 数据展示 -->
    <section class="py-16 bg-base-200">
      <div class="max-w-6xl mx-auto px-4">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div v-for="s in stats" :key="s.label">
            <div class="text-4xl font-bold text-primary">{{ s.value }}</div>
            <div class="mt-2 text-sm text-base-content/60">{{ s.label }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- 我们的优势 -->
    <section class="py-20 px-4 max-w-6xl mx-auto">
      <h2 class="text-3xl font-bold text-center mb-4">为什么选择我们</h2>
      <p class="text-center text-base-content/60 mb-12">我们为每一位员工提供最好的工作体验</p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div v-for="a in advantages" :key="a.title" class="flex gap-4 p-6 rounded-2xl bg-base-100 border border-base-200">
          <div class="flex-shrink-0 mt-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-success" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <div>
            <h3 class="font-semibold text-lg">{{ a.title }}</h3>
            <p class="text-base-content/60 text-sm mt-1">{{ a.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-16 bg-primary text-primary-content text-center">
      <div class="max-w-2xl mx-auto px-4">
        <h2 class="text-3xl font-bold">准备好加入我们了吗？</h2>
        <p class="mt-4 text-primary-content/80">立即注册账号，投递简历，开启你的职业旅程。</p>
        <div class="mt-8 flex gap-4 justify-center">
          <router-link :to="{ name: 'register-index' }" class="btn btn-lg bg-white text-primary border-none hover:bg-white/90">
            免费注册
          </router-link>
          <router-link :to="{ name: 'campus-index' }" class="btn btn-lg btn-outline text-white border-white hover:bg-white/10">
            浏览校招岗位
          </router-link>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer footer-center p-10 bg-base-200 text-base-content">
      <aside>
        <p class="font-bold text-lg">Brent的招聘系统</p>
        <p>Copyright © 2026 — All rights reserved</p>
      </aside>
    </footer>
  </div>
</template>

<style scoped>
</style>
