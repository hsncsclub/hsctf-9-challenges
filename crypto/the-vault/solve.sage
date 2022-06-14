key = (7024170033995563248669070948202275621832659349979887130360116095557494224289964760016097751188998415, 3170315055328760291009922771816122, 250376935805204674013389241468539348499776429965769848974957007209785494103442398289504600645160477724, 43395542902454917488842651277236247)
publicKey = 51133059403872132269736212485462945485381032580683758205093039961914793947944949374017744787298892843604322756848647643991762827932760
def lenToXY(hyp,leg1,leg2):
    t = (leg1+leg2)/2
    s = hyp/2
    r = abs(leg2-t)
    x = s^2
    y = r*s*t
    return(x,y)
def multiplyPoint(N,multiplier,x,y):
    E = EllipticCurve([-N^2,0])
    P = E(x,y)
    P2 = P*multiplier
    return (P2[0],P2[1])
def XYToLen(x,y,N):
    r,t = var('r t')
    s_ = sqrt(x)
    solns = [s for s in solve([r*t==abs(y)/s_, t^2-r^2==2*N],r,t) if s[0].rhs().is_real() and s[1].rhs().is_real() and s[0].rhs()>0 and s[1].rhs()>0][0]
    return(sqrt(x)*2,abs(solns[0].rhs()-solns[1].rhs()),solns[0].rhs()+solns[1].rhs())
leg1 = key[0]/key[1]
leg2 = key[2]/key[3]
hyp = sqrt(leg1^2+leg2^2)
N = publicKey/8
newXY = lenToXY(hyp,leg1,leg2)
newP = multiplyPoint(N,9,newXY[0],newXY[1])
p = (XYToLen(newP[0],newP[1],N))
print(p[1].numerator())
print(p[1].denominator())
print(p[2].numerator())
print(p[2].denominator())
