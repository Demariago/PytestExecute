import pytest
import requests

# 基础配置
BASE_URL = "http://test.zhongautohealth.com/navis-gateway-admin/navis-swagger/api/merchant/serv/detail/shop"


class TestShopDetail:
    """测试获取门店详情接口"""

    @pytest.mark.parametrize("serv_id", [1, 100, 9999])
    def test_normal_request(self, serv_id):
        """测试正常请求场景：参数正确、必填项完整"""
        params = {"servId": serv_id}
        response = requests.get(BASE_URL, params=params)

        # 断言状态码
        assert response.status_code == 200, f"状态码异常: {response.status_code}"

        # 断言响应体结构
        response_json = response.json()
        assert "code" in response_json
        assert "message" in response_json
        assert "data" in response_json

        # 断言业务逻辑：code为0表示成功
        assert response_json["code"] == 0, f"业务code异常: {response_json['code']}"

        # 验证data字段中的关键信息
        data = response_json["data"]
        if data:  # 如果data不为空
            assert "id" in data
            assert "merchantName" in data
            assert "contactMobile" in data
            assert "businessStatus" in data
            # 验证营业状态在有效范围内
            assert data["businessStatus"] in [1, 2, 3, 4], f"无效的营业状态: {data['businessStatus']}"

    def test_missing_required_param(self):
        """测试异常场景：缺失必填参数servId"""
        response = requests.get(BASE_URL)

        # 断言状态码（根据实际情况调整，可能是400或自定义错误码）
        assert response.status_code != 200, "缺失必填参数但请求成功"

        # 验证错误响应
        response_json = response.json()
        assert response_json["code"] != 0, "缺失必填参数但业务code为0"

    @pytest.mark.parametrize("invalid_serv_id", ["abc", None, ""])
    def test_invalid_param_type(self, invalid_serv_id):
        """测试异常场景：参数类型错误"""
        params = {"servId": invalid_serv_id}
        response = requests.get(BASE_URL, params=params)

        # 断言非200状态码或错误业务码
        assert response.status_code != 200 or response.json().get("code") != 0

    def test_boundary_value(self):
        """测试边界值：servId为0和极大值"""
        # 测试0值
        response_0 = requests.get(BASE_URL, params={"servId": 0})
        # 测试极大值
        response_large = requests.get(BASE_URL, params={"servId": 9999999999})

        # 验证边界值处理
        assert response_0.status_code == 200 or response_0.json().get("code") != 0
        assert response_large.status_code == 200 or response_large.json().get("code") != 0


if __name__ == "__main__":
    pytest.main(["-v", __file__])