import Math.Combinatorics.Exact.Binomial (choose)
import Data.Bits (shiftR)
trib n = if n<3 then n else tribs!!fromIntegral n where tribs=0:1:2:zipWith3(\a b c->a+b+c)tribs(tail tribs)(drop 2 tribs)
maldad n = let pisoLog2 x = fromIntegral(length(takeWhile(>0)(iterate(`shiftR`1)x))-1) in trib(pisoLog2((choose(fromIntegral n)(fromIntegral(pisoLog2 n))*choose(fromIntegral n)(fromIntegral(pisoLog2 n -1)))`div`n)+1)
