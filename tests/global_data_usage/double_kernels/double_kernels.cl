__constant double double_arr[] = {-1.0, 1.0, -2.2, 3.9, -4.20, 5.12345};

__kernel __attribute__((reqd_work_group_size(8, 8, 1)))
void float_test(__global double* out, int i) {
	uint id = get_global_id(0);
	out[id] = double_arr[id];
}
