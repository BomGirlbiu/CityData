package com.ruoyi.system.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ruoyi.system.mapper.CityNewsMapper;
import com.ruoyi.system.domain.CityNews;
import com.ruoyi.system.service.ICityNewsService;

/**
 * 新闻列表Service业务层处理
 * 
 * @author zrt
 * @date 2024-11-07
 */
@Service
public class CityNewsServiceImpl implements ICityNewsService 
{
    @Autowired
    private CityNewsMapper cityNewsMapper;

    /**
     * 查询新闻列表
     * 
     * @param newsID 新闻列表主键
     * @return 新闻列表
     */
    @Override
    public CityNews selectCityNewsByNewsID(Long newsID)
    {
        return cityNewsMapper.selectCityNewsByNewsID(newsID);
    }

    /**
     * 查询新闻列表列表
     * 
     * @param cityNews 新闻列表
     * @return 新闻列表
     */
    @Override
    public List<CityNews> selectCityNewsList(CityNews cityNews)
    {
        return cityNewsMapper.selectCityNewsList(cityNews);
    }

    /**
     * 新增新闻列表
     * 
     * @param cityNews 新闻列表
     * @return 结果
     */
    @Override
    public int insertCityNews(CityNews cityNews)
    {
        return cityNewsMapper.insertCityNews(cityNews);
    }

    /**
     * 修改新闻列表
     * 
     * @param cityNews 新闻列表
     * @return 结果
     */
    @Override
    public int updateCityNews(CityNews cityNews)
    {
        return cityNewsMapper.updateCityNews(cityNews);
    }

    /**
     * 批量删除新闻列表
     * 
     * @param newsIDs 需要删除的新闻列表主键
     * @return 结果
     */
    @Override
    public int deleteCityNewsByNewsIDs(Long[] newsIDs)
    {
        return cityNewsMapper.deleteCityNewsByNewsIDs(newsIDs);
    }

    /**
     * 删除新闻列表信息
     * 
     * @param newsID 新闻列表主键
     * @return 结果
     */
    @Override
    public int deleteCityNewsByNewsID(Long newsID)
    {
        return cityNewsMapper.deleteCityNewsByNewsID(newsID);
    }
}
