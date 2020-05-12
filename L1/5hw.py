revenue = int(input('Введите выручку вашей компании: '))
costs = int(input('Введите издержки вашей компании: '))
if revenue > costs:
    fin_results = revenue-costs
    rent = fin_results/revenue
    print('Ваша прибыль составляет: ', fin_results)
    workers = int(input('Сколько челове работает у вас на фирме: '))
    wokers_money = fin_results/workers
    print(wokers_money, 'прибыль на одного сотрудика')
elif revenue == costs:
    print('Ваши сотрудники не получают денег!')
else:
    print ('Вы в минусе! Плохо! Чем вы платите заработанную плату? Улучшайте показатели!')