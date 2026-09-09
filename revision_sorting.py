class Sorting:
    def Bubblesort(self,bubble_array):
        n = len(bubble_array)

        for i in range(n-1):
            for j in range(n-i-1):
                if bubble_array[j] > bubble_array[j+1]:
                    bubble_array[j],bubble_array[j+1] = bubble_array[j+1],bubble_array[j]

        return bubble_array
    
    def Selectionsort(self,selection_array):
        n=len(selection_array)

        for i in range(n-1):
            min_index = i
            for j in range(i+1,n):
                if selection_array[j] < selection_array[min_index]:
                    min_index = j
            min_value = selection_array.pop(min_index)

            selection_array.insert(i, min_value)

        return selection_array

    def Insertionsort(self,insertion_array):
        n =len(insertion_array)

        for i in range(1,n):
            insert_index =i
            current_value = insertion_array.pop(i)
            for j in range(i-1, -1,-1):
                if insertion_array[j] > current_value:
                    insert_index=j

            insertion_array.insert(insert_index,current_value)

        return insertion_array



if __name__ == "__main__":
    obj = Sorting()

bubble_array = [44,4,23,2,14,1]
selection_array = [9,8,7,6,5,4,3,2,1]
insertion_array = [9,8,7,6,5,4,4,3,2,1]
print("Bubble sort:",obj.Bubblesort(bubble_array))
print("selection sort:",obj.Selectionsort(selection_array))
print("Insertion sort:",obj.Insertionsort(insertion_array))