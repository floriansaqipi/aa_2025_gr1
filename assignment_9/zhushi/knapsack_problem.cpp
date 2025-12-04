#include<iostream>

struct backpack_item {
	int weight;
	int value;
	float value_per_weight = 0;
};

int solve_knapsack(std::vector<backpack_item> INSTANCE, int BACKPACK_CAPACITY);
void sort_by_coefficient(std::vector<backpack_item>& INSTANCE);

int main(){

	std::vector<backpack_item> instance = {
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
		backpack_item{1, 4},
	};
		
	int backpack_capacity = 4;

	unsigned int result = solve_knapsack(instance, backpack_capacity);

	std::cout << "Sipas algoritmit, vlera më e lartë për instancën e përdorur është " << result << "!\n";

	return 0;
}

int solve_knapsack(std::vector<backpack_item> INSTANCE, int BACKPACK_CAPACITY){

	// llogarite koeficientin val per wt
	// sorto sipas qatij koeficienti
	// edhe nisja, while theres capacity... += value; -= weight

	size_t n = INSTANCE.size();
	for (int i = 0; i < n; i++) {
		INSTANCE[i].value_per_weight = 1.0 * INSTANCE[i].value / INSTANCE[i].weight;
	}
	
	sort_by_coefficient(INSTANCE);

	int available_space = BACKPACK_CAPACITY;
	int total_value= 0;
	for (int i = 0; available_space > 0 && i < n; i++){
		total_value += INSTANCE[i].value;
		available_space -= INSTANCE[i].weight;
	}

	return total_value;
}

void sort_by_coefficient(std::vector<backpack_item>& INSTANCE){
	
	size_t n = INSTANCE.size();
	for (int i = 0; i < n-1; i++){
		for (int j = i; j < n; j++){
			if (INSTANCE[i].value_per_weight > INSTANCE[j].value_per_weight){
				backpack_item temp = INSTANCE[i];
				INSTANCE[i] = INSTANCE[j];
				INSTANCE[j] = temp;
			}
		}
	}
}
