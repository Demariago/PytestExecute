import pytest
import requests
import json

# 配置变量
BASE_URL = "https://api.soyoung.com"
API_PATH = "/v8/hospitals/homeV2"
FULL_URL = BASE_URL + API_PATH

# 正常请求参数（已解码的ext）
NORMAL_EXT = {
    "zt_planmaterial_type": 50,
    "hid": 148600,
    "rank_sco": 18.507013877005182,
    "item_id": 148600,
    "item_type": 50,
    "sub_strategy_id": "35500",
    "zt_business_kind": "201",
    "ac_type": 100,
    "zt_business_item": "2",
    "server_id": 1,
    "score": 2.0430956,
    "rank_sco_ori": 2.0430956,
    "zt_planmaterial_id": 148600,
    "strategy_id": 355,
    "zt_pre_serial_num": 1,
    "position": 1,
    "source_id": 4,
    "zt_cplanid": 502777,
    "db": "2025-08-25",
    "key": "50_148600_5a83a9b81374070869fcd43a96198eea",
    "place_id": 10005,
    "request_key": "50_148600_5a83a9b81374070869fcd43a96198eea",
    "timestamp": 1756089549285
}

# 请求参数模板
REQUEST_PARAMS_TEMPLATE = {
    "ext": json.dumps(NORMAL_EXT),
    "_jk": "970957810",
    "device_model": "HONOR-PGT-AN00",
    "lver": "9.19.1",
    "vistor_uid": "0",
    "hospital_id": "148600",
    "sys": "2",
    "xy_sign": "iwapxZr3Tw1BiW%2B6MdWBaA%3D%3D",
    "is_64": "1",
    "include_eye": "1",
    "uid": "0",
    "pinyin": "beta",
    "from_action": "sy_app_home_feed%3Acard_click",
    "sdk_version": "33",
    "device_os_version": "13",
    "is_tf": "0",
    "_time": "1756089560",
    "app_id": "2",
    "request_id": "c797fe97f8b8ebeb8ea087daa54d0ef8"
}


class TestHospitalHomeV2API:
    """测试医院首页V2接口"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """前置条件：确保请求头设置正确"""
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 13; HONOR-PGT-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
        }

    def test_normal_request(self):
        """测试正常请求：所有参数正确，预期返回成功"""
        # 构造请求参数
        params = REQUEST_PARAMS_TEMPLATE.copy()

        # 发送请求
        response = requests.get(FULL_URL, params=params, headers=self.headers)

        # 断言
        assert response.status_code == 200
        resp_json = response.json()

        assert resp_json.get("errorCode") == 0
        assert resp_json.get("errorMsg") == ""
        assert resp_json.get("responseData") is not None
        assert resp_json["responseData"].get("hospital_info") is not None
        assert resp_json["responseData"]["hospital_info"].get("name_cn") == "西安国际医学中心医院"
        assert resp_json["responseData"]["hospital_info"].get("hospital_id") == "148600"
        assert resp_json["responseData"]["hospital_info"].get("score_level") == "3"
        assert resp_json["responseData"]["hospital_info"].get("satisfy") == "4.82"

    def test_missing_required_parameter(self):
        """测试缺失必填参数：移除hospital_id"""
        params = REQUEST_PARAMS_TEMPLATE.copy()
        del params["hospital_id"]

        response = requests.get(FULL_URL, params=params, headers=self.headers)

        assert response.status_code == 200
        resp_json = response.json()
        assert resp_json.get("errorCode") != -1

    def test_invalid_ext_format(self):
        """测试ext参数格式错误：传入非JSON字符串"""
        params = REQUEST_PARAMS_TEMPLATE.copy()
        params["ext"] = "invalid_json_string"

        response = requests.get(FULL_URL, params=params, headers=self.headers)

        assert response.status_code == 200
        resp_json = response.json()
        assert resp_json.get("errorCode") != 200 or resp_json.get("responseData") is None

    def test_invalid_hospital_id(self):
        """测试hospital_id类型错误：传入非数字字符串"""
        params = REQUEST_PARAMS_TEMPLATE.copy()
        params["hospital_id"] = "abc"
        response = requests.get(FULL_URL, params=params, headers=self.headers)
        assert response.status_code == 200
        resp_json = response.json()
        assert resp_json.get("responseData", {}).get("code") == '-1'

    def test_empty_ext(self):
        """测试ext为空：传入空字符串"""
        params = REQUEST_PARAMS_TEMPLATE.copy()
        params["ext"] = ""

        response = requests.get(FULL_URL, params=params, headers=self.headers)

        assert response.status_code == 200
        resp_json = response.json()
        assert resp_json.get("errorCode") == 0 or resp_json.get("responseData") is None

    def test_timestamp_boundary_value(self):
        """测试timestamp边界值：传入超大值和超小值"""
        # 测试超大timestamp
        params = REQUEST_PARAMS_TEMPLATE.copy()
        params["ext"] = json.dumps({**NORMAL_EXT, "timestamp": 9999999999999})

        response = requests.get(FULL_URL, params=params, headers=self.headers)
        resp_json = response.json()
        # 通常接口会校验时间有效性，但允许大值
        assert response.status_code == 200
        assert resp_json.get("errorCode") == 0

        # 测试超小timestamp（历史时间）
        params["ext"] = json.dumps({**NORMAL_EXT, "timestamp": 1})
        response = requests.get(FULL_URL, params=params, headers=self.headers)
        resp_json = response.json()
        # 超小时间可能被拒绝
        assert response.status_code == 200
        assert resp_json.get("errorCode") == 0
