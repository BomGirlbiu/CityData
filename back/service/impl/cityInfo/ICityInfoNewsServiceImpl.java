package com.douyuehan.doubao.service.impl.cityInfo;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.douyuehan.doubao.mapper.cityInfoMapper.CityInfoNewsMapper;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityImages;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityVideo;
import com.douyuehan.doubao.service.cityInfoService.ICityInfoNewsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ICityInfoNewsServiceImpl extends ServiceImpl<CityInfoNewsMapper, CityNews> implements ICityInfoNewsService {
    @Autowired
    private CityInfoNewsMapper cityInfoNewsMapper;
    /**
     * 获取新闻
     */
    @Override
    public List<CityNews> getCityNewsInfo(String city){
        List<CityNews> cityNewsList = cityInfoNewsMapper.getCitiesInfo(city);
        return cityNewsList;
    }
    /**
     * 获取按钮
     */
    @Override
    public List<String> getCitiesButton(String province) {
        List<String> citiesButtonList = cityInfoNewsMapper.getCitiesButtonList(province);
        return citiesButtonList;
    }
    /**
     * 获取轮播图
     */
    @Override
    public List<CityImages> getCityNewsSlider(String city) {
        List<CityImages> citiesSlider = cityInfoNewsMapper.getCitiesSliderList(city);
        return citiesSlider;
    }

    @Override
    public List<CityVideo> getCityNewsVideo(String city) {
        List<CityVideo> citiesVideo = cityInfoNewsMapper.getCitiesVideoList(city);
        return citiesVideo;
    }

}
