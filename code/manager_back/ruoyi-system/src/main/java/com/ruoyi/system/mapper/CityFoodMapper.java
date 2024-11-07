package com.ruoyi.system.mapper;

import java.util.List;
import com.ruoyi.system.domain.CityFood;

/**
 * 美食数据（1）Mapper接口
 * 
 * @author zrt
 * @date 2024-11-07
 */
public interface CityFoodMapper 
{
    /**
     * 查询美食数据（1）
     * 
     * @param id 美食数据（1）主键
     * @return 美食数据（1）
     */
    public CityFood selectCityFoodById(Long id);

    /**
     * 查询美食数据（1）列表
     * 
     * @param cityFood 美食数据（1）
     * @return 美食数据（1）集合
     */
    public List<CityFood> selectCityFoodList(CityFood cityFood);

    /**
     * 新增美食数据（1）
     * 
     * @param cityFood 美食数据（1）
     * @return 结果
     */
    public int insertCityFood(CityFood cityFood);

    /**
     * 修改美食数据（1）
     * 
     * @param cityFood 美食数据（1）
     * @return 结果
     */
    public int updateCityFood(CityFood cityFood);

    /**
     * 删除美食数据（1）
     * 
     * @param id 美食数据（1）主键
     * @return 结果
     */
    public int deleteCityFoodById(Long id);

    /**
     * 批量删除美食数据（1）
     * 
     * @param ids 需要删除的数据主键集合
     * @return 结果
     */
    public int deleteCityFoodByIds(Long[] ids);
}
