package com.douyuehan.doubao.mapper.BigscreenMapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import com.douyuehan.doubao.model.entity.BigscreenEntity.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface TourMapper {
    @Select("select * from city_data where cityname=#{cityName}")
    public List<Tourism> findtourbyname(String cityName);
}
