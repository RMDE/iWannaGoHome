// 设置cookie
export function setCookie (cookieName, value) {
  let date = new Date()
  date.setSeconds(date.getSeconds() + 1800)
  document.cookie = cookieName + '=' + escape(value) + '; expires=' + date.toUTCString() + '; path=/'
}

// 获取cookie
export function getCookie (cookieName) {
  if (document.cookie.length > 0) {
    let start = document.cookie.indexOf(cookieName + '=')
    if (start !== -1) {
      start = start + cookieName.length + 1
      let end = document.cookie.indexOf(';', start)
      if (end === -1) end = document.cookie.length
      return unescape(document.cookie.substring(start, end))
    }
  }
  return ''
}

/* 删除cookie */
export function delCookie (cookieName) {
  setCookie(cookieName, '', -1)
}
