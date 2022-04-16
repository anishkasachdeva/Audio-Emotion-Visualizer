# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m

    
@function
def mircentroid(x=None,varargin=None,*args,**kwargs):
    varargin = mircentroid.varargin
    nargin = mircentroid.nargin

    #   c = mircentroid(x) calculates the centroid (or center of gravity) of x.
#   x can be either:
#       - a spectrum (spectral centroid),
#       - an envelope (temporal centroid)
#       - a histogram,
#       - or any data. Only the positive ordinates of the data are taken
#           into consideration.
#   c = mircentroid(x,'Peaks') calculates the centroid of the peaks only.
    
    # Beauchamp 1982 version?
    
    peaks.key = copy('Peaks')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:13
    peaks.type = copy('String')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:14
    peaks.choice = copy(cellarray([0,'NoInterpol','Interpol']))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:15
    peaks.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:16
    peaks.keydefault = copy('NoInterpol')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:17
    option.peaks = copy(peaks)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:18
    minrms.key = copy('MinRMS')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:20
    
    minrms.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:21
    minrms.type = copy('Numerical')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:22
    minrms.default = copy(0.005)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:23
    option.minrms = copy(minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:24
    maxentropy.key = copy('MaxEntropy')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:26
    maxentropy.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:27
    maxentropy.type = copy('Numerical')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:28
    maxentropy.default = copy(0.95)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:29
    option.maxentropy = copy(maxentropy)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:30
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:32
    varargout=mirfunction(mircentroid,x,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:34
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if not_(isamir(x,'mirdata')) or isamir(x,'miraudio'):
        x=mirspectrum(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:39
    
    type_='mirscalar'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:41
    
@function
def main(x=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(x):
        x=x[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:46
    
    if option.peaks:
        if strcmpi(option.peaks,'Interpol'):
            pt=get(x,'PeakPrecisePos')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:50
            pv=get(x,'PeakPreciseVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:51
        else:
            pt=get(x,'PeakPos')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:53
            pv=get(x,'PeakVal')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:54
        cx=cell(1,length(pt))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:56
        for h in arange(1,length(pt)).reshape(-1):
            cx[h]=cell(1,length(pt[h]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:58
            for i in arange(1,length(pt[h])).reshape(-1):
                pti=pt[h][i]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:60
                pvi=pv[h][i]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:61
                nfr=size(pti,2)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:64
                nbd=size(pti,3)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:65
                ci=zeros(1,nfr,nbd)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:66
                for j in arange(1,nfr).reshape(-1):
                    for k in arange(1,nbd).reshape(-1):
                        ptk=pti[1,j,k]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:69
                        pvk=pvi[1,j,k]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:70
                        sk=sum(pvk)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:71
                        ci[1,j,k]=sum(multiply(ptk,pvk)) / sk
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:72
                cx[h][i]=ci
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:75
    else:
        cx=peaksegments(centroid,get(x,'Data'),get(x,'Pos'))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:79
    
    if isa(x,'mirspectrum'):
        t='Spectral centroid'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:82
    else:
        if isa(x,'mirenvelope'):
            t='Temporal centroid'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:84
        else:
            t=concat(['centroid of ',get(x,'Title')])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:86
    
    c=mirscalar(x,'Data',cx,'Title',t)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:88
    if isstruct(postoption):
        c=after(x,c,postoption.minrms,postoption.maxentropy)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:90
    
    
@function
def centroid(d=None,p=None,*args,**kwargs):
    varargin = centroid.varargin
    nargin = centroid.nargin

    c=(dot(p.T,d)) / sum(d)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:95
    
@function
def after(x=None,c=None,minrms=None,maxentropy=None,*args,**kwargs):
    varargin = after.varargin
    nargin = after.nargin

    v=get(c,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:99
    if minrms and strcmpi(get(x,'Title'),'Spectrum'):
        r=mirrms(x,'Warning',0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:101
        v=mircompute(trimrms,v,get(r,'Data'),minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:102
    
    if maxentropy and maxentropy < 1:
        h=mirentropy(x,'MinRMS',minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:105
        v=mircompute(trimentropy,v,get(h,'Data'),maxentropy)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:106
    
    c=set(c,'Data',v)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:108
    
@function
def trimrms(d=None,r=None,minrms=None,*args,**kwargs):
    varargin = trimrms.varargin
    nargin = trimrms.nargin

    r=r / max(max(r))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:112
    pos=find(r < minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:113
    for i in arange(1,length(pos)).reshape(-1):
        d[pos(i)]=NaN
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:115
    
    d=cellarray([d])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:118
    
@function
def trimentropy(d=None,r=None,minentropy=None,*args,**kwargs):
    varargin = trimentropy.varargin
    nargin = trimentropy.nargin

    pos=find(r > minentropy)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:122
    for i in arange(1,length(pos)).reshape(-1):
        d[pos(i)]=NaN
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:124
    
    d=cellarray([d])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mircentroid.m:126