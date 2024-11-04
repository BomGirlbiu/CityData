package com.douyuehan.doubao.model.dto;
import java.util.List;

public class CityDTO {
    private List<String> cities;

    // 构造器、getter和setter省略
    public CityDTO() {

    }
    public CityDTO(List<String> cities) {
        this.cities = cities;
    }

    public List<String> getCities() {
        return cities;
    }

    public void setCities(List<String> cities) {
        this.cities = cities;
    }
}
