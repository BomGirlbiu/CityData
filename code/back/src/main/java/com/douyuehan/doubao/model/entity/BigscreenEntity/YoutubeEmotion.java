package com.douyuehan.doubao.model.entity.BigscreenEntity;


import java.util.Date;

public class YoutubeEmotion {
    String cityName;
    int joyNum;
    int sadnessNum;
    int angerNum;
    int fearNum;
    int surpriseNum;
    int loveNum;
    int disgustNum;
    int travelNum;
    int foodNum;
   String insert_time;
   String platform;

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public int getJoyNum() {
        return joyNum;
    }

    public void setJoyNum(int joyNum) {
        this.joyNum = joyNum;
    }

    public int getSadnessNum() {
        return sadnessNum;
    }

    public void setSadnessNum(int sadnessNum) {
        this.sadnessNum = sadnessNum;
    }

    public int getAngerNum() {
        return angerNum;
    }

    public void setAngerNum(int angerNum) {
        this.angerNum = angerNum;
    }

    public int getFearNum() {
        return fearNum;
    }

    public void setFearNum(int fearNum) {
        this.fearNum = fearNum;
    }

    public int getSurpriseNum() {
        return surpriseNum;
    }

    public void setSurpriseNum(int surpriseNum) {
        this.surpriseNum = surpriseNum;
    }

    public int getLoveNum() {
        return loveNum;
    }

    public void setLoveNum(int loveNum) {
        this.loveNum = loveNum;
    }

    public int getDisgustNum() {
        return disgustNum;
    }

    public void setDisgustNum(int disgustNum) {
        this.disgustNum = disgustNum;
    }

    public int getTravelNum() {
        return travelNum;
    }

    public void setTravelNum(int travelNum) {
        this.travelNum = travelNum;
    }

    public int getFoodNum() {
        return foodNum;
    }

    public void setFoodNum(int foodNum) {
        this.foodNum = foodNum;
    }

    public String getInsert_time() {
        return insert_time;
    }

    public void setInsert_time(String insert_time) {
        this.insert_time = insert_time;
    }

    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }

    public YoutubeEmotion(String cityName, int joyNum, int sadnessNum, int angerNum, int fearNum, int surpriseNum, int loveNum, int disgustNum, int travelNum, int foodNum, String insert_time, String platform) {
        this.cityName = cityName;
        this.joyNum = joyNum;
        this.sadnessNum = sadnessNum;
        this.angerNum = angerNum;
        this.fearNum = fearNum;
        this.surpriseNum = surpriseNum;
        this.loveNum = loveNum;
        this.disgustNum = disgustNum;
        this.travelNum = travelNum;
        this.foodNum = foodNum;
        this.insert_time = insert_time;
        this.platform = platform;
    }
}
