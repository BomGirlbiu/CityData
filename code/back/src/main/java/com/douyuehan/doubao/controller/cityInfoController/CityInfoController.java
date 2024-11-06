package com.douyuehan.doubao.controller.cityInfoController;

import com.douyuehan.doubao.service.cityInfoService.ICityInfoNewsService;
import com.douyuehan.doubao.service.cityInfoService.ICityInfoService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.ArrayList;
import java.util.List;

/**
 * 城市信息页面
 */
@RestController
@RequestMapping("/CityInfo")
public class CityInfoController {
    @Resource
    private ICityInfoService iCityInfoService;
    /**
     * 获取当前省份城市选项按钮
     */
    @GetMapping("/{flag}")
    public List<String> getProvince(@PathVariable String flag) {
        List<String> provinceList = iCityInfoService.getProvince(flag);
        return provinceList;
    }

}
