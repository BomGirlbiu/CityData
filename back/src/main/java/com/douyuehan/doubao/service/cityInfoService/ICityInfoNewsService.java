package com.douyuehan.doubao.service.cityInfoService;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.model.vo.PostVO;

import java.util.List;

public interface ICityInfoNewsService extends IService<CityNews> {
    /**
     * 获取城市信息·新闻页面·新闻内容
     *
     * @param city
     * @return
     */
    List<CityNews> getCityNewsInfo(String city);
    /**
     * 获取城市所有按钮
     *
     * @param province
     * @return
     */
    List<String> getCitiesButton(String province);
}
