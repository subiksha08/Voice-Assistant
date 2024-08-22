
const msgerForm = get(".msger-inputarea");
const msgerChat = get(".msger-chat");
// Onclick of the button
const msgerInput = get(".msger-input");
const Listener = document.getElementById("listener");
const date = document.getElementById("date");
const day = document.getElementById("day");

// const BOT_IMG = "img/chatbot1.png";
const BOT_IMG = "linear-gradient(135deg, lightgreen 0%, lightgray 100%)";
const PERSON_IMG = "linear-gradient(45deg, lightgray 0%, lightgreen 100%)";
// const PERSON_IMG = "img/panda.png";
let BOT_NAME = "Zara"
const PERSON_NAME = "User";

themes = [
    [
        'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)',
        'linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%)',
        '#fff',
        '#000',
        '2px solid #ddd',
        '#ececec',
        '#579ffb',
        'none',
        'rgb(0, 180, 50)',
        '#ddd',
        '#eee',
        '#666',
        '#bdbdbd',
        'rgba(0, 0, 0, 0.2)',
    ],
    [
        'linear-gradient(326deg, #ea365d 0%, #f387b0 74%)',
        'lightpink',
        '#fff',
        '#ffae6f',
        '2px solid #f387b0',
        '#fff',
        '#f387b0',
        '2px solid #ffae6f',
        '#ffae6f',
        '#fff',
        '#fff',
        '#ffae6f',
        '#ffae6f',
        'rgba(255, 255, 255, 0.7)',
    ]

]

let ary = ['--body-bg', '--img-bg:', '--msger-bg', '--msger-bg1', '--border', '--left-msg-bg', '--right-msg-bg', '--msg-box-border', '--theme-box-color', '--theme-box-color1', '--theme-box-color2', '--theme-text-color', '--theme-text-color1', '--theme-shadow-color']


document.querySelector(".btn").onclick = async function () {
    // js_Day()
    eel.random_python('0')
}

// document.querySelector("#stop").onclick = async function () {
//     // js_Day()
//     eel.stop()
// }

// Icons made by Freepik from www.flaticon.com
// const BOT_IMG = "https://image.flaticon.com/icons/svg/327/327779.svg";
// const PERSON_IMG = "https://image.flaticon.com/icons/svg/145/145867.svg";

eel.expose(nameJs)
function nameJs(name, bol) {
    BOT_NAME = name
    let ind = 0

    if (bol % 2 == 1) {
        ind = 0
    }

    if (bol % 2 == 0) {
        ind = 1
    }

    // ary.forEach((element, index) => {
    //     let style = themes[ind][index]
    //     document.documentElement.style.setProperty(element, style);
    // });
    console.log(ind);
}


eel.expose(js_rightbox)
function js_rightbox(text) {
    if (text != '')
        appendMessage(PERSON_NAME, PERSON_IMG, "right", '', text, '');
}

eel.expose(js_listenebox)
function js_listenebox(text) {
    Listener.innerHTML = `<span class="listener">${text}</span>`
}

eel.expose(js_inputBox)
function js_inputBox(text) {
    text = window.prompt(`Somtimes Typing is better than you want to convay by saying \n ${text}`)
    // setTimeout(js_inputBox,5000)
    console.log(text);
    return text
}

eel.expose(js_Day)
function js_Day() {
    const dates = new Date()
    let day = `${dates.getDate()}/${dates.getMonth()}/${dates.getFullYear()}`
    let date = `${dates.toLocaleString('en-US', { hour: 'numeric', hour12: true, minute: 'numeric', second: '2-digit' })}`
    day.innerHTML = day
    date.innerHTML = date
    setTimeout(js_Day, 1000);
}


msgerForm.addEventListener("submit", event => {
    event.preventDefault();
    js_rightbox('')
});


function appendMessage(name, img, side, src, text, url) {
    if (text != '') {
        console.log(img);

        //   Simple solution for small apps
        const msgHTML = `
        <div class="msg ${side}-msg">
        <div class="msg-img" style="background: ${img} "></div>
        <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

            <div class="msg-text">
                ${(src != '') ? `<img src="${src}" alt="${src}" class="img-box"><br><br>` : ''}
                ${text}
                ${(url != '') ? `<a style='margin-top:5px' href="${url}" target='_blank'>${url}</a>` : ''}
            </div>
        </div>
        </div>
        `;

        msgerChat.insertAdjacentHTML("beforeend", msgHTML);
        msgerChat.scrollTop += 500;
    }
}

eel.expose(js_textbox)
function js_textbox(text) {
    if (text == '1') {
        text = ''
    }
    appendMessage(BOT_NAME, BOT_IMG, "left", '', text, '');
}

eel.expose(js_imgbox)
function js_imgbox(src, text, url) {
    if (text == '1') {
        text = ''
    }
    appendMessage(BOT_NAME, BOT_IMG, "left", src, `<h2>${text}</h2>`, url);
}

// Utils
function get(selector, root = document) {
    return root.querySelector(selector);
}

function formatDate(date) {
    const h = "0" + date.getHours();
    const m = "0" + date.getMinutes();

    return `${h.slice(-2)}:${m.slice(-2)}`;
}

function random(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}
//# sourceURL=pen.js
