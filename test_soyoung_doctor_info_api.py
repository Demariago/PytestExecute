import pytest
import requests
import json

# 配置基础URL和请求头
BASE_URL = "https://api.soyoung.com/v8/doctors/InfoBasicByDynamic842"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; HONOR-PGT-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.158 Mobile Safari/537.36",
    "Content-Type": "application/json",
}

# 请求参数（正常情况）
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
    "doctor_id": "228007",
    "uid": "0",
    "from_action": "sy_app_home_feed:card_click",
    "sdk_version": "33",
    "is_tf": "0",
    "_time": "1756105579",
    "app_id": "2",
    "ext": {
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
    },
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


# 测试类
class TestDoctorInfoBasicByDynamic842:
    @pytest.fixture(autouse=True)
    def setup(self):
        """每次测试前执行"""
        self.url = BASE_URL

    def test_normal_request(self):
        """测试正常请求 - 所有参数正确"""
        response = requests.get(self.url, headers=HEADERS, params=NORMAL_PARAMS)

        # 断言状态码
        assert response.status_code == 200, f"期望状态码 200，实际为 {response.status_code}"

        # 解析响应体
        resp_data = response.json()

        # 断言 errorCode 为 0
        assert resp_data.get("errorCode") == 0, f"期望 errorCode 为 0，实际为 {resp_data.get('errorCode')}"

        # 断言 errorMsg 为空
        assert resp_data.get("errorMsg") == "", f"期望 errorMsg 为空，实际为 {resp_data.get('errorMsg')}"

        # 断言 responseData 存在
        assert "responseData" in resp_data, "响应中缺少 responseData"

        # 断言医生信息存在
        doctor_data = resp_data["responseData"]["doctor"]
        doctor_data_statistics=resp_data["responseData"]["statistics"]
        assert doctor_data is not None, "医生信息为空"

        # 验证关键字段
        assert doctor_data["doctor_id"] == "228007", "doctor_id 不匹配"
        assert doctor_data["name_cn"] == "王珮蓉", "name_cn 不匹配"
        assert doctor_data["gender"] == "女", "gender 不匹配"
        assert doctor_data["hospital_show_words"] == "北京雅靓医疗美容诊所", "hospital_show_words 不匹配"

        # 验证职称
        assert doctor_data["position"] == "医师", "position 不匹配"

        # 验证认证信息
        assert doctor_data["certified"] == "1", "certified 不匹配"

        # 验证评价信息
        stats = doctor_data_statistics
        assert stats["fans_cnt"] == "1", "粉丝数不匹配"
        assert stats["patient_cnt"] == "158", "服务人次不匹配"
        assert stats["diary_cnt"] == "19", "日记数不匹配"

        # 验证医生标签
        op_labels = resp_data["responseData"]["doctor_op_label"]
        assert any(label["key"] == "yishi" for label in op_labels), "未找到 '医师' 标签"
        assert any(label["key"] == "wjw_verify" for label in op_labels), "未找到 '查资质' 标签"

        # 验证专家专长
        expert_all = doctor_data["extend"]["expert_all"]
        assert len(expert_all) > 0, "专家专长为空"
        assert any(e["name"] == "瘦脸轮廓" for e in expert_all), "缺少 '瘦脸轮廓' 专长"
        assert any(e["name"] == "玻尿酸" for e in expert_all), "缺少 '玻尿酸' 专长"

        # 验证图文面诊设置
        face_consultation = resp_data["responseData"]["face_consultation_card"]
        assert face_consultation["is_show"] == "1", "视频面诊不可见"

        # 验证服务人次统计
        assert resp_data['responseData']["statistics"]["patient_cnt"] == "158", "服务人次统计错误"

    def test_missing_doctor_id(self):
        """测试 doctor_id 缺失"""
        params = NORMAL_PARAMS.copy()
        del params["doctor_id"]

        response = requests.get(self.url, headers=HEADERS, params=params)

        assert response.status_code == 200
        resp_data = response.json()
        assert resp_data.get("errorCode") != 0, "缺少 doctor_id 应返回错误"
        assert resp_data.get("errorMsg"), "缺少 doctor_id 时应返回错误信息"

    def test_invalid_doctor_id(self):
        """测试 doctor_id 为非法值"""
        params = NORMAL_PARAMS.copy()
        params["doctor_id"] = "invalid_id"

        response = requests.get(self.url, headers=HEADERS, params=params)

        assert response.status_code == 200
        resp_data = response.json()
        assert resp_data.get("errorCode") == 0, "无效 doctor_id 应仍返回成功，但数据为空或错误"
        # 实际业务中可能返回空或错误，但此处假设仍返回 0
        # 可根据实际行为调整断言

    def test_missing_ext(self):
        """测试 ext 参数缺失"""
        params = NORMAL_PARAMS.copy()
        del params["ext"]

        response = requests.get(self.url, headers=HEADERS, params=params)

        assert response.status_code == 200
        resp_data = response.json()
        assert resp_data.get("errorCode") == 0, "缺少 ext 参数应返回成功或特定错误"
        # 根据实际行为调整断言

    def test_invalid_ext_format(self):
        """测试 ext 参数格式错误"""
        params = NORMAL_PARAMS.copy()
        params["ext"] = "invalid_json"

        response = requests.get(self.url, headers=HEADERS, params=params)

        assert response.status_code == 200
        resp_data = response.json()
        assert resp_data.get("errorCode") != 0 or "responseData" not in resp_data, "无效 ext 应导致错误或空结果"

    def test_include_eye_zero(self):
        """测试 include_eye=0 时返回结果是否正常"""
        params = NORMAL_PARAMS.copy()
        params["include_eye"] = "0"

        response = requests.get(self.url, headers=HEADERS, params=params)

        assert response.status_code == 200
        resp_data = response.json()
        assert resp_data.get("errorCode") == 0
        # 确保响应结构完整，即使 include_eye=0 也不应崩溃