// 用户名匹配
export function nameRule(rule, value, callback) {
    //  请输入4-10位昵称
    let reg = /(^[a-zA-Z0-9]{4,10}$)/;
    if (value === "") {
        callback(new Error("请输入用户名"));
    } else if (!reg.test(value)) {
        callback(new Error("请输入4-10位用户名"));
    } else {
        callback();
    }
}
// 邮箱匹配
export function emailRule(rule, value, callback) {
    let reg = /(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)/;
    if (value === "") {
        callback(new Error("邮箱不能为空"));
    } else if (!reg.test(value)) {
        callback(new Error("请输入正确的邮箱地址"));
    } else {
        callback();
    }
}
// 电话匹配
export function phoneRule(rule, value, callback) {
    let reg = /(^\+?(\d[\s-]?)?(?:\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4})$)/;
    if (value === "") {
        callback(new Error("电话不能为空"));
    } else if (!reg.test(value)) {
        callback(new Error("请输入正确的电话号码"));
    } else {
        callback();
    }
}

// 密码正则匹配
export function passRule(rule, value, callback) {
    //   6-12位密码需要包含大小写字母和数字以及特殊符号
    let pass = /^\S*(?=\S{6,12})(?=\S*\d)(?=\S*[A-Z])(?=\S*[a-z])(?=\S*[!@#$%^&*? ])\S*$/;
    if (value === "") {
        callback(new Error("请输入密码"));
    } else if (!pass.test(value)) {
        callback(new Error("6-12位密码需要包含大小写字母和数字及特殊符号"));
    } else {
        callback();
    }
}