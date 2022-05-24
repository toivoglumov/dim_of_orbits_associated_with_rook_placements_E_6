import numpy
import time
import copy
print(time.ctime())
positive_roots=['010000', '010100', '010110', '010111', '011100', '011110', '011111', '011210', '011211', '011221', '001000', '001100', '001110', '001111', '000100', '000110', '000111', '000010', '000011', '000001', '122321', '111100', '111110', '111111', '111210', '111211', '111221', '100000', '112210', '112211', '112221', '101000', '112321', '101100', '101110', '101111']
dim=6
scalar_product_matrix=[[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
def dot_product(alpha,beta):
    sum=0
    for i in range(0,len(alpha)):
        for j in range(0,len(beta)):
            sum=sum+int(alpha[i])*int(beta[j])*scalar_product_matrix[i][j]
    return(sum)
def dot_product_matrix():
    list_dot_products=[]
    n=len(positive_roots)
    for i in range(0,n):
        list_dot_products.append([])
        for j in range(0,n):
            list_dot_products[i].append(dot_product(positive_roots[i],positive_roots[j]))
    return(list_dot_products)
dpm=dot_product_matrix()
print('matrix calculated')
print(time.ctime())
def test_orth(list_of_roots):
    n=len(list_of_roots)
    b=1
    for i in range(0,n-1):
        for j in range(i+1,n):
            if (dpm[list_of_roots[i]][list_of_roots[j]])>0.0:
                b=0
    return(b)
def multiply_root_by_constant(constant, root):
    root1=copy.copy(root)
    for i in range(0,dim):
        root1[i]=constant*root[i]
    return root1
def root_to_list(alpha):
    b=0
    if alpha[0]=='-':
        b=1
        alpha=alpha[1:]
    result_list=[]
    for i in range(0,len(alpha)):
        result_list.append(int(alpha[i]))
    if b==1:
        result_list=multiply_root_by_constant(-1, result_list)
    return(result_list)
def positive_roots_list():
    result_list=[]
    for i in range(0,len(positive_roots)):
        result_list.append(root_to_list(positive_roots[i]))
    return(result_list)
prl=positive_roots_list()
def roots_to_list(list_of_roots):
    result_list=[]
    for i in range(0,len(list_of_roots)):
        result_list.append(prl[list_of_roots[i]])
    return(result_list)
#postitive_roots_list=roots_to_list(positive_roots)
print(prl)
def all_orth_subset():
    result_list=[]
    result_list_numbers=[[]]
    n=len(positive_roots)
    for i in range(0,n):
        result_list.append([root_to_list(positive_roots[i])])
        result_list_numbers[0].append([i])
    for i in range(1,dim+1):
        print(i)
        print(len(result_list))
        result_list_numbers.append([])
        for j in range(0,len(result_list_numbers[i-1])):
            test_list=copy.copy(result_list_numbers[i-1][j])
            test_list.append(result_list_numbers[i-1][j][i-1])
            while test_list[i]+1<n:
                test_list[i]=test_list[i]+1
                if test_orth(test_list)==1:
                    result_list_numbers[i].append(copy.copy(test_list))
                    result_list.append(roots_to_list(test_list))
    return(result_list)
aos=all_orth_subset()
def determine_height_of_root(root):
    root_list=root_to_list(root)
    height=0
    for i in range(0,dim):
        height=height+root_list[i]
    return height
def determine_maximal_height_of_rook_placement(rook_placement):
    max=0
    for i in range(0,len(rook_placement)):
        sum=0
        for j in range(0,len(rook_placement[i])):
            sum=sum+rook_placement[i][j]
        if sum>max:
            max=sum
    return max
def determine_minimal_height_of_rook_placement(rook_placement):
    min=11
    for i in range(0,len(rook_placement)):
        sum=0
        for j in range(0,len(rook_placement[i])):
            sum=sum+rook_placement[i][j]
        if sum<min:
            min=sum
    return min
def determine_maximal_height(aos):
    max=0
    for i in range(0,len(aos)):
        if determine_maximal_height_of_rook_placement(aos[i])>max:
            max=determine_maximal_height_of_rook_placement(aos[i])
    return max
def divide_rook_placements_by_maximal_height(aos):
    n=determine_maximal_height(aos)
    list_of_heights=[]
    for i in range(0,n):
        list_of_heights.append(0)
    for i in range(0,len(aos)):
        list_of_heights[determine_maximal_height_of_rook_placement(aos[i])-1]=list_of_heights[determine_maximal_height_of_rook_placement(aos[i])-1]+1
    return list_of_heights
#print(divide_rook_placements_by_maximal_height(aos))
#print(determine_maximal_height(aos))
#print(len(aos))
#print(time.ctime())
def roots_difference(root1,root2):
	result_list=[]
	for i in range(0,dim):
		result_list.append(root1[i]-root2[i])
	return result_list
def set_of_singular_roots(root):
	list_of_singular_roots=[]
	for i in range(0,len(prl)):
		difference=copy.copy(roots_difference(root,prl[i]))
		#print(difference)
		if difference in prl:
			#print(prl[i],difference)
			list_of_singular_roots.append(difference)
	return list_of_singular_roots
#print(len(set_of_singular_roots(root_to_list('1232'))))
#print(set_of_singular_roots(root_to_list('1232')))
def all_coefficients_are_nonnegative(root):
	b=1
	for i in range(0,dim):
		if root[i]<0:
			b=0
	return b
def find_maximal_roots(orth_subset):
	list_of_maximal_roots=[]
	for i in range(0,len(orth_subset)):
		b=1
		for j in range(0,len(orth_subset)):
			#print(i)
			#print(j)
			if i!=j:
				#print(roots_difference(orth_subset[j],orth_subset[i]))
				if all_coefficients_are_nonnegative(roots_difference(orth_subset[j],orth_subset[i])):
					b=0
		if b==1:
			list_of_maximal_roots.append(orth_subset[i])
	return list_of_maximal_roots
def find_all_orth_subset_of_possible_dim(dim,aos):
    result_list=[]
    for i in range(0,len(aos)):
        list_of_maximal_roots=find_maximal_roots(aos[i])
        max=0
        for j in range(0,len(list_of_maximal_roots)):
            k=len(set_of_singular_roots(list_of_maximal_roots[j]))
            if (k>max):
                max=k
        if max<=dim:
            result_list.append(copy.copy(aos[i]))
    return result_list
def multiply_root_by_constant(constant, root):
    root1=copy.copy(root)
    for i in range(0,dim):
        root1[i]=constant*root[i]
    return root1
def compare_roots_list(root1,root2):
    b=-1
    i=0
    while ((b==-1) and (i!=dim)):
        if (root1[i]>root2[i]) and (b==-1):
            b=1
        elif (root1[i]<root2[i]) and (b==-1):
            b=0
        i=i+1
    return b
print(compare_roots_list([0, 0, 0, 0, 0, 1],[1, 1, 1, 1, 0, 0]))
def positive_roots_sorting(positive_roots_list):
    sorted_roots=copy.copy(positive_roots_list)
    for i in range(0,len(sorted_roots)):
        for j in range(i+1,len(sorted_roots)):
            if compare_roots_list(sorted_roots[i],sorted_roots[j])==1:
                #print(sorted_roots[i],sorted_roots[j])
                root=copy.copy(sorted_roots[i])
                sorted_roots[i]=copy.copy(sorted_roots[j])
                sorted_roots[j]=copy.copy(root)
    return sorted_roots
print(positive_roots_sorting(prl))
sprl=copy.copy(positive_roots_sorting(prl))
def sum_of_roots_list(root1,root2):
    sum_list=[]
    for i in range(0,dim):
        sum_list.append(root1[i]+root2[i])
    return sum_list
def root_list_to_string(root):
    b=1
    for i in range(0,len(root)):
        if root[i]<0:
            b=0
            root=multiply_root_by_constant(-1,root)
    s=''
    if b==0:
        s=s+'-'
    for i in range(0,len(root)):
        s=s+str(root[i])
    return s
def list_of_roots_to_list_of_string(list_of_roots):
    list_of_strings=[]
    for i in range(0,len(list_of_roots)):
        list_of_strings.append(root_list_to_string(list_of_roots[i]))
    return list_of_strings
def determine_special_pairs(positive_root_list):
    d=dict.fromkeys(list_of_roots_to_list_of_string(positive_root_list))
    for i in d.keys():
        d[i]=[]
    for i in range(0,len(sprl)):
        for j in range(i+1,len(positive_root_list)):
            if sum_of_roots_list(positive_root_list[i],positive_root_list[j]) in positive_root_list:
                d[root_list_to_string(sum_of_roots_list(positive_root_list[i],positive_root_list[j]))].append([positive_root_list[i],positive_root_list[j]])
    return d
special_pairs_dict=determine_special_pairs(sprl)
for i in special_pairs_dict.keys():
    print(i)
    print(special_pairs_dict[i])
str_sprl=list_of_roots_to_list_of_string(sprl)
all_roots=[]
for i in range(len(str_sprl)-1,-1,-1):
    all_roots.append('-'+str_sprl[i])
for i in range(0,len(str_sprl)):
    all_roots.append(str_sprl[i])
print(all_roots)
def generate_associated_pairs_plus(por):
    app=[]
    root1=por[0]
    root2=por[1]
    mr1mr2=root_list_to_string(sum_of_roots_list(multiply_root_by_constant(-1,root1),multiply_root_by_constant(-1,root2)))
    mr1=root_list_to_string(multiply_root_by_constant(-1,root1))
    mr2=root_list_to_string(multiply_root_by_constant(-1,root2))
    r1pr2=root_list_to_string(sum_of_roots_list(root1,root2))
    r1=root_list_to_string(root1)
    r2=root_list_to_string(root2)
    app.append((r2,mr1mr2))
    app.append((mr1mr2,r1))
    app.append((mr1,mr2))
    app.append((mr2,r1pr2))
    app.append((r1pr2,mr1))
    return app
def generate_associated_pairs_minus(por):
    apm=[]
    root1=por[0]
    root2=por[1]
    mr1mr2=root_list_to_string(sum_of_roots_list(multiply_root_by_constant(-1,root1),multiply_root_by_constant(-1,root2)))
    mr1=root_list_to_string(multiply_root_by_constant(-1,root1))
    mr2=root_list_to_string(multiply_root_by_constant(-1,root2))
    r1pr2=root_list_to_string(sum_of_roots_list(root1,root2))
    r1=root_list_to_string(root1)
    r2=root_list_to_string(root2)
    apm.append((r2,r1))
    apm.append((mr1mr2,r2))
    apm.append((r1,mr1mr2))
    apm.append((mr2,mr1))
    apm.append((r1pr2,mr2))
    apm.append((mr1,r1pr2))
    return apm
print(generate_associated_pairs_plus(special_pairs_dict['000011'][0]))
print(str_sprl)
def structure_constants_dictionary(sprl,str_sprl,all_roots,special_pairs_dict):
    dictionary_keys=[]
    for i in range(0,len(all_roots)):
        for j in range(0,len(all_roots)):
            dictionary_keys.append((all_roots[i],all_roots[j]))
    d=dict.fromkeys(dictionary_keys)
    for i in d.keys():
        rft=sum_of_roots_list(root_to_list(i[0]),root_to_list(i[1]))
        minus_rft=copy.copy(multiply_root_by_constant(-1,rft))
        if (rft not in sprl) and (minus_rft not in sprl):
            d[i]=0
    print(len(str_sprl))
    for i in range(0,len(str_sprl)):
        if len(special_pairs_dict[str_sprl[i]])!=0:
            por1_string=list_of_roots_to_list_of_string(special_pairs_dict[str_sprl[i]][0])
            por1=(por1_string[0],por1_string[1])
            d[por1]=1
            r1=special_pairs_dict[str_sprl[i]][0][0]
            s1=special_pairs_dict[str_sprl[i]][0][1]
            app=generate_associated_pairs_plus((r1,s1))
            apm=generate_associated_pairs_minus((r1,s1))
            for k in app:
                d[k]=1
            for k in apm:
                d[k]=-1
            mr1=root_list_to_string(multiply_root_by_constant(-1,r1))
            ms1=root_list_to_string(multiply_root_by_constant(-1,s1))
            r1=root_list_to_string(r1)
            s1=root_list_to_string(s1)
            for j in range(1,len(special_pairs_dict[str_sprl[i]])):
                por_string=list_of_roots_to_list_of_string(special_pairs_dict[str_sprl[i]][j])
                por=(por_string[0],por_string[1])
                r=special_pairs_dict[str_sprl[i]][j][0]
                s=special_pairs_dict[str_sprl[i]][j][1]
                mr=root_list_to_string(multiply_root_by_constant(-1,r))
                ms=root_list_to_string(multiply_root_by_constant(-1,s))
                r=root_list_to_string(r)
                s=root_list_to_string(s)
                const=-d[(s,mr1)]*d[(r,ms1)]-d[(mr1,r)]*d[(s,ms1)]
                d[por]=const
                r=special_pairs_dict[str_sprl[i]][j][0]
                s=special_pairs_dict[str_sprl[i]][j][1]
                app=generate_associated_pairs_plus((r,s))
                apm=generate_associated_pairs_minus((r,s))
                for k in app:
                    d[k]=const
                for k in apm:
                    d[k]=-const
    return d
structure_constants_dictionary=structure_constants_dictionary(sprl,str_sprl,all_roots,special_pairs_dict)
print(structure_constants_dictionary[('000001','000010')])
print(structure_constants_dictionary[('000011','000100')])
print(structure_constants_dictionary[('-000001','000011')])
print(structure_constants_dictionary[('000100','-000110')])
#structure_constants_dictionary(sprl,all_roots)
for i in structure_constants_dictionary.keys():
    sc=structure_constants_dictionary[i]
    if (sc!=1) and (sc!=-1) and (sc!=0):
        print(i)
candidates=find_all_orth_subset_of_possible_dim(30,aos)
#for i in range(0,len(candidates)):
#    print(candidates[i])
numbers_dictionary=dict.fromkeys(str_sprl)
for i in range(0,len(str_sprl)):
    numbers_dictionary[str_sprl[i]]=i
print(numbers_dictionary)
def dimension_of_orbit(rook_placement):
    mfrc=[]
    for i in range(0,len(sprl)):
        mfrc.append([])
        for j in range(0,len(sprl)):
            mfrc[i].append(0)
    for i in range(0,len(sprl)):
        for j in range(0,len(sprl)):
            sum=sum_of_roots_list(sprl[i],sprl[j])
            if sum in rook_placement:
                mfrc[i][j]=structure_constants_dictionary[(root_list_to_string(sprl[i]),root_list_to_string(sprl[j]))]
    return numpy.linalg.matrix_rank(mfrc)
print(len(candidates))
print(len(str_sprl))
print(len(prl))
print(prl)
print(sprl)
print(str_sprl)
print(candidates[0])
print(dimension_of_orbit(candidates[0]))
quantity=0
list_of_dimensions=[]
for i in range(0,len(aos)):
    if dimension_of_orbit(aos[i]) not in list_of_dimensions:
        list_of_dimensions.append(dimension_of_orbit(aos[i]))
print(list_of_dimensions)
def remove_singular_roots(rook_placement):
	rp1=copy.copy(rook_placement)
	for i in range(0,len(rp1)):
		sosr=set_of_singular_roots(rp1[i])
		for j in range(0,len(sosr)):
			if sosr[j] in rp1:
				pr1=copy.copy(rp1.remove(sosr[j]))
	return rp1
quantity=0
candidates1=[]
candidates=find_all_orth_subset_of_possible_dim(32,aos)
for i in range(0,len(candidates)):
    if dimension_of_orbit(candidates[i])==32:
        rp=copy.copy(remove_singular_roots(candidates[i]))
        if rp not in candidates1:
            candidates1.append(rp)
            print(rp)
        quantity=quantity+1
print(len(candidates1))
print(quantity)
#print(dimension_of_orbit(candidates[0]))

