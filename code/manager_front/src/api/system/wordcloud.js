import request from '@/utils/request'

// 查询词云列表
export function listWordcloud(query) {
  return request({
    url: '/system/wordcloud/list',
    method: 'get',
    params: query
  })
}

// 查询词云详细
export function getWordcloud(cityName) {
  return request({
    url: '/system/wordcloud/' + cityName,
    method: 'get'
  })
}

// 新增词云
export function addWordcloud(data) {
  return request({
    url: '/system/wordcloud',
    method: 'post',
    data: data
  })
}

// 修改词云
export function updateWordcloud(data) {
  return request({
    url: '/system/wordcloud',
    method: 'put',
    data: data
  })
}

// 删除词云
export function delWordcloud(cityName) {
  return request({
    url: '/system/wordcloud/' + cityName,
    method: 'delete'
  })
}
