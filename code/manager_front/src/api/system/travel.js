import request from '@/utils/request'

// 查询城市旅游列表
export function listTravel(query) {
  return request({
    url: '/system/travel/list',
    method: 'get',
    params: query
  })
}

// 查询城市旅游详细
export function getTravel(id) {
  return request({
    url: '/system/travel/' + id,
    method: 'get'
  })
}

// 新增城市旅游
export function addTravel(data) {
  return request({
    url: '/system/travel',
    method: 'post',
    data: data
  })
}

// 修改城市旅游
export function updateTravel(data) {
  return request({
    url: '/system/travel',
    method: 'put',
    data: data
  })
}

// 删除城市旅游
export function delTravel(id) {
  return request({
    url: '/system/travel/' + id,
    method: 'delete'
  })
}
