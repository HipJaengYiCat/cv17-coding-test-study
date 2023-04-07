import sys
species_dict={}
count=0
while True:
    species=sys.stdin.readline().rstrip()
    if not species:
        break
    count+=1
    if species in species_dict.keys():
        species_dict[species]+=1
    else:
        species_dict[species]=1
        
species_dict=sorted(species_dict.items())
for k,v in species_dict:
    print(k,f'{v/count*100:.4f}')

