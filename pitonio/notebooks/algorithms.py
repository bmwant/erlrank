import itertools
from functools import partial


def f_buy_safe_case(df):
    price_drops = 0
    desired_drops = 2
    min_value = df.iloc[0]['low']
    for i in range(len(df.index)):
        low_value = df.iloc[i]['low']
        if low_value < min_value:
            min_value = low_value
            price_drops += 1
        if price_drops == desired_drops:
            return low_value


def f_sell_on_threshold(df, v, *, diff):
    # import pdb; pdb.set_trace()
    for i in range(len(df.index)):
        value = df.iloc[i]['high']
        if value - v >= diff:
            return value
    return value


def calculate_(df, period, f_buy, f_sell):
    total_profit = 0
    success_cycles = 0
    standby_cycles = 0
    bad_cycles = 0

    for i in itertools.count():
        if period*(i+2) > len(df.index):
            break

        period_t0 = df[period*i:period*(i+1)]
        period_t1 = df[period*(i+1):period*(i+2)]
        v_t0 = f_buy(period_t0)
        if v_t0 is None:
            standby_cycles += 1
            continue

        v_t1 = f_sell(period_t1, v_t0)

        profit = v_t1 - v_t0
        if profit > 0:
            success_cycles += 1
        else:
            bad_cycles += 1
        total_profit += profit

    total_cycles = success_cycles + bad_cycles + standby_cycles
    print(
        'Profit: {total_profit}. '
        'Success cycles: {success_cycles}/{total_cycles}. '
        'Bad cycles: {bad_cycles}/{total_cycles}. '
        'Standby cycles: {standby_cycles}/{total_cycles}'.format(
            total_profit=total_profit,
            success_cycles=success_cycles,
            bad_cycles=bad_cycles,
            standby_cycles=standby_cycles,
            total_cycles=total_cycles,
        ))


f_buy_best_case = lambda df, *args: df['low'].min()
f_sell_best_case = lambda df, *args: df['high'].max()
calculate_best_case = partial(calculate_, f_buy=f_buy_best_case, f_sell=f_sell_best_case)


f_buy_worst_case = lambda df, *args: df['high'].max()
f_sell_worst_case = lambda df, *args: df['low'].min()
calculate_worst_case = partial(calculate_, f_buy=f_buy_worst_case, f_sell=f_sell_worst_case)


f_sell_safe_case = partial(f_sell_on_threshold, diff=200)
calculate_safe_case = partial(calculate_, f_buy=f_buy_safe_case, f_sell=f_sell_safe_case)
