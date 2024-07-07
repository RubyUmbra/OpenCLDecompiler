from src.base_instruction import BaseInstruction
from src.decompiler_data import set_reg_value
from src.register_type import RegisterType
from src.register import is_vector_type


class VPerm(BaseInstruction):
    def __init__(self, node, suffix):
        super().__init__(node, suffix)
        self.vdst = self.instruction[1]
        self.src0 = self.instruction[2]
        self.src1 = self.instruction[3]
        self.src2 = self.instruction[4]

    def to_print_unresolved(self):
        if self.suffix == "b32":
            tab = "    "
            qword = "qword" + str(self.decompiler_data.number_of_qword)
            choice = "choice" + str(self.decompiler_data.number_of_choice)
            result = "result" + str(self.decompiler_data.number_of_result)
            self.decompiler_data.write(f"{self.vdst} = 0 // v_perm_b32\n")
            self.decompiler_data.write(f"ulong {qword} = (((ulong){self.src0})<<32) | {self.src1}\n")
            self.decompiler_data.write("for (int i = 0; i < 4; i++)\n")
            self.decompiler_data.write("{\n")
            self.decompiler_data.write(tab + f"byte {choice} = ({self.src2} >> (8*i)) & 0xff\n")
            self.decompiler_data.write(tab + f"byte {result}\n")
            self.decompiler_data.write(tab + f"if ({choice} >= 13)\n")
            self.decompiler_data.write(tab + tab + f"{result} = 0xff\n")
            self.decompiler_data.write(tab + f"else if ({choice} == 12)\n")
            self.decompiler_data.write(tab + tab + f"{result} = 0\n")
            self.decompiler_data.write(tab + f"else if ({choice} >= 8)\n")
            self.decompiler_data.write(tab + tab + f"{result} = 0xff * {qword}>>(({choice}-8)*16 + 15)\n")
            self.decompiler_data.write(tab + "else\n")
            self.decompiler_data.write(tab + tab + f"{result} = ({qword}>>({choice}*8)) & 0xff\n")
            self.decompiler_data.write(tab + f"{self.vdst} |= ({result} << (i * 8))\n")
            self.decompiler_data.write("}\n")
            self.decompiler_data.number_of_qword += 1
            self.decompiler_data.number_of_choice += 1
            self.decompiler_data.number_of_result += 1
            return self.node
        return super().to_print_unresolved()

    def to_fill_node(self):
        if self.suffix == "b32":
            if self.node.state.registers[self.src2].val == "0x2010004":
                new_value = self.node.state.registers[self.src0].val + ", " + self.node.state.registers[self.src1].val
                reg_type = RegisterType.KERNEL_ARGUMENT_VALUE
                if is_vector_type(self.node.state.registers[self.src0].data_type):
                    src0_data_type_name = self.node.state.registers[self.src0].data_type[:1]
                    src0_data_type_size = self.node.state.registers[self.src0].data_type[-1:]
                else:
                    src0_data_type_name = self.node.state.registers[self.src0].data_type
                    src0_data_type_size = 1

                if is_vector_type(self.node.state.registers[self.src1].data_type):
                    src1_data_type_name = self.node.state.registers[self.src1].data_type[:1]
                    src1_data_type_size = int(self.node.state.registers[self.src1].data_type[-1:])
                else:
                    src1_data_type_name = self.node.state.registers[self.src1].data_type
                    src1_data_type_size = 1

                if src1_data_type_name == src0_data_type_name:
                    data_type = src1_data_type_name + str(src1_data_type_size + src0_data_type_size)
                else:
                    data_type = self.node.state.registers[self.src1].data_type
                set_reg_value(self.node, new_value, self.vdst, [], data_type, reg_type=reg_type)
            return self.node
        return super().to_fill_node()
