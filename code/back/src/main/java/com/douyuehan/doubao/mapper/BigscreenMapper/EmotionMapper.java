package com.douyuehan.doubao.mapper.BigscreenMapper;

import com.douyuehan.doubao.model.entity.BigscreenEntity.YoutubeEmotion;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import com.douyuehan.doubao.model.entity.BigscreenEntity.Emotion;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface EmotionMapper {
    @Select("select * from emotion where cityName=#{cityName} and platform='Bilibili'")
    public List<Emotion> findbilibili(String cityName);
    @Select("select * from emotion_youtube where cityName=#{cityName}")
    public List<YoutubeEmotion> findyoutube(String cityName);
}
