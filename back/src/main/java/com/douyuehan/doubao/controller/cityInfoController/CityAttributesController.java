package com.douyuehan.doubao.controller.cityInfoController;

import com.douyuehan.doubao.model.entity.BigscreenEntity.CityAttributes;
import com.douyuehan.doubao.model.dto.CityDTO;
import com.douyuehan.doubao.service.cityInfoService.CityAttributesService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@RestController
@CrossOrigin
public class CityAttributesController {

    @Autowired
    private CityAttributesService cityAttributesService;

    static class MyResponse {
        private List<CityAttributes> list;
        private int total;
        public void setList(List<CityAttributes> list) {
            this.list = list;
        }
        public List<CityAttributes> getList() {
            return list;
        }

        public void setTotal(int total) {
            this.total = total;
        }

        public int getTotal() {
            return total;
        }

    }

    /**
     * 城市传播指数页面
     */
//    所有城市
    @GetMapping("/index/evaluate")
    public MyResponse MyResponseList() {
        List<CityAttributes> list = cityAttributesService.selectAllCityList();
        int total = list.size();
        MyResponse response = new MyResponse();
        response.setList(list);
        response.setTotal(total);
        return response;
    }

    //挑选城市
    @PostMapping("/index/evaluate")
    public MyResponse queryCities(@RequestBody CityDTO cityDTO) {
        List<CityAttributes> list = cityAttributesService.findCitiesByNames(cityDTO.getCities());
        MyResponse myResponse = new MyResponse();
        myResponse.setList(list);
        myResponse.setTotal(list.size());
        return myResponse;
    }
    /**
     * 后台页面
     */
//删除城市
    @DeleteMapping("/home/citys/{cityId}")
    public String deleteBycityId(@PathVariable int cityId) {
        int i = cityAttributesService.deleteBycityId(cityId);
        return "删除成功";
    }
//所有城市信息
    @GetMapping("/home/citys")
    public MyResponse query2() {
        List<CityAttributes> list = cityAttributesService.selectAllCityList();
        int total = list.size();

        MyResponse response = new MyResponse();
        response.setList(list);
        response.setTotal(total);

        return response;
    }

    //根据城市名搜索城市信息
    @GetMapping("/home/citys/{cityName}")
    public MyResponse query2(@PathVariable String cityName) {
        List<CityAttributes> list = cityAttributesService.selectCityByCityName(cityName);
        int total = list.size();
        // 封装响应
        MyResponse response = new MyResponse();
        response.setList(list);
        response.setTotal(total);

        return response;
    }
    //计算修改后的城市信息
    @PostMapping("/home/citys")
    public List<Double> change(@RequestBody CityAttributes cityAttributes) {
        System.err.println("接收到的城市形象"+cityAttributes);
        List<Double> weightList = cityAttributesService.updateCityInfo(cityAttributes);
        return weightList;
    }
}
