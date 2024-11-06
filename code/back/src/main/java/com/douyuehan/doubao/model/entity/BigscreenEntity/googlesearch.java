package com.douyuehan.doubao.model.entity.BigscreenEntity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;

@TableName("googlesearch")
public class googlesearch {
    @TableId(type = IdType.AUTO)
    Integer gid;
    String cityName;
    String week;
    int counts;

    public googlesearch(Integer gid, String cityName, String week, int counts) {
        this.gid = gid;
        this.cityName = cityName;
        this.week = week;
        this.counts = counts;
    }

    public googlesearch() {
    }

    public Integer getGid() {
        return gid;
    }

    public void setGid(Integer gid) {
        this.gid = gid;
    }

    public String getCityName() {
        return cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public String getWeek() {
        return week;
    }

    public void setWeek(String weeks) {
        this.week= weeks;
    }

    public int getCounts() {
        return counts;
    }

    public void setCounts(int counts) {
        this.counts = counts;
    }
}
