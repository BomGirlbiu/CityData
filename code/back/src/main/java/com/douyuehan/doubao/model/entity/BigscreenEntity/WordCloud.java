package com.douyuehan.doubao.model.entity.BigscreenEntity;


public class WordCloud {
    String cityName;
    String name;
    Float value;

    public String getCityName() {
        return cityName;
    }

    public WordCloud(String name, Float value) {
        this.name = name;
        this.value = value;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Float getValue() {
        return value;
    }

    public void setValue(Float value) {
        this.value = value;
    }



    public WordCloud() {
    }
}
