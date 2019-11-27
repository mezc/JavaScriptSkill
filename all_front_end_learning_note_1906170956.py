1.v-bind 是单向数据绑定，简写 ”:“,v-model是双向数据绑定

v-if ,v-show

v-if=""
如果为true，相当于appendChild
false：相当于removeChild

v-show:
true:oDiv.style.display = "block
false:oDiv.style.display = "none"

v-on:原生js的事件名=”逻辑“
v-on:原生js事件名=“方法名”，该方法必须在methods
简写：@

v-bind:xxx=''
v-bind：标签中原生属性
v-bind:自定义属性

v-model 只能应用在表单控件 ui控件中

2.webpack安装在开发环境下:cnpm i webpack@3 --save-dev

3.webpack:
//1.执行webpack时识别webpack.config.js
//2.使用其他文件名，更改脚本
scripts:{
    "dev":"webpack --config ./webpack.dev.config.js"
}
//3.css-loader:
cnpm i css-loader style-loader -D
//4.处理图片的loader
cnpm i url-loader file-loader -D
//处理图片时，设置合理的limit很有必要
limit小于图片大小时，显示的是url 
//5.less-loader:
cnpm i less-loader less -D
//6.配置dist
在config.js中，具体见 05less-loader/webpack.dev.config.jss
//7.html-webpack-plugin:
cnpm i html-webpack-plugin@2 -D
参照物里的index.html自动打包到dist里，并且在html中不用导入build.js
//8.webpack-dev-server:
webpack-dev-server:
--open 自动打开浏览器
--hot 热更新，不在刷新的情况下替换css样式
--inline 自动刷新
--port 9999 指定端口
--process 显示编译进度
//在package.json文件中配置：
"scripts":{
    "dev":"webpack-dev-server --open --hot --inline --config ./webpack.dev.config.js",
    "pro":"webpack --config ./webpack.pro.config.js"
}
//npm run dev 
//9es6解析
cnpm i babel-core babel-loader@7 panel-preset-env babel-plugin-transform-runtime -D
//在webpack-dev-config.js文件中配置：
loader:{
    //处理es6，7，8
    test:/\.js$/,
    loader:"babel-loader",
    options:{
        presets:["env"],
        plugins:["transform-runtime"]
    }
}
//10解析.vue的loader：
cnpm i vue-loader@14 vue-template-compiler@2 -D
//配置vue文件：
{
    test:/\.vue$/,
    loader:"vue-loader"
}
//main.js:
new Vue({
    el:"#app",
    render:c=>c(App)
})


4.$emit $on 必须绑定一个公共的是实例，才能够触发。
新建
//公有vue实例
var Event = new Vue();

5.vue-cli,需要安装全局
cnpm i -g vue-cli

//拉取vue-cli 2,全局安装桥接工具
cnpm i -g @vue/cli-init
//vue-cli@2:

//vue init 模版名 项目名
//vue init webpack my-project


//vue-cli 支持的模块有：
webpack,webpack-simple,browserify,browserify-simple,pwa,simple

6.vue-cli相关文件介绍：
//build文件夹：里面对webpack开发和打包的相关配置，包括入口文件，输出文件，使用的模块

//config文件夹：指定开发和打包的静态资源，要压缩的文件类型，开发使用的端口号，开发使用虚拟服务器跨域请求api

//.editorconfig:代码规范文件，规定使用空格/tab缩进，缩进长度是两位四位的代码风格

//src
//main.js:整个项目的入口文件
//App.vue:入口组件
//router:路由模块
//components:公有组件
//assets:放置每个组件的静态资源|（static放置的是公有静态资源）

//router/index.js:
//此时的router是局部对象，必须使用Vue.use(Router),就可以在任意的组件中使用this.$router,this.$route

//设置顺序
//1新建是有组件文件夹
//1.1创建只有组件
//2router/index.js下配置路由
//3App.vue入口组件中配置

//config/index.js:整个文件的配置入口

//build/webpack.base.conf.js
//处理后缀名：
//resolve:{
    extensions:[
        ".js",".vue",".json"//以这几个后缀名可以省略不写
    ],
    alias:{//以一个别名代表一个路径
        "vue$":"vue/dist/vue.esm.js",
        "@":resolve("src")
    }
}


---------------------------------------------------------------

webpack-dev-server@2.9.1
webpack@3.4.1 


6.npm cnpm
安装cnpm:   npm install cnpm -g -registry

1.全局安装
npm i webpack -g
npm install  webpack@3.4.1  -g
版本4.x.x有问题
npm i webpack webpack-cli --save-dev

2.安装jquery
npm init -y
npm i jquery -S,这一步完成后生成了node_modules文件夹

3.
"scripts": {
    "dev":"webpack --mode development",
    "build":"webpack --mode production"
  },
  运行npm run build/ npm run dev

4.新建webpack.config.js 配置文件，设置 modules.exports={
    entry:path.join(__dirname,"相对路径"),//输出
    output:{
        path:path.join(__dirname,"相对路径")
        filename:"boundle.js"//输入
    }
}

5.
//cnpm i webpack-dev-server@2.9.1 -D 实现自动打包编译功能
//本地安装的依赖不能在命令行直接运行，需在package.json里scripts配置
//"scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev":"webpack-dev-server"
  },
//要求在本地安装webpack,命令为cnpm i webpack -D
npm install webpack@3.4.1 -D

//使用时用npm run dev,  html中js引用路径改成根路径，<script src="/boundle.js">

//webpack-dev-server自动打包生成的boundle.js文件并没有放到实际的物理磁盘上，而是直接托管到电脑内存中，所以在项目根目录中根本找不到打包好的boundle.js,存放目录与src,node_modules平级看不见的文件。
//通过服务器访问由webpack-dev-server的js包地址是：localhost:8080/boundle.js

7.不手动点击localhost:8080配置：
package.json 里配置：
"dev":"webpack-dev-server --open --port 3000 --contentBase src --hot"//手动打开浏览器//端口更改为3000//内容的根路径更改为src,意思是/localhost:3000/src,//--hot热重载，热更新，减少代码的更新,实现网页不重载就能局部刷新

8.配置dev-server的第二种方式，这种方式要麻烦些,

在webpack.config.js中配置：
第1步：
defServer:{
  open:true,//自动打开浏览器
  port:3000,//设置启动时候运行端口
  contentBase:"src",//指定托管的根目录
  hot:true//启用热更新
} 

第2步：
const webpack = require("webpack")

第3步：//new一个热更新的模块对象
plugins:[
  new webpack.HotModuleReplacemnetPlugin()
]

第4步：
package.json里；
"scripts":{
  "dev2":webpack-dev-server --open --port 3000 --contentBase src --hot,
  "dev":"webpack-dev-server"
}

第5步：
npm run dev

9.将页面放入内存中,安装插件
cnpm i html-webpack-plugin -D

//配置文件：
plugins:[new htmlWebpackPlugin({
template:path.join(__dirname,".src/index.html"),
filename:"index.html"})]

10.loader-配置处理css文件loader
// 1.处理css文件，安装cnpm i style-loader css-loader -D
// 2.webpack.config.js里新增一个配置节点，module，这个module对象上有rules属性，是数组，这个数组中存放了第三方文件的匹配和处理规则。
//3.webpack处理顺序，从后往前调用

11.loader处理less文件
cnpm i less-loader -D
cnpm i less@2.3.1 -D

12.loader处理scss文件
cnpm i sass-loader -D
cnpm i node-sass -D


13.
//webpack可以处理css/less/scss,不能处理带有url地址的样式
cnpm i url-loader file-loader -D

//{test:/\.(jpg|png|gif|bmp|jpeg)$/,use:"url-loader"}//处理图片路径的loader

14.安装bootstrap,注意用3的版本
cpm i bootstrap@3 -D
//使用时,去掉--contentBase src
"dev":"web pack-dev-server --open --port 3000 --hot
//main.js中导入：import "bootstrap/dist/css/bootstrap.css"
//通过路径形式引入node_modules中相关文件，可直接省略路径前面的node_modules这一层目录，直接写包的名称。然后跟上具体的文件路径
//webpack.config.js中
{test:/\.(ttf|eot|svg|woff|woff2)$/,use:"url-loader"}

15.静态属性：可以直接通过类名直接访问的属性
//实例属性：只能通过类的实例来访问的属性

15.//webpack需要借助第三方loader把高级语法转为低级语法后把结果交给webpack打包到bundle.js中
//1.1在webpack中可以通过babel将高级语法转换为低级语法
//通过安装如下两套包，安装babel相关loader功能
//第一套包转换工具：cnpm i babel-core babel-loader@7 babel-plugin-transform-runtime -D
//第二套包语法：cnpm i babel-preset-env babel-preset-stage-0 -D
//默认安装版本时babel-loader@8 ,注意版本不一致会导致运行错误，解决方法，降低babel版本npm install -D babel-loader@7
//2.1webpack.config.js中module节点下，rules数组中添加一个新的匹配规则
{test:/\.js$/,use:"babel-loader",exclude:/node_modules/}
//在配置babel时，必须把node_modules目录通过exclude排除掉，否则会将node_modules中的所有js文件打包编译。
//3.1在项目根目录中，新建一个.babelrc的配置文件，属于json格式
//内容为：
{
"presets":["env","stage-0"],
"plugins":["transform-runtime"]}
//目前安装的babel-preset-env是比较新的语法，之前安装的是babel-preset-es2015，-env包含了所有和es***相关的语法。


16.使用vue
//安装：cnpm i vue -D
//调用main.js:import Vue from "vue"
//import Vue from "vue"中导入的是node_modules/vue/package.json/main属性
//要导入全的包，第一种方式：import Vue from "../node_modules/vue/dist/vue.js"
//第二种方式，在web pack.config.js中，resolve:{alias:{"vue$":"vue/dist/vue.js"}}

17.使用vue组件
//在src下创建login.vue(此时main.js中可以使用import Vue from "vue")
//login.vue分成3部分：
<template></template>,<script></script>,<style></style>
//1导入组件，在main.js:import login from "./login.vue"
//2安装相关loader打包.vue文件：cnpm i vue-loader@14 ,vue-template-compiler -D
//备注vue-loader版本问题：
为了引入.vue文件，安装完vue-loader和vue-template-compiler后，运行报错：

vue-loader was used without the corresponding plugin.Make sure to include VueLoaderPlugin in your webpack config.

百度了一下，是因为vue-loader，15的版本需要再添加plugin的配置。有两种解决方法：

1.把安装版本改为14的

2.在webpack.config.js中添加：

const { VueLoaderPlugin } = require('vue-loader')
 
module.exports = {
  // ...
  plugins: [
    new VueLoaderPlugin()
  ]
}
//3在配置文件webpack.config.js中新增loader{test:/\.vue$/,use:"vue-loader"} 
//4main.js中，render:function(createElement){
return createElement(login)}
//5在html中<login></login>
//6在webpack中，如果要通过vue把一个组件放到页面中展示，只能用render函数

18.render的改写：
// render:function(createElement){
    //     return createElement(login)
    // }//可以简写成下面的形式
    render:c=>c(login)
    //逻辑：1.改写成箭头函数： (createElement)=>{return createElement(login)}
    // 2.()里只有一个变量，可以去掉（），{}里只有一条函数，可以去掉{},不加{}默认为return，可以去掉return:
    // createElement=>createElement(login)
    // 3.变量名太长，改成c:c=>c(login)

19.在login.vue中定义组件的data和method：
<script>export default{
data(){return {}},
methods:{
show(){console.log("xxxx")}
}
}
</script>

20.//es6:使用import 模块名 from “模块标识符”
/在es6中使用export default和export向外暴露成员
//node中：使用var/const 名称 = require("模块标识符")
//node:使用module.exports 和exports 来暴露成员
//export default向外暴露的成员，可以使用任意变量来接收
//在一个模块中，export default只允许向外暴露一次
//export向外暴露成员，只能通过{}来接收
//export可以多次暴露成员
//export导出的成员，导出时必须严格使用导出时的名称使用{}来接收，可以使用as 来取别名

21.cnpm i 通过package.json安装，尽量不要复制node_modules

22.vue-router的使用
//1安装路由：cnpm i vue-router -D
//2main.js导入包：import VueRouter from "vue-router"
//3手动安装router：Vue.use(VueRouter)
//4创建路由对象：var router = new VueRouter({
routes:[
{path:"/account",component:account},
{path:"/goodslist",component:goodslist}
]
})
//5导入组件：
//import account from  "./main/Account.vue"
//import goods list from "./main/GoodList.vue"
//6
//app这个组件是通过vm的render函数渲染出来的，render如果要渲染组件，渲染出来的的组件只能放到el所指向的#app元素中；
//account/goodlist是由路由匹配监听到的，这两个组件只能放到属于路由的<router-view>/<router-link>中，不能放到el所指向的#app中，会被render函数的渲染清空，应放在app.vue中

19.图标提示包：vue 2 snippets,vetur

20.设置组件样式
//<style scoped>设置局部样式
//普通style标签只支持普通的样式，启用scss/less需要为style元素设置lang属性<style lang="scss">,div{font-style:italic}

21.抽离路由：
新建router.js,将导入组件，创建路由对象挪出,
//暴露路由对象export default router
//main.js接收路由:import router from "./router.js"

22.mint ui:
//安装cnpm i mint-ui -D
//引入全部组件：import Vue from "vue"，
//import MintUI from "mint-ui",
//导入样式
//import "mint-ui/lib/style.css"
//导入app组件
//import App from "./App.vue"
//安装mintui
//Vue.use(Mint)
//new Vue({
el:"#app",
components:{App}
})
//引入部分组件：import {Cell,Checklist} from "mini-ui"
//Vue.component(Cell.name,Cell)
//Vue.component(Checklist.name,Checklist)
//使用时，需配置.babelrc文件：
{
"presets":["env","stage-0"],
"plugins":["transform-runtime"]}
并在webpack.config.js中配置：
{test:/\.css$/,use:["style-loader","css-loader"]}

23.mint-ui中toast使用
//App.vue中
// Toast("点击出现提示信息")，调用toast后会有一个返回值，返回值有close方法，调用close方法，可以手动关闭
                this.toastInstance = Toast({
                    message:"设置提示内容",
                    position:"设置出现位置",
                    duration:-1,
                    iconClass:"glyphicon glyphicon-heart",//设置图标,用bootstrap,在main.js中导入图标,import "bootstrap/dist/css/bootstrap.css",打开bootstrap,将图标样式放在iconClass中，webpack.config.js中配置{test:/\.(ttf|eot|svg|woff|woff2)$/,use:"url-loader"}
                    className:'mytoast',//自定义toast的样式，需自己提供一个类名新建css文件夹/app.css,在main.js中导入import "./css/app.css"
})

24.//借助 cnpm i babel-plugin-component -D按需引入需要的组件，以达到减小项目体积的目的。
//.babelrc:
{
    "presets":["env","stage-0"],
    "plugins":[
        "transform-runtime",
        [
            "component",
            [
                {
                    "libraryName":"mint-ui",
                    "style":true
                }
            ]
        ]
    ]
}
//在main.js中引入组件和注册按钮：

25.使用mui：需要手动下载压缩包，不能npm安装
//拷贝dist到src/lib/mui中，放置的是手动安装的包
//mui-master/examples/hello-mui/examples/buttons.html,拷贝标签到 App.vue
//main.js引入mui，import "./lib/mui/css/mui.min.css"


26.使用局部样式：
style with scss (scoped)


27.版本管理工具
//1.根目录下创建.gitignore:忽略那些要上传的文件:
node_modules
.idea
.vscode
.git
//2.创建README.md:
用#
//3.开源项目的协议，mui-masters/LICENSE,放到根目录下
//4.创建新仓git init
//5git status
//6git add .
//7提交git commit -m "xxx"
//8新增git remote add origin githubadress
//9推送到远程git push -u origin master
//10全局设置：
git config --global user.name "...."
git config -- global user.email "...."
//11删除本地分支：git branch -d 分支名
//12删除远程分支：git push origin --delete devs
//13创建新分支并切换到新分支： git checkout -b 新分支名
//14创建新分支不切换到新分支：git branch 新分支名
//15.1.本地分支重命名 git branch -m oldBranchName newBranchName
//15.2.远程分支重命名:如果修改远程分支，只需要将本地分支重命名为新分支名称，然后删除远程分支，再把本地分支上传就可以了
//fatal:Authentication failed -> git config --system -unset credential.helper 再push，提示输入用户名，密码
----------------------------------------------------------------------------------------------------------
补充：git command
#查看远程分支
git branch -r
 
#查看本地分支
git branch
 
#拉取远程分支
git checkout -b 本地分支 origin/远程分支
 
#拉取远程分支
git pull origin 远程分支　
 
#建立分支
git branch --set-upstream-to origin/远程分支名  本地分支名
 
#拉取分支
git pull
 
#遇到本地冲突，先删除本地分支，再重新拉取远程分支
git branch -D 本地分支名称

27.2.1查看远程分支
使用如下git命令查看所有远程分支：

git branch -r
 

27.2.2拉取远程分支并创建本地分支
方法一
使用如下命令：

git checkout -b 本地分支名x origin/远程分支名x
 

使用该方式会在本地新建分支x，并自动切换到该本地分支x。

采用此种方法建立的本地分支会和远程分支建立映射关系。

方式二
使用如下命令：

git fetch origin 远程分支名x:本地分支名x

使用该方式会在本地新建分支x，但是不会自动切换到该本地分支x，需要手动checkout。

采用此种方法建立的本地分支不会和远程分支建立映射关系。

27.2.3本地分支和远程分支建立映射关系的作用
git branch --set-upstream-to origin/远程分支名  本地分支名

27.2.4切换分支
git checkout 本地分支名

27.2.5合并分支
git merge 本地分支名称
-------------------

28.mui图标，在example的icon里找，标签里的mui-icon 不能删除，引入样式：/css/icons-extra.css" ,font


29.mui-active,高亮
//配置高亮
//在router.js中：
linkActiveClass:"mui-active"//覆盖默认路由高亮的类

30.Promise:
// 1.Promise是一个构造函数，new Promise()得到一个Promise实例
// 2Promise上有resolve(成功之后的回调函数)，reject(失败之后的回调函数)
//3.Promise.Prototype.then(),只要是promise创建的实例，都可以访问到.then()方法,.then()预先指定了成功调用resolve函数和失败调用reject函数
// 4.Promise()表示一个异步操作，每new一个实例，这个实例就表示一个具体的异步操作
//5.异步的结果，成功和失败
//5.1执行成功，在内部调用resolve将结果返回给调用者
//5.2执行失败，在内部调用reject将结果返回
//5.3异步操作内部拿到结果后，不能用return，只能使用回调函数的形式将结果返回
//6.每new一个Promise实例，就会立即执行异步操作里的代码,如不要立即执行，则需创建function函数，调用时才会执行

//7.在上一个节点返回的promise,可以用继续使用.then()


31.时间格式化，
//安装时间插件：cnpm i moment -D
//导入时间插件：import moment from "moment"

32.在组件中引入子组件：

--------------------------------------------------

1.数据数组的操作：
//1.1数组的变异方法
不能用下标操作
push 末尾添加
pop 末尾删除
shift 行首删除
unshift 行首添加
splice 截取-----splice(下标，删除的条数，在当前位置 增加的内容)
sort 排序
reverse 取反
//1.2使用Vue.set(vm.msg,下标，变更的内容)
//1.3使用vm.$set(vm.msg,下标，变更的内容)

2.不想用div渲染，可以换成<template>包裹
3.更新字典数据，用Vue.set(vm.msg,"","")  或  vm.$set(vm.msg,"","")

4.h5编码规则，table>tbody,tbody里只能放tr
<tbody><tr is="component"></tr>/tobody>
<ul><li is="component"></li></ul>
<select><option is = "component"></option></select>

5.组件数据，要求是一个函数要有返回值，data(){return}或data:function(){
    return
}

6.获取dom节点，设置<div ref="refName"></div>，获取this.$refs.refName.inneHTML

7.父子组件传数据：父组件中设置参数，传递给子组件，子组件用props:[""]接收，子组件不能修改父组件中的参数，否则会报错。可以通过在子抓紧设置自己的data，data(){return {
    number
}},更改里面的数据

8.props特性
//8.1参数不会展示在dom标签中
//8.2可以在子组件中通过差值表达式获取参数的值
非props特性：
//8.3参数会显示在dom标签中
//8.4不能直接获取参数的值

9.监听原生事件用@click.native

10.非父子组件间的传值：
Vue.prototype.bus = new Vue()

11.vue作用域插槽
//11.1子组件用<slot></slot>封装
//11.2父组件用<template slot-scope="变量名">
{{变量名.参数}}
</template>

12.动态组件，vue自带：
<component :is></component>

13.动画效果原理:通过在dom上增加样式来实现
<transition name="fade"></transition>
//如果不写name，则默认为v-enter,v-enter-active
////出现
//第1针：创建fade-enter,fade-enter-active
//第2针，销毁fade-enter,创建fade-enter-to
//第3针，销毁fade-enter-active,销毁fade-enter-to 
////消失
//第1针：创建fade-leave,fade-leave-active
//第2针，销毁fade-leave,创建fade-leave-to
//第3针，销毁fade-leave-active,销毁fade-leave-to
.v-enter,.v-leave-to{
    opacity:0
}
.v-enter-active,.v-leave-active{
    transition:opacity 1s;
}

14.列表过渡：
<transition-group></transition-group>
+<style></style>

15.transition中的钩子函数：
<transition
        name="fade"
        @before-enter="handleBeforeEnter"
        @enter = "handleEnter"
        @after-enter="handleAfterEnter"
        >
methods:{
    handleBeforeEnter(el){},
    handleEnter(el,done){
        done()
    },
    handleAfterEnter(el){}
}

16.配置ssh
//16.1步骤1.检查是否已经存在SSH Key
ls -al ~/.ssh
//16.1.1 ssh-keygen -t rsa -C "your_email@example.com"
//16.1.2 pbcopy < ~/.ssh/id_rsa.pub 获得的SSH Key粘贴到
//16.2 打开GitLab, 登录->点击右上角的用户头像->点击settings->在settings里找到SSH的设置->点击“ADD SSH KEY”按钮添加->将已经获得的SSH Key粘贴到“Key”，标题可以随便取，这样就保持了本地与服务器端的联系.

17.创建项目
npm install --global vue-cli
vue init webpack my-project
cd my-project
npm install
npm run dev

18.样式依赖:stylus
cnpm i stylus -S
cnpm i stylus-loader -S

19./* 使用stlus样式:lang="stylus"，要使该样式只对class="header"作用的话，可加上scoped */

20.reset.css里面：
html {overflow-x: hidden;height: 100%;font-size: 50px;-webkit-tap-highlight-color: transparent;}
相对50px，1rem = html font-size = 50px，所以,43px =43 * 1/50px=43/50=0.86rem
,设计稿是两倍尺寸，所以代码里的像素要除以2，再除以50px=rem单位,或者两倍尺寸除以100px

21.定义全局css样式，并在stylus中使用
//在src/assets/style/新建varibles.styl
//样式里面引入样式要用@import
//“@” 代表src这个路径，如果在css中引入其他的css，又要使用@的话要变成："~@"

22.自定义路径代表符:
//22.1 build/webpack.base.conf.js/
//22.2 resolve:{
    alias:{
        "styles":resolve("src/assets/styles")
    }
}

23.企业级开发，不同功能创建不同分支

24.轮播图组件
https://github.com/surmon-china/vue-awesome-swiper
cnpm i vue-awesome-swiper@2.6.7 -S

25.全局使用vue-awesome-swiper,main.js
import Vue from 'vue'
import VueAwesomeSwiper from 'vue-awesome-swiper'

// require styles
import 'swiper/dist/css/swiper.css'

Vue.use(VueAwesomeSwiper, /* { default global options } */)

//图片地址
http://piao.qunar.com/touch/

26.将长字符串用省略号显示
ellipsis()
    overflow:hidden
    white-space:nowrap
    text-overflow:ellipsis


27.vue中发送ajax的方法：
vue-resource
axios(推荐使用)
//cnpm i axios -S
//axios使用:
//27.1import axios from "axios
//27.2使用生命周期函数mounted (){}
//27.2.1mounted (){
    this.getHomeInfo()
}
//static放置静态文件/mock文件夹/index.json,只有static里的内容能被外部访问到
//防止被提交到仓库，在.gitignore中添加static/mock
//在home.vue中写axios请求，可以传给每一个子组件

28.对api下json的请求转发到static/mock/xx.json下，使用vue中的proxy代理
//config文件夹/index.js文件
////dev:{
    proxyTable:{
        "/api":{
            target:"http://localhost:8080",
            pathRewrite:{
                //一旦请求是以api开头，转发到'/static/mock下'
                "^/api":"/static/mock"
            }
        }
    }
}

29.v-if="list.length",当list为空数组，length为0， v-if=“false”
30.页面跳转
<router-link></router-link>

31.解决列表区域不能拖动，引入第三方包，better-scroll
31.1 cnpm install better-scroll --save
31.2 使用参考文档：https://github.com//ustbhuangyi/better-scroll
31.3 使用better-scroll必须符合下列结构：
    <div>
        <ul>
            <li></li>
            <li></li>
            <li></li>
        </ul>
    </div>
31.4
    import BScroll from 'better-scroll'
    const wrapper = document.querySelector('.wrapper')
    const scroll = new BScroll(wrapper)//创建一个新BScroll的实例，接收一个dom元素（使用ref获取dom元素）

32.发送ajax的步骤
32.1在最外面的页面建立，import axios from "axios"
32.2 mounted(){
    this.getCityInfo()
}
33.大量数据的传递用vuex
33.1安装cnpm install vuex --save
33.2 创建store，src/store/index.js
【
    import Vue from "vue"
import Vuex from "vuex"
Vue.use(Vuex)
export default new Vuex.Store({
    state:{
        city:"北京"
    }
})
】
33.3 main.js里import
调用state，首先调用actions，再调用mutations
33.4
//state:储存公用数据
//mutations:储存同步数据的改变
//action:异步数据

34.webpack默认不支持通过ip访问，
在package.json里配置，
"scripts":{"dev":--host 0.0.0.0}
    ifconfig,获取inet本机ip -> 10.71.41.48
    输入10.71.41.48:8080访问

35.解决手机端不支持promise,解决白屏问题
    cnpm install babel-polyfill --save
    在main.js中,import 'babel-polyfill'

36.打包编译上线过程
    >命令行：npm run build -> 生成的dist文件夹，就是最终要上线的代码。
    >将dist里文件放在后端服务器的根目录下即可。
    >修改dist文件所放的路径：config - index.js - build:{assetsPublicPath:'/project'}
    则相应打开的路径为：localhost/project

37.dist详解：
    >static
        >css
        >js
            >app.js > 各个逻辑代码
            >manifest.js > 打包的配置文件
            >vendor.js > 各个组件公用的代码

38.vue知识点
    >vue-rooter
    >vuex
    >vue服务端渲染
--------------------------- 20190709-复习vue_qunaer_app-- ---------
1.vscode快捷键打开chrome：alt + b
2.父组件->子组件：发送 -> v-bind:名称1=“值1” v-bind:名称2=“值2”
                接收 -> props:["名称1","名称2"]
  子组件->父组件：发送 -> this.$emit("click"//事件名,变量名)
                接收 -> @事件名="方法名1"
                        Vue实例：methods:{
                            方法名1:function(){
                                数据变化逻辑代码
                            }
                        }
3. v-on:click="" -> @click=""
   v-bind:名称1="对象/数组" -> :名称1="对象/数组 -> 这里面是一个js表达式，对应实例中的data",

4.钩子函数：在某一个时间点会被自动执行的函数；该函数不放在methods里，直接放在vue实例里。
  beforeCreate:function(){}
  created:function(){}
  beforeMount:function(){} -> 页面未渲染
  mounted:function(){} -> 页面渲染完毕
  beforeDestroy:function(){} -> 当vm.$destroy()被调用，即将销毁时
  destroyed:function(){} -> 当vm被完全销毁时
  beforeUpdate:function(){} -> 当数据改变，页面还未被重新渲染
  updated:function(){} -> 数据改变，页面渲染完毕时。
  activated: function () {} ->使用keep-alive时产生

5.计算属性，computed:{},如果计算属性依赖的变量没有任何改变，则不会重新计算，会一直存在计算属性中。
6.监听器，watch:{},也存在缓存机制。
    优势: computed > watch > methods
7.v-if = "" -> 不会频繁将页面dom元素删除和添加
  v-show = "" ->
  v-if = "", v-else-if = "", v-else = ""
  <div key= ""> -> 添加key值，以保证不被复用。切换div时，信息被清除。

8.template:模版占位符，可以包裹元素，但在循环中，并不会被渲染到页面上 。
9.-> 改变数组的7种变异方法：push（从尾部增加一个）, 
                pop(从尾部删除一个), 
                splice(索引值，个数，在该索引位置新增内容), 
                shift（从头部删除一个）, 
                unshift(0,从头部增加一个), 
                sort, 
                reverse
  ->Vue使用set方法，改变数据
    Vue.set(vm.userInfo,"address->新增key","beijing->新增value") -> 页面的值也会跟着改变
  ->实例使用set方法，改变数据
    vm.$set(vm.userInfo,"address","beijing")
10.使用is标签解决模版标签的bug
    <tbody>
        <tr is="row"></tr>
        <tr is="row"></tr>
    </tbody>
    ----------------
    <ul>
        <li is="row"></li>
    </ul>
    ----------------
    <select>
        <option is="row"></option>
    </select>
    ----------------

11.->实例中定义data：
    data:{
        content:"this is content"
    }

   ->组件中定义data，要求必须是函数
   data:function(){
        return {content:"this is content"}
   }
12.在vue中操作dom用ref
13.父组件传递到子组件的值只能用，不能修改，如果想要用，就在子组件本身中data接收，改变自身data的值。
14.使用插槽:当子组件显示的值是从父组件传来;
   插槽只有一个，具名插槽可以有多个。
   作用域插槽必须是以<template slot-scope="props"></template>,子组件传递过来的属性存在props中。
   啥时候使用作用域插槽：当子组件内部做循环；或子组件的dom结构由父组件决定时

15.动态组件：    <component :is="type"></component>
16.动画：
    开始时产生的两个函数
    .v-enter,
    .v-leave-to{
      opacity: 0;
    }

    结束时产生的两个函数
    .v-enter-active,
    .v-leave-active{
      transition:opacity 3s;
    }
17.动画 -> animated.css
    <link rel="stylesheet" href="../animated.css">

    <transition 
    enter-active-class="animated shake"
    leave-active-class="animated fadeOut">
      <div v-if="show">hello world</div>
    </transition>
18.过渡动画-> 第一次出现时，也具备动画
    <transition 
    appear
    appear-active-class="animated shake"
    >
    </transition>

    动画时长：
    type,:duration

19.项目
    19.1项目预热：
        19.1.1 项目环境配置
            19.1.1.1 创建项目
                >npminstall --global vue-cli
                >vue init webpack my-project
                >cd my-project
                >npm install
                >npm run dev
        19.1.2 多页面
            > template里只能暴露一个标签
            > 多页面跳转没有重新请求html原理：js检测到url地址到变化，先将页面内容清除，再添加新的内容。
        19.1.3 项目初始化:
            > minimum-scale=1.0,maximum-scale=1.0 保证页面的大小始终是1:1 
              user-scalable=no 保证用户用手指放大缩小无效 
            > 把不同手机默认样式统一，引入 reset.css文件
                > 目录：src -> assets -> styles -> .css
                > 所有的import 文件都在main.js中
            > 解决移动端1px问题,引入 border.css
            > 解决移动执行click事件延迟300ms ,
                > nmp install fastclick --save (save不管是开发环境还是线上环境都需要的意思，安装在dependencies里面)
                > import fastClick from 'fastclick'
                > fastClick.attach(document.body)
    19.2 项目首页开发
        19.2.1 首页区域开发
            > 使用stylus 
                > npm install stylus stylus-loader --save
                >子组件使用的样式不会对其他组件产生影响，使用scoped
                > css 
                    > .header {
                        color: red
                        }
                >stylus
                    > .header
                        color: red
                >reset.css里html font-size = 50px;即 1 rem = html font-size = 50px
                    ----->1px = 1/50 rem
                >定义全部变量
                    >定义：styles -> varibles.styl->
                        $bgColor = #00bcd4
                    >使用：
                        <styles>
                            @import '../../../assets/styles/varibles.styl'
                        </styles>
                >css中import其他css，使用@，前面加～，即：~@
                 css中引用其他css，import要加@
                >自定义路径代表符：
                    build->webpack.base.conf.js->resolve
        19.2.2 iconfont的使用
            > iconfont.woff/.woff2/.ttf/.svg/.eot/.css 
            > path: 
                >iconfont.woff/.woff2/.ttf/.svg/.eot/ ====> src->assets->styles->iconfont
                >iconfont.css =====> src->assets->styles
                >更改iconfont.css里url路径：
            >       <span class="iconfont">&#xe624;</span>
        19.2.3 首页轮播图
            > 轮播插件: https://github.com/surmon-china/vue-awesome-swiper
                >安装 npm install vue-awesome-swiper@2.6.7 --save
                >使用：
                    > import VueAwesomeSwiper from "vue-awesome-swiper"
                    > import 'swiper/dist/css/swiper.css'
                    >Vue.use(VueAwesomeSwiper)
            > 相对比例固定图片长宽 ： 
                overflow: hidden
                width: 100%
                height: 0
                padding-bottom: 31.25% //相对宽度撑开 31.25%

            >左右划点由样式：swiper-pagination-bullet-active控制，这是属于swiper的组件，其他组件的样式修改不会影响swiper组件本身的样式。
                解决方法：
                    .wrapper >>> .swiper-pagination-bullet-active
                    background-color red
            > 文字过长自动缩减
                overflow hidden
                white-space nowrap
                text-overflow ellipsis
                >设置全局变量 ->文件名 ：mixins.styl
                    ellipsis()
                      overflow: hidden
                      white-space: nowrap
                      text-overflow: ellipsis
        19.2.4 ajax动态获取数据
            >安装 npm install axios --save
            > import axios from 'axios'
                >
                    methods: {
                        getHomeInfo: function () {
                          // axios.get('/api/index.json')
                          axios.get('/static/mock/index.json')
                            .then(this.getHomeInfoSucc)
                        },
                        getHomeInfoSucc: function (result) {
                          console.log(result)
                        }
                      },
                      mounted () {
                        this.getHomeInfo()
                      }

            >静态文件放置位置： static->mock->
                http://localhost:8080/static/mock/index.json

            >设置api转发到本地static/mock路径：
                config -> index.js -> dev -> proxyTable
                >proxyTable: {
                '/api': {
                target: 'http://localhost:8080',
                pathRewrite: {
                '^/api': '/static/mock'
                }
                }
                }
            > ajax获取的数据传给每个子组件
            ><swiper :options="swiperOption" v-if="homeSwiperList.length">,保证swiper由完整的数组创建，不由空数组创建，这样就不会显示最后一张图片，而是第一章图片
        19.2.5
            > 控制border的颜色：
                .border-topbottom
                    &:before//上边框线
                        border-color #eee
                    &:after//下边框线
                        border-color #eee
        19.2.6 better-scroll
            > https://github.com/ustbhuangyi/better-scroll
            > 安装: cnpm install better-scroll --save
            > 使用:
                >import BScroll from 'better-scroll'
                >const wrapper = document.querySelector('.wrapper')//接收dom元素
                >const scroll = new BScroll(wrapper)//创建better-scroll实例
            >结构要求-> 三层：
                <div class="wrapper">
                    <ul class="content">
                        <li></li>
                        <li></li>
                    </ul>
                </div>
        19.2.7柱形垂直居中
             //垂直居中
                display flex
                flex-direction column
                justify-content center
        19.2.8 
            > 一个元素距离顶部的高度： const startY = this.$refs['A'][0].offsetTop
            >touch事件 -> 手机端才有用
                >touchstart
                >touchmove
                >touchend
            > 返回小于等于x的最大整数: Math.floor(1.6);-> 1
            > 数据优化：
                > 数据变化时，用钩子函数
                    updated
                > 节流，timer
                /Users/Czhang/Desktop/quaner_app_review/6_项目预热/travel/src/pageComponents/cityPage/cityComponents/cityList.vue
    19.3 vuex 跨组件数据传递
        > 安装：nmp install vuex --save, 使用全局script标签引用时，不需要以上安装过程。
        > 使用：
            import Vue from 'vue'
            import Vuex from 'vuex'
            Vue.use(Vuex)
            export default new Vuex.Store({
                state: {
                    city: '北京'
                }
                })
        > 注册：main.js
            import store from './store/index.js'
        > 各个组件可以使用
            this.$store.state获取值
        > Vue ---dispatch--> actions ---commit--> mutations ---mutate--> state ---render--> Vue
        >函数中页面跳转：
            this.$router.push('/') -> 跳转到首页
        > store -> index.js
            export default new Vuex.Store({
              state: {
                city: '北京'
              },
              actions: {
                changeCityActions (ctx, cityName) {
                  // console.log('index.js->changeCityActions:', cityName)
                  ctx.commit('changeCityMutations', cityName)
                }
              },
              mutations: {
                // state指：共有数据state
                changeCityMutations (state, cityName) {
                  state.city = cityName
                }
              }
            })
        > localStorage:
            >
                export default new Vuex.Store({
                  state: {
                    city: localStorage.city || '北京'// 优先从localStorage中取，如果取不到再取北京
                  },
                  actions: {
                    changeCityActions (ctx, cityName) {
                      // console.log('index.js->changeCityActions:', cityName)
                      ctx.commit('changeCityMutations', cityName)
                    }
                  },
                  mutations: {
                    // state指：共有数据state
                    changeCityMutations (state, cityName) {
                      state.city = cityName
                      localStorage.city = cityName
                    }
                  }
                })

            > 使用localStorage时推荐使用try,catch
                let defaultCity = "上海"

                try {
                  if (localStorage.city) {
                    defaultCity = localStorage.city
                  }
                } catch (e) {}

                export default new Vuex.Store({
                  state: {
                    city: defaultCity// 优先从localStorage中取，如果取不到再取北京
                  },
                  actions: {
                    changeCityActions (ctx, cityName) {
                      // console.log('index.js->changeCityActions:', cityName)
                      ctx.commit('changeCityMutations', cityName)
                    }
                  },
                  mutations: {
                    // state指：共有数据state
                    changeCityMutations (state, cityName) {
                      state.city = cityName
                      try {
                        localStorage.city = cityName
                      } catch (e) {}
                    } 
                  }
                })
            > 优化代码 this.$store.state.city
                >
                    >state -> mapState, 
                    >mutations -> mapMutations, 
                    >actions -> mapActions, 
                    >getters -> mapGetters//当需要从state中计算属性时，用getter
                        >index.js:
                            getters: {
                                doubleCity(state) {
                                    return state.city + ' ' + state.city
                                }
                            }
                        >.vue:
                            computed: {
                                ...mapGetters(['doubleCity'])
                            }
                        >使用：
                            {{this.doubleCity}}
                    >module
                        const moduleA = {
                        state:{},
                        actions: {},
                        mutations: {},
                        getters: {}
                        }

                        const moduleB = {
                        state:{},
                        actions: {},
                        mutations: {},
                        getters: {}
                        }

                        const store = new Vuex.Store({
                            modules: {
                            a: moduleA,
                            b: moduleB
                            }
                            })

                        store.state.a
                        store.state.b
                >展开运算符：
                    >数组合并：
                     var arr1=['a','b','c'];
                     var arr2=[...arr1,'d','e']; //['a','b','c','d','e']
                    >数组 push：
                     var arr1=['a','b','c'];
                     var arr2=['d','e'];
                     arr1.push(...arr2); //['a','b','c','d','e']

                > this.$store.state.city===>computed -> mapState===>简写
                    >computed: {
                        ...mapState(['city']) ---> 使用{{this.city}}
                        //或
                        ...mapState({
                            currentCity: 'city'
                            }) --->使用{{this.currentCity}}
                    }

                >   >methods: {
                    handleClick () {
                        this.$store.commit('changeCityMutation', cityName)
                            }
                    }//简写
                    >methods: {
                    handleClick () {
                        this.changeCityMutation(cityName)
                            },
                    ...mapMutations(['changeCityMutation'])
                    }

                >this.$store.dispatch('changeCityActions')===>简写
                    >methods: {
                        handleClick () {this.changeCityActions(cityName)},
                        ...mapActions(['changeCityActions'])
                        }
                > mapGetters===>computed

    19.4 vuex -> module
        const moduleA = {
          state: { ... },
          mutations: { ... },
          actions: { ... },
          getters: { ... }
        }

        const moduleB = {
          state: { ... },
          mutations: { ... },
          actions: { ... }
        }

        const store = new Vuex.Store({
          modules: {
            a: moduleA,
            b: moduleB
          }
        })

        store.state.a // -> moduleA 的状态
        store.state.b // -> moduleB 的状态
    19.5 keep-alive优化性能
        <keep-alive>
            <router-view></router-view>
        </keep-alive>
        //意思是：路由加载过一次之后，就把它放在内存之中，再进入路由时不需要重新执行钩子函数，只需要重新拿出来用就可以了。
    19.6 ajax请求携带参数：
    > getHomeInfo: function () {
      // axios.get('/api/index.json')
      axios.get('/static/mock/index.json?city=' + this.currentCity)
        .then(this.getHomeInfoSucc)
    }

    > this.currentCity通过{mapState}传递

    19.7 详情页
        19.7.1 动态路由
        > router -> 
            {
          path: '/detail/:id',
          name: 'Detail',
          component: Detail
            }
        > router-link -> 
            <router-link tag="li" class="recommend-item border-bottom" v-for="item in homeRecommendList":key="item.id" :to="'/detail/' + item.id">
        
        19.7.2 css
            渐变：background-image linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, .8))//从上到下，渐变透明度 0 到 0.8
        19.7.3 公用组件
            src->common->组件文件夹->组件名

handleLetterClick: function (letter) {
      // console.log(letter.target.innerText)
      this.$emit('letterChange', letter.target.innerText)
    }
>>>>>>>>>>>>>>>>>>>>>>>JavaScript_Learning_Note_1906051000>>>>>>>>>>>>>>>>>>>>>
1.day1-js基础语法
    1.1交换两个变量方式：
        1.1.1
            var a = 10;
            var b = 20;
            a = a ^ b
            b = a ^ b
            a = a ^ b
            console.log(a, b)
        1.1.2 值先计算右边，再将值赋值给左边
            var a = 10
            var b = 10
            a = a + b
            b = a - b
            a = a - b
        1.1.1打开html方式，alt + b
        1.1.3注释
            单行注释 ，//，一般用在一行代码上面
            多汗注释,/**/,用在函数或一段代码上面
            代码中如果没有注释，不规范
    1.2获取变量类型：
        typeof(xx)
        typeof xx
        蓝色字体，number类型
        黑色字体，string类型
        null的类型不是null，string(null)的类型是null
    
    1.3数字类型
        二进制 遇到2进1
            00000001----1
            00000010----2
            00000011----3
            00000100----4
            00000101----5
            00000110----6

        八进制 遇到8进1
            00000001----1
            00000002----2
            00000003----3
            00000004----4
            00000005----5
            00000006----6
            00000007----7
            00000011----8
            00000012----9

        十进制 遇到10进1
            1
            2
            3
            4
            5
            6
            7
            8
            9
            10
        十六进制-遇到f进1
            00000001----1
            00000002----2
            00000003----3
            00000004----4
            00000005----5
            00000006----6
            00000007----7
            00000008----8
            00000009----9
            0000000a----10
            0000000b----11
            0000000c----12
            0000000d----13
            0000000e----14
            0000000f----15
            00000010----16
            00000011----17
            00000012----18
        数字的最大值，最小值
            console.log(Number.MAX_VALUE)
            console.log(Number.MIN_VALUE)
            
        不要用NaN验证NaN,应使用isNaN(),表示是不是不是一个数字
        isNaN(数字)---false--是数字
        isNaN(不是数字)---true--不是数字
        !isNaN()--是数字

    1.6string
        1.6.1长度：str.length
        1.6.2 
            \t--水平制表符
            \n--换行
            \r--回车 
            \b--空格
        1.6.3字符串拼接:使用 +
            只要有一个字符串，其他是数字，使用+，都是字符串；
            只要有一个字符串，其他是数字，使用-，都是数字；
            只要有一个字符串，其他是数字，使用*，都是数字；
         
    1.7类型转换：
        1.7.1其他类型转数字类型
            1.7.1.1 parseInt()//转整数
                parseInt("10.98")--10
                parseInt("10aa")--10
                parseInt("aa10")--NaN
            1.7.1.2 parseFloat("10.98")--10
                parseFloat("10aa")--10
                parseFloat("aa10")--NaN//转小数
                parseFloat("10.98")--10.98
                parseFloat("10.98aa")--10.98
                parseFloat("aa10")--NaN
            1.7.1.3 Number()//转数字
                Number("10")--NaN
                Number("aa10")--NaN
                Number("10aa")--NaN
                Number("10.98")--10.98
                Number("10.98aa")--NaN

        1.7.2其他类型转字符串类型
            1.7.2.1 toString()
                要求被转类型要有意义
            1.7.2.2 String()

        1.7.3其他类型转布尔类型
            Boolean(值)
            Boolean(1)--true
            Boolean(0)--false
            Boolean(-10)--true
            Boolean("haha")--true
            Boolean("")--false
            Boolean(null)--false
            Boolean(undefined)--false
        1.8运算符
            1.8.1算数运算符
                + - * / %
            1.8.2一元运算符
                ++ --
            1.8.3复合运算符
                += -= *= /= %=
                num += 5 -> num = num + 5
            1.8.4关系运算符,结果是布尔类型
                > < >= <= == === != !==
                ==: 不严格，值相同，类型不一定相同
                ===:严格，值相同，类型相同
            1.8.5逻辑运算符
                && 并且
                || 或
                ！取反
            1.8.6 优先级
                >（）优先级
                >一元运算符 ++ -- 
                >算数运算符 * /  % 后 +
                >关系运算符 > >= < <=
                >相等运算符   == != ===
                >逻辑运算符 先$$ 后||
                >赋值运算符 += -=

2.day2流程控制
    2.1一元运算符
        >++ -- 分前后
        >不参与运算时，无区别
        >参与运算时，++在后面，num++ +10 ,num先参与运算，运算结束后自身再加1
            >var num = 10;
            num++ + 10 //10+10 = 20
            num //11
        >++在前面，num自身先加1，再参与运算
            >var num = 10;
            ++num + 10 // 11 + 10 = 21
            num //11
    2.2流程控制
        2.2.1顺序结构
        2.2.2分子结构：
            >if,
            >if-else,if-else if-else...
                >if(表达式){代码块1}else{代码块2}
                    >先判断表达式结果是true还是false,如果true则执行代码块，如果为false,则不执行代码块。
                    >var age = parseInt(prompt("请输入"))#弹框并且有输入
                >if(表达式1){代码块1}
                else if(表达式2){代码块2}
                else if（表达式3){代码块3}
                else{代码块4}
                    >表达式1的结果为true，则执行代码块1，流程结束；结果为false，则判断表达式2的结果，如果表达式结果为true则执行代码块2，流程结束；为false则判断表达式3的结果，代码3的结果为true，则执行代码块3，流程结束；否则，执行代码块4。
            >switch-case
            >三元表达式:
                > var 变量 = 表达式1 ？ 表达式2 ：表达式3；
                    > 表达式1的结果是true还是false，如果为true则执行表达式2，如果为false则执行表达式3，并将结果赋值给变量。
                        >例：var x = 10;
                            var y = 20;
                            var result = x > y ? x : y;
                            console.log(result)
        2.2.3循环结构
            while
            do-while
            for
            for-in

Vue中使用fontawesome:
1. 安装
    cnpm install --save @fortawesome/fontawesome-svg-core//Font Awesome的核心部分
    cnpm install --save @fortawesome/vue-fontawesome//Vue环境中使用需要的Vue组件
    cnpm install --save @fortawesome/free-solid-svg-icons//solid风格图标
    cnpm install --save @fortawesome/free-brands-svg-icons//商标图标
2. 配置，main.js
    >import { library } from '@fortawesome/fontawesome-svg-core'
    >import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
    >Vue.component('font-awesome-icon', FontAwesomeIcon)
    >   > class="fas fa-user"//fas代表solid风格，fa-user代表这个图标的名称
        >import {faUser} from '@fortawesome/free-solid-svg-icons'
        > class="fa fa-plus-square-o"
        >import {fa-plus-square-o} from '@fortawesome/free-solid-svg-icons'
    >library.add(faUser)
    >使用 <font-awesome-icon :icon="['fas', 'user']"></font-awesome-icon>
3.

-----------------------------CSS样式1907181651----190720_慕课网_全面系统讲解CSS 工作应用+面试一步搞定----------------------------------------
1. html
    1.1 html 常见属性
        1.1.1 
        <meta charset="UTF-8"> //指定编码
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"> //viewport指定适用于移动端； user-scalable手指不能放大说下；width=device-width宽度等于设备宽度
    1.1.2 html 重要属性
     >a[href,target]//target 默认target=self在当前窗口打开；target="_blank"在新窗口打开
     >img[src="",alt=""] // 当src不可用时，使用alt替换资源
     > <table><tr colspan="2" rowspan="2"></tr></table> tb//colspan:占据两列单元格；rowspan:占据两行单元格
     >  
        <input type="text" placeholder="text"> 
        <input type="password" placeholder="password">
        <input type="radio" placeholder="radio单选框" name="text1" id="text1">
            //type="radio"是单选框，name一样时，表示为一组，只能选中一个。
        <label for="text1">radio单选框1</label> // for="id号"，点击文字时可选中
        <input type="radio" placeholder="radio单选框" name="text2">
        <label for="text2">radio单选框2</label>
        <input type="checkbox" placeholder="checkbox复选框">checkbox复选框1
        <input type="checkbox" placeholder="checkbox复选框">checkbox复选框2

         <button type="button">普通按钮</button>
        <!-- submit 触发form actions -->
        <button type="submit">提交按钮</button>
        <button type="reset">重置按钮</button>
        <!-- submit用input写 -->
        <input type="submit">
        <!-- reset用input写 -->
        <input type="reset">
    1.1.3 html的嵌套关系
        > 块级元素可以包含行内元素
        > 块级元素不一定能包含块级元素
        > 行内元素一般不能包含块级元素

2. css 基础
    2.1 选择器分类
        > 元素选择器 a {}
        > 类选择器 .link {}
        > id选择器 #app {}
        > 属性选择器 [type=radio]{}
        > 伪元素选择器 ::before{} //没有显示在dom和html中，但是是真实存在的可以设置样式的元素
        > 伪类选择器 :hover{} //属性
        > 组合选择器 [type=checkbox]+label{}
        > 否定选择器 :not(.link){}
        > 通用选择器 *{}
    2.2 选择器权重：
        > id选择器 +100 > 类选择器 +10 > 元素/伪元素选择器 +1 > 其他选择器 +0
        > !important 优先级最高
          写到元素属性上的style比写在<style>中的style优先级高
          相同权重 后写的生效
    2.3 非布局样式 
        2.3.1 字体:
            自定义字体
        2.3.2 行高:
            > line-height 行高由line-box决定，line box 由inline box决定，inline box的高度会决定行高的高度；line-height会撑起line-box的高度，但不会引起自身高度的变化。
            > line-height: 默认垂直居中
            > 默认按底线对其，垂直居中 vertical-align: middle/top/bottom(按底线对齐,消除图片的底部缝隙)
            > 图片3px空隙问题：<img>按基线对齐，基线到底线还有段空隙，解决方式：vertical-align:padding-bottom,按底线对齐。
        2.3.3 背景:
            >background
                >背景颜色：
                    >rgb: #FF0000
                    >rgb:rgb(255, 0, 0)
                    >rgba:rgba(255, 0, 0, .3)
                    >hsl:(色相，饱和度，亮度, 透明度)
                    >背景图: background: url(./test.png)
                > 线性渐变/多背景叠加：
                    >background: linear-gradient(to right, red, green) //从左到右
                    >background: linear-gradient(135deg, red 0, green 50%, blue 100%); /*角度，num%表示相对位置*/
                    >background: linear-gradient(135deg, transparent 0, transparent 50%, red 50%, red 50.5%, transparent 50.5%, transparent 100%),linear-gradient(45deg, transparent 0, transparent 50%, green 50%, green 50.5%, transparent 50.5%,transparent 100%);//transparent表该处透明
                     background-size: 5px 5px;
                >背景图片和属性
                    > height: 900px;
                      background: pink url(./test.png);
                      background-repeat: no-repeat;/*repeat平铺，repeat-y纵向平铺，repeat-x横向平铺,no-repeat*/
                      /* background-position: center ;center top,center bottom, center center */
                      background-position: 200px 30px;/*左，上*/
                      background-size: 100px 50px;/*设置图片大小

        2.3.4 边框
            >边框的属性
                >线型
                >大小
                >颜色
            >边框背景图
            >边框衔接
            >
                .c1 {
                  /* 边框 */
                  width: 400px;
                  height: 200px;
                  /* border: 1px solid red; */
                  border: 5px dotted red;
                  border-bottom-color: green
                  /* border: 5px dashed red; */
                }
                .c2 {
                  /* 图片填充 */
                  margin-top: 2px;
                  width:400px;
                  height:200px;
                  /* border-width:30px; */
                  border:30px solid transparent;
                  border-image: url(./border.png) 30 round;
                }
                .c3 {
                  /* 三角形 */
                  width: 0px;
                  height: 200px;
                  border-bottom: 30px solid red;
                  border-right: 30px solid blue;
                  border-right: 30px solid transparent;
                  border-left: 30px solid transparent;
                }

        2.3.5 滚动
            > visible:滚动条隐藏,超出文本框的部分显示
            > hidden:超出文本框的部分隐藏
            > scroll：一直显示滚动条，超出文本框的不跟隐藏
            > auto：超出文本框时才显示滚动条，超出文本框的部分隐藏
            overflow: hidden
        2.3.6 文本折行
            > overflow-wrap:是否保留单词
                >overflow-wrap:normal //保留单词
                >overflow-wrap:break-word //打断单词，但尽量保证单词的完整性。
            > word-break:针对多字节文字，以字母为单位让单词换行，或者以单词为单位，不让单词换行。中文句子也是一个单词。
                >word-break:break-all //打断单词，不保存单词的完整性
                >word-break:keep-all //
            >white-space 空白处是否断行
                >white-space:no-wrap //不换行
                >white-space:normal //换行

        2.3.7 装饰性属性
            >字重font-weight
                {
                    font-weight: normal;
                    font-weight: bold;
                    font-weight: bolder;
                    font-weight: lighter;
                    font-weight: 100;//该值只能取100-900，100的整数倍
                }
            >斜体 font-style:italic
            >下划线 text-decoration
            >指针 cursor
        2.3.8 hack:在一部分浏览器上生效的css写法。

3.css布局：
    3.1table表格布局
    3.2float浮动+margin
    3.3inline-block布局
    3.4flexbox布局
||vscode打开默认浏览器快捷键：alt+b||
