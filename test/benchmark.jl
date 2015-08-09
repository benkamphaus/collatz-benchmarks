include("../src/julia/collatz.jl")
using Collatz

@time collatz(10000)
@time collatz_repeat(10000)
@time collatz_reverse(10000)
