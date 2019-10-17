def reorder_logs(logs):
    digs = []
    alpha = []
    for item in logs:
        lst = [char for char in item]
        if lst[-1].isdigit():
            digs.append(item)
        else:
            alpha.append(item)
            j = len(alpha)
            alphaList = sorted(sorted(alpha), key=lambda n: n.split()[1:j])

    if len(logs):
        if len(alphaList) > 0 and len(digs) > 0:
            logs = alphaList + digs
        elif len(alphaList):
            logs = alphaList
        elif len(digs):
            logs = digs

    return logs