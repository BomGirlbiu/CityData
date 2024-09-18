const express = require('express');  
const bodyParser = require('body-parser');  
const app = express();  
  
app.use(bodyParser.json());  
  
// 假设有一个验证用户的函数  
function validateUser(username, password) {  
  // 这里应该与数据库交互来验证用户  
  // 这里只是一个示例  
  return username === '1111' && password === '111111';  
}  
  
app.post('/api/login', (req, res) => {  
  const { username, password } = req.body;  
  if (validateUser(username, password)) {  
    res.json({ success: true, message: '登录成功' });  
  } else {  
    res.status(401).json({ success: false, message: '用户名或密码错误' });  
  }  
});  
  
app.listen(3000, () => {  
  console.log('Server is running on port 3000');  
});