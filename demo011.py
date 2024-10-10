import random

def execute_simulation():
    people = list(range(1, 601))  # 600个人，位置从1到600
    while len(people) > 1:
        # 随机选择一个奇数位置的人
        # 由于列表中奇数位置和偶数位置是交错的，我们随机选择一个奇数索引
        index_to_shoot = random.choice([*range(0, len(people), 2)])
        # 移除被枪毙的人
        people.pop(index_to_shoot)
    # 返回最后一个存活的人的位置
    return people[0]

# 进行模拟，次数可以根据需要调整，这里使用10000次作为例子
simulations = 1000
position_survival_count = [0] * 600

for _ in range(simulations):
    survivor_position = execute_simulation()
    position_survival_count[survivor_position - 1] += 1  # 由于列表索引从0开始，所以减1

# 计算每个位置的存活概率，并跳过最初的0位置
survival_probabilities = [count / simulations for count in position_survival_count]

# 找到存活概率最大的位置（从1开始计数）
max_prob_index = max(range(1, 601), key=lambda x: survival_probabilities[x-1])
print(f"一开始位于位置 {max_prob_index} 的人存活概率最大，概率为 {survival_probabilities[max_prob_index-1]:.4f}")