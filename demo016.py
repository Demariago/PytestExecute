import pytest
from unittest.mock import patch
from datetime import time, datetime, timedelta
from demo015 import input_time, time_difference

class TestInputTime:
    def test_input_time_valid(self):
        """测试有效的输入时间"""
        with patch('builtins.input', return_value='12:34:56'):
            user_time = input_time()
            assert user_time == time(12, 34, 56)

    def test_input_time_invalid(self):
        """测试无效的输入时间"""
        with patch('builtins.input', side_effect=['12:34:567', '12:34', '12:34:56']):
            user_time = input_time()
            assert user_time == time(12, 34, 56)

class TestTimeDifference:
    def test_time_difference_positive(self):
        """测试正向时间差"""
        time_a = time(12, 34, 56)
        time_b = time(10, 30, 40)
        delta = time_difference(time_a, time_b)
        expected_delta = timedelta(hours=2, minutes=4, seconds=16)
        assert delta == expected_delta

    def test_time_difference_negative(self):
        """测试负向时间差"""
        time_a = time(10, 30, 40)
        time_b = time(12, 34, 56)
        delta = time_difference(time_a, time_b)
        expected_delta = timedelta(hours=-2, minutes=-4, seconds=-16)
        assert delta == expected_delta

# 运行测试
if __name__ == "__main__":
    pytest.main()
