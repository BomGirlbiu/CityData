package com.douyuehan.doubao.service.impl;


import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.douyuehan.doubao.mapper.SysNoticeMapper;
import com.douyuehan.doubao.model.entity.SysNotice;
import com.douyuehan.doubao.service.IBmsSysNoticeService;
import org.springframework.stereotype.Service;

@Service
public class IBmsSysNoticeServiceImpl extends ServiceImpl<SysNoticeMapper
        , SysNotice> implements IBmsSysNoticeService {

}
