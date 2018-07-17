import itertools


def f_buy(df):
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


def f_sell(df, v, diff):
    for i in range(len(df.index)):
        value = df.iloc[i]['high']
        if value - v >= diff:
            return value
    return value


def calculate_safe_case(df):
    total_profit = 0
    success_cycles = 0
    do_nothing_cycles = 0
    bad_cycles = 0  # we we do not buy anything
    T = 7
    diff = 200  # we want at least gain 200$ for each cycle

    for w in itertools.count():
        if T*(w+2) > len(df.index):
            break
        week_t0 = df[T*w:T*(w+1)]
        week_t1 = df[T*(w+1):T*(w+2)]
        v_t0 = f_buy(week_t0)
        if v_t0 is None:
            do_nothing_cycles += 1
            continue

        v_t1 = f_sell(week_t1, v_t0, diff)
        profit = v_t1 - v_t0
        if profit > 0:
            success_cycles += 1
        else:
            print('We lost {}$'.format(profit))
            bad_cycles += 1
        total_profit += profit

    total_cycles = success_cycles + bad_cycles + do_nothing_cycles
    print(
        'Profit: {profit}. Good cycles: {good_cycles}/{total_cycles}. '
        'Bad cycles: {bad_cycles}/{total_cycles}. Do nothing: {do_nothing}/{total_cycles}'.format(
            profit=total_profit,
            good_cycles=success_cycles,
            do_nothing=do_nothing_cycles,
            bad_cycles=bad_cycles,
            total_cycles=total_cycles,
    ))


def calculate_worst_case(df):
    total_profit = 0
    success_cycles = 0
    bad_cycles = 0
    T = 7
    for w in itertools.count():
        if T*(w+2) > len(df.index):
            break
        week_t0 = df[T*w:T*(w+1)]
        week_t1 = df[T*(w+1):T*(w+2)]
        v_t1_min = week_t1['low'].min()
        v_t0_max = week_t0['high'].max()
        profit = v_t1_min - v_t0_max
        if profit > 0:
            success_cycles += 1
            print('Wow! We found success week v_min(t1)={} > v_max(t0)={}'.format(v_t1_min, v_t0_max))
        else:
            # print('Bad week: v_min(t1)={} < v_max(t0)={}'.format(v_t1_min, v_t0_max))
            bad_cycles += 1
        total_profit += profit

    total_cycles = success_cycles + bad_cycles
    print(
        'Profit: {profit}. Good cycles: {good_cycles}/{total_cycles}. '
        'Bad cycles: {bad_cycles}/{total_cycles}'.format(
            profit=total_profit,
            good_cycles=success_cycles,
            bad_cycles=bad_cycles,
            total_cycles=total_cycles,
    ))


def calculate_best_case(df):
    total_profit = 0
    success_cycles = 0
    bad_cycles = 0
    for w in itertools.count():
        if 7*(w+2) > len(df.index):
            break
        week_t0 = df[7*w:7*(w+1)]
        week_t1 = df[7*(w+1):7*(w+2)]
        v_t0_min = week_t0['low'].min()
        v_t1_max = week_t1['high'].max()
        profit = v_t1_max - v_t0_min
        if profit > 0:
            success_cycles += 1
        else:
            print('Bad week: v_max(t1)={} < v_min(t0)={}'.format(v_t1_max, v_t0_min))
            bad_cycles += 1
        total_profit += profit

    total_cycles = success_cycles + bad_cycles
    print(
        'Profit: {profit}. Good cycles: {good_cycles}/{total_cycles}. '
        'Bad cycles: {bad_cycles}/{total_cycles}'.format(
            profit=total_profit,
            good_cycles=success_cycles,
            bad_cycles=bad_cycles,
            total_cycles=total_cycles,
    ))
