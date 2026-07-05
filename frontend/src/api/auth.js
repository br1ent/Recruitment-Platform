import request from '@/utils/request'

// 登录
export function login(data) {
  return request.post('/api/auth/login/', data)
}

// 注册
export function register(data) {
  return request.post('/api/auth/register/', data)
}

// 重置密码
export function resetPassword(data) {
  return request.post('/api/auth/resetpwd/', data)
}

// 获取用户信息
export function getUserInfo() {
  return request.get('/api/auth/get_info/')
}

// 登出
export function logout() {
  return request.post('/api/auth/logout/')
}
