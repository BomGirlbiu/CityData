package com.douyuehan.doubao.service.cityInfoService;

import cn.hutool.core.util.NumberUtil;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.douyuehan.doubao.model.entity.BigscreenEntity.CityAttributes;
import com.douyuehan.doubao.mapper.BigscreenMapper.CityAttributesMapper;
import com.douyuehan.doubao.utils.ShangFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class CityAttributesService {
    @Autowired
    private CityAttributesMapper cityAttributesMapper;

    public List<CityAttributes> findCitiesByNames(List<String> cityNames) {
        if (cityNames == null || cityNames.isEmpty()) {
            return Collections.emptyList();
        }
        String cityNamesStr = cityNames.stream().map(name -> "'" + name + "'").collect(Collectors.joining(","));
        QueryWrapper<CityAttributes> queryWrapper = new QueryWrapper<>();
        queryWrapper.in("cityName", cityNamesStr.substring(1, cityNamesStr.length() - 1)); // 去除首尾的单引号

        return cityAttributesMapper.selectCitiesByNames(cityNames);
    }
    public String getDataByCityAsString() {
        List<CityAttributes> cityAttributesList = cityAttributesMapper.selectList(null);
        StringBuilder sb = new StringBuilder();

        List<Float> searchinValues = new ArrayList<>();
        List<Float> networkValues = new ArrayList<>();
        List<Float> mediatrValues = new ArrayList<>();
        List<Float> tourismValues = new ArrayList<>();
        List<Float> socialValues = new ArrayList<>();

        for (CityAttributes ca : cityAttributesList) {
            searchinValues.add(ca.getSearchin());
            networkValues.add(ca.getNetwork());
            mediatrValues.add(ca.getMediatr());
            tourismValues.add(ca.getTourism());
            socialValues.add(ca.getSocial());
        }

// 接下来，将这些列表转换为字符串格式
        sb.append("[").append(valuesToString(searchinValues)).append("],");
        sb.append("[").append(valuesToString(networkValues)).append("],");
        sb.append("[").append(valuesToString(mediatrValues)).append("],");
        sb.append("[").append(valuesToString(tourismValues)).append("],");
        sb.append("[").append(valuesToString(socialValues)).append("]");

// 注意：这里直接返回了，没有处理最后一个逗号，实际使用时可能需要去掉或替换
        return sb.toString();
    }
    private String valuesToString(List<Float> values) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < values.size(); i++) {
            sb.append(values.get(i));
            if (i < values.size() - 1) {
                sb.append(",");
            }
        }
        return sb.toString();
    }
    public int deleteBycityId(int cityId){
        int i = cityAttributesMapper.deleteById(cityId);
        return i;
    }
    public List<CityAttributes> selectAllCityList(){
        List<CityAttributes> list = cityAttributesMapper.selectList(null);
        return list;
    }
    public List<CityAttributes> selectCityByCityName(String cityName){
        List<CityAttributes> list = cityAttributesMapper.selectCitiesByName(cityName);
        return  list;
    }
    public List<Double> updateCityInfo(CityAttributes cityAttributes){

        String cityName = cityAttributes.getCityName();
        float searchin = cityAttributes.getSearchin();
        float network = cityAttributes.getNetwork();
        float mediatr = cityAttributes.getMediatr();
        float tourism = cityAttributes.getTourism();
        float social = cityAttributes.getSocial();

        if(cityAttributesMapper.selectCitiesByName(cityName).size()==0){
//            执行插入语句
            cityAttributesMapper.insertCity(searchin,network,mediatr,tourism,social,cityName);
            System.out.println(cityAttributesMapper.selectCitiesByName(cityName));
        }

//将修改数据存入数据库
        int i = cityAttributesMapper.updateCityByName(searchin,network,mediatr,tourism,social,cityName);
//计算新权重
        List<List<Double>> dataList = readyData();
        ShangFactory shangFactory = new ShangFactory(dataList);
        List<Double> weightList = shangFactory.listWeight();

//获取权重
        for (Double double1 : weightList) {
            System.out.println(double1);
        }
        System.out.println(weightList);
//根据新权重修改传播指数
        cityAttributesMapper.updateMColumnWithWeights(weightList);
        return weightList;
    }
    public List<List<Double>> readyData() {

        String dataStr=getDataByCityAsString();
        System.out.println("dataStr:"+dataStr);
//        String dataStr =
//                "[100.0, 83.33, 75.0], [83.33, 72.86, 70.0], [85.0, 66.0, 64.53, 5.0], [99.0, 55.0, 40.0, 17.17], [75.0, 65.53, 52.18], [70.0, 64.53, 33.0, 23.19], [75.0, 70.53, 28.99], [85.0, 83.33], [75.0, 64.53, 28.13], [75.0, 66.53], [75.0, 57.97], [83.33, 25.0], [100.0], [64.53, 34.38], [66.67, 31.25], [66.67, 25.0], [85.71], [83.33], [83.33], [83.33], [75.0], [75.0], [75.0], [75.0], [71.43], [65.53], [65.53], [64.53], [34.38]";
        List<List<Double>> dataList = new ArrayList<List<Double>>();
        List<String> list = Arrays.asList(dataStr.split("],"));
        List<Double> dataNumList;
        for (String string : list) {
            string = string.replace("[", "");
            string = string.replace("]", "");
            dataNumList = new ArrayList<Double>();
            List<String> numList = Arrays.asList(string.split(","));
            for (String numStr : numList) {
                dataNumList.add(NumberUtil.parseNumber(numStr.trim()).doubleValue());
            }
            dataList.add(dataNumList);
        }
        System.out.println("dataList:"+dataList);
        return dataList;
    }
}


