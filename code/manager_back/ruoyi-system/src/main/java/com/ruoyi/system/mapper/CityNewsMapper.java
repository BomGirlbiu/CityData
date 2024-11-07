package com.ruoyi.system.mapper;

import java.util.List;
import com.ruoyi.system.domain.CityNews;

/**
 * 新闻列表Mapper接口
 * 
 * @author zrt
 * @date 2024-11-07
 */
public interface CityNewsMapper 
{
    /**
     * 查询新闻列表
     * 
     * @param newsID 新闻列表主键
     * @return 新闻列表
     */
    public CityNews selectCityNewsByNewsID(Long newsID);

    /**
     * 查询新闻列表列表
     * 
     * @param cityNews 新闻列表
     * @return 新闻列表集合
     */
    public List<CityNews> selectCityNewsList(CityNews cityNews);

    /**
     * 新增新闻列表
     * 
     * @param cityNews 新闻列表
     * @return 结果
     */
    public int insertCityNews(CityNews cityNews);

    /**
     * 修改新闻列表
     * 
     * @param cityNews 新闻列表
     * @return 结果
     */
    public int updateCityNews(CityNews cityNews);

    /**
     * 删除新闻列表
     * 
     * @param newsID 新闻列表主键
     * @return 结果
     */
    public int deleteCityNewsByNewsID(Long newsID);

    /**
     * 批量删除新闻列表
     * 
     * @param newsIDs 需要删除的数据主键集合
     * @return 结果
     */
    public int deleteCityNewsByNewsIDs(Long[] newsIDs);
}
