#include<iostream>

struct backpack_item {
	int weight;
	int value;
	float value_per_weight = 0;
}

int solve_knapsack(std::vector<backpack_item> INSTANCE, int BACKPACK_CAPACITY);

int main(){

	std::vector<backpack_item> instance = {
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
	}
		
	int backpack_capacity = 4;

	int result = solve_knapsack(instance, backpack_capacity);

	std::cout << "Vlera më e lartë për instancën e përdorur është " << result << "!\n";

	return 0;
}

int solve_knapsack(std::vector<backpack_item> INSTACE, int BACKPACK_CAPACITY){

	// llogarite koeficientin val per wt
	// sorto sipas qatij koeficienti
	// edhe nisja, while theres capacity... += value; -= weight

	return total
}
