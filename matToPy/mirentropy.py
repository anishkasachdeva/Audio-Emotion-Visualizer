# Generated with SMOP  0.41-beta
from libsmop import *
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m

    
@function
def mirentropy(x=None,varargin=None,*args,**kwargs):
    varargin = mirentropy.varargin
    nargin = mirentropy.nargin

    #   h = mirentropy(a) calculates the relative entropy of a.
#   (Cf. User's Manual.)
#   mirentropy(..., ?Center?) centers the input data before
#       transforming it into a probability distribution.
    
    center.key = copy('Center')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:7
    center.type = copy('Boolean')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:8
    center.default = copy(0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:9
    option.center = copy(center)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:10
    minrms.key = copy('MinRMS')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:12
    minrms.when = copy('After')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:13
    minrms.type = copy('Numerical')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:14
    minrms.default = copy(0.005)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:15
    option.minrms = copy(minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:16
    specif.option = copy(option)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:18
    varargout=mirfunction(mirentropy,x,varargin,nargout,specif,init,main)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:20
    
@function
def init(x=None,option=None,*args,**kwargs):
    varargin = init.varargin
    nargin = init.nargin

    if isamir(x,'miraudio'):
        x=mirspectrum(x)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:25
    
    type_='mirscalar'
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:27
    
@function
def main(x=None,option=None,postoption=None,*args,**kwargs):
    varargin = main.varargin
    nargin = main.nargin

    if iscell(x):
        x=x[1]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:32
    
    m=get(x,'Data')
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:34
    v=cell(1,length(m))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:35
    for h in arange(1,length(m)).reshape(-1):
        mh=m[h]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:37
        if logical_not(iscell(mh)):
            mh=cellarray([mh])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:39
        v[h]=cell(1,length(mh))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:41
        for k in arange(1,length(mh)).reshape(-1):
            mk=mh[k]
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:43
            mn=copy(mk)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:44
            if isa(x,'mirhisto') or isa(x,'mirscalar'):
                mn=mn.T
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:46
            if option.center:
                mn=center(mn)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:50
            # Negative data is trimmed:
            mn[mn < 0]=0
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:54
            mn=mn / repmat(sum(mn) + repmat(1e-12,concat([1,size(mn,2),size(mn,3),size(mn,4)])),concat([size(mn,1),1,1,1]))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:57
            v[h][k]=- sum(multiply(mn,log(mn + 1e-12))) / log(size(mn,1))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:62
            if isa(x,'mirhisto') or isa(x,'mirscalar'):
                v[h][k]=v[h][k].T
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:65
    
    t=concat(['Entropy of ',get(x,'Title')])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:69
    h=mirscalar(x,'Data',v,'Title',t)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:70
    if (isa(x,'miraudio') or (isa(x,'mirspectrum') and strcmpi(get(x,'Title'),'Spectrum')) or isa(x,'mircepstrum')) and isstruct(postoption) and isfield(postoption,'minrms') and postoption.minrms:
        h=after(x,h,postoption.minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:76
    
    
@function
def after(x=None,h=None,minrms=None,*args,**kwargs):
    varargin = after.varargin
    nargin = after.nargin

    r=mirrms(x,'Warning',0)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:81
    v=mircompute(trim,get(h,'Data'),get(r,'Data'),minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:82
    h=set(h,'Data',v)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:83
    
@function
def trim(d=None,r=None,minrms=None,*args,**kwargs):
    varargin = trim.varargin
    nargin = trim.nargin

    r=r / max(max(r))
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:87
    pos=find(r < minrms)
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:88
    for i in arange(1,length(pos)).reshape(-1):
        d[pos(i)]=NaN
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:90
    
    d=cellarray([d])
# ../MIRtoolbox1.8.1/MIRtoolbox1.8.1/MIRToolbox/mirentropy.m:92