###2022-01-25
谈谈思路：
>首先创建项目，然后创建填充一堆数据。再去query请求、校验。\
> 只是大致想法是这样，具体怎么搞明天详细展开说说。

###2022-02-17
list那种接口 后面有data、total_count的，args必填，因为。。
我想到了再写。

###2022-02-18
我想到了，比如下面这段code
```python
    def material_list(self, args, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        m_list = op.material_list(
            limit=10,
            filter=eval(f"{kwargs}"),
        )
        m_list.data.__fields__(*args)
        m_list.total_count()
        data = endpoint(op)
        res = (op + data).material_list
        return res
```
中的这两行
```python
        m_list.data.__fields__(*args)
        m_list.total_count()
```
其含义就是返回`data`中的指定字段、以及`total_count`, 那么我可以把代码改成：
```python
    def material_list(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        m_list = op.material_list(
            limit=10,
            filter=eval(f"{kwargs}"),
        )
        if args:
            m_list.data.__fields__(*args)
            m_list.total_count()
        else:
            pass
        data = endpoint(op)
        res = (op + data).material_list
        return res
```

###2022-02-22
有关联的时候 还是不要查了 新增更好；避免啥也没有就跑不下去了。\
现在`project_data.py`文件中，涉及到了flow_id的查询，后续写完`flowApi`，\
再做修改。
现在在写的`material_apis.py`，依赖到`category_id`，需要新增一个。\
也就是说，先创建类别，再创建物料。

###2022-03-24
注意到schema中包含create_user接口。那到时候看看，能不能在conftest.py文件中，\
设置session级别的fixture，令检测user数量是否达到预期，若是pass，否则新增用户。\
这个是后话，晚点确认下。