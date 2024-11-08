package com.ruoyi.system.service;

import java.util.List;
import com.ruoyi.system.domain.Cityattributes;

/**
 * 城市传播指数Service接口
 * 
 * @author zrt
 * @date 2024-11-08
 */
public interface ICityattributesService 
{
    /**
     * 查询城市传播指数
     * 
     * @param cityID 城市传播指数主键
     * @return 城市传播指数
     */
    public Cityattributes selectCityattributesByCityID(Integer cityID);

    /**
     * 查询城市传播指数列表
     * 
     * @param cityattributes 城市传播指数
     * @return 城市传播指数集合
     */
    public List<Cityattributes> selectCityattributesList(Cityattributes cityattributes);

    /**
     * 新增城市传播指数
     * 
     * @param cityattributes 城市传播指数
     * @return 结果
     */
    public int insertCityattributes(Cityattributes cityattributes);

    /**
     * 修改城市传播指数
     * 
     * @param cityattributes 城市传播指数
     * @return 结果
     */
    public int updateCityattributes(Cityattributes cityattributes);

    /**
     * 批量删除城市传播指数
     * 
     * @param cityIDs 需要删除的城市传播指数主键集合
     * @return 结果
     */
    public int deleteCityattributesByCityIDs(Integer[] cityIDs);

    /**
     * 删除城市传播指数信息
     * 
     * @param cityID 城市传播指数主键
     * @return 结果
     */
    public int deleteCityattributesByCityID(Integer cityID);
}
