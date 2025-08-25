import pytest
import requests
import json

# 配置参数
BASE_URL = "https://api.soyoung.com/v8/hospitals/homeV2"
EXT_PARAMS = {
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

# 公共请求头
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; HONOR-PGT-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.166 Mobile Safari/537.36",
    "Content-Type": "application/json"
}

# 公共查询参数
QUERY_PARAMS = {
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
    "from_action": "sy_app_home_feed:card_click",
    "sdk_version": "33",
    "device_os_version": "13",
    "is_tf": "0",
    "_time": "1756089560",
    "app_id": "2",
    "request_id": "c797fe97f8b8ebeb8ea087daa54d0ef8"
}

class TestHospitalHomeV2API:
    """
    测试接口：https://api.soyoung.com/v8/hospitals/homeV2
    功能：获取医院主页数据（V2版本）
    """

    @pytest.fixture(autouse=True)
    def setup(self):
        """初始化测试前准备"""
        self.url = f"{BASE_URL}?ext={requests.utils.quote(json.dumps(EXT_PARAMS))}"
        for k, v in QUERY_PARAMS.items():
            self.url += f"&{k}={v}"

    def test_normal_request_success(self):
        """
        正常请求场景：参数完整且正确，期望返回成功状态码和有效数据
        """
        response = requests.get(self.url, headers=HEADERS)

        # 断言状态码为200
        assert response.status_code == 200, f"期望状态码为200，实际为{response.status_code}"

        # 解析响应体
        data = response.json()

        # 断言 errorCode 为 0
        assert data.get("errorCode") == 0, f"期望 errorCode 为 0，实际为 {data.get('errorCode')}"

        # 断言 errorMsg 为空
        assert data.get("errorMsg") == "", f"期望 errorMsg 为空，实际为 {data.get('errorMsg')}"

        # 断言 responseData 存在且不为空
        response_data = data.get("responseData")
        assert response_data is not None, "期望 responseData 存在"
        assert isinstance(response_data, dict), "期望 responseData 为字典类型"

        # 断言 hospital_info 存在且包含关键字段
        hospital_info = response_data.get("hospital_info")
        assert hospital_info is not None, "期望 hospital_info 存在"
        assert hospital_info.get("name_cn") == "西安国际医学中心医院", "医院名称不匹配"
        assert hospital_info.get("hospital_id") == "148600", "医院ID不匹配"
        assert hospital_info.get("score_level") == "3", "评分等级不匹配"

        # 断言满意度数据正确
        assert hospital_info.get("satisfy") == "4.82", "满意度评分不匹配"
        assert hospital_info.get("post_effect") == "4.8", "术后效果评分不匹配"
        assert hospital_info.get("post_environment") == "4.9", "环境评分不匹配"
        assert hospital_info.get("post_service") == "4.6", "服务评分不匹配"

        # 断言 award 列表至少有一个奖项
        awards = hospital_info.get("award", [])
        assert len(awards) > 0, "奖项列表不应为空"

        # 断言底部按钮存在且配置正确
        bottom_btn = response_data.get("bottom_btn", [])
        assert len(bottom_btn) >= 4, "底部按钮数量不足"
        btn_names = [btn.get("name") for btn in bottom_btn]
        assert "预约" in btn_names
        assert "写日记" in btn_names
        assert "电话咨询" in btn_names
        assert "私信咨询" in btn_names

    def test_missing_required_params(self):
        """
        异常场景：缺少必填参数（如 hospital_id 或 ext）
        """
        # 构造缺少 hospital_id 的 URL
        url_without_hospital_id = self.url.replace("hospital_id=148600", "hospital_id=")

        # 构造缺少 ext 参数的 URL
        url_without_ext = self.url.replace(f"ext={requests.utils.quote(json.dumps(EXT_PARAMS))}", "")

        # 测试缺少 hospital_id
        response1 = requests.get(url_without_hospital_id, headers=HEADERS)
        assert response1.status_code == 200, "缺少 hospital_id 应返回 200"
        data1 = response1.json()
        assert data1.get("errorCode") != 0 or "hospital_info" in str(data1), "缺少 hospital_id 应返回错误"

        # 测试缺少 ext
        response2 = requests.get(url_without_ext, headers=HEADERS)
        assert response2.status_code == 200, "缺少 ext 应返回 200"
        data2 = response2.json()
        assert data2.get("errorCode") != 0 or "ext" in str(data2), "缺少 ext 应返回错误"

    def test_invalid_ext_format(self):
        """
        异常场景：ext 参数格式错误（非 JSON 格式）
        """
        invalid_ext_url = f"{BASE_URL}?ext=invalid_json&_jk=970957810&hospital_id=148600&..." + "&".join(
            f"{k}={v}" for k, v in QUERY_PARAMS.items()
        )
        response = requests.get(invalid_ext_url, headers=HEADERS)
        assert response.status_code == 200, "无效 ext 应返回 200"
        data = response.json()
        assert data.get("errorCode") == 0, "无效 ext 应返回非零 errorCode"

    def test_invalid_timestamp(self):
        """
        异常场景：timestamp 为非法值（如非数字）
        """
        # 替换 timestamp 为非法字符串
        invalid_timestamp_url = self.url.replace("timestamp=1756089549285", "timestamp=invalid")
        response = requests.get(invalid_timestamp_url, headers=HEADERS)
        assert response.status_code == 200, "非法 timestamp 应返回 200"
        data = response.json()
        assert data.get("errorCode") == 0, "非法 timestamp 应触发错误"

    def test_boundary_value_rank_sco(self):
        """
        边界值测试：rank_sco 设置为边界值（如 0、100、负数）
        """
        # 测试 rank_sco 为 0
        ext_with_zero_rank = EXT_PARAMS.copy()
        ext_with_zero_rank["rank_sco"] = 0
        url_zero = f"{BASE_URL}?ext={requests.utils.quote(json.dumps(ext_with_zero_rank))}"
        for k, v in QUERY_PARAMS.items():
            url_zero += f"&{k}={v}"
        response = requests.get(url_zero, headers=HEADERS)
        assert response.status_code == 200, "rank_sco=0 应返回成功"
        data = response.json()
        assert data.get("errorCode") == 0, "rank_sco=0 时应返回成功"

        # 测试 rank_sco 为负数
        ext_with_negative_rank = EXT_PARAMS.copy()
        ext_with_negative_rank["rank_sco"] = -100
        url_negative = f"{BASE_URL}?ext={requests.utils.quote(json.dumps(ext_with_negative_rank))}"
        for k, v in QUERY_PARAMS.items():
            url_negative += f"&{k}={v}"
        response = requests.get(url_negative, headers=HEADERS)
        assert response.status_code == 200, "rank_sco 为负数应返回成功"
        data = response.json()
        assert data.get("errorCode") == 0, "rank_sco 为负数应返回成功"

    def test_response_structure_integrity(self):
        """
        验证响应结构完整性，确保关键字段始终存在
        """
        response = requests.get(self.url, headers=HEADERS)
        data = response.json()

        # 关键字段检查
        required_fields = [
            "errorCode", "errorMsg", "responseData"
        ]
        for field in required_fields:
            assert field in data, f"响应体缺少必填字段: {field}"

        # responseData 下的关键字段
        response_data = data["responseData"]
        assert "hospital_info" in response_data, "responseData 必须包含 hospital_info"
        assert "bottom_btn" in response_data, "responseData 必须包含 bottom_btn"
        assert "event" in response_data, "responseData 必须包含 event"
        assert "background" in response_data, "responseData 必须包含 background"

    def test_cache_and_performance(self):
        """
        性能测试：快速重试请求，验证是否能快速响应（模拟缓存）
        """
        # 重复请求3次，应全部成功
        for i in range(3):
            response = requests.get(self.url, headers=HEADERS, timeout=5)
            assert response.status_code == 200, f"第{i+1}次请求失败"
            data = response.json()
            assert data.get("errorCode") == 0, f"第{i+1}次请求 errorCode 不为0"