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