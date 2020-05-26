(defvar num)
(format t "Enter the no. ~%")
(setq num (read))

(defun factorial (n)
  (defvar fact 1)
  (if (= n 0)
   (return-from factorial 1) 
   (loop 
     (setq fact (* fact n))
     (setq n (- n 1))
     (when (< n 1) (return-from factorial fact))
    )
   )
)
  
(format t "The factorial is ~d ~%" (factorial num))
