package com.douyuehan.doubao.mapper.BigscreenMapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.douyuehan.doubao.model.entity.BigscreenEntity.CityAttributes;
import org.apache.ibatis.annotations.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface CityAttributesMapper extends BaseMapper<CityAttributes> {
    List<CityAttributes> getSelectCities(List<String> cities);
    @Select("<script>" +
            "SELECT * FROM cityattributes " +
            "WHERE cityName IN " +
            "<foreach item='cityName' collection='cityNames' open='(' separator=',' close=')'>" +
            "#{cityName}" +
            "</foreach>" +
            "</script>")
    List<CityAttributes> selectCitiesByNames(@Param("cityNames") List<String> cityNames);//用于根据用户选择的城市名显示这些城市的各项指标
    
    @Insert("INSERT INTO cityattributes (cityName, mediatr, network, searchin,social,tourism) VALUES (#{cityName}, #{mediatr}, #{network}, #{searchin},#{social},#{tourism})")
    int insertCity(@Param("searchin") float searchin, @Param("network") float network, @Param("mediatr") float mediatr, @Param("tourism") float tourism, @Param("social") float social,@Param("cityName") String cityName);

    @Update("UPDATE cityattributes SET searchin=#{searchin}, network = #{network},mediatr=#{mediatr},tourism=#{tourism},social=#{social} WHERE cityName = #{cityName}")
    int updateCityByName(@Param("searchin") float searchin, @Param("network") float network, @Param("mediatr") float mediatr, @Param("tourism") float tourism, @Param("social") float social,@Param("cityName") String cityName);
    void updateMColumnWithWeights(List<Double> weightList);
    @Select("select * from cityattributes where cityName=#{cityName}")
    public List<CityAttributes> findallbyname(String cityName);
    List<CityAttributes> selectCitiesByName(@Param("cityName") String cityName);//后台查询城市信息
}
