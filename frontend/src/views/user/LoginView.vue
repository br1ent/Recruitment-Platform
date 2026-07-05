<script setup>

</script>

<template>
  <div class="flex justify-center align-center mt-30">
    <fieldset class="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
      <legend class="fieldset-legend text-base">登录</legend>

      <label class="label text-base">邮箱</label>
      <input type="email" class="input"/>

      <label class="label text-base">密码</label>
      <input type="password" class="input" />

      <button class="btn btn-neutral mt-4">登录</button>
      <div class="mt-2">
        <span class="text-sm">还没有账号？点击</span>
        <router-link :to="{name: 'register-index'}" class="link link-hover text-sm">注册</router-link>
      </div>
    </fieldset>
  </div>
</template>

<style scoped>

</style>