class DNA:
    def __init__(self,dna_string):
        self.dna_string = dna_string
    def count_nucleotides(self):
        dna_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
        for i in self.dna_string:
            if i == "A":
                dna_dict["A"] += 1
            elif i == "C":
                dna_dict["C"] += 1
            elif i == "G":
                dna_dict["G"] += 1
            else:
                dna_dict["T"] += 1
        return dna_dict
    def calculate_complement(self):
        char_list = list(self.dna_string)
        for i in range(len(char_list)):
            if char_list[i] == "A":
                char_list[i] = "T"
            elif char_list[i] == "T":
                char_list[i] = "A"
            elif char_list[i] == "G":
                char_list[i] = "C"
            else:
                char_list[i] = "G"
        the_string = ""
        for i in char_list:
            the_string += i
        the_string = the_string[::-1]
        return the_string        
            
    def count_point_mutations(self,dna):
        if self.dna_string == dna:
            return "Hamming distance is 0"
        else:
            count = 0
            for i in range(len(self.dna_string)):
                if self.dna_string[i] != dna[i]:
                    count += 1
        return f"Hamming distance is {count}"     
    def find_motif(self,dna):
        index_list = []
        the_string = self.dna_string
        for i in range(len(the_string)):
            if the_string[i:(i+len(dna))] == dna:
                index_list.append(i)
        return index_list
test_dna = DNA("GATATATGCATATACTT")
print(test_dna.count_nucleotides())
print(test_dna.calculate_complement())
print(test_dna.count_point_mutations("GATATATGCATATGCAT"))
print(test_dna.find_motif("ATAT"))
