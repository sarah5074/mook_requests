from mock import mock
def mock_test(mock_method,request_data,method,url,response_data):
    #mock_method表示的是调用的mock函数对象的函数名及方法名，response_data表示设置的自动响应的数据
    #method表示调用函数对象的参数中的方法，request_data表示调用函数中的请求数据，
    # url表示调用函数的url参数

    mock_data = mock.Mock(return_value=response_data)
    mock_method= mock_data
    res = mock_method(url,method,request_data)#可以理解为mock_method只是为了表示显示函数名称，方便写参数
    return res
