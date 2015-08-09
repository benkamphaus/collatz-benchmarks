module Collatz

export collatz, collatz_reverse, collatz_repeat

"""
Genterate a collatz sequence starting with `n`. Truncate the trivial cycle
`(4, 2, 1)` to the first `1` encountered.
"""
function collatz(n::Int64)
  seq = Int64[n]
  while true
    push!(seq, n%2 == 1 ? (3*n + 1) : (n / 2))
    n = seq[end]
    if n == 1
      return seq
    end
  end
end

"""
For each number that serves as the start of a Collatz sequence, return two
tuples (as a dictionary):
    (number first seen in previous sequence, nth iteration of this sequence
                                             at which we see it.)
    (number starting sequence where first seen, nth iteration of that seq.
                                                where we first saw it.)
"""
function collatz_repeat(n::Int64)
  reverse_at = Dict{Int64,Array{Int64}}()
  result = Dict{Int64,Array{Int64}}()
  for i in 1:n
    result[i] = Int64[0, 0]
    for (i_j, j) in enumerate(collatz(i))
      if ~(j in reverse_at.keys)
        reverse_at[j] = Int64[i, i_j]
      else
        result[i] = Int64[j, i_j, reverse_at[j][1], reverse_at[j][2]]
        break
      end
    end
  end
  result
end

"""
For each numbers reached by a collatz sequence up to n, track all seeds
that reach it and at which term they reach it.
"""
function collatz_reverse(n::Int64)
  reverse_at = Dict{Int64,Array{Int64}}()
  for i in 1:n
    for (i_j, j) in enumerate(collatz(n))
      if ~(j in reverse_at.keys)
        reverse_at[j] = Int64[i_j, i]
      else
        append!(reverse_at[j], [i_j, i])
      end
    end
  end
  reverse_at
end

# module end
end
