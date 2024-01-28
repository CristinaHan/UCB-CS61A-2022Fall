"""https://inst.eecs.berkeley.edu/~cs61a/fa22/disc/disc11/"""

#Q1: If Program Python
def if_program(condition, true_result, false_result):
    """
    >>> eval(if_program("True", "3", "4"))
    3
    >>> eval(if_program("0", "'if true'", "'if false'")) 
    'if false'
    >>> eval(if_program("1", "print('true')", "print('false')"))
    true
    >>> eval(if_program("print('condition')", "print('true_result')", "print('false_result')"))
    condition
    false_result
    """
    "*** YOUR CODE HERE ***"
    return f'{true_result} if {condition} else {false_result}'

#Q2: Writing Quasiquote Expressions
scm> `(a b c)
(a b c)

scm> `(a ,b c)
(a 1 c)

scm> (a b c)
3

scm> `(a (b ,b) c)
(a (b 1) c)

scm> `(a ,(a b c) c)
(a 3 c)

scm> `(if ,condition ,if-true ,if-false) 
(if (= 1 1) (print 3) (print 5))

#Q3: If Program Scheme
(define (if-program condition if-true if-false)
  'YOUR-CODE-HERE
   `(if ,condition ,if-true ,if-false)
)

#Q4: Exponential Powers
(define (pow-expr n p)
    'YOUR-CODE-HERE
    (if (= p 0) 1
        `(* ,(pow-expr n (- p 1)) ,n))
)

#Q5: Swap
(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (swap expr)
    (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
        (if (> (eval second) (eval first))
            (cons op (cons second (cons first rest)))
            expr)
    )
)

#Q6: Make Or
(define (make-or expr1 expr2)
    `(let ((v1, expr1))
        (if v1 v1 ,expr2))
)

#Q7: Make "Make Or"
(define (make-make-or)
  'YOUR-CODE-HERE
  '(define (make-or expr1 expr2) `(let ((v1 ,expr1)) (if v1 v1 ,expr2)))
)