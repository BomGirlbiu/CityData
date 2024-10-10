package com.douyuehan.doubao.mapper.cityInfoMapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityImages;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityVideo;
import org.apache.ibatis.annotations.Select;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CityInfoNewsMapper extends BaseMapper<CityNews> {

    /**
     *获得城市新闻信息
     */
    @Select("select * from CityNews where city=#{city}")
    List<CityNews> getCitiesInfo(String city);


    @Select("select city from CityImages where province=#{province} group by city")
    List<String> getCitiesButtonList(String province);

    @Select("select imagesURL from CityImages where city=#{city}")
    List<CityImages> getCitiesSliderList(String city);

    @Select("select * from CityVideo where city=#{city}")
    List<CityVideo> getCitiesVideoList(String city);

}
