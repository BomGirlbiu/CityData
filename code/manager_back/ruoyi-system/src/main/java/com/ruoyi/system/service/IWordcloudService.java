package com.ruoyi.system.service;

import java.util.List;
import com.ruoyi.system.domain.Wordcloud;

/**
 * 词云Service接口
 * 
 * @author childa
 * @date 2024-11-08
 */
public interface IWordcloudService 
{
    /**
     * 查询词云
     * 
     * @param cityName 词云主键
     * @return 词云
     */
    public Wordcloud selectWordcloudByCityName(String cityName);

    /**
     * 查询词云列表
     * 
     * @param wordcloud 词云
     * @return 词云集合
     */
    public List<Wordcloud> selectWordcloudList(Wordcloud wordcloud);

    /**
     * 新增词云
     * 
     * @param wordcloud 词云
     * @return 结果
     */
    public int insertWordcloud(Wordcloud wordcloud);

    /**
     * 修改词云
     * 
     * @param wordcloud 词云
     * @return 结果
     */
    public int updateWordcloud(Wordcloud wordcloud);

    /**
     * 批量删除词云
     * 
     * @param cityNames 需要删除的词云主键集合
     * @return 结果
     */
    public int deleteWordcloudByCityNames(String[] cityNames);

    /**
     * 删除词云信息
     * 
     * @param cityName 词云主键
     * @return 结果
     */
    public int deleteWordcloudByCityName(String cityName);
}
