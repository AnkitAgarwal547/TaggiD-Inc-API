#the below function can be used for the  human readable fromater


def human_format(num:float, force=None, ndigits=2):
    perfixes = ('p', 'n', 'u', 'm', '', 'K', 'M', 'G', 'T')
    one_index = perfixes.index('')
    if num >= 10000:
        if force:
            if force in perfixes:
                index = perfixes.index(force)
                magnitude = 3*(index - one_index)
                num = num/(10**magnitude)
            else:
                raise ValueError('force value not supported.')
        else:
            div_sum = 0
            if(abs(num) >= 1000):
                while abs(num) >= 1000:
                    div_sum += 1
                    num /= 1000
            else:
                while abs(num) <= 1:
                    div_sum -= 1
                    num *= 1000
            temp = round(num, ndigits) if ndigits else num
            if temp < 1000:
                num = temp 
            else:
                num = 1
                div_sum += 1
            index = one_index + div_sum
        return str(num).rstrip('0').rstrip('.') + perfixes[index]
    else:
        return str(num)
