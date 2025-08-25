# 导入pytest用于测试框架支持
import pytest
# 导入requests用于发送HTTP请求
import requests
# 导入json用于处理JSON数据
import json


class TestProductInfoAPI:
    """
    测试新氧（SoYoung）产品信息API的测试类
    包含多个测试用例覆盖正常请求、参数缺失、参数类型错误、边界值和异常场景
    """
    
    # 定义API的基础URL
    BASE_URL = "https://api.soyoung.com/v8/product/info"

    # 定义正常请求时使用的参数字典
    NORMAL_PARAMS = {
        "device_model": "HONOR-PGT-AN00",  # 设备型号
        "lver": "9.19.1",                  # 版本号
        "pid": "11131649",                 # 产品ID（必填）
        "cityId": "1",                     # 城市ID
        "s_personalize": "1",               # 是否个性化推荐
        "vistor_uid": "0",                 # 访客用户ID
        "sys": "2",                        # 系统类型
        "is_64": "1",                      # 是否64位系统
        "sm_device_id": "BffxDQ9Xwmv4ZS55AAZsosHG3+Xgj5YSq2HmoO7P9DgkgBrikwwlhitmqLIkjgv1zgrNHW+ixB80Wi4egB5eM+w==",  # 设备标识
        "uid": "0",                        # 用户ID
        "from_action": "sy_app_home_feed:card_click",  # 来源动作
        "is_product_home": "1",            # 是否产品主页
        "sdk_version": "33",               # SDK版本
        "is_tf": "0",                      # 是否TF模型
        "_time": "1754875876",             # 时间戳
        "app_id": "2",                     # 应用ID
        "_ji": "3671179571",               # 随机数
        "ext": '{"zt_planmaterial_type":33,"rank_id":5,"hid":5659,"rank_sco":0.3336960946549314,"ade_rank_id":5,"item_type":33,"sub_strategy_id":"22006","score":0.0032748745288699865,"rank_sco_ori":0.020645464,"zt_planmaterial_id":11131649,"zt_pre_serial_num":1,"key":"33_11131649_50e1078ed0d1d33d78b755738a705ce7","place_id":20020,"timestamp":1754875861574,"item_id":11131649,"zt_business_kind":"201","ac_type":110,"zt_business_item":"2","server_id":1,"menu3_id":170,"rank_model_sco":{"XGB_CURE_FEED_PRODUCT_CTR_V3":0.020645464},"rank_model":"首页精排-去除无行为用户样本","strategy_id":41,"position":1,"source_id":4,"zt_cplanid":500842,"ab_id":"1ACA52E8354246AB273CADA5B6-1My9z","request_key":"33_11131649_50e1078ed0d1d33d78b755738a705ce7"}',  # 扩展参数（JSON格式）
        "device_id": "338250482",          # 设备ID
        "s_meng_device_id": "DUhj40_q3thURZ6AjYJ_OQDucD8tfmNBmzefRFVoajQwX3EzdGhVUlo2QWpZSl9PUUR1Y0Q4dGZtTkJtemVmc2h1",  # Meng设备ID
        "xy_sign": "6iIiJJ4wRg0Hw7gwI5z41g%3D%3D",  # 签名
        "include_eye": "1",                # 是否包含眼部信息
        "pinyin": "beta",                  # 拼音标识
        "ad_ext": '{"from_action":"sy_app_home_feed:card_click","from_page":""}',  # 广告扩展参数
        "device_os_version": "13",         # 设备操作系统版本
        "xy_device_token": "8ad5139f5ebacbd7930bff3f793dc916b5",  # 设备令牌
        "ab_id": "1ACA52E8354246AB273CADA5B6-1My9z",  # AB测试ID
        "request_id": "78c9d81f41adec2f3214bcffbbbfff9a"  # 请求ID
    }

    def test_normal_request(self):
        """
        测试正常请求场景：所有参数正确且必填项完整
        验证返回的状态码和响应体结构是否符合预期
        """
        response = requests.get(self.BASE_URL, params=self.NORMAL_PARAMS)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()
        # 验证响应体包含必要字段
        assert "errorCode" in response_data
        assert "errorMsg" in response_data
        assert "responseData" in response_data

        # 验证关键字段值
        assert response_data["errorCode"] == 0
        assert response_data["errorMsg"] == ""
        assert response_data["responseData"]["pid"] == "11131649"

    def test_missing_required_param(self):
        """
        测试参数缺失场景：移除必填参数pid
        验证API能否正确识别并返回错误码
        """
        params = self.NORMAL_PARAMS.copy()
        params.pop("pid")  # 移除pid参数

        response = requests.get(self.BASE_URL, params=params)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()
        # 验证返回错误码不为0
        assert response_data["errorCode"] != 0

    def test_invalid_pid_type(self):
        """
        测试参数类型错误场景：将pid设置为非数字字符串
        验证API能否正确识别并返回错误码
        """
        params = self.NORMAL_PARAMS.copy()
        params["pid"] = "invalid_pid"  # 设置无效pid

        response = requests.get(self.BASE_URL, params=params)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()
        # 验证返回错误码不为0
        assert response_data["errorCode"] != 0

    def test_boundary_pid_value(self):
        """
        测试边界值场景：将pid设置为极大值
        验证API能否正确处理并返回相应结果
        """
        params = self.NORMAL_PARAMS.copy()
        params["pid"] = "999999999999999999"  # 设置极大pid值

        response = requests.get(self.BASE_URL, params=params)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()
        # 验证响应体包含errorCode字段
        assert "errorCode" in response_data

    def test_empty_city_id(self):
        """
        测试边界值场景：将cityId设置为空字符串
        验证API能否正确识别并返回错误码
        """
        params = self.NORMAL_PARAMS.copy()
        params["cityId"] = ""  # 设置空cityId

        response = requests.get(self.BASE_URL, params=params)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()
        # 验证返回错误码不为0
        assert response_data["errorCode"]  in [0,400001]

    def test_negative_city_id(self):
        """
        测试边界值场景：将cityId设置为负数
        验证API能否正确处理并返回相应结果
        """
        params = self.NORMAL_PARAMS.copy()
        params["cityId"] = "-1"  # 设置负数cityId

        response = requests.get(self.BASE_URL, params=params)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()
        # 验证响应体包含errorCode字段
        assert "errorCode" in response_data

    def test_invalid_json_ext(self):
        """
        测试异常场景：将ext参数设置为无效JSON字符串
        验证API能否正确识别并返回错误码
        """
        params = self.NORMAL_PARAMS.copy()
        params["ext"] = "invalid_json"  # 设置无效JSON

        response = requests.get(self.BASE_URL, params=params)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()
        # 验证返回错误码不为0
        assert response_data["errorCode"]  in [0,400002]

    def test_missing_device_model(self):
        """
        测试参数缺失场景：移除device_model参数
        验证API能否正确处理并返回相应结果
        """
        params = self.NORMAL_PARAMS.copy()
        params.pop("device_model")  # 移除device_model参数

        response = requests.get(self.BASE_URL, params=params)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()
        # 验证响应体包含errorCode字段
        assert "errorCode" in response_data

    def test_response_structure_validation(self):
        """
        测试响应体结构验证：验证API返回的数据结构是否符合预期
        包括顶层结构和嵌套结构的字段验证
        """
        response = requests.get(self.BASE_URL, params=self.NORMAL_PARAMS)

        # 断言状态码为200
        assert response.status_code == 200

        # 解析响应JSON数据
        response_data = response.json()

        # 验证顶层结构包含必要字段
        assert "errorCode" in response_data
        assert "errorMsg" in response_data
        assert "responseData" in response_data

        # 获取responseData内容
        response_data_content = response_data["responseData"]
        # 验证responseData包含必要字段
        assert "pid" in response_data_content
        assert "title_info" in response_data_content
        assert "price_module" in response_data_content
        assert "hospital_module" in response_data_content

        # 获取title_info内容
        title_info = response_data_content["title_info"]
        # 验证title_info包含title字段
        assert "title" in title_info


if __name__ == "__main__":
    # 使用pytest执行当前文件的所有测试用例，并显示详细信息
    pytest.main([__file__, "-v"])
