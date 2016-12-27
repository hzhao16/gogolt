/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *a = new ListNode(0);
        ListNode *b = a;
        l1 = reverseList(l1);
        l2 = reverseList(l2);
        int n = 0;
        while (l1 || l2 || n) {
            if (l1) {
                n += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                n+=l2->val;
                l2 = l2->next;
            }
            b->next = new ListNode(n%10);
            n /= 10;
            b = b->next;
        }
        a = reverseList(a->next);
        return a;        
    }
    
    ListNode* reverseList(ListNode* head) {
        ListNode* pre = NULL;
        ListNode* curr = head;
        while (curr) {
            ListNode* temp = curr->next;
            curr->next = pre;
            pre = curr;
            curr = temp;
        }
        head = pre;
        return head;
    }
};