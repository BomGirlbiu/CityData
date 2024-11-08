package com.douyuehan.doubao.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.douyuehan.doubao.mapper.BmsTipMapper;
import com.douyuehan.doubao.model.entity.BmsTip;
import com.douyuehan.doubao.service.IBmsTipService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service
public class IBmsTipServiceImpl extends ServiceImpl<BmsTipMapper
        , BmsTip> implements IBmsTipService {

//    @Override
//    public ArrayList<BmsTip> getRandomTip() {
//        ArrayList<BmsTip> todayTip = null;
//        try {
//            todayTip = this.baseMapper.getRandomTip();
//        } catch (Exception e) {
//            log.info("tip转化失败");
//        }
//        return todayTip;
//    }

        @Override
    public List<BmsTip> getRandomTip() {
            List<BmsTip> todayTip = null;
        try {
            todayTip = this.baseMapper.getRandomTip();
        } catch (Exception e) {
            log.info("tip转化失败");
        }
        return todayTip;
    }

}
