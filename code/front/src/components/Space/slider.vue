<template>
<div class="slider-ai">
    <ul class="slider-ul">
	<li class="slider-li">
            <router-link :to="{ name: '首页' }" class="slider-a">
			<i class="el-icon-house"></i>
			<span class="slider-span">主页</span>
            </router-link>
	</li>
	<li class="slider-li">
		<a href="#"  class="slider-a">
			<i class="el-icon-picture-outline"></i>
			<span class="slider-span">图片分析</span>
		</a>
	</li>	
	<li class="slider-li">
                    <router-link :to="{ name: '视频生成' }" class="slider-a">
		<a href="#"  class="slider-a">
			<i class="el-icon-video-play"></i>
			<span class="slider-span">视频</span>
		</a>
                    </router-link>
	</li>
	<li class="slider-li">
                    <router-link :to="{ name: '聊天' }" class="slider-a">

		<a href="#"  class="slider-a">
			<i class="el-icon-chat-dot-square"></i>
			<span class="slider-span">聊天</span>
		</a>
                    </router-link>
	</li>	
	<li class="slider-li">
		<a href="#"  class="slider-a">
			<i class="el-icon-coordinate"></i>
			<span class="slider-span">视频解析</span>
		</a>
	</li>
	<li class="slider-li">
		<a href="#"  class="slider-a">
			<i class="el-icon-bell"></i>
			<span class="slider-span">通知</span>
		</a>
	</li>
	<li class="slider-li">	
		<a href="#"  class="slider-a">
			<i class="el-icon-setting"></i>
			<span class="slider-span">设置</span>
		</a>
	</li>
	<li class="slider-li">
		<a href="#"  class="slider-a">
			<i class="el-icon-user"></i>
			<span class="slider-span">使用者</span>
		</a>
	</li>
</ul>

<details>
	<summary>如何写文本描述？<i class="ai-question-fill"></i></summary>
	<div>
			<p>以下是<strong>文生视频</strong>构建提示词的关键组成部分：

<code>&lt;提示词 = (镜头语言 +景别角度+ 光影) + 主体 (主体描述) + 主体运动 +场景 (场景描述) + (氛围) &gt;</code> 
 </p>
		<p>
      <pre>
        <code><strong>镜头语言</strong>: 通过镜头的各种应用以及镜头之间的衔接和切换来传达故事或信息，并创造出特定的视觉效果和情感氛围。如镜头平移，推近、拉远、升降拍摄、摇摄、跟随拍摄、手持拍摄、无人机航拍等;
景别角度：控制相机与被摄对象之间距离和角度，实现不同的视觉效果和情感表达。如大全景、中景、近景 、鸟瞰视角 、跟随视角、鱼眼效果等;
<strong>光影</strong>: 光影是赋予摄影作品灵魂的关键元素，光影的运用可以使照片更具深度，更具情感，我们可以通过光影创造出富有层次感和情感表达力的作品。如自然光、丁达尔效应、柔和散射、硬光直射 、逆光剪影、三点布光等;
<strong>主体</strong>: 主体是视频中的主要表现对象。如儿童、狮子、向日葵，汽车、城堡等;
<strong>主体描述</strong>: 对主体外貌细节和肢体姿态等的描述，如人物的服饰、动物的毛色、植物的颜色、物体的状态和建筑的风格;
<strong>主体运动</strong>: 对主体运动状态的描述，包括静止和运动等，运动状态不宜过于复杂，符合6s视频内可以展现的画面即可，
<strong>场景</strong>: 场景是主体所处的环境，包括前景、背景等;
<strong>场景描述</strong>: 对主体所处环境的细节描述。如都市环境、乡村风光、工业区等;
<strong>氛围</strong>: 对预期视频画面的氛围描述。如喧嚣繁忙、悬疑惊悚、宁静舒适等;</code></pre> </p>
<p>
  <strong>图生视频</strong>提示词建议使用“主体（背景）+ 运动描述”的表达方式。

</p>
</div>
</details>
</div>
</template>

<script>
export default {};
</script>

<style lang="scss" scope>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap");
//@import url("https://unpkg.com/akar-icons-fonts");
// *,
// *:after,
// *:before {
//   box-sizing: border-box;
// }

// body {
//   font-family: "Inter", sans-serif;
//   line-height: 1.5;
//   min-height: 100vh;
//   display: flex;
//   flex-direction: column;
//   align-items: center;
//   justify-content: center;
//   padding-top: 5vh;
//   padding-bottom: 5vh;
//   background-color: #f2f5f7;
// }
.slider-ai {
  font-family: "Inter", sans-serif;
  line-height: 1.5;
  min-height: 100vh;
  display: flex;
  // width:80px;
  flex-direction: column;
  align-items: baseline;
  justify-content: center;
  padding-top: 5vh;
  padding-bottom: 5vh;
  background-color: #f2f5f7;
}

.slider-ul {
  list-style: none;
  margin: 0;
  padding: 0;
  margin-left: 20px;
  margin-right: auto;
  background-color: #05043e;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 0.75rem;
  border-radius: 10px;
  box-shadow: 0 10px 50px 0 rgba(#05043e, 0.25);
}

.slider-li:nth-child(6) {
  margin-top: 5rem;
  padding-top: 1.25rem;
  border-top: 1px solid #363664;
}

.slider-li + .slider-li {
  margin-top: 0.75rem;
}

.slider-a {
  color: #fff;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 3rem;
  height: 3rem;
  border-radius: 8px;
  position: relative;
  &:hover,
  &:focus,
  &.active {
    background-color: #30305a;
    outline: 0;

    .slider-span {
      transform: scale(1);
      opacity: 1;
    }
  }

  i {
    font-size: 1.375rem;
  }

  .slider-span {
    position: absolute;
    background-color: #30305a;
    white-space: nowrap;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    left: calc(100% + 1.5rem);
    transform-origin: center left;
    transform: scale(0);
    opacity: 0;
    transition: 0.15s ease;
    &:before {
      content: "";
      display: block;
      width: 12px;
      height: 12px;
      position: absolute;
      background-color: #30305a;
      left: -5px;
      top: 50%;
      transform: translatey(-50%) rotate(45deg);
      border-radius: 3px;
    }
  }
}

details {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  margin-top: 2rem;
  color: #05043e;
  display: flex;
  flex-direction: column;

  div {
    background-color: #fff;
    box-shadow: 0 5px 10px rgba(#000, 0.15);
    padding: 1.25rem;
    border-radius: 8px;
    position: absolute;
    max-height: calc(100vh - 100px);
    width: 400px;
    max-width: calc(100vw - 2rem);
    bottom: calc(100% + 1rem);
    right: 0;
    overflow: auto;
    transform-origin: 100% 100%;
    &::-webkit-scrollbar {
      width: 15px;
      background-color: #fff;
    }

    &::-webkit-scrollbar-thumb {
      width: 5px;
      border-radius: 99em;
      background-color: #ccc;
      border: 5px solid #fff;
    }
    & > * + * {
      margin-top: 0.75em;
    }

    p > code {
      font-size: 1rem;
      font-family: monospace;
      color: #185adb;
      font-weight: 600;
    }

    pre {
      white-space: pre-line;
      background-color: #f9f9f9;
      border: 1px solid #95a3b9;
      border-radius: 6px;
      font-family: monospace;
      padding: 0.75em;
      font-size: 0.875rem;
      // color: #fff;
    }
  }

  &[open] div {
    animation: scale 0.25s ease;
  }
}

summary {
  display: inline-flex;
  margin-left: auto;
  margin-right: auto;
  justify-content: center;
  align-items: center;
  font-weight: 600;
  padding: 0.625em 1.25em 0.625em 1.25em;
  border-radius: 99em;
  color: #fff;
  background-color: #185adb;
  box-shadow: 0 5px 15px rgba(#000, 0.1);
  list-style: none;
  text-align: center;
  cursor: pointer;
  transition: 0.15s ease;
  position: relative;
  &::-webkit-details-marker {
    display: none;
  }

  &:hover,
  &:focus {
    background-color: mix(#000, #185adb, 20%);
    // color: #6366f1;
  }

  i {
    font-size: 1.375em;
    margin-left: 0.25em;
  }
}

@keyframes scale {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1);
  }
}
</style>