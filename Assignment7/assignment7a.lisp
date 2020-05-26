(setq *print-case* :capitalize)

(setq nums '(1 2 3 4 5 6 7 8 9 10))
(format t "List:~d ~%" nums)


(defvar *nelement*)
(format t "Enter the no. of the element you want. ~%")
(setf *nelement* (read) )

(defun getelements (nelement)
  (format t "The ~dth element of the list is ~d.~%" nelement (nth nelement nums))
  )

(getelements *nelement*)
