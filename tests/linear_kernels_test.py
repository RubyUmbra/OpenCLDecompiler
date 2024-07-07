import pytest

from .conftest import template


class TestLinearKernels:
    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_addition(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels",
            dir_name="addition",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_subtraction(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels",
            dir_name="subtraction",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_multiplication(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels",
            dir_name="multiplication",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_many_linears(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels",
            dir_name="many_linears",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_x(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_x",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_get_global_offset(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_get_global_offset",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_get_local_id(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_get_local_id",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_get_group_id(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_get_group_id",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_get_local_size(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_get_local_size",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_get_global_id(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_get_global_id",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_get_global_size(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_get_global_size",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_get_num_groups(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_get_num_groups",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )

    @pytest.mark.parametrize(
        ["mcpu", "disasm", "is_new_parser"],
        [
            ("", "clrxdisasm", False),
            ("gfx1010", "clrxdisasm", False),
            ("gfx1030", "clrxdisasm", False),
            ("gfx1103", "amdgpu-dis", True),
        ],
    )
    def test_copy_get_work_dim(self, mcpu, disasm, is_new_parser):
        template(
            path_to_dir="linear_kernels/work_item_built_in_functions",
            dir_name="copy_get_work_dim",
            mcpu=mcpu,
            disasm=disasm,
            is_new_parser=is_new_parser,
        )
