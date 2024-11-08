package com.ruoyi.system.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ruoyi.system.mapper.CityattributesMapper;
import com.ruoyi.system.domain.Cityattributes;
import com.ruoyi.system.service.ICityattributesService;

/**
 * 城市传播指数Service业务层处理
 * 
 * @author zrt
 * @date 2024-11-08
 */
@Service
public class CityattributesServiceImpl implements ICityattributesService 
{
    @Autowired
    private CityattributesMapper cityattributesMapper;

    /**
     * 查询城市传播指数
     * 
     * @param cityID 城市传播指数主键
     * @return 城市传播指数
     */
    @Override
    public Cityattributes selectCityattributesByCityID(Integer cityID)
    {
        return cityattributesMapper.selectCityattributesByCityID(cityID);
    }

    /**
     * 查询城市传播指数列表
     * 
     * @param cityattributes 城市传播指数
     * @return 城市传播指数
     */
    @Override
    public List<Cityattributes> selectCityattributesList(Cityattributes cityattributes)
    {
        return cityattributesMapper.selectCityattributesList(cityattributes);
    }

    /**
     * 新增城市传播指数
     * 
     * @param cityattributes 城市传播指数
     * @return 结果
     */
    @Override
    public int insertCityattributes(Cityattributes cityattributes)
    {
        return cityattributesMapper.insertCityattributes(cityattributes);
    }

    /**
     * 修改城市传播指数
     * 
     * @param cityattributes 城市传播指数
     * @return 结果
     */
    @Override
    public int updateCityattributes(Cityattributes cityattributes)
    {
        return cityattributesMapper.updateCityattributes(cityattributes);
    }

    /**
     * 批量删除城市传播指数
     * 
     * @param cityIDs 需要删除的城市传播指数主键
     * @return 结果
     */
    @Override
    public int deleteCityattributesByCityIDs(Integer[] cityIDs)
    {
        return cityattributesMapper.deleteCityattributesByCityIDs(cityIDs);
    }

    /**
     * 删除城市传播指数信息
     * 
     * @param cityID 城市传播指数主键
     * @return 结果
     */
    @Override
    public int deleteCityattributesByCityID(Integer cityID)
    {
        return cityattributesMapper.deleteCityattributesByCityID(cityID);
    }
}
