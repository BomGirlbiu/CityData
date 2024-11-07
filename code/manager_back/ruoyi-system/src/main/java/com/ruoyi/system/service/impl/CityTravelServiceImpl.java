package com.ruoyi.system.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ruoyi.system.mapper.CityTravelMapper;
import com.ruoyi.system.domain.CityTravel;
import com.ruoyi.system.service.ICityTravelService;

/**
 * 城市旅游Service业务层处理
 * 
 * @author zrt
 * @date 2024-11-07
 */
@Service
public class CityTravelServiceImpl implements ICityTravelService 
{
    @Autowired
    private CityTravelMapper cityTravelMapper;

    /**
     * 查询城市旅游
     * 
     * @param id 城市旅游主键
     * @return 城市旅游
     */
    @Override
    public CityTravel selectCityTravelById(Long id)
    {
        return cityTravelMapper.selectCityTravelById(id);
    }

    /**
     * 查询城市旅游列表
     * 
     * @param cityTravel 城市旅游
     * @return 城市旅游
     */
    @Override
    public List<CityTravel> selectCityTravelList(CityTravel cityTravel)
    {
        return cityTravelMapper.selectCityTravelList(cityTravel);
    }

    /**
     * 新增城市旅游
     * 
     * @param cityTravel 城市旅游
     * @return 结果
     */
    @Override
    public int insertCityTravel(CityTravel cityTravel)
    {
        return cityTravelMapper.insertCityTravel(cityTravel);
    }

    /**
     * 修改城市旅游
     * 
     * @param cityTravel 城市旅游
     * @return 结果
     */
    @Override
    public int updateCityTravel(CityTravel cityTravel)
    {
        return cityTravelMapper.updateCityTravel(cityTravel);
    }

    /**
     * 批量删除城市旅游
     * 
     * @param ids 需要删除的城市旅游主键
     * @return 结果
     */
    @Override
    public int deleteCityTravelByIds(Long[] ids)
    {
        return cityTravelMapper.deleteCityTravelByIds(ids);
    }

    /**
     * 删除城市旅游信息
     * 
     * @param id 城市旅游主键
     * @return 结果
     */
    @Override
    public int deleteCityTravelById(Long id)
    {
        return cityTravelMapper.deleteCityTravelById(id);
    }
}
