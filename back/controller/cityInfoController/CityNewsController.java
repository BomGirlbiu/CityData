package com.douyuehan.doubao.controller.cityInfoController;

import com.douyuehan.doubao.mapper.cityInfoMapper.CityInfoNewsMapper;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityImages;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityNews;
import com.douyuehan.doubao.model.entity.cityInfoEntity.CityVideo;
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
@RequestMapping("/CityNews")
public class CityNewsController {
    @Resource
    private ICityInfoNewsService iCityInfoNewsService;

    static class CityNewsResponse {
        private List<CityNews> cityNewsList;
        private List<CityImages> citySliderList;
        private List<CityVideo> cityVideoList;
        private int cityNewsListTotal;
        private int citySliderListTotal;
        private int cityVideoListTotal;

        public void setCityNewsList(List<CityNews> cityNews) {
            this.cityNewsList = cityNews;
        }
        public void setCityNewsTotal(int total) {
            this.cityNewsListTotal = total;
        }

        public void setCitySliderList(List<CityImages> citySliderList) {
            this.citySliderList = citySliderList;
        }
        public void setSliderListTotal(int Slidertotal) {
            this.citySliderListTotal = Slidertotal;
        }

        public List<CityNews> getCityNewsList() {
            return cityNewsList;
        }

        public List<CityImages> getCitySliderList() {
            return citySliderList;
        }

        public int getCityNewsListTotal() {
            return cityNewsListTotal;
        }

        public int getCitySliderListTotal() {
            return citySliderListTotal;
        }

        public List<CityVideo> getCityVideoList() {
            return cityVideoList;
        }

        public void setCityVideoList(List<CityVideo> cityVideoList) {
            this.cityVideoList = cityVideoList;
        }

        public int getCityVideoListTotal() {
            return cityVideoListTotal;
        }

        public void setCityVideoListTotal(int cityVideoListTotal) {
            this.cityVideoListTotal = cityVideoListTotal;
        }
    }
    /**
     * 获取当前城市数据
     */
    @PostMapping("/{city}")
    public CityNewsResponse postCityNewsInfo(@PathVariable String city) {
        System.out.println(city);
        List<CityNews> cityNewsList = iCityInfoNewsService.getCityNewsInfo(city);
        List<CityImages> citySliderList = iCityInfoNewsService.getCityNewsSlider(city);
        List<CityVideo> cityVideoList = iCityInfoNewsService.getCityNewsVideo(city);

        int cityNewsListTotal = cityNewsList.size();
        int citySliderListTotal = citySliderList.size();
        int cityVideoListTotal = cityVideoList.size();
//      封装响应
        CityNewsResponse cityNewsResponse = new CityNewsResponse();
//      新闻
        cityNewsResponse.setCityNewsList(cityNewsList);
        cityNewsResponse.setCityNewsTotal(cityNewsListTotal);
//      轮播图
        cityNewsResponse.setCitySliderList(citySliderList);
        cityNewsResponse.setSliderListTotal(citySliderListTotal);
//       视频
        cityNewsResponse.setCityVideoList(cityVideoList);
        cityNewsResponse.setCityVideoListTotal(cityVideoListTotal);

        return cityNewsResponse;
    }
    /**
     * 获取当前省份城市选项按钮
     */
    @GetMapping("/{province}")
    public List<String> getCitiesButton(@PathVariable String province) {
        List<String> list = iCityInfoNewsService.getCitiesButton(province);
        System.out.println(list);
        return list;
    }

}
