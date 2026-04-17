import pytest
import pandas as pd
import numpy as np
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks.task_manager import *


def test_is_monster_killed():
    assert type(is_monster_killed(0.5)) == bool

def test_simulate_monster_hunts():
    result = simulate_monster_hunts(100, 0.6)
    assert 0 <= result <= 100

def test_expected_poison_attacks():
    total = expected_poison_attacks(2.0, 3)
    assert total >= 0

def test_probability_k_monsters_killed():
    prob = probability_k_monsters_killed(3, 10, 0.5)
    assert 0 <= prob <= 1

def test_poisson_probability():
    p = poisson_probability(4, 3.0)
    assert 0 <= p <= 1

def test_average_kill_rate():
    rate = average_kill_rate(1000, 0.5)
    assert 0.4 <= rate <= 0.6

def test_compare_two_witchers():
    winner = compare_two_witchers(0.6, 0.7, 500)
    assert winner in ["Witcher 1", "Witcher 2", "Tie"]

def test_simulate_poison_attacks_day():
    attacks = simulate_poison_attacks_day(24, 3.0)
    assert len(attacks) == 24
    assert all(isinstance(a, int) and a >= 0 for a in attacks)

def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")

class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://kaizu-api-8cd10af40cb3.herokuapp.com/projectLog"
    payload = {
        "user_id": 34,
        "project_id": 665,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)

if __name__ == "__main__":
    run_tests()
