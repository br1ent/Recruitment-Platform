<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const email = ref('')
const password = ref('')
const error_message = ref('')
const userStore = useUserStore()
const router = useRouter()

async function handleLogin() {
  error_message.value = ''

  if (!email.value) {
    error_message.value = '邮箱不能为空!'
    return
  }
  if (!password.value) {
    error_message.value = '密码不能为空!'
    return
  }

  try {
    await userStore.login({
      email: email.value, password: password.value
    })
    await router.push({
      name: 'home-index'
    })
  } catch (e) {
    error_message.value = e.message || '登录失败'
  }
}
</script>

<template>
  <div class="flex justify-center align-center mt-30">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <legend class="fieldset-legend text-base">登录</legend>

      <label class="label text-base">邮箱</label>
      <input type="email" class="input" v-model="email" />

      <label class="label text-base">密码</label>
      <input type="password" class="input" v-model="password" />

      <div class="mt-2" v-if="error_message">
        <span class="text-base text-red-500">{{ error_message }}</span>
      </div>

      <button class="btn btn-accent mt-4" @click="handleLogin">登录</button>

      <div class="mt-2">
        <span class="text-sm">还没有账号？点击</span>
        <router-link :to="{ name: 'register-index' }" class="link link-accent link-hover text-sm">注册</router-link>
      </div>
      <div>
        <span class="text-sm">忘记密码了？点击</span>
        <router-link :to="{ name: 'resetpwd-index' }" class="link link-hover link-accent text-sm">忘记密码</router-link>
      </div>
    </fieldset>
  </div>
</template>

<style scoped>

</style>
