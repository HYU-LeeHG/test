fun unzip3 triples =
    case triples of
        [] => ([],[],[])
        | (a,b,c)::tl =>
         let val (l1, l2, l3) = unzip3 tl
         in
             (a::l1,b::l2,c::l3)
         end


fun nondecreasing xs =
    case xs of
        [] => true
        | x::[] => true
        | head::neck::rest => head <= neck andalso
                                nondecreasing(tl(xs))

datatype sgn = P|N|Z

fun multsign (x1, x2) =
    let fun sign x = if x=0 then Z else if x>0 then P else N
        in 
            case (sign(x1), sign(x2)) of
                 (Z, _) => Z
                | (_, Z) => Z
                | (P, P) => P
                | (N, N) => P
                | _      => N
        end