# If you need to check something quickly, use the interpreter
import procedures as pro

trees_bcn = pro.extract_trees_bcn('data/Trees_Barcelona.json')
print(len(trees_bcn))


trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn('data/Trees_Barcelona.json'))


print(len(trees_bcn))
"""
trees_bcn = pro.extract_trees_bcn_stream('data/Trees_Barcelona.json')
print(len(trees_bcn))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))
trees_bcn.append(pro.extract_trees_bcn_stream('data/Trees_Barcelona.json'))

print(len(trees_bcn))
"""
