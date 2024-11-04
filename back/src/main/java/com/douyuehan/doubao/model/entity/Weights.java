package com.douyuehan.doubao.model.entity;

public class Weights {
    private Double searchinWeights;
    private Double networkWeights;
    private Double madiatrWeights;
    private Double tourismWeights;

    private Double socialWeights;

    public Weights(Double searchinWeights, Double networkWeights, Double madiatrWeights, Double tourismWeights ,Double socialWeights) {
        this.searchinWeights = searchinWeights;
        this.networkWeights = networkWeights;
        this.madiatrWeights = madiatrWeights;
        this.tourismWeights = tourismWeights;
        this.socialWeights = socialWeights;
    }

    public Double getSocialWeights() {
        return socialWeights;
    }

    public void setSocialWeights(Double socialWeights) {
        this.socialWeights = socialWeights;
    }

    public Double getSearchinWeights() {
        return searchinWeights;
    }

    public void setSearchinWeights(Double searchinWeights) {
        this.searchinWeights = searchinWeights;
    }

    public Double getNetworkWeights() {
        return networkWeights;
    }

    public void setNetworkWeights(Double networkWeights) {
        this.networkWeights = networkWeights;
    }

    public Double getMadiatrWeights() {
        return madiatrWeights;
    }

    public void setMadiatrWeights(Double madiatrWeights) {
        this.madiatrWeights = madiatrWeights;
    }

    public Double getTourismWeights() {
        return tourismWeights;
    }

    public void setTourismWeights(Double tourismWeights) {
        this.tourismWeights = tourismWeights;
    }

}
