<!-- TABLE OF CONTENTS -->
<details>
  <summary>目录</summary>
  <ol>
    <li>
      <a href="#项目介绍">项目介绍</a>
      <ul>
        <li><a href="#公司项目背景">公司项目背景</a></li>
        <li><a href="#遇到问题">遇到问题</a></li>
        <li><a href="#解决思路">解决思路</a></li>
      </ul>
    </li>
    <li>
      <a href="#一些细节">一些细节</a>
    </li>
    <li><a href="#效果展示">效果展示</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## 项目介绍
本项目为我司工业互联网SaaS平台中plm项目（产品生命周期）的接口自动化测试项目。采用Python + pytest + sgqlc 技术栈完成。
###公司项目背景
公司后端技术采取的是 [https://example.com](GraphQL) 来定义接口。每次项目开发之后，后端开发会先给出一份schema，前端根据这份schema去了解数据定义，schema先行，前端根据这份schema也有自己的mock技术，前后端并行开发。
采取微服务方式部署，GraphQL网关会把所有的微服务集合起来，暴露一个地址给前端调用
一个GraphQL定义的请求体大概是这样的：
```json
{
  "operationName": "typeCompanies",
  "variables": {
    "filter": {
      "search": ""
    },
    "scenario": "COMPANY"
  },
  "query": "query typeCompanies($filter: CompanyFilter, $scenario: TypeCompaniesScenario) {\n  typeCompanies(filter: $filter, scenario: $scenario) {\n    data {\n      type {\n        id\n        name\n        __typename\n      }\n      companies {\n        ...companyFields\n        __typename\n      }\n      __typename\n    }\n    totalCount\n    __typename\n  }\n}\n\nfragment companyFields on Company {\n  id\n  name\n  county\n  address\n  uscc\n  contact\n  email\n  phone\n  province\n  city\n  type {\n    id\n    name\n    __typename\n  }\n  isMine\n  __typename\n}\n"
}
```
在query中，graphql定义了要传入的参数，和返回的值，其中返回的值可以进行按需查询
```
query  typeCompanies($filter:  CompanyFilter,  $scenario:  TypeCompaniesScenario)  {
    typeCompanies(filter:  $filter,  scenario:  $scenario)  {
        data  {
            type  {
                id
                name
                __typename
            }
            companies  {
                ...companyFields
                __typename
            }
            __typename
        }
        totalCount
        __typename
    }
}
fragment  companyFields  on  Company  {
    id
    name
    county
    address
    uscc
    contact
    email
    phone
    province
    city
    type  {
        id
        name
        __typename
    }
    isMine
    __typename
}
```