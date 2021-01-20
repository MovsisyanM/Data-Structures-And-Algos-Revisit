# Binary Search Trees

Many ops.  
Can be used a s dict, priority queue.  
Ops depend on height

Binary Search Tree property:  
Nodes in left subtree < root < nodes in right subtree

Node contains:  
key,  
ref to parent node  
ref to left child  
ref to right child  
sattelite data  
end

In-Order-Tree-Walk(node):  
-- if sure node.key exists  
-- -- recurse(node.left)  
-- -- print(node.key)  
-- -- recurse(node.right)  
-- end if  
end

Tree-Search(node, key):  
-- if (node == Null || key == node.key):  
-- -- return node  
-- end if  
-- recurse(key < node.key ? node.left : node.right, k)  
end

Tree-Minimum(node):  
-- while node.left != null:  
-- -- node = node.left  
-- end while  
-- return node  
end

Tree-Maximum(node):  
-- while node.right != null:  
-- -- node = node.right  
-- end while  
-- return node  
end

Successor(node):  
-- if node.right exists:  
-- -- return Tree-Minimum(node.right)  
-- end if  
-- parent = node.parent  
-- while parent exists and node == parent.right:  
-- -- node = parent  
-- -- parent = parent.parent  
-- end while  
-- return parent  
end

Predecessor(node):  
-- if node.left exists:  
-- -- return Tree-Maximum(node.left)  
-- end if  
-- parent = node.parent  
-- while parent exists and node == parent.left:  
-- -- node = parent  
-- -- parent = parent.parent  
-- end while  
-- return parent  
end

Preorder-Tree-Walk(node):
