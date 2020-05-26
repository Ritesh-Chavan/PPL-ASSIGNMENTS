(defvar num)
(format t "Enter the no. ~%")
(setq num (read))

(defun factorial (n)
   (defvar fact 1)
   (if (= n 0)
     (return-from factorial 1)
   )
   
   (if (>= n 1)
     (setq fact (* n (factorial (- n 1))))
   )
   (return-from factorial fact)
)
  
(format t "The factorial is ~d ~%" (factorial num))
