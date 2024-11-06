package com.douyuehan.doubao.model.entity.BigscreenEntity;


public class Emotion {
    String cityName;
    int positiveNum;
    int negativeNum;
    int neutralityNum;
    String platform;

    public Emotion() {
    }

    public Emotion(String cityName, int positiveNum, int negativeNum, int neutralityNum, String platform) {
        this.cityName = cityName;
        this.positiveNum = positiveNum;
        this.negativeNum = negativeNum;
        this.neutralityNum = neutralityNum;
        this.platform = platform;
    }

    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public int getPositiveNum() {
        return positiveNum;
    }

    public void setPositiveNum(int positiveNum) {
        this.positiveNum = positiveNum;
    }

    public int getNegativeNum() {
        return negativeNum;
    }

    public void setNegativeNum(int negativeNum) {
        this.negativeNum = negativeNum;
    }

    public int getNeutralityNum() {
        return neutralityNum;
    }

    public void setNeutralityNum(int neutralityNum) {
        this.neutralityNum = neutralityNum;
    }
}
