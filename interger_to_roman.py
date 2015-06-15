import sys

class Solution:
    # @param {integer} num
    # @return {string}
    def get_rom(self, num, high, med, low):
        if num == 0:
            return ''
        elif num <= 3:
            return num * low
        elif num == 4:
            return low + med
        elif num <=8:
            return med + (num-5)*low
        else:
            return low + high

    def intToRoman(self, num):
        ret = ''
        ret += num/1000 * 'M'
        h = (num%1000)/100
        ret += self.get_rom(h, 'M', 'D', 'C')
        t = (num%100)/10
        ret += self.get_rom(t, 'C', 'L', 'X')
        d = num%10
        ret += self.get_rom(d, 'X', 'V', 'I')
        return ret

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "input digital number to convert (1-3999)"
    print Solution().intToRoman(int(sys.argv[1]))