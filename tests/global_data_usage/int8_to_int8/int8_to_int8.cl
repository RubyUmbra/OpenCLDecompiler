__constant int8 gdata0[] = {(int8)(1, 2, 3, 4, 5, 6, 7, 8), (int8)(9, 10, 11, 12, 13, 14, 15, 16), (int8)(17, 18, 19, 20, 21, 22, 23, 24)};

__kernel __attribute__((reqd_work_group_size(64, 1, 1)))
void int_test(__global int8* out, int i) {
	uint id0 = get_global_id(0);
	out[id0] = gdata0[id0];
}
