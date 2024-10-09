package com.douyuehan.doubao.controller.cityInfoController;

import com.douyuehan.doubao.mapper.cityInfoMapper.CityInfoNewsMapper;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityImages;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.service.IBmsCommentService;
import com.douyuehan.doubao.service.cityInfoService.ICityInfoNewsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.util.List;

/**
 * 城市信息的新闻板块
 */
@RestController
@CrossOrigin
public class CityNewsController {
    @Resource
    private ICityInfoNewsService iCityInfoNewsService;

    static class CityNewsResponse {
        private List<CityNews> cityNewsList;
        private int cityNewsListTotal;

        public void setCityNewsList(List<CityNews> cityNews) {
            this.cityNewsList = cityNews;
        }
        public void setCityNewsTotal(int total) {
            this.cityNewsListTotal = total;
        }
    }

    @PostMapping("/CityNews/{city}")
    public CityNewsResponse postCityNewsInfo(@PathVariable String city) {
        List<CityNews> cityNewsList = iCityInfoNewsService.getCityNewsInfo(city);
        int cityNewsListTotal = cityNewsList.size();
        // 封装响应
        CityNewsResponse cityNewsResponse = new CityNewsResponse();
        cityNewsResponse.setCityNewsList(cityNewsList);
        cityNewsResponse.setCityNewsTotal(cityNewsListTotal);
        return cityNewsResponse;
    }
    /**
     * 获取当前省份城市选项按钮
     */
    @GetMapping("/CityNews/{province}")
    public List<String> getCitiesButton(@PathVariable String province) {
        List<String> list = iCityInfoNewsService.getCitiesButton(province);
        System.out.println(list);
        return list;
    }
}
