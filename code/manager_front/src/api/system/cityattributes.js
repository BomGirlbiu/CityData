import request from '@/utils/request'

// 查询城市传播指数列表
export function listCityattributes(query) {
  return request({
    url: '/system/cityattributes/list',
    method: 'get',
    params: query
  })
}

// 查询城市传播指数详细
export function getCityattributes(cityID) {
  return request({
    url: '/system/cityattributes/' + cityID,
    method: 'get'
  })
}

// 新增城市传播指数
export function addCityattributes(data) {
  return request({
    url: '/system/cityattributes',
    method: 'post',
    data: data
  })
}

// 修改城市传播指数
export function updateCityattributes(data) {
  return request({
    url: '/system/cityattributes',
    method: 'put',
    data: data
  })
}

// 删除城市传播指数
export function delCityattributes(cityID) {
  return request({
    url: '/system/cityattributes/' + cityID,
    method: 'delete'
  })
}
