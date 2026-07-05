import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import request from '@/utils/request'
import { setAccessToken, clearAccessToken } from '@/utils/auth'

export const useUserStore = defineStore('user', () => {
  // 用户信息
  const userId = ref(null)
  const username = ref('')
  const email = ref('')
  const phone = ref('')
  const avatar = ref('')
  const resume = ref('')
  const role = ref('')
  const status = ref('')

  // 是否已登录
  const isLoggedIn = computed(() => !!userId.value)

  // 是否是 HR
  const isHR = computed(() => role.value === 'hr_admin')

  // 登录
  async function login(form) {
    const res = await request.post('/api/auth/login/', form)
    if (res.message !== 'success') {
      throw new Error(res.message)
    }
    setAccessToken(res.access_token)
    userId.value = res.user_id
    email.value = res.email
    phone.value = res.phone
    avatar.value = res.avatar
    resume.value = res.resume
    role.value = res.role
    status.value = res.status
    return res
  }

  // 获取用户信息（用于刷新页面后恢复状态）
  async function fetchUserInfo() {
    const res = await request.get('/api/auth/get_info/')
    userId.value = res.user_id
    username.value = res.username
    email.value = res.email
    phone.value = res.phone
    avatar.value = res.avatar
    resume.value = res.resume
    role.value = res.role
    status.value = res.status
    return res
  }

  // 登出
  async function logout() {
    try {
      await request.post('/api/auth/logout/')
    } catch {}
    clearState()
  }

  // 清除状态
  function clearState() {
    clearAccessToken()
    userId.value = null
    username.value = ''
    email.value = ''
    phone.value = ''
    avatar.value = ''
    resume.value = ''
    role.value = ''
    status.value = ''
  }

  return {
    userId, username, email, phone, avatar, resume, role, status,
    isLoggedIn, isHR,
    login, fetchUserInfo, logout, clearState,
  }
})
