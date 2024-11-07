<template>

<!-- https://codepen.io/Hyperplexed/pen/QOeQNK -->

<div id="chat-wrapper">
  <div id="chat-bot-mood">
    <div id="chat-bot-mood-icon"></div>
    <div id="chat-bot-mood-label">
      <h1 id="chat-bot-mood-text">Chatbot is feeling</h1>
      <h1 id="chat-bot-mood-value">Mood</h1>
    </div>
  </div>
  <div id="letter-pool"></div>
  <div id="temp-letter-pool"></div>
  <div id="letter-overlay"></div>
  <div id="chat-message-window">
    <div id="message-input-wrapper">
      <div id="message-input">
        <input id="message-input-field" type="text" placeholder="Type a message" maxlength="100"/>
        <div id="send-message-button"><i class="far fa-arrow-alt-circle-right"></i></div>
      </div>
    </div>
    <div class="scroll-bar" id="chat-message-column-wrapper">
      <div class="static" id="chat-message-column"></div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "ChatWin",
  mounted() {
    const LETTER_POOL = getEl("letter-pool"),
  TEMP_LETTER_POOL = getEl("temp-letter-pool"),
  LETTER_OVERLAY = getEl("letter-overlay"),
  CHAT_MESSAGE_COLUMN_WRAPPER = getEl("chat-message-column-wrapper"),
  CHAT_MESSAGE_COLUMN = getEl("chat-message-column"),
  MESSAGE_INPUT = getEl("message-input"),
  MESSAGE_INPUT_FIELD = getEl("message-input-field"),
  CHAT_BOT_MOOD = getEl("chat-bot-mood"),
  CHAT_BOT_MOOD_VALUE = getEl("chat-bot-mood-value");

const STATE = {
  isUserSendingMessage: false,
  isChatBotSendingMessage: false,
  letterPool: {
    transitionPeriod: 30000,
    intervals: []
  },
  moods: ["friendly", "suspicious", "boastful"],
  currentMood: "",
  chatbotMessageIndex: 0,
  nLetterSets: 4
};

const getRandMood = () => {
  const rand = getRand(1, 3);
  return STATE.moods[rand - 1];
};

const setChatbotMood = () => {
  STATE.currentMood = getRandMood();
  for (let i = 0; i < STATE.moods.length; i++) {
    removeClass(CHAT_BOT_MOOD, STATE.moods[i]);
  }
  addClass(CHAT_BOT_MOOD, STATE.currentMood);
  CHAT_BOT_MOOD_VALUE.innerHTML = STATE.currentMood;
};

const getRandGreeting = () => {
  let rand = 0;
  switch (STATE.currentMood) {
    case "friendly":
      rand = getRand(1, greetings.friendly.length);
      return greetings.friendly[rand - 1];
    case "suspicious":
      rand = getRand(1, greetings.suspicious.length);
      return greetings.suspicious[rand - 1];
    case "boastful":
      rand = getRand(1, greetings.boastful.length);
      return greetings.boastful[rand - 1];
    default:
      break;
  }
};

const getRandConvo = () => {
  let rand = 0;
  switch (STATE.currentMood) {
    case "friendly":
      rand = getRand(1, convo.friendly.length);
      return convo.friendly[rand - 1];
    case "suspicious":
      rand = getRand(1, convo.suspicious.length);
      return convo.suspicious[rand - 1];
    case "boastful":
      rand = getRand(1, convo.boastful.length);
      return convo.boastful[rand - 1];
    default:
      break;
  }
};

const createLetter = (cName, val) => {
  const letter = document.createElement("div");
  addClass(letter, cName);
  setAttr(letter, "data-letter", val);
  letter.innerHTML = val;
  return letter;
};

const getAlphabet = (isUpperCase) => {
  let letters = [];
  for (let i = 65; i <= 90; i++) {
    let val = String.fromCharCode(i),
      letter = null;
    if (!isUpperCase) val = val.toLowerCase();
    letter = createLetter("pool-letter", val);
    letters.push(letter);
  }
  return letters;
};

const startNewLetterPath = (letter, nextRand, interval) => {
  clearInterval(interval);
  nextRand = getRandExcept(1, 4, nextRand);
  let nextPos = getRandPosOffScreen(nextRand),
    transitionPeriod = STATE.letterPool.transitionPeriod,
    delay = getRand(0, STATE.letterPool.transitionPeriod),
    transition = `left ${transitionPeriod}ms linear ${delay}ms, top ${transitionPeriod}ms linear ${delay}ms, opacity 0.5s`;
  setElPos(letter, nextPos.x, nextPos.y);
  setStyle(letter, "transition", transition);
  interval = setInterval(() => {
    startNewLetterPath(letter, nextRand, interval);
  }, STATE.letterPool.transitionPeriod + delay);
  STATE.letterPool.intervals.push(interval);
};

const setRandLetterPaths = (letters) => {
  for (let i = 0; i < letters.length; i++) {
    let letter = letters[i],
      startRand = getRand(1, 4),
      nextRand = getRandExcept(1, 4, startRand),
      startPos = getRandPosOffScreen(startRand),
      nextPos = getRandPosOffScreen(nextRand),
      transitionPeriod = STATE.letterPool.transitionPeriod,
      delay = getRand(0, STATE.letterPool.transitionPeriod) * -1,
      transition = `left ${transitionPeriod}ms linear ${delay}ms, top ${transitionPeriod}ms linear ${delay}ms, opacity 0.5s`;

    setElPos(letter, startPos.x, startPos.y);
    setStyle(letter, "transition", transition);
    addClass(letter, "invisible");
    LETTER_POOL.appendChild(letter);
    setTimeout(() => {
      setElPos(letter, nextPos.x, nextPos.y);
      removeClass(letter, "invisible");
      let interval = setInterval(() => {
        startNewLetterPath(letter, nextRand, interval);
      }, STATE.letterPool.transitionPeriod + delay);
    }, 1);
  }
};

const fillLetterPool = (nSets = 1) => {
  for (let i = 0; i < nSets; i++) {
    const lCaseLetters = getAlphabet(false),
      uCaseLetters = getAlphabet(true);
    setRandLetterPaths(lCaseLetters);
    setRandLetterPaths(uCaseLetters);
  }
};

const findMissingLetters = (letters, lCount, isUpperCase) => {
  let missingLetters = [];
  for (let i = 65; i <= 90; i++) {
    let val = isUpperCase
        ? String.fromCharCode(i)
        : String.fromCharCode(i).toLowerCase(),
      nLetter = letters.filter((letter) => letter === val).length;
    if (nLetter < lCount) {
      let j = nLetter;
      while (j < lCount) {
        missingLetters.push(val);
        j++;
      }
    }
  }
  return missingLetters;
};

const replenishLetterPool = (nSets = 1) => {
  const poolLetters = LETTER_POOL.childNodes;
  let charInd = 65,
    currentLetters = [],
    missingLetters = [],
    lettersToAdd = [];

  for (let i = 0; i < poolLetters.length; i++) {
    currentLetters.push(poolLetters[i].dataset.letter);
  }
  missingLetters = [
    ...missingLetters,
    ...findMissingLetters(currentLetters, nSets, false)
  ];
  missingLetters = [
    ...missingLetters,
    ...findMissingLetters(currentLetters, nSets, true)
  ];
  for (let i = 0; i < missingLetters.length; i++) {
    const val = missingLetters[i];
    lettersToAdd.push(createLetter("pool-letter", val));
  }
  setRandLetterPaths(lettersToAdd);
};

const clearLetterPool = () => {
  removeAllChildren(LETTER_POOL);
};

const scrollToBottomOfMessages = () => {
  CHAT_MESSAGE_COLUMN_WRAPPER.scrollTop =
    CHAT_MESSAGE_COLUMN_WRAPPER.scrollHeight;
};

const checkMessageColumnHeight = () => {
  if (CHAT_MESSAGE_COLUMN.clientHeight >= window.innerHeight) {
    removeClass(CHAT_MESSAGE_COLUMN, "static");
  } else {
    addClass(CHAT_MESSAGE_COLUMN, "static");
  }
};

const appendContentText = (contentText, text) => {
  for (let i = 0; i < text.length; i++) {
    const letter = document.createElement("span");
    letter.innerHTML = text[i];
    setAttr(letter, "data-letter", text[i]);
    contentText.appendChild(letter);
  }
};

const createChatMessage = (text, isReceived) => {
  let message = document.createElement("div"),
    profileIcon = document.createElement("div"),
    icon = document.createElement("i"),
    content = document.createElement("div"),
    contentText = document.createElement("h1"),
    direction = isReceived ? "received" : "sent";

  addClass(content, "content");
  addClass(content, "invisible");
  addClass(contentText, "text");
  addClass(contentText, "invisible");
  appendContentText(contentText, text);
  content.appendChild(contentText);

  addClass(profileIcon, "profile-icon");
  addClass(profileIcon, "invisible");
  profileIcon.appendChild(icon);

  addClass(message, "message");
  addClass(message, direction);

  if (isReceived) {
    addClass(icon, "fab");
    addClass(icon, "fa-cloudsmith");
    addClass(message, STATE.currentMood);
    message.appendChild(profileIcon);
    message.appendChild(content);
  } else {
    addClass(icon, "far");
    addClass(icon, "fa-user");
    message.appendChild(content);
    message.appendChild(profileIcon);
  }

  return message;
};

const findLetterInPool = (targetLetter) => {
  let letters = LETTER_POOL.childNodes,
    foundLetter = null;
  for (let i = 0; i < letters.length; i++) {
    const nextLetter = letters[i];
    if (
      nextLetter.dataset.letter === targetLetter &&
      !nextLetter.dataset.found
    ) {
      foundLetter = letters[i];
      setAttr(foundLetter, "data-found", true);
      break;
    }
  }
  return foundLetter;
};

const createOverlayLetter = (val) => {
  const overlayLetter = document.createElement("span");
  addClass(overlayLetter, "overlay-letter");
  addClass(overlayLetter, "in-flight");
  overlayLetter.innerHTML = val;
  return overlayLetter;
};

const removePoolLetter = (letter) => {
  addClass(letter, "invisible");
  setTimeout(() => {
    removeChild(LETTER_POOL, letter);
  }, 500);
};

const setElPosFromRight = (el, x, y) => {
  setStyle(el, "right", x + "px");
  setStyle(el, "top", y + "px");
};

const animateOverlayLetter = (letter, contentText, finalPos, isReceived) => {
  removePoolLetter(letter);
  const initPos = letter.getBoundingClientRect(),
    overlayLetter = createOverlayLetter(letter.dataset.letter);
  if (isReceived) {
    setElPos(overlayLetter, initPos.left, initPos.top);
  } else {
    setElPosFromRight(
      overlayLetter,
      window.innerWidth - initPos.right,
      initPos.top
    );
  }
  LETTER_OVERLAY.appendChild(overlayLetter);
  setTimeout(() => {
    if (isReceived) {
      setElPos(overlayLetter, finalPos.left, finalPos.top);
    } else {
      setElPosFromRight(
        overlayLetter,
        window.innerWidth - finalPos.right,
        finalPos.top
      );
    }
    setTimeout(() => {
      //asdf
      removeClass(contentText, "invisible");
      addClass(overlayLetter, "invisible");
      setTimeout(() => {
        removeChild(LETTER_OVERLAY, overlayLetter);
      }, 1000);
    }, 1500);
  }, 100);
};

const animateMessageLetters = (message, isReceived) => {
  const content = message.getElementsByClassName("content")[0],
    contentText = content.getElementsByClassName("text")[0],
    letters = contentText.childNodes,
    textPos = contentText.getBoundingClientRect();
  for (let i = 0; i < letters.length; i++) {
    const letter = letters[i],
      targetLetter = findLetterInPool(letter.dataset.letter),
      finalPos = letter.getBoundingClientRect();
    if (targetLetter) {
      animateOverlayLetter(targetLetter, contentText, finalPos, isReceived);
    } else {
      const tempLetter = createLetter("temp-letter", letter.dataset.letter),
        pos = getRandPosOffScreen();
      addClass(tempLetter, "invisible");
      setElPos(tempLetter, pos.x, pos.y);
      TEMP_LETTER_POOL.appendChild(tempLetter);
      animateOverlayLetter(tempLetter, contentText, finalPos, isReceived);
      setTimeout(() => {
        removeChild(TEMP_LETTER_POOL, tempLetter);
      }, 100);
    }
  }
};

const addChatMessage = (text, isReceived) => {
  const message = createChatMessage(text, isReceived),
    content = message.getElementsByClassName("content")[0],
    contentText = content.getElementsByClassName("text")[0],
    profileIcon = message.getElementsByClassName("profile-icon")[0];
  CHAT_MESSAGE_COLUMN.appendChild(message);
  toggleInput();
  setTimeout(() => {
    removeClass(profileIcon, "invisible");
    setTimeout(() => {
      removeClass(content, "invisible");
      setTimeout(() => {
        animateMessageLetters(message, isReceived);
        setTimeout(() => replenishLetterPool(STATE.nLetterSets), 2500);
      }, 1000);
    }, 250);
  }, 250);
};

const checkIfInputFieldHasVal = () => MESSAGE_INPUT_FIELD.value.length > 0;

const clearInputField = () => {
  MESSAGE_INPUT_FIELD.value = "";
};

const disableInputField = () => {
  MESSAGE_INPUT_FIELD.blur();
  MESSAGE_INPUT_FIELD.value = "";
  MESSAGE_INPUT_FIELD.readOnly = true;
};

const enableInputField = () => {
  MESSAGE_INPUT_FIELD.readOnly = false;
  MESSAGE_INPUT_FIELD.focus();
};

const getChatbotMessageText = () => {
  if (STATE.chatbotMessageIndex === 0) {
    return getRandGreeting();
  } else {
    return getRandConvo();
  }
};

const sendChatbotMessage = () => {
  const text = getChatbotMessageText();
  STATE.isChatBotSendingMessage = true;
  addChatMessage(text, true);
  STATE.chatbotMessageIndex++;
  setTimeout(() => {
    STATE.isChatBotSendingMessage = false;
    toggleInput();
  }, 4000);
};

const sendUserMessage = () => {
  const text = MESSAGE_INPUT_FIELD.value;
  STATE.isUserSendingMessage = true;
  addChatMessage(text, false);
  setTimeout(() => {
    STATE.isUserSendingMessage = false;
    toggleInput();
  }, 4000);
};

const onEnterPress = (e) => {
  sendUserMessage();
  setTimeout(() => {
    sendChatbotMessage();
  }, 4000);
  toggleInput();
  clearInputField();
};

const initLetterPool = () => {
  clearLetterPool();
  fillLetterPool(STATE.nLetterSets);
};

const init = () => {
  setChatbotMood();
  initLetterPool();
  sendChatbotMessage();
  toggleInput();
  setMoodInterval(getRandMoodInterval());
};

let resetTimeout = null;
const resetLetterPool = () => {
  const intervals = STATE.letterPool.intervals;
  for (let i = 0; i < intervals.length; i++) {
    clearInterval(intervals[i]);
  }
  clearTimeout(resetTimeout);
  clearLetterPool();
  resetTimeout = setTimeout(() => {
    initLetterPool();
  }, 200);
};

const toggleInput = () => {
  if (checkIfInputFieldHasVal() && canSendMessage()) {
    addClass(MESSAGE_INPUT, "send-enabled");
  } else {
    removeClass(MESSAGE_INPUT, "send-enabled");
  }
};

const isValidLetter = (e) => {
  return (
    !e.ctrlKey &&
    e.key !== "Enter" &&
    e.keyCode !== 8 &&
    e.keyCode !== 9 &&
    e.keyCode !== 13
  );
};

const canSendMessage = () =>
  !STATE.isUserSendingMessage && !STATE.isChatBotSendingMessage;

const getRandMoodInterval = () => getRand(20000, 40000);

let moodInterval = null;
const setMoodInterval = (time) => {
  moodInterval = setInterval(() => {
    clearInterval(moodInterval);
    setChatbotMood();
    setMoodInterval(getRandMoodInterval());
  }, time);
};

MESSAGE_INPUT_FIELD.onkeypress = (e) => {
  if (checkIfInputFieldHasVal() && e.key === "Enter") {
    removeClass(MESSAGE_INPUT, "send-enabled");
    if (canSendMessage()) {
      onEnterPress(e);
    }
  }
};

MESSAGE_INPUT_FIELD.onkeyup = () => {
  toggleInput();
};

MESSAGE_INPUT_FIELD.oncut = () => toggleInput();

window.onload = () => init();

window.onfocus = () => resetLetterPool();

window.onresize = _.throttle(resetLetterPool, 200);

const greetings = {
  friendly: [
    "Hiya, pal. I hope you're having a terrific day!",
    "Good day to you, friend!"
  ],
  suspicious: [
    "Hmm, I would introduce myself, but I'm not so sure thats a good idea.",
    "Hello, how are you? Wait, don't answer that, I have no way of verifying your response!"
  ],
  boastful: [
    "Hey, did I mention I am built on JavaScript? Which is the greatest language ever by the way!",
    "Good day to you. Though I must say that I am having a GREAT day!"
  ]
};

const convo = {
  friendly: [
    "What a great thing you just said. I'm so glad you said it.",
    "Ahh, yes, I agree. It is so great to say things, isn't it?",
    "Please, tell me more. It brings me such joy to respond to the things you say.",
    "Ahh, yes valid point. Or was it? Either way, you're fantastic!",
    "Anyways, did I mention that I hope you're having a great day? If not, I hope it gets better!"
  ],
  suspicious: [
    "I just don't know if I can trust that thing you just said...",
    "Oh, interesting. I totally believe you. (Not really)",
    "Uh-huh, yeah, listen...I'm not going to fully invest in this conversation until I'm certain I know your motive.",
    "Wait, what the heck is that?? Oh, phewf, it's just another rogue letter 'R' that escaped the letter pool.",
    "You can't fool me, I know that's not true!"
  ],
  boastful: [
    "That's interesting. I'll have you know that I have an extremely advanced learning algorithm that analyzes everything you say...well, not really, but I wish.",
    "Hey, while I have you, I should probably tell you that I can respond in 4 seconds flat. Which is pretty fast if you ask me.",
    `Listen, that's neat and all, but look how fast I can calculate this math problem: 12345 * 67890 = ${
      12345 * 67890
    }. Didn't even break a sweat.`,
    "Oh, I forgot to mention that I've existed for over 100,000 seconds and that's something I'm quite proud of.",
    "Wow, thats pretty cool, but I can hold my breath for all of eternity. And it took me 0 seconds to gain that ability."
  ]
};

  },
};
</script>

<style lang="scss" scope>
$gray250: rgb(250, 250, 250);
$gray240: rgb(240, 240, 240);
$gray230: rgb(230, 230, 230);
$gray220: rgb(220, 220, 220);
$gray210: rgb(210, 210, 210);
$gray200: rgb(200, 200, 200);
$gray180: rgb(180, 180, 180);
$gray150: rgb(150, 150, 150);
$gray120: rgb(120, 120, 120);
$gray90: rgb(90, 90, 90);
$gray60: rgb(60, 60, 60);
$gray50: rgb(50, 50, 50);
$gray40: rgb(40, 40, 40);
$gray30: rgb(30, 30, 30);

$purple: rgb(171, 71, 188);
$darkPurple: rgb(74, 20, 140);
$blue: rgb(3, 169, 244);
$darkBlue: rgb(26, 35, 126);
$lightGreen: rgb(205, 220, 57);
$green: rgb(76, 175, 80);
$darkGreen: rgb(46, 125, 50);
$red: rgb(211, 47, 47);
$darkRed: rgb(183, 28, 28);
$orange: rgb(255, 111, 0);
$darkOrange: rgb(216, 67, 21);
$yellow: rgb(251, 192, 45);
$darkYellow: rgb(249, 168, 37);

$shadow1: rgba(0, 0, 0, 0.12) 0px 1px 6px, rgba(0, 0, 0, 0.12) 0px 1px 4px;
$shadow2: rgba(0, 0, 0, 0.16) 0px 3px 10px, rgba(0, 0, 0, 0.23) 0px 3px 10px;
$shadow3: rgba(0, 0, 0, 0.19) 0px 10px 30px, rgba(0, 0, 0, 0.23) 0px 6px 10px;

@mixin center {
  left: 50%;
  position: absolute;
  top: 50%;
  transform: translateX(-50%) translateY(-50%);
}

html,
body {
  font-family: "Roboto", sans-serif;
  height: 100%;
  margin: 0px;
  overflow: hidden;
  padding: 0px;
  width: 100%;
}

.invisible {
  opacity: 0;
}

.scroll-bar {
  &::-webkit-scrollbar {
    background-color: $gray200;
    width: 2px;
  }

  &::-webkit-scrollbar-thumb {
    background-color: $gray90;
  }
}

#chat-wrapper {
  background-color: white;
  height: 100%;
  overflow: hidden;
  width: 100%;

  #chat-bot-mood {
    left: 0px;
    padding: 20px;
    position: absolute;
    top: 0px;
    white-space: nowrap;
    z-index: 10;

    &.friendly {
      #chat-bot-mood-icon {
        background: linear-gradient(to right, $blue, $green);
      }

      #chat-bot-mood-label {
        #chat-bot-mood-value {
          color: $blue;
        }
      }
    }

    &.suspicious {
      #chat-bot-mood-icon {
        background: linear-gradient(to right, $red, $orange);
      }

      #chat-bot-mood-label {
        #chat-bot-mood-value {
          color: $red;
        }
      }
    }

    &.boastful {
      #chat-bot-mood-icon {
        background: linear-gradient(to right, $orange, $yellow);
      }

      #chat-bot-mood-label {
        #chat-bot-mood-value {
          color: $orange;
        }
      }
    }

    #chat-bot-mood-icon {
      border-radius: 30px;
      box-shadow: $shadow1;
      display: inline-block;
      height: 30px;
      margin-left: 10px;
      vertical-align: top;
      width: 30px;
    }

    #chat-bot-mood-label {
      background-color: white;
      border-radius: 20px;
      box-shadow: $shadow1;
      display: inline-block;
      height: 20px;
      margin-left: 5px;
      padding: 5px 15px;
      vertical-align: top;
      h1 {
        display: inline-block;
        font-size: 0.9em;
        font-weight: 300;
        height: 20px;
        line-height: 20px;
        margin: 0px;
        vertical-align: top;
      }

      #chat-bot-mood-text {
        color: $gray60;
      }
    }
  }

  #letter-pool,
  #temp-letter-pool {
    backface-visibility: hidden;
    height: 100%;
    left: 0px;
    overflow: hidden;
    position: absolute;
    top: 0px;
    user-select: none;
    width: 100%;
    z-index: 1;

    .pool-letter,
    .temp-letter {
      color: $gray210;
      display: inline-block;
      font-weight: 300;
      position: absolute;
    }
  }

  #letter-overlay {
    height: 100%;
    left: 0px;
    pointer-events: none;
    position: absolute;
    top: 0px;
    width: 100%;
    z-index: 5;

    .overlay-letter {
      color: $gray210;
      font-weight: 300;
      position: absolute;
      transition: all 1.5s, opacity 0.5s;
      transition-timing-function: ease-in-out;

      &.in-flight {
        animation: pulse-letter 1s ease-in-out;
        color: $gray210;
      }
    }
  }

  #chat-message-window {
    height: 100%;
    left: 0px;
    min-width: 600px;
    overflow: hidden;
    position: absolute;
    top: 0px;
    width: 100%;
    z-index: 2;

    #message-input-wrapper {
      bottom: 0px;
      height: 90px;
      left: 0px;
      position: absolute;
      width: 100%;
      z-index: 2;

      #message-input {
        @include center;
        background-color: white;
        border-radius: 100px;
        box-shadow: $shadow1;
        height: 50px;
        line-height: 50px;
        overflow: hidden;
        width: 500px;

        &.send-enabled {
          #send-message-button {
            &:before,
            &:after {
              @include center;
              animation: pulse 2s ease-in-out infinite;
              border-radius: 100px;
              content: "";
              height: 30px;
              width: 30px;
            }

            i {
              color: $blue;
            }
          }
        }

        #message-input-field {
          border: none;
          color: $gray180;
          font-size: 1em;
          font-weight: 300;
          margin-left: 20px;
          outline: none;
          width: 430px;

          &::placeholder {
            color: $gray180;
          }
        }

        #send-message-button {
          cursor: pointer;
          height: 50px;
          position: absolute;
          right: 0px;
          text-align: center;
          top: 0px;
          width: 50px;

          i {
            color: $gray230;
            height: 50px;
            line-height: 50px;
            font-size: 2em;
            transition: all 0.5s;
            width: 50px;
          }
        }
      }
    }

    #chat-message-column-wrapper {
      bottom: 0px;
      height: 100%;
      left: 0px;
      overflow: hidden;
      position: absolute;
      width: 100%;
      z-index: 1;

      #chat-message-column {
        bottom: 0px;
        left: 0px;
        min-height: 70px;
        margin-bottom: 70px;
        overflow: hidden;
        padding: 20px 20px 0px 20px;
        width: calc(100% - 40px);

        &.static {
          position: absolute;
        }

        .message {
          animation: expand 0.5s ease-in-out;
          margin-bottom: 20px;
          white-space: nowrap;

          &.received {
            text-align: left;

            &.friendly {
              .profile-icon {
                background: linear-gradient(to right, $blue, $green);
              }
            }

            &.suspicious {
              .profile-icon {
                background: linear-gradient(to right, $red, $orange);
              }
            }

            &.boastful {
              .profile-icon {
                background: linear-gradient(to right, $orange, $yellow);
              }
            }

            .profile-icon {
              i {
                font-size: 1.5em;
                &:before {
                  display: inline-block;
                  transform: rotate(90deg);
                }
              }
            }

            .content {
              animation: bounceInLeft 1s ease-in-out;
              animation-delay: 0.5s;
              margin-left: 20px;
            }
          }

          &.sent {
            text-align: right;

            .profile-icon {
              background: linear-gradient(to right, $purple, $blue);

              i {
                font-size: 1.25em;
              }
            }

            .content {
              animation: bounceInRight 1s ease-in-out;
              animation-delay: 0.5s;
              margin-right: 20px;
            }
          }

          .profile-icon {
            animation: bounceIn 1s ease-in-out;
            animation-delay: 0.25s;
            border-radius: 100px;
            box-shadow: $shadow1;
            display: inline-block;
            height: 50px;
            position: relative;
            vertical-align: top;
            width: 50px;
            z-index: 2;

            i {
              color: white;
              height: 50px;
              line-height: 50px;
              text-align: center;
              width: 50px;
            }
          }

          .content {
            background-color: white;
            border-radius: 25px;
            box-shadow: $shadow1;
            display: inline-block;
            max-width: 300px;
            padding: 15px 20px;
            position: relative;
            text-align: left;
            transition: all 0.5s;
            vertical-align: top;
            white-space: normal;
            z-index: 1;

            .text {
              color: $gray180;
              font-size: 1em;
              font-weight: 300;
              margin: 0px;
              min-height: 20px;
              transition: all 0.5s;
              word-wrap: break-word;

              span {
                height: 20px;
              }
            }
          }
        }
      }
    }
  }
}

@keyframes flash-dot {
  from,
  to {
    background-color: rgba($gray200, 1);
  }
  50% {
    background-color: rgba($gray200, 0.5);
  }
}

@keyframes expand {
  from {
    max-height: 0px;
  }
  to {
    max-height: 200px;
  }
}

@keyframes bounceIn {
  from,
  20%,
  40%,
  60%,
  80%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    transform: scale3d(1, 1, 1);
  }
}

@keyframes bounceInUp {
  from,
  60%,
  75%,
  90%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  from {
    opacity: 0;
    transform: translate3d(0, 3000px, 0);
  }

  60% {
    opacity: 1;
    transform: translate3d(0, -20px, 0);
  }

  75% {
    transform: translate3d(0, 10px, 0);
  }

  90% {
    transform: translate3d(0, -5px, 0);
  }

  to {
    transform: translate3d(0, 0, 0);
  }
}

@keyframes bounceInLeft {
  from,
  60%,
  75%,
  90%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    transform: translate3d(-3000px, 0, 0);
  }

  60% {
    opacity: 1;
    transform: translate3d(25px, 0, 0);
  }

  75% {
    transform: translate3d(-10px, 0, 0);
  }

  90% {
    transform: translate3d(5px, 0, 0);
  }

  to {
    transform: none;
  }
}

@keyframes bounceInRight {
  from,
  60%,
  75%,
  90%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  from {
    opacity: 0;
    transform: translate3d(3000px, 0, 0);
  }

  60% {
    opacity: 1;
    transform: translate3d(-25px, 0, 0);
  }

  75% {
    transform: translate3d(10px, 0, 0);
  }

  90% {
    transform: translate3d(-5px, 0, 0);
  }

  to {
    transform: none;
  }
}

@keyframes bounceOutRight {
  20% {
    opacity: 1;
    transform: translate3d(-20px, 0, 0);
  }

  to {
    opacity: 0;
    transform: translate3d(2000px, 0, 0);
  }
}

@keyframes pulse {
  0% {
    box-shadow: 0px 0px 0px 0px rgba($blue, 0.5);
  }
  100% {
    box-shadow: 0px 0px 0px 20px rgba($blue, 0);
  }
}

@keyframes pulse-letter {
  from,
  to {
    color: $gray210;
  }
  50% {
    color: $blue;
  }
}

</style>