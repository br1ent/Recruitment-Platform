// access_token 仅存在内存中，页面刷新后丢失，需要用 refresh_token 重新获取
let accessToken = null

export function setAccessToken(token) {
  accessToken = token
}

export function getAccessToken() {
  return accessToken
}

export function clearAccessToken() {
  accessToken = null
}
