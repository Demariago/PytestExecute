import pytest
import requests
import json
import os
from dotenv import load_dotenv  # 需要安装: pip install python-dotenv

# 加载环境变量
load_dotenv()

BASE_URL = "http://test.zhongautohealth.com/navis-gateway-admin"
TOKEN = os.getenv("ZHEALTH_TOKEN", "default_token_if_not_set")
FULL_URL = f"{BASE_URL}?token={TOKEN}"


class TestMerchantListByPage:
    """测试分页获取商户资料接口"""

    @pytest.fixture(scope="class")
    def session(self):
        """创建会话，复用连接"""
        with requests.Session() as session:
            yield session

    def test_normal_request(self, session):
        """正常请求场景: 参数正确、必填项完整"""
        url = f"{FULL_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}
        payload = {
            "merchantName": "",
            "servType": 0,
            "pageNum": 1,
            "pageSize": 10
        }

        response = session.post(url, headers=headers, json=payload)

        # 断言状态码
        assert response.status_code == 200
        # 断言响应体结构和内容
        response_data = response.json()
        assert "code" in response_data
        assert response_data["code"] == 200
        assert "message" in response_data
        assert response_data["message"] == "success"
        assert "pageData" in response_data
        # 断言分页数据
        assert "pageNum" in response_data["pageData"]
        assert response_data["pageData"]["pageNum"] == 1
        assert "pageSize" in response_data["pageData"]
        assert response_data["pageData"]["pageSize"] == 10
        assert "pageDataList" in response_data["pageData"]
        assert isinstance(response_data["pageData"]["pageDataList"], list)

    def test_missing_required_params(self, session):
        """异常场景：缺少必填参数"""
        url = f"{FULL_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}
        # 缺少pageNum和pageSize
        payload = {
            "merchantName": "",
            "servType": 0
        }

        response = session.post(url, headers=headers, json=payload)

        # 断言状态码和错误信息
        assert response.status_code == 400
        response_data = response.json()
        assert "code" in response_data
        assert response_data["code"] != 200
        assert "message" in response_data
        assert "参数错误" in response_data["message"]

    def test_wrong_param_type(self, session):
        """异常场景：参数类型错误"""
        url = f"{FULL_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}
        # servType应该是整数，但传入字符串
        payload = {
            "merchantName": "",
            "servType": "invalid_type",
            "pageNum": 1,
            "pageSize": 10
        }

        response = session.post(url, headers=headers, json=payload)

        # 断言状态码和错误信息
        assert response.status_code == 400
        response_data = response.json()
        assert "code" in response_data
        assert response_data["code"] != 200
        assert "message" in response_data
        assert "参数类型错误" in response_data["message"]

    def test_boundary_values(self, session):
        """边界值测试：pageSize和pageNum的边界值"""
        url = f"{FULL_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}

        # 测试最小有效pageSize
        payload_min = {
            "merchantName": "",
            "servType": 0,
            "pageNum": 1,
            "pageSize": 1  # 最小每页条数
        }

        response_min = session.post(url, headers=headers, json=payload_min)
        assert response_min.status_code == 200

        # 测试最大有效pageSize
        payload_max = {
            "merchantName": "",
            "servType": 0,
            "pageNum": 1,
            "pageSize": 100  # 假设最大支持100
        }

        response_max = session.post(url, headers=headers, json=payload_max)
        assert response_max.status_code == 200

        # 测试无效pageSize（负数）
        payload_invalid_size = {
            "merchantName": "",
            "servType": 0,
            "pageNum": 1,
            "pageSize": -1
        }

        response_invalid_size = session.post(url, headers=headers, json=payload_invalid_size)
        assert response_invalid_size.status_code == 400

        # 测试无效pageNum（0）
        payload_invalid_num = {
            "merchantName": "",
            "servType": 0,
            "pageNum": 0,
            "pageSize": 10
        }

        response_invalid_num = session.post(url, headers=headers, json=payload_invalid_num)
        assert response_invalid_num.status_code == 400

    def test_serv_type_enum_values(self, session):
        """测试业务类型枚举值"""
        url = f"{FULL_URL}/navis-swagger/api/merchant/serv/getListByPage"
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

            response = session.post(url, headers=headers, json=payload)
            assert response.status_code == 200
            response_data = response.json()
            assert response_data["code"] == 200
            assert "pageData" in response_data
            assert "pageDataList" in response_data["pageData"]

    def test_invalid_serv_type(self, session):
        """测试无效的业务类型值"""
        url = f"{FULL_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}

        # 测试无效的servType值
        payload = {
            "merchantName": "",
            "servType": 99,  # 无效的业务类型
            "pageNum": 1,
            "pageSize": 10
        }

        response = session.post(url, headers=headers, json=payload)
        # 对于无效枚举值，通常应返回200但pageDataList为空
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["code"] == 200
        assert "pageData" in response_data
        assert "pageDataList" in response_data["pageData"]
        assert len(response_data["pageData"]["pageDataList"]) == 0

    def test_merchant_name_search(self, session):
        """测试商户名称搜索功能"""
        url = f"{FULL_URL}/navis-swagger/api/merchant/serv/getListByPage"
        headers = {"Content-Type": "application/json"}

        # 测试带商户名称的搜索
        test_merchant_name = "测试商户"
        payload = {
            "merchantName": test_merchant_name,
            "servType": 0,
            "pageNum": 1,
            "pageSize": 10
        }

        response = session.post(url, headers=headers, json=payload)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["code"] == 200
        # 验证返回的数据结构
        assert "pageData" in response_data
        assert "pageDataList" in response_data["pageData"]
        # 如果有结果，验证商户名称是否匹配（根据实际接口实现调整）
        if len(response_data["pageData"]["pageDataList"]) > 0:
            for item in response_data["pageData"]["pageDataList"]:
                assert test_merchant_name in item.get("merchantName", "")