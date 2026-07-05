import axios from 'axios'
import { getAccessToken, setAccessToken, clearAccessToken } from '@/utils/auth'

const request = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 10000,
})

// 是否正在刷新 token
let isRefreshing = false
// 等待刷新完成的请求队列
let pendingQueue = []

// 请求拦截器：自动添加 access_token
request.interceptors.request.use(
  (config) => {
    const token = getAccessToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

// 响应拦截器：处理 401 自动刷新
request.interceptors.response.use(
  (response) => response.data,
  async (error) => {
    const { response, config } = error

    if (!response) {
      return Promise.reject({ message: '网络错误，请检查网络连接' })
    }

    // 不是 401 或者已经重试过，直接返回错误
    if (response.status !== 401 || config._retry) {
      return Promise.reject(response.data)
    }

    // 刷新 token 请求本身 401，说明 refresh_token 也过期了
    if (config.url === '/api/auth/refresh/') {
      clearAccessToken()
      try {
        await request.post('/api/auth/logout/')
      } catch {}
      return Promise.reject({ message: '登录已过期，请重新登录' })
    }

    // 如果正在刷新，把当前请求挂起到队列
    if (isRefreshing) {
      return new Promise((resolve, reject) => {
        pendingQueue.push({
          onSuccess: (newToken) => {
            config.headers.Authorization = `Bearer ${newToken}`
            resolve(request(config))
          },
          onError: (err) => reject(err),
        })
      })
    }

    // 开始刷新
    isRefreshing = true
    config._retry = true

    try {
      const { data } = await axios.post('http://127.0.0.1:8000/api/auth/refresh/', null, {
        withCredentials: true,
      })

      const newToken = data.access
      setAccessToken(newToken)

      // 执行队列中的请求
      pendingQueue.forEach((cb) => cb.onSuccess(newToken))
      pendingQueue = []

      // 重新发起当前请求
      config.headers.Authorization = `Bearer ${newToken}`
      return request(config)
    } catch {
      // refresh_token 过期，调用后端 logout
      clearAccessToken()
      pendingQueue.forEach((cb) => cb.onError({ message: '登录已过期，请重新登录' }))
      pendingQueue = []
      try {
        await axios.post('http://127.0.0.1:8000/api/auth/logout/', null, {
          withCredentials: true,
        })
      } catch {}
      return Promise.reject({ message: '登录已过期，请重新登录' })
    } finally {
      isRefreshing = false
    }
  }
)

export default request
