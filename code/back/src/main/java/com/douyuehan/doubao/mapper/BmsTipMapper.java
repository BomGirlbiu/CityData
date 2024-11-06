package com.douyuehan.doubao.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.douyuehan.doubao.common.api.ApiResult;
import com.douyuehan.doubao.model.entity.BmsTip;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface BmsTipMapper extends BaseMapper<BmsTip> {
    List<BmsTip> getRandomTip();
}
