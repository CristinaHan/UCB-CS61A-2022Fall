(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s)  (car (cddr s)))

(define (ascending? asc-lst) 
    (cond
        ((<= (length asc-lst) 1) #t)
        ((<= (car asc-lst) (cadr asc-lst)) (ascending? (cdr asc-lst)))
        (else #f)
    )
)

(define (square n) (* n n))

(define (pow base exp)
    (cond
        ((= exp 0) 1)
        ((= base 1) 1)
        ((even? exp) (square (pow base (/ exp 2))))
        (else (* base (pow base (- exp 1))))
        )
)
