import request from '@/utils/request'

// 查询新闻列表列表
export function listNews(query) {
  return request({
    url: '/system/news/list',
    method: 'get',
    params: query
  })
}

// 查询新闻列表详细
export function getNews(newsID) {
  return request({
    url: '/system/news/' + newsID,
    method: 'get'
  })
}

// 新增新闻列表
export function addNews(data) {
  return request({
    url: '/system/news',
    method: 'post',
    data: data
  })
}

// 修改新闻列表
export function updateNews(data) {
  return request({
    url: '/system/news',
    method: 'put',
    data: data
  })
}

// 删除新闻列表
export function delNews(newsID) {
  return request({
    url: '/system/news/' + newsID,
    method: 'delete'
  })
}
