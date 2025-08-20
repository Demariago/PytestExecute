```python
import pytest
import requests
import json

BASE_URL = "http://test.zhongautohealth.com/navis-gateway-admin?token=7eb6d5e0511e4476bc477d266554b9f7"


class TestMerchantListByPage:
    """测试分页获取商户资料接口"""

    def test_normal_request(self):
        """正常请求场景：参数正确、必填项完整"""
        url = f"{BASE_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}
        payload = {
            "merchantName": "",
            "servType": 0,
            "pageNum": 1,
            "pageSize": 10
        }

        response = requests.post(url, headers=headers, json=payload)

        # 断言状态码
        assert response.status_code == 200
        # 断言响应体结构
        response_data = response.json()
        assert "code" in response_data
        assert "message" in response_data
        assert "pageData" in response_data
        # 断言分页数据
        assert "pageNum" in response_data["pageData"]
        assert "pageSize" in response_data["pageData"]
        assert "pageDataList" in response_data["pageData"]

    def test_missing_required_params(self):
        """异常场景：缺少必填参数"""
        url = f"{BASE_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}
        # 缺少pageNum和pageSize
        payload = {
            "merchantName": "",
            "servType": 0
        }

        response = requests.post(url, headers=headers, json=payload)

        # 断言接口处理异常（可能是400或500，具体看接口实现）
        assert response.status_code != 200

    def test_wrong_param_type(self):
        """异常场景：参数类型错误"""
        url = f"{BASE_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}
        # servType应该是整数，但传入字符串
        payload = {
            "merchantName": "",
            "servType": "invalid_type",
            "pageNum": 1,
            "pageSize": 10
        }

        response = requests.post(url, headers=headers, json=payload)

        # 断言接口处理类型错误
        assert response.status_code != 200

    def test_boundary_values(self):
        """边界值测试：pageSize和pageNum的边界值"""
        url = f"{BASE_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}

        # 测试最小pageSize
        payload_min = {
            "merchantName": "",
            "servType": 0,
            "pageNum": 1,
            "pageSize": 1  # 最小每页条数
        }

        response_min = requests.post(url, headers=headers, json=payload_min)
        assert response_min.status_code == 200

        # 测试较大pageSize
        payload_max = {
            "merchantName": "",
            "servType": 0,
            "pageNum": 1,
            "pageSize": 100  # 较大每页条数
        }

        response_max = requests.post(url, headers=headers, json=payload_max)
        assert response_max.status_code == 200

    def test_serv_type_enum_values(self):
        """测试业务类型枚举值"""
        url = f"{BASE_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}

        # 测试所有有效的servType值
        valid_serv_types = [1, 2, 3, 4]  # 1-到店服务；2-电商服务；3-健康服务；4-零工服务

        for serv_type in valid_serv_types:
            payload = {
                "merchantName": "",
                "servType": serv_type,
                "pageNum": 1,
                "pageSize": 10
            }

            response = requests.post(url, headers=headers, json=payload)
            assert response.status_code == 200

    def test_invalid_serv_type(self):
        """测试无效的业务类型值"""
        url = f"{BASE_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}

        # 测试无效的servType值
        payload = {
            "merchantName": "",
            "servType": 99,  # 无效的业务类型
            "pageNum": 1,
            "pageSize": 10
        }

        response = requests.post(url, headers=headers, json=payload)
        # 接口可能返回空列表或错误码
        assert response.status_code == 200

    def test_merchant_name_search(self):
        """测试商户名称搜索功能"""
        url = f"{BASE_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}

        # 测试带商户名称的搜索
        payload = {
            "merchantName": "测试商户",
            "servType": 0,
            "pageNum": 1,
            "pageSize": 10
        }

        response = requests.post(url, headers=headers, json=payload)
        assert response.status_code == 200
        response_data = response.json()
        # 验证返回的数据结构
        assert "pageData" in response_data
        assert "pageDataList" in response_data["pageData"]


```