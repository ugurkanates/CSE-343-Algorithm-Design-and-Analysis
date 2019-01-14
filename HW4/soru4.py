
kisi = ['alice', 'recep', 'john', 'cassie', 'baraka', 'kemal', 'raiden', 'rept', 'coco', 'ucan', 'adam','list']
pair_list = ['alice-recep', 'john-cassie', 'baraka-raiden','coco-ucan','adam-list','recep-rept']

def recursive_activity_selector(s, f, k, n):

    m = k + 1
    while m < n and s[m] < f[k]:  # find an activity starting after our last
                                   # finish
        m = m + 1
    if m < n:
        print("best choice pairs " + str(m) + " that unions at "
              + str(f[m]))
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []

recursive_activity_selector(kisi,pair_list,0,5)