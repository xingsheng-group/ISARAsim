from math import log2


class in_layer:
    def __init__(self):
        self.cycles = 0
        self.buffer_reg = 0
        self.pe_num = 0
        self.pe_row_num = 0
        self.pe_col_num = 0

        self.weight_num = 0
        self.weight_row_num = 0
        self.weight_col_num = 0
        self.weight_op = 0

        self.energy_mac = 0
        self.energy_add = 0
        self.energy_reg = 0
        self.energy_sfu = 0

        # topo
        self.layer_name = ''
        self.layer_num = 0

        self.IFMAP_height = 0
        self.IFMAP_width = 0
        self.OFMAP_height = 0
        self.OFMAP_width = 0
        self.filter_height = 0
        self.filter_width = 0
        self.channels = 0
        self.num_filter = 0
        self.strides = 0

        self.flatten = False

        self.is_last_layer = False

        self.input_bit_width = 4
        self.weight_bit_width = 4
        self.output_bit_width = 4

        # conf
        self.mac_size = 64
        self.systolic_cycle = 1  # 脉动周期
        self.mac_cycle = 64  # MAC计算周期数
        self.mac_delay = 16  # MAC计算输出延迟周期

        self.mac_energy = 0       # 单次MAC计算能耗 pJ
        self.mac_energy11 = 317   # 单次MAC计算能耗 pJ
        self.mac_energy22 = 634   # 单次MAC计算能耗 pJ
        self.mac_energy44 = 2000  # 单次MAC计算能耗 pJ
        self.mac_energy48 = 2500  # 单次MAC计算能耗 pJ
        self.mac_energy84 = 2100  # 单次MAC计算能耗 pJ
        self.mac_energy88 = 2536  # 单次MAC计算能耗 pJ

        self.reg_energy = 0.075  # reg能耗 pJ
        self.add_energy = 1.353625  # adder能耗 pJ
        self.sfu_energy = 46.25  # sfu能耗

    def set_params(self, topo: list, conf=None) -> None:
        if conf is not None:
            self.mac_size, \
                self.systolic_cycle, \
                self.mac_cycle, \
                self.mac_delay, \
                self.mac_energy, \
                = conf
        if topo is not None:
            self.layer_name, \
                self.layer_num, \
                self.IFMAP_height, \
                self.IFMAP_width, \
                self.OFMAP_height, \
                self.OFMAP_width, \
                self.filter_height, \
                self.filter_width, \
                self.channels, \
                self.num_filter, \
                self.strides, \
                self.flatten, \
                self.is_last_layer, \
                self.input_bit_width, \
                self.weight_bit_width, \
                self.output_bit_width, \
                = topo

    def run(self) -> None:
        # 计算权重矩阵规模
        if self.flatten:
            self.weight_row_num = self.IFMAP_height * self.IFMAP_width * self.channels
        else:
            self.weight_row_num = self.filter_height * self.filter_width * self.channels

        self.weight_col_num = self.num_filter

        # 计算所用MAC阵列规模
        self.pe_row_num = self.weight_row_num // self.mac_size + (self.weight_row_num % self.mac_size > 0)
        self.pe_col_num = self.weight_col_num // self.mac_size + (self.weight_col_num % self.mac_size > 0)

        if self.output_bit_width == 8:
            self.pe_col_num *= 2
            self.weight_col_num *= 2

        self.weight_num = self.weight_row_num * self.weight_col_num
        self.weight_op = self.weight_num * self.OFMAP_width * self.OFMAP_height

        self.pe_num = self.pe_row_num * self.pe_col_num

        # 计算阵列内部延时
        self.cycles = self.systolic_cycle * self.pe_row_num + self.mac_cycle + self.mac_delay
        # 激活演延时
        self.cycles += 1

        if self.is_last_layer:
            self.cycles += self.systolic_cycle * self.pe_col_num

        # 计算缓存消耗
        self.buffer_reg = self.pe_num * 80

        # 计算能量消耗
        if self.input_bit_width == 1 and self.output_bit_width == 1:
            self.mac_energy = self.mac_energy11
        elif self.input_bit_width == 2 and self.output_bit_width == 2:
            self.mac_energy = self.mac_energy22
        elif self.input_bit_width == 4 and self.output_bit_width == 4:
            self.mac_energy = self.mac_energy44
        elif self.input_bit_width == 4 and self.output_bit_width == 8:
            self.mac_energy = self.mac_energy48
        elif self.input_bit_width == 8 and self.output_bit_width == 4:
            self.mac_energy = self.mac_energy84
        elif self.input_bit_width == 8 and self.output_bit_width == 8:
            self.mac_energy = self.mac_energy88

        self.energy_mac += self.OFMAP_width * self.OFMAP_height * self.mac_energy \
                           * self.pe_num
        self.energy_add += self.OFMAP_width * self.OFMAP_height * self.add_energy \
                           * (self.pe_row_num - 1) * self.pe_col_num
        self.energy_reg += self.OFMAP_width * self.OFMAP_height * self.reg_energy \
                           * (self.weight_row_num * self.pe_col_num * self.output_bit_width
                              + self.weight_col_num * self.pe_row_num * (self.output_bit_width + log2(self.pe_row_num)))
        self.energy_sfu += self.OFMAP_width * self.OFMAP_height * self.sfu_energy \
                           * self.weight_col_num

    def show(self):
        print('Layer', self.layer_num, ':', self.layer_name)
        print('--- Cycles     :', self.cycles)
        print('--- Latency    :', self.cycles * 1.25 / 1000, 'us')
        print('--- PE num     :', self.pe_num)
        print('--- Weight num :', self.weight_num)
        print('--- Buffer reg :', self.buffer_reg)
