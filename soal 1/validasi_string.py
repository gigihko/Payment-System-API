def validasi_string(input_str):
    # Cek panjang string
    if len(input_str) < 1 or len(input_str) > 4096:
        return False

    # Stack untuk menyimpan karakter pembuka
    stack = []
    
    # Mapping pasangan pembuka-penutup yang valid
    pasangan = {'<': '>', '{': '}', '[': ']'}

    for char in input_str:
        # Jika karakter adalah pembuka, tambahkan ke stack
        if char in pasangan.keys():
            stack.append(char)
        # Jika karakter adalah penutup, cek apakah cocok dengan pembuka terakhir di stack
        elif char in pasangan.values():
            # Jika stack kosong atau pembuka terakhir tidak sesuai, return False
            if not stack or pasangan[stack.pop()] != char:
                return False
        else:
            # Jika karakter tidak valid (harus <>{}[]), return False
            return False

    # Jika stack tidak kosong, ada pembuka yang tidak ditutup
    if stack:
        return False

    return True

# Contoh pengujian
print(validasi_string('{{[<>[{{}}]]}}'))  # True
print(validasi_string('{<{[[{{[]<{{[{[]<>}]}}<>>}}]]}>}'))  # True
print(validasi_string('{{[{<[[{<{<<<[{{{[]{<{[<[[<{{[[[[[<{[{<[<<[[<<{[[{[<<<<<<<[{[{[{{<{[[<{<<<{<{[<>]}>}>>[]>}>]]}>}}]}]}]>>>>>>>]}]]}>>]]>>]>}]}>]]]]]}}>]]>]}>}}}}]>>>}>}]]>}]}}'))  # True
print(validasi_string('[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{[{{[{{{{[<<{{{<{[{[[[{<<<[{[<{<<<>>>}>]}]>>>}]]]}]}>}}}>>]}}}}]}}]}>]>}>}>}}>>]}}>]>]]]>>>]}}>]]]>]>]}}>]>]]]}]}>}>]'))  # True
print(validasi_string('[[{[[<{{{{[[[<[{[[<{{{{[{[{[[[<<{<{[{<<<[[<[{[<{{[{[<[[<<[{<<[[[{<[{[[{{<<>[<<{{<<{[[[<{}{[{{{[[{{[[<[{}]>]]}}]]}}}]}>]]]}>>}}>>]>}}]]}]>}]]]>>}]>>]]>]}]}}>]}]>]]>>>}]}>}>>]]]}]}]}}}}>]]}]>]]]}}}}>]]}]]'))  # True
print(validasi_string('[{}<>]'))  # True



print(validasi_string(']'))
print(validasi_string(']['))
print(validasi_string('[>]'))
print(validasi_string('[>'))
print(validasi_string('{{[<>[{{}}]]}}'))
print(validasi_string('{<{[[{{[]<{[{[]<>}]}}<>>}}]]}>}'))
print(validasi_string('{{[{<[[{<{<<<[{{{[]{<{[<[[<{{[[[[<{[{<[<<[[<<{[[{[<<<<<<<[{[{[{{<{[[<{<<<{<{[<>]}>}>>[]>}>]]}'))
print(validasi_string('>}}]}]}]>>>>>>]}]]}>>]]>>]>}]}>]]]]]}}>]]>]}>}}}}]>>>}>}]]>}]}}'))
print(validasi_string('[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{[{{[{{{{[<<{{{<{[{[[[{<<<[{[<{<<>>[]}]>>>}]]]}]}>}}}>>]}}}}]}}]}>]>}>}>}}>>]}}>]>]]]>>>]}}>]]]>]>]}}>]>]]]}]}>}>]'))
print(validasi_string('[{}<[>]'))