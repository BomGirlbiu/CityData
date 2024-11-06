package com.douyuehan.doubao.service.cityInfoService;

import com.baomidou.mybatisplus.extension.service.IService;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityImages;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityVideo;

import java.util.List;

public interface ICityInfoService extends IService<CityNews> {
    /**
     * 获取城市信息省份选项
     *
     * @param flag
     * @return
     */
    List<String> getProvince(String flag);
}
