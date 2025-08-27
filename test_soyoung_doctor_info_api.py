import pytest
import requests
import json

# 配置基础URL和请求参数
BASE_URL = "https://api.soyoung.com/v8/doctors/InfoBasicByDynamic842"
DOCTOR_ID = "228007"

# 请求头设置（模拟移动端请求）
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; HONOR-PGT-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Content-Type": "application/json",
}

# 正常请求参数（原始接口参数）
NORMAL_PARAMS = {
    "device_model": "HONOR-PGT-AN00",
    "lver": "9.19.1",
    "cityId": "1",
    "s_personalize": "1",
    "vistor_uid": "0",
    "page_display_unique_id": "00246741bf35bb7a8f809cb1059f43a5",
    "sys": "2",
    "is_64": "1",
    "sm_device_id": "BqdOCnhtqdaUDFUGfBP80xReY N6umFg5P XXtafM4vLcKgN6OH0oOse92HYJrsNI4vI1SPWW bYT7zthY7ttBQ==",
    "doctor_id": DOCTOR_ID,
    "uid": "0",
    "from_action": "sy_app_home_feed:card_click",
    "sdk_version": "33",
    "is_tf": "0",
    "_time": "1756105579",
    "app_id": "2",
    "ext": json.dumps({
        "zt_planmaterial_type": 43,
        "hid": 182779,
        "rank_sco": 0,
        "item_id": 228007,
        "item_type": 43,
        "sub_strategy_id": "61001",
        "ac_type": 0,
        "server_id": 1,
        "score": 0.125,
        "rank_sco_ori": 0,
        "zt_planmaterial_id": 228007,
        "strategy_id": 467,
        "zt_pre_serial_num": 1,
        "position": 1,
        "source_id": 4,
        "ab_id": "C21DDA9F7131146B559111B08B-1MyAD",
        "db": "2025-08-25",
        "key": "43_228007_91b3f23c06a0e4cef891a9381ee7fba4",
        "place_id": 10006,
        "request_key": "43_228007_91b3f23c06a0e4cef891a9381ee7fba4",
        "timestamp": 1756105564883
    }),
    "_jk": "4060343230",
    "device_id": "338250482",
    "s_meng_device_id": "DU8LtcMfxmSWdOm-WIY7HNzJm501pTDvB970RFU4THRjTWZ4bVNXZE9tLVdJWTdITnpKbTUwMXBURHZCOTcwc2h1",
    "xy_sign": "rpgf5vmNLImwWce TKvVA==",
    "include_eye": "1",
    "pinyin": "beta",
    "device_os_version": "13",
    "xy_device_token": "6ad5139f5ebacbd7930bff3f793dc916b4",
    "ab_id": "C21DDA9F7131146B559111B08B-1MyAD",
    "request_id": "a5d738253e152240fb7f7ef320e95c24"
}


class TestDoctorInfoApi:
    """
    测试医生基本信息接口 /v8/doctors/InfoBasicByDynamic842
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        """前置操作：初始化请求参数"""
        self.url = BASE_URL
        self.headers = HEADERS
        self.params = NORMAL_PARAMS.copy()

    def test_normal_request_success(self):
        """测试正常请求 - 参数完整且正确"""
        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)

        # 断言状态码
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        # 解析响应体
        resp_json = response.json()

        # 验证业务逻辑字段
        assert resp_json.get("errorCode") == 0, "Expected errorCode=0"
        assert resp_json.get("errorMsg") == "", "Expected errorMsg to be empty"

        data = resp_json.get("responseData")
        assert data is not None, "Expected responseData to exist"

        doctor = data.get("doctor")
        assert doctor is not None, "Expected doctor object in responseData"

        # 校验医生核心信息
        assert doctor.get("doctor_id") == DOCTOR_ID, f"Expected doctor_id={DOCTOR_ID}"
        assert doctor.get("name_cn") == "王珮蓉", "Expected doctor name_cn=王珮蓉"
        assert doctor.get("gender") == "女", "Expected gender=女"
        assert doctor.get("hospital_show_words") == "北京雅靓医疗美容诊所", "Expected hospital_show_words"

        # 检查是否有资质认证标签
        verify_labels = doctor.get("is_follow")
        assert verify_labels in ("0", "1"), "Expected is_follow to be 0 or 1"

    def test_missing_doctor_id(self):
        """测试缺少 doctor_id 参数"""
        self.params.pop("doctor_id", None)

        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)

        # 预期返回错误码
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

        resp_json = response.json()
        assert resp_json.get("errorCode") != 0, "Expected errorCode != 0 when doctor_id missing"
        assert "doctor_id" in resp_json.get("errorMsg", ""), "Expected error message about doctor_id missing"

    def test_invalid_doctor_id(self):
        """测试无效 doctor_id（非数字）"""
        self.params["doctor_id"] = "invalid_id"

        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)

        assert response.status_code == 200
        resp_json = response.json()

        # 预期返回错误
        assert resp_json.get("errorCode") != 0, "Expected error for invalid doctor_id"
        assert "invalid" in resp_json.get("errorMsg", "").lower(), "Expected error related to invalid doctor_id"

    def test_invalid_timestamp(self):
        """测试 timestamp 参数异常（超大值）"""
        self.params["ext"] = json.dumps({
            **json.loads(self.params["ext"]),
            "timestamp": 9999999999999
        })

        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)

        assert response.status_code == 200
        resp_json = response.json()

        # 检查是否返回异常
        assert resp_json.get("errorCode") != 0 or "timeout" in resp_json.get("errorMsg", "").lower()

    def test_empty_ext_param(self):
        """测试 ext 参数为空"""
        self.params["ext"] = "{}"

        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)

        assert response.status_code == 200
        resp_json = response.json()

        assert resp_json.get("errorCode") == 0, "Expected success when ext is empty"
        assert resp_json.get("responseData") is not None, "Expected responseData when ext is empty"

    def test_invalid_ext_json(self):
        """测试 ext 参数为非法 JSON"""
        self.params["ext"] = "{\"invalid\":}"

        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)

        assert response.status_code == 200
        resp_json = response.json()

        # 预期返回解析失败
        assert resp_json.get("errorCode") != 0, "Expected error when ext is invalid JSON"
        assert "json" in resp_json.get("errorMsg", "").lower() or "parse" in resp_json.get("errorMsg", "").lower()

    def test_request_with_invalid_device_id(self):
        """测试 device_id 为非法值"""
        self.params["device_id"] = "-1"

        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)

        assert response.status_code == 200
        resp_json = response.json()

        # 通常这类接口不会因 device_id 失效而直接报错，但可检查逻辑是否正常
        assert resp_json.get("errorCode") == 0 or resp_json.get(
            "errorMsg") == "", "Expected valid response even with invalid device_id"

        # 检查返回数据是否合理
        data = resp_json.get("responseData")
        assert data is not None
        assert "doctor" in data, "Expected doctor info in response"

    def test_request_with_expired_timestamp(self):
        """测试时间戳过期（模拟时间错乱）"""
        self.params["ext"] = json.dumps({
            **json.loads(self.params["ext"]),
            "timestamp": 1000000000  # 2001年，远早于当前时间
        })

        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)

        assert response.status_code == 200
        resp_json = response.json()

        # 检查是否返回时间验证失败
        assert resp_json.get("errorCode") != 0 or "time" in resp_json.get("errorMsg", "").lower()

    def test_response_structure(self):
        """测试响应结构完整性"""
        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=10)
        resp_json = response.json()

        # 验证基础字段
        assert "errorCode" in resp_json
        assert "errorMsg" in resp_json
        assert "responseData" in resp_json

        # 验证 responseData 下的关键结构
        data = resp_json["responseData"]
        assert "doctor" in data
        assert "statistics" in data
        assert "hospital_list" in data
        assert "face_consultation_card" in data
        assert "koubeiAndDiary" in data

        # 检查是否包含医生画像信息
        doctor = data["doctor"]
        assert "name_cn" in doctor
        assert "hospital_show_words" in doctor
        assert "avatar" in doctor
