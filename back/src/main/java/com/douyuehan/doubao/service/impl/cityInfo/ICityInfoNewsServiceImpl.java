package com.douyuehan.doubao.service.impl.cityInfo;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.douyuehan.doubao.mapper.cityInfoMapper.CityInfoNewsMapper;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.service.cityInfoService.ICityInfoNewsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ICityInfoNewsServiceImpl extends ServiceImpl<CityInfoNewsMapper, CityNews> implements ICityInfoNewsService {
    @Autowired
    private CityInfoNewsMapper cityInfoNewsMapper;
    @Override
    public List<CityNews> getCityNewsInfo(String city){
        List<CityNews> cityNewsList = cityInfoNewsMapper.getCitiesInfo(city);
        return cityNewsList;
    }

    @Override
    public List<String> getCitiesButton(String province) {
        List<String> citiesButtonList = cityInfoNewsMapper.getCitiesButtonList(province);
        return citiesButtonList;
    }

}
