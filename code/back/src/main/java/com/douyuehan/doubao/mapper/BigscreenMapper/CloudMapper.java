package com.douyuehan.doubao.mapper.BigscreenMapper;

import com.douyuehan.doubao.model.entity.BigscreenEntity.WordCloud;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface CloudMapper {
    @Select("select * from wordcloud where cityName=#{cityName}")
    public List<WordCloud> findwordbyname(String cityName);
}
