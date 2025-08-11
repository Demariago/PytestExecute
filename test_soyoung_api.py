import pytest
import requests

class TestSoyoungAPI:
    # 基础URL和通用参数
    BASE_URL = "https://api.soyoung.com/v8/product/info"
    COMMON_PARAMS = {
        "device_model": "HONOR-PGT-AN00",
        "lver": "9.19.1",
        "pid": "11131649",
        "cityId": "1",
        "s_personalize": "1",
        "vistor_uid": "0",
        "sys": "2",
        "is_64": "1",
        "sm_device_id": "BffxDQ9Xwmv4ZS55AAZsosHG3%2BXgj5YSq2HmoO7P9DgkgBrikwwlhitmqLIkjgv1zgrNHW%2BixB80Wi4egB5eM%2Bw%3D%3D",
        "uid": "0",
        "from_action": "sy_app_home_feed%3Acard_click",
        "is_product_home": "1",
        "sdk_version": "33",
        "is_tf": "0",
        "_time": "1754875876",
        "app_id": "2",
        "_ji": "3671179571",
        "ext": "%7B%22zt_planmaterial_type%22%3A33%2C%22rank_id%22%3A5%2C%22hid%22%3A5659%2C%22rank_sco%22%3A0.3336960946549314%2C%22ade_rank_id%22%3A5%2C%22item_type%22%3A33%2C%22sub_strategy_id%22%3A%2222006%22%2C%22score%22%3A0.0032748745288699865%2C%22rank_sco_ori%22%3A0.020645464%2C%22zt_planmaterial_id%22%3A11131649%2C%22zt_pre_serial_num%22%3A1%2C%22key%22%3A%2233_11131649_50e1078ed0d1d33d78b755738a705ce7%22%2C%22place_id%22%3A20020%2C%22timestamp%22%3A1754875861574%2C%22item_id%22%3A11131649%2C%22zt_business_kind%22%3A%22201%22%2C%22ac_type%22%3A110%2C%22zt_business_item%22%3A%222%22%2C%22server_id%22%3A1%2C%22menu3_id%22%3A170%2C%22rank_model_sco%22%3A%7B%22XGB_CURE_FEED_PRODUCT_CTR_V3%22%3A0.020645464%7D%2C%22rank_model%22%3A%22%5Cu9996%5Cu9875%5Cu7cbe%5Cu6392-%5Cu53bb%5Cu9664%5Cu65e0%5Cu884c%5Cu4e3a%5Cu7528%5Cu6237%5Cu6837%5Cu672c%22%2C%22strategy_id%22%3A41%2C%22position%22%3A1%2C%22source_id%22%3A4%2C%22zt_cplanid%22%3A500842%2C%22ab_id%22%3A%221ACA52E8354246AB273CADA5B6-1My9z%22%2C%22request_key%22%3A%2233_11131649_50e1078ed0d1d33d78b755738a705ce7%22%7D",
        "device_id": "338250482",
        "s_meng_device_id": "DUhj40_q3thURZ6AjYJ_OQDucD8tfmNBmzefRFVoajQwX3EzdGhVUlo2QWpZSl9PUUR1Y0Q4dGZtTkJtemVmc2h1",
        "xy_sign": "6iIiJJ4wRg0Hw7gwI5z41g%253D%253D",
        "include_eye": "1",
        "pinyin": "beta",
        "ad_ext": "%7B%22from_action%22%3A%22sy_app_home_feed%3Acard_click%22%2C%22from_page%22%3A%22%22%7D",
        "device_os_version": "13",
        "xy_device_token": "8ad5139f5ebacbd7930bff3f793dc916b5",
        "ab_id": "1ACA52E8354246AB273CADA5B6-1My9z",
        "request_id": "78c9d81f41adec2f3214bcffbbbfff9a"
    }

    def test_successful_request(self):
        """测试成功请求API"""
        response = requests.get(self.BASE_URL, params=self.COMMON_PARAMS)
        # 检查响应状态码
        assert response.status_code == 200
        # 检查响应JSON格式
        response_json = response.json()
        assert isinstance(response_json, dict)
        # 检查错误码
        assert response_json.get("errorCode") == 0
        assert response_json.get("errorMsg") == ""
        # 检查响应数据
        response_data = response_json.get("responseData")
        assert response_data is not None
        assert isinstance(response_data, dict)
        # 检查产品ID是否匹配
        assert response_data.get("pid") == "11131649"
        # 检查标题信息
        title_info = response_data.get("title_info")
        assert title_info is not None
        assert isinstance(title_info, dict)
        assert "title" in title_info

    def test_missing_required_param(self):
        """测试缺少必填参数"""
        # 复制通用参数并删除一个必填参数
        invalid_params = self.COMMON_PARAMS.copy()
        invalid_params.pop("pid")  # pid应该是必填参数
        
        response = requests.get(self.BASE_URL, params=invalid_params)
        # 这里假设缺少必填参数会返回非200状态码或错误码非0
        # 实际情况可能需要根据API文档调整
        response_json = response.json()
        assert response_json.get("errorCode") != 0 or response.status_code != 200

    def test_invalid_param_value(self):
        """测试无效的参数值"""
        # 复制通用参数并修改一个参数值为无效值
        invalid_params = self.COMMON_PARAMS.copy()
        invalid_params["pid"] = "invalid_pid"
        
        response = requests.get(self.BASE_URL, params=invalid_params)
        response_json = response.json()
        # 检查是否返回错误
        assert response_json.get("errorCode") != 0 or response.status_code != 200

    def test_response_data_structure(self):
        """测试响应数据结构"""
        response = requests.get(self.BASE_URL, params=self.COMMON_PARAMS)
        response_json = response.json()
        response_data = response_json.get("responseData")
        
        # 检查更多数据结构
        assert "is_vip" in response_data
        assert "is_vip_user" in response_data
        assert "is_qzy" in response_data
        assert "request_time" in response_data
        assert "menu1_id" in response_data
        
        # 检查模块顺序
        assert "module_order" in response_data
        assert isinstance(response_data["module_order"], list)
        
        # 检查头部模块
        assert "header_module" in response_data
        header_module = response_data["header_module"]
        assert "image" in header_module
        assert isinstance(header_module["image"], list)
        assert len(header_module["image"]) > 0
        assert "img_url" in header_module["image"][0]

if __name__ == "__main__":
    pytest.main(["-v", "test_soyoung_api.py"])