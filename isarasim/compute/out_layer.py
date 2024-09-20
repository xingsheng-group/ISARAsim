from isarasim.compute.in_layer import in_layer


class out_layer:
    def __init__(self):
        self.next_layer = None
        self.last_layer = None
        self.bit_width = 4

        self.cycles = 0
        self.cycles_per_cal = 0
        self.buffer_reg = 0
        self.buffer_sram = 0

        self.energy_reg = 0
        self.energy_sram = 0
        self.energy_wire = 0

        # conf
        self.mac_size = 64
        self.systolic_cycle = 1  # 脉动周期
        self.mac_cycle = 64  # MAC计算周期数
        self.mac_delay = 16  # MAC计算输出延迟周期

        self.reg_energy = 0.0075  # reg能耗 pJ
        self.add_energy = 1.353625  # adder能耗 pJ
        self.sram_energy = 0.0042691345  # sram能耗 nJ
        self.wire_energy = 0.06  # 总线能耗 8bit

    def set_params(self, next_layer, last_layer=None) -> None:
        self.next_layer = next_layer
        self.last_layer = last_layer

        self.bit_width = next_layer.input_bit_width

    def run(self) -> None:
        # 层间消耗
        if self.last_layer is not None:
            # long wire 传输消耗
            self.cycles += self.last_layer.pe_col_num
            self.buffer_reg += self.last_layer.pe_col_num ** 2 * self.bit_width

            self.energy_reg += self.last_layer.pe_col_num * self.last_layer.weight_col_num * self.bit_width \
                               * self.last_layer.OFMAP_height * self.last_layer.OFMAP_width * self.reg_energy

            self.energy_wire += self.last_layer.pe_col_num * self.last_layer.weight_col_num \
                                * self.last_layer.OFMAP_height * self.last_layer.OFMAP_width * self.wire_energy

        # 输入层消耗
        else:
            # 卷积耗时
            self.cycles += (self.next_layer.OFMAP_height * self.next_layer.OFMAP_width - 1) * self.mac_cycle
            self.cycles_per_cal = self.next_layer.OFMAP_height * self.next_layer.OFMAP_width * self.mac_cycle

            # long wire 传输消耗
            self.buffer_reg += self.next_layer.pe_row_num * (self.next_layer.pe_row_num - 1) // 2 * self.bit_width

            self.energy_reg += self.next_layer.pe_row_num * self.next_layer.channels * self.bit_width \
                               * self.next_layer.IFMAP_height * self.next_layer.IFMAP_width * self.reg_energy / 2  # ..

            self.energy_wire += self.next_layer.pe_row_num * self.next_layer.channels \
                                * self.next_layer.IFMAP_height * self.next_layer.IFMAP_width * self.wire_energy / 2  # ..

        # 卷积缓存
        self.buffer_sram += (self.next_layer.filter_height - 1) * self.next_layer.IFMAP_width \
                            * self.bit_width * self.next_layer.channels

        self.energy_sram += (self.next_layer.filter_height - 1) * self.next_layer.IFMAP_width \
                            * self.bit_width * self.next_layer.channels \
                            * self.next_layer.IFMAP_width * self.next_layer.IFMAP_height * self.sram_energy

        # 池化
        if self.last_layer is not None:
            pool_height = self.last_layer.OFMAP_height // self.next_layer.IFMAP_height
            pool_width = self.last_layer.OFMAP_width // self.next_layer.IFMAP_width

            self.buffer_reg += (pool_width - 1) * pool_height * self.bit_width * self.next_layer.channels
            self.buffer_sram += (self.last_layer.OFMAP_width - pool_width + 1) * (pool_height - 1) \
                                * self.bit_width * self.next_layer.channels

            self.cycles += 1

            self.energy_reg += (pool_width - 1) * pool_height * self.bit_width * self.next_layer.channels \
                               * self.last_layer.OFMAP_width * self.last_layer.OFMAP_height * self.reg_energy
            self.energy_sram += (self.last_layer.OFMAP_width - pool_width + 1) * (pool_height - 1) \
                                * self.bit_width * self.next_layer.channels \
                                * self.last_layer.OFMAP_width * self.last_layer.OFMAP_height * self.sram_energy

        # 展开
        if self.next_layer.flatten:
            self.buffer_reg += (self.last_layer.OFMAP_height * self.last_layer.OFMAP_width - 1) \
                               * self.bit_width * self.next_layer.channels

            self.energy_reg += (self.last_layer.OFMAP_height * self.last_layer.OFMAP_width - 1) \
                               * self.bit_width * self.next_layer.channels * self.reg_energy

    def show(self):
        if self.last_layer is None:
            print('Input -', self.next_layer.layer_num, ':', self.next_layer.layer_name)
        else:
            print(self.last_layer.layer_num, ':', self.last_layer.layer_name, '-', self.next_layer.layer_num, ':',
                  self.next_layer.layer_name)
        print('--- Cycles     :', self.cycles)
        print('--- Latency    :', self.cycles * 1.25 / 1000, 'us')
        print('--- Buffer reg :', self.buffer_reg)
        print('--- Buffer SRAM:', self.buffer_sram)
