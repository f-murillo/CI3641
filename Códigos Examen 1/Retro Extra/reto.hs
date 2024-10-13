import Math.Combinatorics.Exact.Binomial(choose)
import Data.Bits(shiftR)
trib::Integer->Integer
trib n
  | n<3=n
  | otherwise=tribs!!fromIntegral n
  where tribs=0:1:2:zipWith3(\a b c->a+b+c)tribs(tail tribs)(drop 2 tribs)
narayana::Integer->Integer->Integer
narayana n k=(choose(fromIntegral n)(fromIntegral k)*choose(fromIntegral n)(fromIntegral(k-1)))`div`n
maldad::Integer->Integer
maldad n = let pisoLog2 x=fromIntegral(length(takeWhile (>0)(iterate(`shiftR`1)x))-1)
            in trib(pisoLog2(narayana n(pisoLog2 n))+1)
