# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m

    
@function
def mirroughness(x=None,varargin=None,*args,**kwargs):
    varargin = mirroughness.varargin
    nargin = mirroughness.nargin

    #   r = mirroughness(x) calculates the roughness, or sensory dissonance,
#           due to beating phenomenon between close frequency peaks. 
#       The frequency components are supposed to remain sufficiently 
#           constant throughout each frame of each audio file.
#   r = mirroughness(...,'Contrast',c) specifies the contrast parameter
#       used for peak picking (cf. mirpeaks).
#       Default value: c = .01
#   [r,s] = mirroughness(x) also displays the spectrum and its peaks, used
#           for the computation of roughness.
#   Optional arguments:
#       Method used:
#           mirroughness(...,'Sethares') (default): based on the summation
#               of roughness between all pairs of sines (obtained through
#               spectral peak-picking).
#               mirroughness(...,'Min'): Variant of the Sethares model
#                   where the summation is weighted by the minimum
#                   amplitude of each pair of sines, instead of the product
#                   of their amplitudes.
#           mirroughness(...,'Vassilakis'): variant of 'Sethares' model
#               with a more complex weighting (Vassilakis, 2001, Eq. 6.23).
#       mirroughness(...,'Normal'): normalises with respect to dynamics.
    
    meth.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:24
    meth.choice = copy(cellarray(['Sethares','Vassilakis']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:25
    meth.default = copy('Sethares')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:26
    option.meth = copy(meth)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:27
    cthr.key = copy('Contrast')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:29
    cthr.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:30
    cthr.default = copy(0.01)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:31
    option.cthr = copy(cthr)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:32
    omin.key = copy('Min')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:34
    omin.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:35
    omin.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:36
    option.min = copy(omin)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:37
    normal.key = copy('Normal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:39
    normal.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:40
    normal.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:41
    option.normal = copy(normal)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:42
    normalthres.key = copy('NormalThreshold')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:44
    normalthres.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:45
    normalthres.default = copy(0.1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:46
    option.normalthres = copy(normalthres)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:47
    frame.key = copy('Frame')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:49
    frame.type = copy('Integer')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:50
    frame.number = copy(2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:51
    frame.default = copy(concat([0.05,0.1]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:52
    option.frame = copy(frame)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:53
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:55
    specif.defaultframelength = copy(0.05)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:56
    specif.defaultframehop = copy(0.1)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:57
    varargout=mirfunction(mirroughness,x,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:60
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if isamir(x,'miraudio') and not_(isframed(x)):
        x=mirframenow(x,option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:65
    
    x=mirspectrum(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:67
    if not_(haspeaks(x)):
        x=mirpeaks(x,'Contrast',option.cthr,'Order','Abscissa')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:69
    
    type_=cellarray(['mirscalar','mirspectrum'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:71
    
@function
def main(p=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(p):
        p=p[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:76
    
    if strcmpi(option.meth,'Sethares') or strcmpi(option.meth,'Vassilakis'):
        pf=get(p,'PeakPosUnit')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:79
        pv=get(p,'PeakVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:80
        if option.normal:
            d=get(p,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:82
        rg=cell(1,length(pf))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:84
        for h in arange(1,length(pf)).reshape(-1):
            rg[h]=cell(1,length(pf[h]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:86
            for i in arange(1,length(pf[h])).reshape(-1):
                pfi=pf[h][i]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:88
                pvi=pv[h][i]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:89
                rg[h][i]=zeros(1,length(pfi))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:90
                for k in arange(1,size(pfi,3)).reshape(-1):
                    for j in arange(1,size(pfi,2)).reshape(-1):
                        pfj=pfi[1,j,k].T
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:93
                        pvj=pvi[1,j,k]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:94
                        f1=repmat(pfj,concat([1,length(pfj)]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:95
                        f2=repmat(pfj.T,concat([length(pfj),1]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:96
                        v1=repmat(pvj,concat([1,length(pvj)]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:97
                        v2=repmat(pvj.T,concat([length(pvj),1]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:98
                        pl=plomp(f1,f2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:99
                        if strcmpi(option.meth,'Sethares'):
                            if option.min:
                                v12[j]=min(v1,v2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:102
                                expo=1
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:103
                            else:
                                v12[j]=multiply(v1,v2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:105
                                expo=2
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:106
                        else:
                            if strcmpi(option.meth,'Vassilakis'):
                                v12[j]=multiply(multiply((multiply(v1,v2)) ** 0.1,0.5),(dot(2,min(v1,v2)) / (v1 + v2)) ** 3.11)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:109
                                expo=0.2
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:110
                        rj=multiply(v12[j],pl)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:112
                        rg[h][i][1,j,k]=sum(sum(rj))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:113
                    if option.normal:
                        normcurve=sum(d[h][i](arange(),arange(),k))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:116
                        normcurvexpo=sum(d[h][i](arange(),arange(),k) ** expo)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:117
                        normcurvexpo[normcurve < dot(max(normcurve),option.normalthres)]=NaN
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:118
                        rg[h][i][1,arange(),k]=rg[h][i](1,arange(),k) / normcurvexpo
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:119
                        #                 elseif option.normal == 2
#                     for j = 1:size(pfi,2)
#                         v12j = tril(v12{j},-1); # We also retain the amplitude-product values that were actually taken into consideration in the computation.
#                         rg{h}{i}(1,j,k) = rg{h}{i}(1,j,k) / sum(sum(v12j));
#                     end
    
    model='Roughness'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:131
    if strcmpi(option.meth,'Sethares'):
        if option.min:
            model=concat([model,' (Sethares, Min variant)'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:134
        else:
            model=concat([model,' (Sethares)'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:136
    else:
        model=concat([model,' (Vassilakis)'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:139
    
    if option.normal:
        model=concat([model,' (Normalised)'])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:142
    
    r=mirscalar(p,'Data',rg,'Title',model)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:144
    r=cellarray([r,p])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:145
    
@function
def plomp(f1=None,f2=None,*args,**kwargs):
    varargin = plomp.varargin
    nargin = plomp.nargin

    # returns the dissonance of two pure tones at frequencies f1 & f2 Hz
# according to the Plomp-Levelt curve (see Sethares)
    b1=3.51
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:151
    b2=5.75
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:152
    xstar=0.24
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:153
    s1=0.0207
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:154
    s2=18.96
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:155
    s=tril(xstar / (dot(s1,min(f1,f2)) + s2))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:156
    pd=exp(multiply(dot(- b1,s),abs(f2 - f1))) - exp(multiply(dot(- b2,s),abs(f2 - f1)))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirroughness.m:157