import request from '@/utils/request'

// 查询美食数据（1）列表
export function listFood(query) {
  return request({
    url: '/system/food/list',
    method: 'get',
    params: query
  })
}

// 查询美食数据（1）详细
export function getFood(id) {
  return request({
    url: '/system/food/' + id,
    method: 'get'
  })
}

// 新增美食数据（1）
export function addFood(data) {
  return request({
    url: '/system/food',
    method: 'post',
    data: data
  })
}

// 修改美食数据（1）
export function updateFood(data) {
  return request({
    url: '/system/food',
    method: 'put',
    data: data
  })
}

// 删除美食数据（1）
export function delFood(id) {
  return request({
    url: '/system/food/' + id,
    method: 'delete'
  })
}
