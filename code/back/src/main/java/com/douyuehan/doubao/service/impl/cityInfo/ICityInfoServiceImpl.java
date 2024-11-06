package com.douyuehan.doubao.service.impl.cityInfo;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.douyuehan.doubao.mapper.cityInfoMapper.CityInfoMapper;
import com.douyuehan.doubao.mapper.cityInfoMapper.CityInfoNewsMapper;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityImages;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityVideo;
import com.douyuehan.doubao.service.cityInfoService.ICityInfoNewsService;
import com.douyuehan.doubao.service.cityInfoService.ICityInfoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ICityInfoServiceImpl extends ServiceImpl<CityInfoMapper, CityNews> implements ICityInfoService {
    @Autowired
    private CityInfoMapper cityInfoMapper;
    /**
     * 获取省份信息
     */
    @Override
    public List<String> getProvince(String flag){
        List<String> provinceList = new ArrayList<>();
        if(flag.equals("CityNews")){
            provinceList = cityInfoMapper.getProvince();
        }
        return provinceList;
    }
//....................
}
