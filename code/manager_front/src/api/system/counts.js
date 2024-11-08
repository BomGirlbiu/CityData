import request from '@/utils/request'

// 查询纽约时报报道量列表
export function listCounts(query) {
  return request({
    url: '/system/counts/list',
    method: 'get',
    params: query
  })
}

// 查询纽约时报报道量详细
export function getCounts(cityname) {
  return request({
    url: '/system/counts/' + cityname,
    method: 'get'
  })
}

// 新增纽约时报报道量
export function addCounts(data) {
  return request({
    url: '/system/counts',
    method: 'post',
    data: data
  })
}

// 修改纽约时报报道量
export function updateCounts(data) {
  return request({
    url: '/system/counts',
    method: 'put',
    data: data
  })
}

// 删除纽约时报报道量
export function delCounts(cityname) {
  return request({
    url: '/system/counts/' + cityname,
    method: 'delete'
  })
}
