package com.ruoyi.system.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ruoyi.system.mapper.CityFoodMapper;
import com.ruoyi.system.domain.CityFood;
import com.ruoyi.system.service.ICityFoodService;

/**
 * 美食数据（1）Service业务层处理
 * 
 * @author zrt
 * @date 2024-11-07
 */
@Service
public class CityFoodServiceImpl implements ICityFoodService 
{
    @Autowired
    private CityFoodMapper cityFoodMapper;

    /**
     * 查询美食数据（1）
     * 
     * @param id 美食数据（1）主键
     * @return 美食数据（1）
     */
    @Override
    public CityFood selectCityFoodById(Long id)
    {
        return cityFoodMapper.selectCityFoodById(id);
    }

    /**
     * 查询美食数据（1）列表
     * 
     * @param cityFood 美食数据（1）
     * @return 美食数据（1）
     */
    @Override
    public List<CityFood> selectCityFoodList(CityFood cityFood)
    {
        return cityFoodMapper.selectCityFoodList(cityFood);
    }

    /**
     * 新增美食数据（1）
     * 
     * @param cityFood 美食数据（1）
     * @return 结果
     */
    @Override
    public int insertCityFood(CityFood cityFood)
    {
        return cityFoodMapper.insertCityFood(cityFood);
    }

    /**
     * 修改美食数据（1）
     * 
     * @param cityFood 美食数据（1）
     * @return 结果
     */
    @Override
    public int updateCityFood(CityFood cityFood)
    {
        return cityFoodMapper.updateCityFood(cityFood);
    }

    /**
     * 批量删除美食数据（1）
     * 
     * @param ids 需要删除的美食数据（1）主键
     * @return 结果
     */
    @Override
    public int deleteCityFoodByIds(Long[] ids)
    {
        return cityFoodMapper.deleteCityFoodByIds(ids);
    }

    /**
     * 删除美食数据（1）信息
     * 
     * @param id 美食数据（1）主键
     * @return 结果
     */
    @Override
    public int deleteCityFoodById(Long id)
    {
        return cityFoodMapper.deleteCityFoodById(id);
    }
}
