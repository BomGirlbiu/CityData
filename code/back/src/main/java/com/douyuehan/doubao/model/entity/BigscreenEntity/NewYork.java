package com.douyuehan.doubao.model.entity.BigscreenEntity;



public class NewYork {
    String cityname;
    String starttime;
    String endtime;
    Integer counts;

    public String getCityname() {
        return cityname;
    }

    public void setCityname(String cityname) {
        this.cityname = cityname;
    }

    public String getStarttime() {
        return starttime;
    }

    public void setStarttime(String starttime) {
        this.starttime = starttime;
    }

    public String getEndtime() {
        return endtime;
    }

    public void setEndtime(String endtime) {
        this.endtime = endtime;
    }

    public Integer getCounts() {
        return counts;
    }

    public void setCounts(Integer counts) {
        this.counts = counts;
    }

    public NewYork(String cityname, String starttime, String endtime, Integer counts) {
        this.cityname = cityname;
        this.starttime = starttime;
        this.endtime = endtime;
        this.counts = counts;
    }

    public NewYork() {
    }
}
