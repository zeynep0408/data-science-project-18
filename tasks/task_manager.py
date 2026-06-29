import random
from typing import List
import numpy as np
from scipy.stats import binom, poisson

# Açıklama:
# Bir Witcher'ın karşılaştığı canavarı öldürme şansı probability ile verilir.
# Bu olay bir Bernoulli deneyidir. Fonksiyon True (öldürdü) ya da False (ölmedi) döndürmelidir.
# Input: probability=0.7
# Output: True veya False
def is_monster_killed(probability: float) -> bool:
    return random.random() < probability
    pass


# Açıklama:
# Witcher 100 kez ava çıktıysa ve her avda canavarı öldürme şansı p ise,
# kaç canavar öldürüldüğünü Binom dağılımı ile simüle edin.
# Input: n=100, p=0.65
# Output: 68 (örnek)
def simulate_monster_hunts(n: int, p: float) -> int:
    return int(binom.rvs(n, p))
    pass


# Açıklama:
# Zehirli Ghoul'lar bir saat içinde ortalama lmbda kez saldırır.
# time saatlik süre için Poisson dağılımı ile toplam saldırı sayısını üretin.
# Input: lmbda=2.5, time=4
# Output: 10 (örnek)
def expected_poison_attacks(lmbda: float, time: int) -> int:
    return int(poisson.rvs(lmbda * time))
    pass


# Açıklama:
# Bir Witcher'ın 10 avdan k tanesini öldürme olasılığını Binom formülüyle hesaplayın.
# Input: k=7, n=10, p=0.6
# Output: 0.215 (örnek)
def probability_k_monsters_killed(k: int, n: int, p: float) -> float:
     return float(binom.pmf(k, n, p))
     pass


# Açıklama:
# Bir Ghoul’un k defa saldırma ihtimali lmbda ortalamasıyla nedir?
# Poisson olasılığı hesaplanmalı.
# Input: k=3, lmbda=2.5
# Output: 0.213 (örnek)
def poisson_probability(k: int, lmbda: float) -> float:
     return float(poisson.pmf(k, lmbda))
     pass


# Açıklama:
# Witcher’ın 1000 denemede ortalama öldürme oranını simüle et.
# Input: trials=1000, p=0.5
# Output: 0.501 (örnek)
def average_kill_rate(trials: int, p: float) -> float:
    basarili = 0
    for _ in range(trials):
        if random.random() < p:
            basarili += 1
    return basarili / trials
    pass


# Açıklama:
# İki Witcher’ın canavar öldürme olasılıkları farklıysa, 1000 denemede kim daha başarılı?
# Input: p1=0.6, p2=0.7, trials=1000
# Output: 'Witcher 2'
def compare_two_witchers(p1: float, p2: float, trials: int) -> str:
    basari1 = sum(1 for _ in range(trials) if random.random() < p1)
    basari2 = sum(1 for _ in range(trials) if random.random() < p2)
    if basari1 > basari2:
        return "Witcher 1"
    elif basari2 > basari1:
        return "Witcher 2"
    else:
        return "Tie"
    pass


# Açıklama:
# Ghoul’lar gün boyu saldırıyor. Her saat için saldırı sayısını liste olarak döndürün.
# Input: hours=24, lmbda=3.0
# Output: [2, 3, 1, 5, ...]
def simulate_poison_attacks_day(hours: int, lmbda: float) -> List[int]:
    return [int(poisson.rvs(lmbda)) for _ in range(hours)]
    pass