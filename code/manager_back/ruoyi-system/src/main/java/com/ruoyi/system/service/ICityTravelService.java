package com.ruoyi.system.service;

import java.util.List;
import com.ruoyi.system.domain.CityTravel;

/**
 * 城市旅游Service接口
 * 
 * @author zrt
 * @date 2024-11-07
 */
public interface ICityTravelService 
{
    /**
     * 查询城市旅游
     * 
     * @param id 城市旅游主键
     * @return 城市旅游
     */
    public CityTravel selectCityTravelById(Long id);

    /**
     * 查询城市旅游列表
     * 
     * @param cityTravel 城市旅游
     * @return 城市旅游集合
     */
    public List<CityTravel> selectCityTravelList(CityTravel cityTravel);

    /**
     * 新增城市旅游
     * 
     * @param cityTravel 城市旅游
     * @return 结果
     */
    public int insertCityTravel(CityTravel cityTravel);

    /**
     * 修改城市旅游
     * 
     * @param cityTravel 城市旅游
     * @return 结果
     */
    public int updateCityTravel(CityTravel cityTravel);

    /**
     * 批量删除城市旅游
     * 
     * @param ids 需要删除的城市旅游主键集合
     * @return 结果
     */
    public int deleteCityTravelByIds(Long[] ids);

    /**
     * 删除城市旅游信息
     * 
     * @param id 城市旅游主键
     * @return 结果
     */
    public int deleteCityTravelById(Long id);
}
