<!-- TABLE OF CONTENTS -->
<details>
  <summary>目录</summary>
  <ol>
    <li>
      <a href="#项目介绍">项目介绍</a>
      <ul>
        <li><a href="#公司项目背景">公司项目背景</a></li>
        <li><a href="#技术选型">技术选型</a></li>
        <li><a href="#实现细节">实现细节</a></li>
      </ul>
    </li>
    <li><a href="#效果展示">效果展示</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## 项目介绍
本项目为我司工业互联网SaaS平台中plm项目（产品生命周期）的接口自动化测试项目。采用Python + pytest + sgqlc 技术栈完成。
###公司项目背景
公司后端技术采取的是 [GraphQL](https://graphql.org/) 来定义接口。每次项目开发之后，后端开发会先给出一份schema，前端根据这份schema去了解数据定义，schema先行，前端根据这份schema也有自己的mock技术，前后端并行开发。
采取微服务方式部署，GraphQL网关会把所有的微服务集合起来，暴露一个地址给前端调用。
在query中，graphql定义了要传入的参数，和返回的值，其中返回的值可以进行按需查询。
###技术选型
首先选用Python + pytest框架，保证编程的简单，可以专注于测试用例设计与测试数据设计。然后通过调研，选用[sgqlc](https://github.com/miyuki-shirogane/sgqlc)第三方库来替代传统的requests库，与GraphQL较好的契合。