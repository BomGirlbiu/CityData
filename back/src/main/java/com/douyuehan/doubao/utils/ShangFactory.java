package com.douyuehan.doubao.utils;

import cn.hutool.core.collection.CollUtil;
import cn.hutool.core.util.NumberUtil;

import java.util.ArrayList;
import java.util.List;

public class ShangFactory {
    private List<List<Double>> readyList;
    private Integer maxNum = 0; // 最大位数
    private Double pvg = 100.0; // 平移数值

    public ShangFactory(List<List<Double>> dataList) {
        getMaxNum(dataList);
        readyList = new ArrayList<List<Double>>();
        tranData(dataList);
    }

    public List<Double> listWeight() {
        System.err.println("平移标准化:" + readyList);
        // 完成数据标准化
        List<List<Double>> aveList = orderData(readyList);
        System.err.println("数据标准化:" + aveList);

        List<Double> shangList = listShang(readyList, aveList);
        // 获取信息熵
        System.err.println("信息熵:" + shangList);
        List<Double> weightList = makeWeight(shangList);
        return weightList;
    }

    // 获取最大位数和平移均值
    private void getMaxNum(List<List<Double>> dataList) {
        for (List<Double> list : dataList) {
            if (list.size() > maxNum) {
                maxNum = list.size();
            }
            double ws = 0.0;
            for (Double w : list) {
                if (w < pvg) {
                    pvg = w;
                }
                ws = ws + w;
            }
            pvg = pvg + (ws / list.size());
        }
        pvg = pvg / dataList.size();
    }

    /**
     * 用平移法，补全缺位数据
     *
     * @param dataList
     * @return
     */
    private void tranData(List<List<Double>> dataList) {
        List<Double> dataNumList;
        for (List<Double> list : dataList) {
            dataNumList = new ArrayList<Double>();
            for (Double weight : list) {
                dataNumList.add(weight + pvg);
            }
            // 补全
            for (int i = 0; i < maxNum - list.size(); i++) {
                dataNumList.add(pvg);
            }
            readyList.add(dataNumList);
        }
    }

    /**
     * 2.1，数据标准化
     *
     * @param dataList
     * @return
     */
    private List<List<Double>> orderData(List<List<Double>> dataList) {
        List<List<Double>> aveList = new ArrayList<List<Double>>();
        // 数据归一化处理 (i-min)/(max-min)
        List<Double> numList;
        List<Double> dataNumList;
        double min, diff, temp;
        for (int i = 0; i < dataList.size(); i++) {
            numList = dataList.get(i);
            min = (double) CollUtil.min(numList);
            diff = CollUtil.max(numList) - min;
            dataNumList = new ArrayList<Double>();
            for (int j = 0; j < numList.size(); j++) {
                temp = ((double) numList.get(j) - min) / diff;
                dataNumList.add(j, temp);
            }
            aveList.add(dataNumList);
        }

        return aveList;
    }

    /**
     * 2.2，求各指标的信息熵
     *
     * @param dataList
     * @param aveList
     * @return
     */
    private List<Double> listShang(List<List<Double>> dataList, List<List<Double>> aveList) {
        List<Double> shangList = new ArrayList<Double>();
        for (int i = 0; i < aveList.size(); i++) {
            List<Double> aveNumList = aveList.get(i);
            double pSum = (double) aveNumList.stream().reduce((x, y) -> (double) x + (double) y).get();
            double sum = 0;
            for (int j = 0; j < aveList.get(i).size(); j++) {
                double p = (double) aveNumList.get(j) / pSum;
                if (p != 0) {
                    sum = sum + p * Math.log(p);
                }
            }
            shangList.add((-1) / Math.log(dataList.get(i).size()) * sum);
        }
        return shangList;
    }

    /**
     * 2.3，确定各指标权重
     *
     * @param shangList
     * @return
     */
    private static List<Double> makeWeight(List<Double> shangList) {
        List<Double> weightList = new ArrayList<Double>();
        Double shangSum = shangList.stream().reduce(Double::sum).get();
        double weight;
        for (int i = 0; i < shangList.size(); i++) {
            weight = (1 - shangList.get(i)) / (shangList.size() - shangSum);
            weight = weight * 100.0;
//			BigDecimal weightDec = NumberUtil.round(weight, 6);
            weightList.add(NumberUtil.round(weight, 6).doubleValue());
        }
        return weightList;
    }
}
