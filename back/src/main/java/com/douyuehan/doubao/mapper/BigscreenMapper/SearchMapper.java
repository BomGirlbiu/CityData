package com.douyuehan.doubao.mapper.BigscreenMapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import com.douyuehan.doubao.model.entity.BigscreenEntity.*;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
@Mapper
public interface SearchMapper extends BaseMapper<googlesearch> {
    @Select("select * from googlesearch where city_name=#{cityName}")
    public List<googlesearch> findgooglebyname(String cityName);
}
