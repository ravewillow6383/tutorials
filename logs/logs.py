def reorder_logs(logs):
    digs = []
    alpha = []
    for item in logs:
        lst = [char for char in item]
        if lst[-1].isdigit():
            digs.append(item)
        else:
            alpha.append(item[1:])
    

            
            print(lst)


    logs.clear()
    logs = alpha + digs

    return logs

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
reorder_logs(logs)