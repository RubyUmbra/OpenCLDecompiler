from src.base_instruction import BaseInstruction
from src.decompiler_data import make_op, set_reg_value
from src.register import is_reg
from src.register_type import RegisterType


class VOr(BaseInstruction):
    def __init__(self, node, suffix):
        super().__init__(node, suffix)
        self.vdst, self.src0, self.src1 = self.instruction[1:4]
        size_of_work_groups = self.decompiler_data.config_data.size_of_work_groups
        self._instruction_special_cases = frozenset({
            *(frozenset({
                size_of_work_groups[i],
                RegisterType[f"WORK_ITEM_ID_{dim}"],
            }) for i, dim in enumerate("XYZ") if i < len(size_of_work_groups)),
            *(frozenset({
                RegisterType[f"WORK_GROUP_ID_{dim}_LOCAL_SIZE"],
                RegisterType[f"WORK_ITEM_ID_{dim}"],
            }) for i, dim in enumerate("XYZ") if i < len(size_of_work_groups)),
        })

    def to_print_unresolved(self):
        if self.suffix == "b32":
            self.decompiler_data.write(f"{self.vdst} = {self.src0} | {self.src1} // {self.instruction[0]}\n")
            return self.node
        return super().to_print_unresolved()

    def to_fill_node(self):
        if self.suffix == "b32":
            new_value = None
            if is_reg(self.src1) and self.node.state.registers[self.src1].type in \
                    [RegisterType[f"WORK_ITEM_ID_{dim}"] for dim in "XYZ"]:
                new_value = make_op(self.node, self.src0, self.src1, "+", "(ulong)", "(ulong)", suffix=self.suffix)
            if self.src0.isdigit() and is_reg(self.src1):
                src_types = frozenset({
                    int(self.src0),
                    self.node.state.registers[self.src1].type,
                })
                if src_types in self._instruction_special_cases:
                    new_value = make_op(self.node, self.src0, self.src1, "+", "(ulong)", "(ulong)", suffix=self.suffix)
            if is_reg(self.src0) and is_reg(self.src1):
                src_types = frozenset({
                    self.node.state.registers[self.src0].type,
                    self.node.state.registers[self.src1].type,
                })
                if src_types in self._instruction_special_cases:
                    new_value = make_op(self.node, self.src0, self.src1, "+", "(ulong)", "(ulong)", suffix=self.suffix)
            if new_value is not None:
                return set_reg_value(
                    node=self.node,
                    new_value=new_value,
                    to_reg=self.vdst,
                    from_regs=[self.src0, self.src1],
                    data_type=self.suffix,
                    integrity=self.node.state.registers[self.src1].integrity,
                )
        return super().to_fill_node()
