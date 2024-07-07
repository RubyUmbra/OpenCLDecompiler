__constant int int_arr[] = {1, 2, 3, 4, 5, 6, 7};

__kernel __attribute__((reqd_work_group_size(8, 8, 1)))
void float_test(__global float* out, int i) {
	uint id = get_global_id(0);
	out[id] = int_arr[id];
}
