package com.douyuehan.doubao.model.entity.BigscreenEntity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;

@TableName("fans")
public class Fans {
    @TableId(type = IdType.AUTO)
    Integer fid;
    String cityname;

    float govern;
    float culture;
    float news;
    String plat;

    public Fans() {
    }

    public Fans(Integer fid, String cityname, float govern, float culture, float news, String plat) {
        this.fid = fid;
        this.cityname = cityname;
        this.govern = govern;
        this.culture = culture;
        this.news = news;
        this.plat = plat;
    }

    public Integer getFid() {
        return fid;
    }

    public void setFid(Integer fid) {
        this.fid = fid;
    }

    public String getPlat() {
        return plat;
    }

    public void setPlat(String plat) {
        this.plat = plat;
    }

    public String getCityname() {
        return cityname;
    }

    public void setCityname(String cityname) {
        this.cityname = cityname;
    }

    public float getGovern() {
        return govern;
    }

    public void setGovern(float govern) {
        this.govern = govern;
    }

    public float getCulture() {
        return culture;
    }

    public void setCulture(float culture) {
        this.culture = culture;
    }

    public float getNews() {
        return news;
    }

    public void setNews(float news) {
        this.news = news;
    }

    public String getPlatform() {
        return plat;
    }

    public void setPlatform(String platform) {
        this.plat = platform;
    }
}
