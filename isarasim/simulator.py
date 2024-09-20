from compute.in_layer import in_layer
from compute.out_layer import out_layer


class simulator():
    def __init__(self):
        self.cycles = 0
        self.cycles_per_cal = 0
        self.buffer_reg = 0
        self.buffer_sram = 0
        self.pe_num = 0
        self.weight_num = 0
        self.weight_op = 0.

        self.energy_mac = 0
        self.energy_add = 0
        self.energy_reg = 0
        self.energy_sfu = 0
        self.energy_sram = 0
        self.energy_wire = 0

        # conf
        self.mac_size = 64
        self.systolic_cycle = 1  # 脉动周期
        self.mac_cycle = 64  # MAC计算周期数
        self.mac_delay = 16  # MAC计算输出延迟周期
        self.mac_energy = 0.1  # 单次MAC计算能耗 nJ

        self.topo = None
        self.conf = None

        self.in_layer_simulator = []
        self.out_layer_simulator = []

    def set_params(self, topo: list, conf=None) -> None:
        self.topo = topo
        self.conf = conf

        last_layer = None
        for layer_topo in self.topo:
            print(layer_topo)

            in_layer_sim = in_layer()
            in_layer_sim.set_params(layer_topo)
            out_layer_sim = out_layer()
            out_layer_sim.set_params(in_layer_sim, last_layer)
            last_layer = in_layer_sim

            self.in_layer_simulator.append(in_layer_sim)
            self.out_layer_simulator.append(out_layer_sim)

    def run(self):
        print('Simnulator start')

        for in_layer_sim in self.in_layer_simulator:
            in_layer_sim.run()
            self.cycles += in_layer_sim.cycles
            self.buffer_reg += in_layer_sim.buffer_reg
            self.pe_num += in_layer_sim.pe_num
            self.weight_num += in_layer_sim.weight_num
            self.weight_op += in_layer_sim.weight_op

            out_layer_sim = self.out_layer_simulator[in_layer_sim.layer_num]
            out_layer_sim.run()
            self.cycles += out_layer_sim.cycles
            self.cycles_per_cal += out_layer_sim.cycles_per_cal
            self.buffer_reg += out_layer_sim.buffer_reg
            self.buffer_sram += out_layer_sim.buffer_sram

            out_layer_sim.show()

            in_layer_sim.show()

            self.energy_mac += in_layer_sim.energy_mac
            self.energy_add += in_layer_sim.energy_add
            self.energy_reg += in_layer_sim.energy_reg
            self.energy_sfu += in_layer_sim.energy_sfu

            self.energy_reg += out_layer_sim.energy_reg
            self.energy_sram += out_layer_sim.energy_sram
            self.energy_wire += out_layer_sim.energy_wire

        # for out_layer_sim in self.out_layer_simulator:
        #     out_layer_sim.run()
        #     self.cycles += out_layer_sim.cycles
        #     self.buffer_reg += out_layer_sim.buffer_reg
        #     self.buffer_sram += out_layer_sim.buffer_sram
        #
        #     out_layer_sim.show()

    def show(self):
        print('Cycles      :', self.cycles)
        print('Latency     :', self.cycles * 1.25 / 1000, 'us')
        print('PE num      :', self.pe_num)
        print('Weight num  :', self.weight_num)
        print('Buffer reg  :', self.buffer_reg)
        print('Buffer SRAM :', self.buffer_sram)
        print('Buffer reg  :', self.buffer_reg / 8 / 1024, 'kB')
        print('Buffer SRAM :', self.buffer_sram / 8 / 1024, 'kB')
        print('RRAM ur     :', self.weight_num / (self.pe_num * self.mac_size ** 2) * 100, '%')
        # print('RRAM ur     :', self.weight_num / (self.pe_num * 2048 * 256) * 100, '%')

        # nJ
        print('Energy mac  :', self.energy_mac / 1000)
        print('Energy add  :', self.energy_add / 1000)
        print('Energy reg  :', self.energy_reg / 1000)
        print('Energy sfu  :', self.energy_sfu / 1000)
        print('Energy SRAM :', self.energy_sram / 1000)
        print('Energy wire :', self.energy_wire / 1000)

        print('Energy all  :', (self.energy_mac + self.energy_add + self.energy_reg
                                + self.energy_sram + self.energy_wire + self.energy_sfu))

        print('Power mW    :', (self.energy_mac + self.energy_add + self.energy_reg
                                + self.energy_sram + self.energy_wire + self.energy_sfu) / 1000 \
              / (self.cycles_per_cal * 1.25 / 1000))

        print('Freq kHz    :', 1000000 / (self.cycles_per_cal * 1.25))

        print('op          :', self.weight_op * 2 / 2)
        print('TOPS        :', self.weight_op * 2 / 2 / (self.energy_mac + self.energy_add + self.energy_sfu
                                                     + self.energy_reg + self.energy_sram + self.energy_wire))

        print('')
