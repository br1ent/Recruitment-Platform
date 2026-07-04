<script setup>

</script>

<template>
  <div class="navbar bg-base-100 shadow-sm">
    <div class="navbar-start">
      <router-link :to="{name: 'home-index'}" class="btn btn-ghost text-xl">Brent的招聘系统</router-link>
    </div>
    <div class="navbar-end">
      <div class="ml-10">
        <router-link :to="{name: 'external-index'}" class="btn btn-ghost text-base font-bold" active-class="btn-active">
          社会招聘
        </router-link>
      </div>
      <div class="ml-10">
        <router-link :to="{name: 'campus-index'}" class="btn btn-ghost text-base font-bold" active-class="btn-active">
          校园招聘
        </router-link>
      </div>
      <div class="ml-10">
        <router-link :to="{name: 'intern-index'}" class="btn btn-ghost text-base font-bold" active-class="btn-active">
          实习生招聘
        </router-link>
      </div>
      <div class="ml-40">
        <router-link :to="{name: 'login-index'}" class="btn text-base font-bold" active-class="btn-active">
          登录
        </router-link>
      </div>
    </div>
  </div>
  <slot></slot>
</template>

<style scoped>

</style>