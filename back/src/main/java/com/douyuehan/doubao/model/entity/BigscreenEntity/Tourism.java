package com.douyuehan.doubao.model.entity.BigscreenEntity;

import com.baomidou.mybatisplus.annotation.TableName;

@TableName("city_data")
public class Tourism {
    int year;
    String cityName;
    int googleCity;
    int tourist;

    public Tourism() {
    }

    public Tourism(int year, String cityName, int googleCity, int tourist) {
        this.year = year;
        this.cityName = cityName;
        this.googleCity = googleCity;
        this.tourist = tourist;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public int getGoogleCity() {
        return googleCity;
    }

    public void setGoogleCity(int googleCity) {
        this.googleCity = googleCity;
    }

    public int getTourist() {
        return tourist;
    }

    public void setTourist(int tourist) {
        this.tourist = tourist;
    }
}
