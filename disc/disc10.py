"""https://inst.eecs.berkeley.edu/~cs61a/fa22/disc/disc10/"""


#Q1: Virahanka-Fibonacci
'''Write a function that returns the n-th Virahanka-Fibonacci number.'''
(define (vir-fib n)
    (cond
        ((= n 0) 0)
        ((= n 1) 1)
        (else (+ 
                 (vir-fib (- n 2)) 
                 (vir-fib (- n 1))
            )
        )
    )
)

(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)


'''=, eq?, equal?

(= <a> <b>) returns true if a equals b. Both must be numbers.
(eq? <a> <b>) returns true if a and b are equivalent primitive values. For two objects, 
 eq? returns true if both refer to the same object in memory. Similar to checking identity
 between two objects using is in Python
(equal? <a> <b>) returns true if a and b are pairs that have the same contents (cars and 
 cdrs are equivalent). Similar to checking equality between two lists using == in Python. 
 If a and b are not pairs, equal? behaves like eq?.
'''

#Q2: List Making
(define with-list
    (list
        'YOUR-CODE-HERE
        (list 'a 'b) 'c 'd (list 'e)
    )
)
(draw with-list)

(define with-quote
    '(
        'YOUR-CODE-HERE
        (a b) c d (e)
    )

)
(draw with-quote)


(define helpful-list
   (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)

(define with-cons
    (cons
        'YOUR-CODE-HERE
        (cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil) nil)))
    )
)
(draw with-cons)

#Q3: List Concatenation
'''Write a function which takes two lists and concatenates them.'''
(define (list-concat a b)
    'YOUR-CODE-HERE
    (if (null? a)
    b
    (cons (car a) (list-concat (cdr a) b)))
)

(expect (list-concat '(1 2 3) '(2 3 4)) (1 2 3 2 3 4))
(expect (list-concat '(3) '(2 1 0)) (3 2 1 0))

#Q4: Map
'''Write a function that takes a procedure and applies it to every element in a given list 
using your own implementation without using the built-in map function.
'''
(define (map-fn fn lst)
    'YOUR-CODE-HERE
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map-fn fn (cdr lst)))
    )
)

(map-fn (lambda (x) (* x x)) '(1 2 3))
; expect (1 4 9)

#Q5: Remove
'''Implement a procedure remove that takes in a list and returns a new list with all instances 
of item removed from lst. You may assume the list will only consist of numbers and will not 
have nested lists.
'''
(define (remove item lst)
  'YOUR-CODE-HERE
  (cond
      ((null? lst) nil)
      ((= item (car lst)) (remove item (cdr lst)))
      (else
          (cons (car lst)
                (remove item (cdr lst))
        )
      )
  )
)

(expect (remove 3 nil) ())
(expect (remove 2 '(1 3 2)) (1 3))
(expect (remove 1 '(1 3 2)) (3 2))
(expect (remove 42 '(1 3 2)) (1 3 2))
(expect (remove 3 '(1 3 3 7)) (1 7))