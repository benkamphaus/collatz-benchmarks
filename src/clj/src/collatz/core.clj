(ns collatz.core)

(defn whole-number? [n]
  (= n (Math/floor n)))

(defn power-of-two? [n]
  (whole-number? (/ (Math/log n) (Math/log 2))))

(defn collatz [x]
  "Generates the collatz sequence starting at x. Does not include 1 or the
  trivial cycle."
  (->> x
       (iterate (fn [n]
                  (if (even? n)
                        (/ n 2)
                        (inc (* n 3)))))
       (take-while #(not= 1 %))))

(def natural-numbers
  (iterate inc 1))

(defn sofar [n]
  "Returns a mapping from a number to the set of all numbers returned by collatz
  sequences that start with it and all previous natural numbers."
  (reduce #(set/union %1 %2) (map #(-> % collatz set) (take n natural-numbers))))

(defn set-so-far [n]
  "Returns a map of all numbers seen so far by the time you have generated the
  collatz sequence for 'n', if you've generated all previous sequences starting
  at 1."
  (apply conj (map (fn [x]
                    {x (sofar x)}) (take n natural-numbers))))

(defn new-at [n]
  "Tells you which numbers have first been seen in a collatz sequence generated
  at n (i.e., they are not in the collatz sequence produced for any previous
  natural number."
  (set/difference ((set-so-far n) n)
                  (if (> n 2)
                    ((set-so-far (dec n)) (dec n))
                    #{1 2 4})))


