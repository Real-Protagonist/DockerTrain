class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        """ ADICIONA UM NÓ NO FINAL DA LISTA. """
        new_node = Node(data)
        if not self.head:   #SE A LISTA ESTIVER VAZIA, O NOVO NÓ SERÁ O PRIMEIRO
            self.head = new_node
        else:
            current = self.head
            while current.next:     # PERCORRE ATÉ O ÚLTIMO NÓ
                current = current.next
            current.next = new_node     # DEFINE O PRÓXIMO DO ÚLTIMO NÓ PARA O NOVO NÓ
            
    def prepend(self, data):
        """ ADICIONA UM NÓ NO INÍCIO DA LISTA. """
        new_node = Node(data)
        new_node.next = self.head      # FAZ O NOVO NÓ APONTAR PARA O ANTIGO PRIMEIRO NÓ
        self.head = new_node       # AGORA O NOVO NÓ É O PRIMEIRO DA LISTA
        
    def delete(self, data):
        """ REMOVE O PRIMEIRO NÓ QUE CONTEM O DADO ESPECÍFICO. """
        current = self.head
        if current and current.data == data:
            self.head = current.next    # SE FOR O PRIMEIRO NÓ, APENAS MUDA A CABEÇA
            current = None
            return
        
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
            
        if current is None:     # O VALOR NÃO FOI ENCONTRADO
            print("Valor não encontrado na lista.")
            return
        
        prev.next = current.next     # REMOVE O NÓ DA LISTA
        current = None
        
    def search(self, data):
        """ BUSCA UM NÓ COM O VALOR ESPECÍFICADO E RETORNA TRUE SE ENCONTRADO. """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
            
    def print_list(self):
        """ IMPRIME TODOS OS ELEMENTOS DA LISTA LIGADA. """
        current = self.head
        if not current:
            print("Lista Vazia.")
            return
        while current:
            print(current.data, end="=>")
            current = current.next
        print("None")
        
    def length(self):
        """ RETORNA O TAMANHO DA LISTA (NUMERO DE NOS). """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def insert_at(self, index, data):
        """ INSERE UM NO EM UMA POSIÇÃO ESPECIFICA (0 INDEXADA). """
        if index < 0 or index > self.length():
            print("Index out out of bound.")
            return
        
        if index == 0:
            self.prepend(data)
            return
        
        new_node = Node(data)
        current = self.head
        count = 0
        while count < index - 1:
            current = current.next
            count += 1
            
        new_node.next = current.next
        current.next = new_node
        
    def delete_at(self, index):
        """ REMOVE UM NO DE UMA POSIÇÃO ESPECÍFICA (0 INDEXADA). """
        if index < 0 or index >= self.length():
            print("Index out of bound.")
            return
        
        current = self.head
        
        if index == 0:
            self.head = current.next    # REMOVE O PRIMEIRO NO
            current = None
            return
        
        count = 0
        prev = None
        while count < index:
            prev = current
            current = current.next
            count += 1
            
        prev.next = current.next    # CONECTA O NO ANTERIOR AO PROXIMO
        current = None
        

if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.append(10)
    linked_list.append(19)
    linked_list.print_list()
    
    linked_list.append(5)
    linked_list.print_list()
    
    linked_list.insert_at(2, 22)
    linked_list.print_list()
    
    linked_list.delete(19)
    linked_list.print_list()
    
    linked_list.delete_at(1)
    linked_list.print_list()
    
    
    print(linked_list.search(10))
    print(linked_list.search(11))
    
    print(linked_list.length())
    