<template>
  <div class="hero is-large is-light">
    <section class="section">
      <div class="columns">
        <div class="column"></div>
        <div class="column is-one-third">
          <h1 class="title">后台数据管理</h1>
          <p class="subtitle">
            中国城市国际传播大数据智能分析平台<strong></strong>
          </p>

          <div class="box" id="loginVue">
            <form asp-action="Login">
              <div
                asp-validation-summary="ModelOnly"
                class="help is-danger"
              ></div>

              <div class="field">
                <div class="control">
                  <div class="select">
                    <select
                      v-model="selected"
                      v-on:change="notNeeded(selected)"
                      required
                    >
                      <option value="">I am ...</option>
                      <option value="E">An Employee</option>
                      <option value="D">A Dealer</option>
                    </select>
                  </div>
                </div>
                <span
                  asp-validation-for="UserType"
                  class="help is-danger"
                ></span>
              </div>

              <div class="field">
                <label asp-for="Username" class="label">账号</label>
                <div class="control">
                  <input
                    asp-for="Username"
                    v-model.trim="username"
                    class="input"
                    type="text"
                    required
                  />
                </div>
                <span
                  asp-validation-for="Username"
                  class="help is-danger"
                ></span>
              </div>

              <div class="field">
                <label asp-for="Password" class="label">密码</label>
                <div class="control">
                  <input
                    asp-for="Password"
                    v-model.trim="password"
                    class="input"
                    type="password"
                    required
                  />
                </div>
                <span
                  asp-validation-for="Password"
                  class="help is-danger"
                ></span>
              </div>

              <div class="field">
                <label asp-for="Account" class="label">Account #</label>
                <div class="control">
                  <input
                    asp-for="Account"
                    class="input"
                    type="text"
                    v-model.trim="account"
                    :disabled="isDisabled"
                    required
                  />
                </div>
                <span
                  asp-validation-for="Account"
                  class="help is-danger"
                ></span>
              </div>

              <div class="field">
                <div class="control">
                  <button @click="login()">
                    <div class="svg-wrapper-1">
                      <div class="svg-wrapper">
                        <!-- <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 24 24"
                          width="24"
                          height="24"
                        >
                          <path fill="none" d="M0 0h24v24H0z"></path>
                          <path
                            fill="currentColor"
                            d="M1.946 9.315c-.522-.174-.527-.455.01-.634l19.087-6.362c.529-.176.832.12.684.638l-5.454 19.086c-.15.529-.455.547-.679.045L12 14l6-8-8 6-8.054-2.685z"
                          ></path>
                        </svg> -->
                        <svg class="svgIcon" viewBox="0 0 384 512">
                          <path
                            d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2V448c0 17.7 14.3 32 32 32s32-14.3 32-32V141.2L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"
                          ></path>
                        </svg>
                      </div>
                    </div>
                    <span>登录</span>
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="column"></div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "Login",
  data: {
    selected: "",
    account: "",
    toggle: false,
  },
  computed: {
    isDisabled() {
      return this.toggle;
    },
  },
  methods: {
    notNeeded: function () {
      if (this.selected == "E") {
        this.toggle = true;
      } else {
        this.toggle = false;
      }
    },
    login(){
        this.$router.push({ name: "后台管理" });
    }
  },
};
</script>

<style lang="scss" scope>
/* From Uiverse.io by adamgiebl */
button {
  font-family: inherit;
  font-size: 15px;
  background: royalblue;
  color: white;
  padding: 0.7em 1em;
  padding-left: 0.9em;
  display: flex;
  align-items: center;
  border: none;
  border-radius: 8px;
  overflow: hidden;
  transition: all 0.2s;
  cursor: pointer;
}

button span {
  display: block;
  margin-left: 0.3em;
  transition: all 0.3s ease-in-out;
}

button svg {
  display: block;
  transform-origin: center center;
  transition: transform 0.3s ease-in-out;
}

button:hover .svg-wrapper {
  animation: fly-1 0.6s ease-in-out infinite alternate;
}

button:hover svg {
  transform: translateX(1.2em) rotate(45deg) scale(1.1);
}

button:hover span {
  transform: translateX(5em);
}

button:active {
  transform: scale(0.95);
}

@keyframes fly-1 {
  from {
    transform: translateY(0.1em);
  }

  to {
    transform: translateY(-0.1em);
  }
}

.svgIcon {
  width: 12px;
  transition-duration: 0.3s;
}

.svgIcon path {
  fill: white;
}

// 布局
.section {
  padding: 16rem 1.5rem;
}
.hero is-large is-light{
    height: 100%;
}
</style>