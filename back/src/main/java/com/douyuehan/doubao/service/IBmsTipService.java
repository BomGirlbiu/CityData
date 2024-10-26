package com.douyuehan.doubao.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.douyuehan.doubao.model.entity.BmsTip;

import java.util.List;

public interface IBmsTipService extends IService<BmsTip> {
    List<BmsTip> getRandomTip();
}
