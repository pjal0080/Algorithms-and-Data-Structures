
#include <bits/stdc++.h>
using namespace std;


class Node {
    public:
        int data;
        Node* next;
        
        Node(int val)
        : data(val),
          next(NULL)
        {
            
        }
    
        
};

class LinkedList {
    public:
        Node* head;
        
        LinkedList()
            : head(NULL)
        {
            
        }
        
        
        ~LinkedList()
        {
            Node* tmp = head;
            while(tmp) {
                Node* nxt = tmp->next;
                delete tmp;
                tmp = nxt;
            }
            
        }
    
        void addNode(int val)
        {
            
            if(head == NULL) {
                Node* node = new Node(val);
                head = node;
                
            } else {
                Node* tmp = head;
                
                while(tmp->next) {
                    tmp = tmp->next;
                }
                
                Node* node = new Node(val);
                tmp->next = node;
                
            }
            
            
        }
     
    
        void printLinkedList() 
        {
            Node* tmp = head;
            while(tmp) {
                if(tmp->next == NULL){
                    cout<<tmp->data;
                }  
                else{
                    cout<<tmp->data<<"->" ;
                    
                }
                
                tmp = tmp->next;
             
            }
        }
    

};


int main() {
    
    LinkedList ll;
    ll.addNode(10);
    ll.addNode(20);
    ll.addNode(30);
    ll.addNode(40);
    ll.addNode(50);
    
    ll.printLinkedList();
	return 0;
}
