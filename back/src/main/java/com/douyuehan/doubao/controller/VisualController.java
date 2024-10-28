package com.douyuehan.doubao.controller;

import com.douyuehan.doubao.model.entity.BigscreenEntity.*;
import com.douyuehan.doubao.mapper.BigscreenMapper.*;
import com.douyuehan.doubao.model.entity.BigscreenEntity.googlesearch;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@CrossOrigin
public class VisualController {
    @Autowired
    private SearchMapper searchMapper;
    @Autowired
    private CityAttributesMapper cityAttributesMapper;
    @Autowired
    private FansMapper fansMapper;
    @Autowired
    private EmotionMapper emotionMapper;
    @Autowired
    private TourMapper tourMapper;
    @Autowired
    private  CloudMapper cloudMapper;
    @Autowired
    private NewYorkMapper newYorkMapper;

    @PostMapping("/index/visual/search/google")
    public List<googlesearch> findgooglebyname(String cityname) {
        List<googlesearch> list = searchMapper.findgooglebyname(cityname);
        System.out.println(list);
        return list;
    }
    @PostMapping("/index/visual/social/fans")
    public List<Fans> findfansbyname(String cityname) {
        List<Fans> list = fansMapper.findfansbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }
    @PostMapping("/index/visual/social/emotion")
    public List<Emotion> findemotionbyname(String cityname) {
        List<Emotion> list = emotionMapper.findbilibili(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }
    @PostMapping("/index/visual/social/youtube")
    public List<Emotion> findyoutube(String cityname) {
        List<Emotion> list = emotionMapper.findyoutube(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }

    @PostMapping("/index/visual/nation/tourism")
    public List<Tourism> findtourbyname(String cityname) {
        List<Tourism> list = tourMapper.findtourbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }

    @PostMapping("/index/visual/conclusion")
    public List<CityAttributes> findallbyname(String cityname) {
        List<CityAttributes> list = cityAttributesMapper.findallbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }
    @PostMapping("/index/visual/media/newyork")
    public List<NewYork> findnewyorkcountsbyname(String cityname) {
        List<NewYork> list = newYorkMapper.findcountsbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }

    @PostMapping("/index/visual/network/cloud")
    public List<WordCloud> findcloudbyname(String cityname) {
        List<WordCloud> list = cloudMapper.findwordbyname(cityname); // 注意：这里假设你的mapper方法只根据cityname查找
        System.out.println(list);
        return list;
    }

    @GetMapping("/index/visual")
    public List<CityAttributes> findcities() {
        List<CityAttributes> list = cityAttributesMapper.selectList(null);
        System.out.println(list);
        return list;
    }

}