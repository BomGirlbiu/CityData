package com.ruoyi.system.service.impl;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.ruoyi.system.mapper.WordcloudMapper;
import com.ruoyi.system.domain.Wordcloud;
import com.ruoyi.system.service.IWordcloudService;

/**
 * 词云Service业务层处理
 * 
 * @author childa
 * @date 2024-11-08
 */
@Service
public class WordcloudServiceImpl implements IWordcloudService 
{
    @Autowired
    private WordcloudMapper wordcloudMapper;

    /**
     * 查询词云
     * 
     * @param cityName 词云主键
     * @return 词云
     */
    @Override
    public Wordcloud selectWordcloudByCityName(String cityName)
    {
        return wordcloudMapper.selectWordcloudByCityName(cityName);
    }

    /**
     * 查询词云列表
     * 
     * @param wordcloud 词云
     * @return 词云
     */
    @Override
    public List<Wordcloud> selectWordcloudList(Wordcloud wordcloud)
    {
        return wordcloudMapper.selectWordcloudList(wordcloud);
    }

    /**
     * 新增词云
     * 
     * @param wordcloud 词云
     * @return 结果
     */
    @Override
    public int insertWordcloud(Wordcloud wordcloud)
    {
        return wordcloudMapper.insertWordcloud(wordcloud);
    }

    /**
     * 修改词云
     * 
     * @param wordcloud 词云
     * @return 结果
     */
    @Override
    public int updateWordcloud(Wordcloud wordcloud)
    {
        return wordcloudMapper.updateWordcloud(wordcloud);
    }

    /**
     * 批量删除词云
     * 
     * @param cityNames 需要删除的词云主键
     * @return 结果
     */
    @Override
    public int deleteWordcloudByCityNames(String[] cityNames)
    {
        return wordcloudMapper.deleteWordcloudByCityNames(cityNames);
    }

    /**
     * 删除词云信息
     * 
     * @param cityName 词云主键
     * @return 结果
     */
    @Override
    public int deleteWordcloudByCityName(String cityName)
    {
        return wordcloudMapper.deleteWordcloudByCityName(cityName);
    }
}
