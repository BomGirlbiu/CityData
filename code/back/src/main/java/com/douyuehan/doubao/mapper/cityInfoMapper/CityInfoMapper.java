package com.douyuehan.doubao.mapper.cityInfoMapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityImages;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityVideo;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CityInfoMapper extends BaseMapper<CityNews> {

    /**
     *获得所有省份
     */
    @Select("select DISTINCT province from city_news")
    List<String> getProvince();
}
