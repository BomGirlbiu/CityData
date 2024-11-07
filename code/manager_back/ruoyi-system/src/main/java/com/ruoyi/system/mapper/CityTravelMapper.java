package com.ruoyi.system.mapper;

import java.util.List;
import com.ruoyi.system.domain.CityTravel;

/**
 * 城市旅游Mapper接口
 * 
 * @author zrt
 * @date 2024-11-07
 */
public interface CityTravelMapper 
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
     * 删除城市旅游
     * 
     * @param id 城市旅游主键
     * @return 结果
     */
    public int deleteCityTravelById(Long id);

    /**
     * 批量删除城市旅游
     * 
     * @param ids 需要删除的数据主键集合
     * @return 结果
     */
    public int deleteCityTravelByIds(Long[] ids);
}
